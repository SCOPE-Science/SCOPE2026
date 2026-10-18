"""Direct numerical checks of the Gaussian first-pivot lq asymptotics.

Use: python verify.py. Requires scipy and numpy.
The calculations are diagnostics; asymptotic assertions are established analytically.
"""
import math
from scipy.integrate import quad


def angular_norm(theta, q):
    c, s = abs(math.cos(theta)), abs(math.sin(theta))
    return max(c, s) if math.isinf(q) else (c**q+s**q)**(1/q)


def tail(x, q):
    if q == 2:
        return math.exp(-x*x)
    val, _ = quad(lambda t: math.exp(-(x/angular_norm(t,q))**2),
                  0, math.pi/4, epsabs=1.e-14, epsrel=1.e-13)
    return 4*val/math.pi


def scaled_angular_tail(x, q):
    u = 2**(1/q-0.5) if q < 2 else 1.0
    a = 1/(u*u)
    val, _ = quad(lambda t: math.exp(-x*x*((1/angular_norm(t,q)**2)-a)),
                  0, math.pi/4, epsabs=1.e-12, epsrel=1.e-12)
    return 4*val*x/math.pi


def angular_tail_constant(q):
    if q == 2:
        raise ValueError('the Euclidean norm has a full circle of maxima')
    if q < 2:
        return 2*2**(1/q-0.5)/math.sqrt(math.pi*(2-q))
    return 2/math.sqrt(math.pi)


def sharp_coefficient(q):
    if q == 2:
        return 1/math.sqrt(2), .5, -.5
    if q < 2:
        u=2**(1/q-0.5)
        a=u*u/2
        return math.gamma(a)*u/math.sqrt(2*math.pi)*(math.sqrt(math.pi*(2-q))/2)**a,a,(a-1)/2
    return math.pi**.25/2,.5,-.25


def pivot_probability(n,q):
    assert n>=2
    def fn(x):
        t=tail(x,q)
        if t >= 1: return 0.
        return math.sqrt(2/math.pi)*math.exp(-x*x/2)*math.exp((n-1)*math.log1p(-t))
    ans,_=quad(fn,0,12,epsabs=1.e-12,epsrel=2.e-10,limit=200)
    return ans


def test():
    assertions = 0
    for q in (1.,1.4,1.8,3.,4.,float('inf')):
        C=angular_tail_constant(q)
        approximations=[scaled_angular_tail(x,q)/C for x in (12.,24.,48.)]
        print('angular:',q,'ratio at x=12,24,48',approximations)
        assert abs(approximations[-1]-1)<.06,(q,approximations)
        assertions+=1
    for n in (2,3,4,6,12,40,200):
        val=pivot_probability(n,1.)
        assert abs(val-1/(2*n-1))<1.e-9,(n,val)
        assertions+=1
    for n in (2,3,4):
        val=pivot_probability(n,2.)
        exact=sum(((-1)**k)*math.comb(n-1,k)/math.sqrt(1+2*k) for k in range(n))
        assert abs(val-exact)<1.e-10
        assertions+=1
    for q in (1.,1.4,1.8,2.,3.,float('inf')):
        K,alpha,beta=sharp_coefficient(q)
        vals=[]
        for n in (200,2000,20000):
            prob=pivot_probability(n,q)
            vals.append(prob/(K*n**(-alpha)*math.log(n)**beta))
        print('pivot:',q,'normalized n=200,2000,20000',vals)
        # Normalized finite-n values may converge slowly for q near 2.
        assert vals[-1]>.15 and vals[-1]<2.6
        assertions+=1
    for n in (2,3,10,100):
        vals=[pivot_probability(n,q) for q in (1.,1.4,2.,3.,float('inf'))]
        print('monotonic',n,vals)
        assert all(x<y for x,y in zip(vals,vals[1:])),(n,vals)
        assertions+=1
    K,alpha,beta=sharp_coefficient(1.)
    assert abs(K-.5)<1.e-12 and abs(alpha-1)<1.e-12 and abs(beta)<1.e-12
    assertions+=1
    K,alpha,beta=sharp_coefficient(2.)
    assert abs(K-1/math.sqrt(2))<1.e-12 and alpha==.5 and beta==-.5
    assertions+=1
    print('PASS',assertions,'numerical and endpoint assertions')


if __name__=='__main__':
    test()
