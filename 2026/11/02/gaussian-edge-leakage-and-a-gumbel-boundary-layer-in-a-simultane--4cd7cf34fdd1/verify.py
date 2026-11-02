"""Numerical diagnostics for Gaussian-edge smoothing under common Poisson resets.

Requirements: Python 3, numpy, scipy.
Run: python verify.py
The analytic limiting assertions are proved separately; these finite calculations are consistency checks.
"""
import math
from scipy.integrate import quad
from scipy.special import ndtr, ndtri, exp1, gamma


def upper_gumbel(y):
    return -math.expm1(-math.exp(-y)) if y > -700 else 1.0


def k(beta, x):
    return quad(lambda v: beta * v**(beta-1) * upper_gumbel(x+v),
                0, 120, epsabs=1e-11, epsrel=1e-11, limit=250)[0]


def max_tail(n, t):
    p = float(ndtr(-t))
    if p == 0: return 0.
    return -math.expm1(n * math.log1p(-p))


def finite_crossover(n, beta, x):
    L = math.log(n)
    u = -float(ndtri(1./n))
    def integrand(v):
        if v>=L: return 0.
        t=(u+x/u)/math.sqrt(1-v/L)
        return beta*v**(beta-1)*max_tail(n,t)
    return quad(integrand, 0, min(L,120), epsabs=2e-11,
                epsrel=3e-9, limit=250)[0]


def finite_leakage(n, beta):
    L=math.log(n)
    a=math.sqrt(2*L)
    def integrand(v):
        if v>=L: return 0.
        t=a/math.sqrt(1-v/L)
        return beta*v**(beta-1)*max_tail(n,t)
    return math.sqrt(L)*quad(integrand,0,min(L,120),epsabs=1e-11,
                             epsrel=4e-9,limit=250)[0]


def check():
    count=0
    def verify(ok, name):
        nonlocal count
        if not ok: raise AssertionError(name)
        count += 1

    for beta in [0.5, 1., 2.]:
        for x in [-1., 0., 1.]:
            kk=k(beta,x)
            verify(kk>0., f'positive K {beta}, {x}')
            for n in [1e6, 1e12, 1e30, 1e80]:
                v=finite_crossover(n,beta,x)
                # The asymptotics are logarithmically slow: large n exhibits improvement.
                verify(math.isfinite(v) and v>0, f'finite cross {beta}, {x}, {n}')
            v1=finite_crossover(1e12,beta,x)
            v2=finite_crossover(1e80,beta,x)
            verify(abs(v2/kk-1)<abs(v1/kk-1)+0.004,
                   f'improving cross {beta}, {x}')
            verify(abs(v2/kk-1)<0.065,f'cross magnitude {beta}, {x}')
        ll=gamma(beta+1)/math.sqrt(4*math.pi)
        vals=[]
        for n in [1e6, 1e12, 1e30, 1e80]:
            val=finite_leakage(n,beta)
            verify(val>0 and math.isfinite(val),f'finite leak {beta}, {n}')
            vals.append(val)
        verify(abs(vals[-1]/ll-1)<abs(vals[1]/ll-1)+0.004,
               f'improving leak {beta}')
        verify(abs(vals[-1]/ll-1)<0.05,f'leak magnitude {beta}')
    verify(abs(k(1.,0.)-(0.5772156649015328606+exp1(1)))<1e-10,
           'Euler and exponential-integral constant')
    for beta in [.5,1.,2.]:
        for x in [10.,15.]:
            verify(abs(k(beta,x)/(gamma(beta+1)*math.exp(-x))-1)<.0001,
                   f'upper x asymptotic {beta}, {x}')
        for x in [-30.,-50.]:
            verify(abs(k(beta,x)/(-x)**beta-1)<.06,
                   f'lower x asymptotic {beta}, {x}')
    print('PASS',count,'numerical and exact-identity diagnostics')
    print('beta   K(beta,0)    finite_crossover(1e80,beta,0)    leakage scaled (1e80)    prediction')
    for beta in [.5,1.,2.]:
        print(beta, '%.9g'%k(beta,0), '%.9g'%finite_crossover(1e80,beta,0),
              '%.9g'%finite_leakage(1e80,beta),
              '%.9g'%(gamma(beta+1)/math.sqrt(4*math.pi)))

if __name__=='__main__': check()
