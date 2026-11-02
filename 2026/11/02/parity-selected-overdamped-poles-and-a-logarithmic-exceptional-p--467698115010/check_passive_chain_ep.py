"""Standalone numerical checks for purely damped poles of a terminal-loss path.

Requires Python 3, NumPy, SciPy.  This checks, but does not replace,
the exact Chebyshev/hyperbolic proof stated in RESULT.md.
"""
import math
import numpy as np
from scipy.optimize import brentq


def gcrit(n):
    assert n >= 2 and n % 2 == 0
    def dlog(u):
        return (n+1)*math.tanh((n+1)*u)-n/math.tanh(n*u)
    u=brentq(dlog,1e-12,2.0,xtol=1e-14)
    q=math.exp(-2*n*u)
    return u, math.exp(u)*(1+q*math.exp(-2*u))/(1-q)


def imag_roots_even(n,g):
    u,gc=gcrit(n)
    if g<gc-1e-10: return []
    if abs(g-gc)<1e-10: return [u]
    def val(t):
        q=math.exp(-2*n*t)
        return math.exp(t)*(1+q*math.exp(-2*t))/(1-q)-g
    return [brentq(val, 1e-12,u),brentq(val,u, max(2.,math.log(g)+2))]


def imag_root_odd(n,g):
    def val(u):
        # sinh((n+1)u)/cosh(nu) = exp(u)*(1-exp(-2*(n+1)*u))/(1+exp(-2*n*u))
        return math.exp(u)*(-math.expm1(-2*(n+1)*u))/(1+math.exp(-2*n*u))-g
    return brentq(val,0.0,max(2.0,math.log(g)+2))


def hmatrix(n,g):
    return np.diag(np.ones(n-1), 1) + np.diag(np.ones(n-1), -1) -1j*g*np.diag([0]*(n-1)+[1])


def char_cheb(n,x,g):
    prev=1+0j
    curr=2*x
    for _ in range(2,n+1):
        prev,curr=curr,2*x*curr-prev
    # curr=U_n, prev=U_(n-1)
    return curr+1j*g*prev


def run():
    ntests=0
    # independent char via determinant, away from exact eigenvalues.
    for n in range(2,16):
        for g in [0.21,0.75,1.1,1.7,2.6,7.]:
            mat=hmatrix(n,g)
            for z in [0.23+0.51j, 1.37-0.16j,-1.21+0.42j]:
                ref=np.linalg.det(2*z*np.eye(n)-mat)
                got=char_cheb(n,z,g)
                assert abs(ref-got)<1e-7*max(1,abs(ref)),(n,g,z,ref,got)
                ntests+=1
    # imaginary poles analytically, confirmed by matrix residual and parity.
    for n in range(2,30):
        if n%2==0:
            uc,gc=gcrit(n)
            for g in [gc*0.7,gc,gc*1.15,gc*2.5]:
                us=imag_roots_even(n,g)
                assert len(us)==(0 if g<gc else 1 if g==gc else 2)
                for u in us:
                    eig=-2j*math.sinh(u)
                    p=np.linalg.det(eig*np.eye(n)-hmatrix(n,g))
                    assert abs(p)<2e-5*max(1,abs(eig)**n)
                    ntests+=1
        else:
            for g in [0.25,1,2,5,20]:
                u=imag_root_odd(n,g)
                eig=-2j*math.sinh(u)
                p=np.linalg.det(eig*np.eye(n)-hmatrix(n,g))
                assert abs(p)<2e-5*max(1,abs(eig)**n)
                ntests+=1
    vals=[gcrit(n)[1] for n in range(2,200,2)]
    assert all(x>y>1 for x,y in zip(vals,vals[1:]))
    ntests+=len(vals)-1
    # asymptotic coefficient is tested with finite-size ratios, not certified from them.
    for n in [100,200,500,1000,5000]:
        _,g=gcrit(n)
        scale=2*n*(g-1)-math.log(4*n)
        assert 0.90 < scale < 1.2,(n,scale)
        ntests+=1
    print('PASS:',ntests,'numerical determinant/pole/ordering/asymptotic checks')
    for n in (2,4,6,8,10,20,100):
        u,g=gcrit(n)
        print(f'n={n}: g_c={g:.12f}; u_c={u:.12f}')

if __name__=='__main__':
    run()
