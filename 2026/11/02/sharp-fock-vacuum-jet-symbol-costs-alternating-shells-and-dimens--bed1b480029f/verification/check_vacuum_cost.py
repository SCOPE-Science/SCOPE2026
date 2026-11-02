"""Supplementary exact combinatorial and numerical checks for Fock vacuum-jet costs.
Run: python verification/check_vacuum_cost.py
Dependencies for numerical shell checks: numpy, scipy.  No certification of
infinite-dimensional or global uniqueness claims is asserted by this program.
"""
from fractions import Fraction
from math import factorial, comb
from itertools import product


def laguerre_coeffs(n, alpha):
    return [Fraction((-1)**j * comb(n+alpha, n-j), factorial(j)) for j in range(n+1)]


def moment_of_poly(coeffs, shape):
    return sum(c * factorial(shape+j-1) for j,c in enumerate(coeffs)) / factorial(shape-1)


def multiply(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def exact_checks():
    count=0
    for d,N in product(range(1,6),range(1,9)):
        q=laguerre_coeffs(N,d)
        assert moment_of_poly(q,d)==1
        count+=1
        for k in range(1,N+1):
            # Moment under gamma(shape=d+k), equals zero.
            assert moment_of_poly(q,d+k)==0
            count+=1
        q0=laguerre_coeffs(N,d-1)
        assert q==[sum(laguerre_coeffs(j,d-1)[i] if i<=j else 0 for j in range(N+1)) for i in range(N+1)]
        count+=1
    for d,m in product(range(1,6),range(0,7)):
        q=laguerre_coeffs(m,d)
        norm=moment_of_poly(multiply(q,q),d)
        assert norm==comb(m+d,d)
        assert sum(q[j]*Fraction(0)**j for j in range(len(q))) == comb(m+d,d)
        count+=2
    return count


def numeric_checks():
    import numpy as np
    from scipy.optimize import root
    from scipy.stats import gamma
    from scipy.special import eval_genlaguerre
    count=0
    estimates=[]
    for d in (1,2,3):
        for N in (1,2,3,4):
            def moments(y):
                rs=np.cumsum(np.exp(y))
                return [(-1)**N+2*sum((-1)**j*gamma.cdf(rs[j],a=d+k) for j in range(N)) for k in range(1,N+1)]
            sol=root(moments,np.log(np.linspace(1.0,2.5,N)),tol=1e-11)
            assert np.linalg.norm(moments(sol.x))<1e-9
            roots=np.cumsum(np.exp(sol.x))
            assert np.all(roots>0) and np.all(np.diff(roots)>0)
            count+=3
            J=(-1)**N+2*sum((-1)**j*gamma.cdf(roots[j],a=d) for j in range(N))
            assert J>0
            M=1/J
            assert comb(N//2+d,d)-1e-7 <=M <= 2**d*comb(N+d,d)+1e-7
            count+=2
            # Quadrature rooted in the exact gamma CDF formula.
            for k in range(1,N+1):
                val=(-1)**N+2*sum((-1)**j*gamma.cdf(roots[j],a=d+k) for j in range(N))
                assert abs(val)<1e-9
                count+=1
            estimates.append((d,N,round(M,6)))
    for d in (1,2,3):
        for N in (1,2,3,4):
            # Sample the classical Fejer-Laguerre inequality used in the
            # constructive upper bound; the proof invokes a Weyl unitary.
            x=np.linspace(0,3*N+10,2000)
            v=np.exp(-x/2)*eval_genlaguerre(N,0,x)
            assert np.max(np.abs(v))<=1+2e-12
            count+=1
    print('exact checks:',exact_checks())
    print('numeric checks:',count)
    print('low-order optimal symbol costs:',estimates)
    return count


if __name__=='__main__':
    n1=exact_checks();n2=numeric_checks()
    print('PASS, supplementary checks:',n1+n2)
