"""Independent finite numerical probes of cross-level radial disk transfer.
Scientific proofs and asymptotic quantifiers remain in RESULT.md.
Requires Python 3, NumPy and SciPy.
"""
import math
import warnings
from scipy.integrate import IntegrationWarning
import numpy as np
from scipy.special import gammaln, iv
from scipy.integrate import quad


def sval(n, x):
    return math.exp((n + 1)*math.log(x) - x - .5*(gammaln(n + 1)+gammaln(n + 2)))


def vector(x):
    end = int(max(x + 16*math.sqrt(x)+40, 80))
    n = np.arange(end+1, dtype=float)
    return np.exp((n+1)*math.log(x)-x-.5*(gammaln(n+1)+gammaln(n+2)))


def verify():
    warnings.filterwarnings("ignore",category=IntegrationWarning)
    tests = 0
    for x in [.06, .35, 1., 1.75, 3.2, 10.1, 35.4, 100.7]:
        for n in range(32):
            y = sval(n,x)
            integ = quad(lambda t: (t**n)*(n+1-t)*math.exp(-t), 0, x,
                         epsabs=1e-13, epsrel=2e-11)[0]/math.exp(.5*(gammaln(n+1)+gammaln(n+2)))
            if n>=24 and x<=1.75:  # integration near underflow still absolute
                assert abs(y-integ)<1e-11
            else:
                assert abs(y-integ)<2e-10*(1+abs(y))
            tests += 1
            if n<31:
                ratio = sval(n+1,x)/y
                assert abs(ratio-x/math.sqrt((n+1)*(n+2))) <2e-12*max(1,ratio)
                tests += 1
        v = vector(x)
        hs = x*math.exp(-2*x)*iv(1,2*x)
        assert abs(np.sum(v*v)-hs)<2e-9*max(1,hs)
        tests += 1
        assert max(v)<1/math.sqrt(2*math.pi)
        tests += 1
    for n in range(40):
        x = n+1
        xn = x+.003
        b = sval(n,x)
        assert b > sval(n,xn)
        assert b > sval(n,max(x-.003,.0001))
        tests += 2
        if n<39:
            assert sval(n+1,n+2)>b
            tests += 1
    for x in [100.,400.,1600.]:
        v=vector(x)
        assert abs(max(v)-1/math.sqrt(2*math.pi))<.01
        tests += 1
        for p in [.5,1.,2.,3.,4.]:
            ratio=sum(v**p)/math.sqrt(x)
            target=(2*math.pi)**((1-p)/2)/math.sqrt(p)
            assert abs(ratio-target)/target < .04
            tests+=1
        for eta in [.05,.15,.25,.35]:
            observed=sum(v>eta)/math.sqrt(x)
            target=2*math.sqrt(2*math.log(1/(math.sqrt(2*math.pi)*eta)))
            assert abs(observed-target)<.20
            tests += 1
    for x in [50., 100., 500., 1000.]:
        n=int(x)
        for u in [-2.,-1.,0.,1.,2.]:
            k=int(x+u*math.sqrt(x))
            observed=sval(k,x)
            target=math.exp(-u*u/2)/math.sqrt(2*math.pi)
            assert abs(observed-target)<.03
            tests+=1
    print(f"PASS: {tests} finite numerical checks (not an infinite-dimensional proof)")

if __name__=='__main__':
    verify()
