"""Reproducible checks of the capsule volume-product profile.

Numerical checks are consistency tests, not proofs of inequalities over continua.
Analytic proofs of the all-dimensional assertions appear in RESULT.md.
"""
import math
import sympy as sp
from scipy.integrate import quad
from scipy.special import gammaln, erfc


def constants(d):
    assert d >= 2
    logkap = lambda k: 0.5*k*math.log(math.pi)-math.lgamma(1+0.5*k)
    K = math.exp(logkap(d))
    m = 2*math.exp(logkap(d-1)-logkap(d))/d
    c = 2*math.exp(gammaln(d/2)-gammaln((d-1)/2))/math.sqrt(math.pi)
    assert abs(c/(d-1)-m) < 1e-12*max(1,m)
    return K,m,c


def ratio(d,s):
    K,m,c = constants(d)
    def integrand(u):
        if u == 1: return 0.0
        return c*math.exp(((d-3)/2)*math.log1p(-u*u)-d*math.log1p(s*u))
    F=quad(integrand,0,1,epsabs=3e-12,epsrel=3e-12,limit=350)[0]
    return (1+d*m*s)*F


def check():
    s=sp.symbols('s', nonnegative=True)
    r3=(3*s+2)*(s+2)/(4*(s+1)**2)
    assert sp.simplify(r3-(1-s**2/(4*(1+s)**2)))==0
    assert sp.factor(sp.diff(r3,s))==-s/(2*(1+s)**3)
    assert sp.series(r3,s,0,4).removeO()==1-s*s/4+s**3/2
    assert sp.series(r3,s,sp.oo,4).removeO()==sp.Rational(3,4)+sp.Rational(1,2)/s-sp.Rational(3,4)/s**2+s**(-3)
    print('THREE_DIMENSIONAL_EXACT_RATIONAL_IDENTITY_PASSED')

    for d in range(2,15):
        K,m,c=constants(d)
        val=[ratio(d,s) for s in [0,.03,.1,.3,.75,2,6,20]]
        assert all(x>y for x,y in zip(val,val[1:])),(d,val)
        L=d*m*m
        assert L<val[-1]<1
        alpha=d*d*m*m-(d+1)/2
        assert alpha>0
        s0=.001
        local=(1-ratio(d,s0))/(s0*s0)
        assert abs(local-alpha)<.02*alpha,(d,local,alpha)
    print('FINITE_DIMENSION_INTEGRAL_AND_SMALL_ASPECT_CHECKS_PASSED')

    # The dimension-two logarithmic coefficient is independently checked
    # against the exact inverse-hyperbolic formula for s > 1.
    for ss in [3,10,100,1000]:
        exact=(2*math.pi+8*ss)*(ss/(ss*ss-1)-math.acosh(ss)/(ss*ss-1)**1.5)
        integ=math.pi**2*ratio(2,ss)
        assert abs(exact-integ)<1e-8
    for ss in [100,1000,3000]:
        exact=(2*math.pi+8*ss)*(ss/(ss*ss-1)-math.acosh(ss)/(ss*ss-1)**1.5)
        approx=8+2*math.pi/ss+8*(1-math.log(2*ss))/ss**2
        assert abs(exact-approx)*ss**2 < .40,(ss,exact,approx)
    print('PLANAR_LOGARITHMIC_TAIL_PASSED')

    for d in [3,4,5,8,12]:
        K,m,c=constants(d)
        ss=500
        P=K*K*ratio(d,ss)
        L=K*K*d*m*m
        approx=L+K*K*m/ss-L/((d-2)*ss*ss)
        assert abs((P-approx)*ss*ss)<.1*L,(d,P,approx)
    print('HIGHER_DIMENSION_SECOND_ORDER_TAIL_PASSED')

    mu=math.sqrt(2/math.pi)
    for tau in [0,.3,1,2,5]:
        target=(1+mu*tau)*math.exp(tau*tau/2)*erfc(tau/math.sqrt(2))
        d=400
        observed=ratio(d,tau/math.sqrt(d))
        assert abs(target-observed)<.004,(tau,target,observed)
    print('GAUSSIAN_CROSSOVER_CONVERGENCE_PASSED')

    for ss in [.3,2]:
        observed=ratio(1000,ss)
        assert abs(observed-2/math.pi)<.12,(ss,observed)
    print('FIXED_ASPECT_HIGH_DIMENSION_CROSSOVER_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    check()
