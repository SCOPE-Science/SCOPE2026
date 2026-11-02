"""Deterministic numerical diagnostics for a two-node Gaussian kernel quadrature collision theorem.

Requires Python 3.10+ with NumPy and SciPy. The universal theorem is established
by analytic arguments in RESULT.md; these computations test formulas only.
"""
import math
import numpy as np
from scipy.special import erf, ndtr
from numpy.polynomial.legendre import leggauss


def mean_kernel(x, a):
    x = np.asarray(x)
    return math.sqrt(math.pi)/(2*math.sqrt(a)) * (erf(math.sqrt(a)*x) + erf(math.sqrt(a)*(1-x)))


def mean_kernel_derivative(x, a):
    x = np.asarray(x)
    return np.exp(-a*x*x) - np.exp(-a*(1-x)**2)


def analytic_constants(a, sigma):
    l1 = math.sqrt(math.pi/a)*(2*math.erf(math.sqrt(a)/2)-math.erf(math.sqrt(a)))
    l2 = math.sqrt(math.pi/(2*a))*(math.erf(math.sqrt(2*a))-2*math.exp(-a/2)*math.erf(math.sqrt(a/2)))
    one_side = sigma*l1/(a*math.sqrt(math.pi))
    ridge = math.pi*l2/(4*a**1.5)
    return l1,l2,one_side,ridge


def gauss_nodes(a,b,n):
    x,w = leggauss(n)
    return (a+b)/2+(b-a)*x/2, (b-a)*w/2


def moments_at_delta(delta, eta, a, order=80):
    # Equal measure for positive and negative signed node separation.
    m, weights = gauss_nodes(delta/2,1-delta/2,order)
    v1=mean_kernel(m+delta/2,a)
    v2=mean_kernel(m-delta/2,a)
    rho=math.exp(-a*delta*delta)
    sm=(v1+v2)/(1+eta+rho)
    df=(v1-v2)/(eta-math.expm1(-a*delta*delta))
    return np.dot(weights,sm*sm+df*df)


def ridge_integral(eta,a,n=130):
    # Transform delta -> z=sqrt(eta/a)*tan(v) to resolve the diagonal layer.
    scale=math.sqrt(eta/a)
    hi=math.atan(1/scale)
    v,w=gauss_nodes(0,hi,n)
    delta=scale*np.tan(v)
    jac=scale/(np.cos(v)**2)
    return sum(wi*ji*moments_at_delta(float(d),eta,a,60) for wi,ji,d in zip(w,jac,delta))


def one_sided_tail(t,a,sigma,n=160):
    # The entire probability at large t is concentrated in delta=O(t^-1).
    # Mapping delta=u/(t+u) clusters quadrature near the diagonal.
    zz,ww=gauss_nodes(0,1,n)
    result=0.0
    for v,wd in zip(zz,ww):
        # delta= v^2 to concentrate around 0; no truncation.
        delta=float(v*v)
        m,wm=gauss_nodes(delta/2,1-delta/2,90)
        v1=mean_kernel(m+delta/2,a)
        v2=mean_kernel(m-delta/2,a)
        rho=math.exp(-a*delta**2)
        sm=(v1+v2)/(1+rho)
        df=(v1-v2)/(-math.expm1(-a*delta**2))
        sd=sigma*np.sqrt((sm*sm+df*df)/2)
        result+=wd*2*v*np.dot(wm,ndtr(-t/sd))
    return t*2*result


def run():
    tests=0
    for a in (.2, .5, 1., 2., 5.):
        l1,l2,tail,ridge=analytic_constants(a,1.)
        assert l1>0 and l2>0 and tail>0 and ridge>0
        x,w=gauss_nodes(0,1,240)
        assert abs(2*np.dot(gauss_nodes(0,.5,160)[1], mean_kernel_derivative(gauss_nodes(0,.5,160)[0],a))-l1)<1e-12
        assert abs(np.dot(w,mean_kernel_derivative(x,a)**2)-l2)<1e-12
        tests+=4
        # Mathematically equivalent direct inverse and symmetric/antisymmetric decomposition.
        for xx,yy,eta in ((.14,.63,0),(.245,.243,.001),(.1,.9,.1),(.37,.57,1e-7)):
            rho=math.exp(-a*(xx-yy)**2)
            k=np.array([[1+eta,rho],[rho,1+eta]])
            mu=np.array([mean_kernel(xx,a),mean_kernel(yy,a)])
            ref=np.linalg.solve(k,mu)
            sm=(mu[0]+mu[1])/(1+eta+rho)
            df=(mu[0]-mu[1])/(1+eta-rho)
            actual=np.array([(sm+df)/2,(sm-df)/2])
            assert np.allclose(ref,actual,rtol=1e-8,atol=1e-8)
            tests+=1
    a=1.
    l1,l2,tail,ridge=analytic_constants(a,1.)
    print('alpha=1 constants: L1=%.12g L2=%.12g one-sided-tail=%.12g ridge=%.12g' % (l1,l2,tail,ridge))
    for eta in (1e-3,1e-4,1e-5,1e-6):
        value=ridge_integral(eta,a)
        normalized=math.sqrt(eta)*value
        print('eta=%.0e E||w||^2=%.10g sqrt(eta)*E||w||^2=%.10g (limit %.10g)'%(eta,value,normalized,ridge))
        assert abs(normalized/ridge-1)<(0.20 if eta>=1e-3 else 0.10)
        tests+=1
    for t in (80.,200.,500.):
        value=one_sided_tail(t,a,1.)
        print('t=%g: t P(noise>t)=%.10g (limit %.10g)'%(t,value,tail))
        assert abs(value/tail-1)<0.06
        tests+=1
    print('PASS: %d independent formula/numerical tests' % tests)

if __name__=='__main__':
    run()
