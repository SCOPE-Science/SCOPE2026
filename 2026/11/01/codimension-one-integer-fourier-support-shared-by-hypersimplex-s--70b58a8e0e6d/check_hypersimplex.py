#!/usr/bin/env python3
"""Arithmetic and alternate integration checks for hypersimplex Fourier claim."""
from itertools import product, combinations
from math import comb, pi
import cmath


def alternating_factor(n, s):
    return sum((-1)**j * comb(n,j) * (s-j) for j in range(s))

def simple_double_formula(n, s, k):
    assert len(k) == n and 1 <= s < n
    groups = {}
    for i, v in enumerate(k): groups.setdefault(v, []).append(i)
    pairs = [(a, ind) for a, ind in groups.items() if len(ind)==2]
    assert len(pairs)==1 and all(len(ind)==1 for a, ind in groups.items() if a!=pairs[0][0])
    a, indices = pairs[0]
    denom = 1
    for j, v in enumerate(k):
        if j not in indices: denom *= 2j*pi*(v-a)
    return ((-1)**(s-1)*comb(n-2,s-1))/denom

def validate_combinatorics():
    checks = 0
    for n in range(3, 24):
        for s in range(1, n):
            assert alternating_factor(n,s) == (-1)**(s-1)*comb(n-2,s-1)
            assert alternating_factor(n,s) == (-1)**n * alternating_factor(n,n-s)
            checks += 2
    for n in (4,5,6,7):
        for N in (1,2,3):
            m = 2*N+1
            single = 0; distinct = 0; multi = 0
            for a in product(range(-N,N+1), repeat=n-1):
                k = a+(0,)
                equal = [(i,j) for i,j in combinations(range(n),2) if k[i]==k[j]]
                if len(equal)==0: distinct += 1
                elif len(equal)==1: single +=1
                else:multi +=1
            assert single+distinct+multi==m**(n-1)
            assert single <= comb(n,2)*m**(n-2)
            # The difference must have at least two equalities, hence lower dimension.
            assert 0 <= comb(n,2)*m**(n-2)-single <= (comb(n,2)**2)*m**(n-3)
            checks+=4
    return checks

def direct_quadrature(n,s,k):
    """Numerically integrate last coordinate exactly, other one/two via scipy.quad.
    Boundaries are explicitly partitioned along x1+x2=1 for n=4,s=2.
    This calculation does not use residues or the formula being checked.
    """
    from scipy.integrate import quad
    def inner(prefix):
        sm=sum(prefix); lo=max(0,s-sm-1);hi=min(1,s-sm)
        if hi<=lo: return 0j
        w=k[n-2]
        if w:
            by=(cmath.exp(-2j*pi*w*hi)-cmath.exp(-2j*pi*w*lo))/(-2j*pi*w)
        else: by=hi-lo
        return cmath.exp(-2j*pi*sum(k[i]*prefix[i] for i in range(n-2)))*by
    def complex_quad(fun,a,b):
        re=quad(lambda x:fun(x).real,a,b,epsabs=5e-12,limit=200)[0]
        im=quad(lambda x:fun(x).imag,a,b,epsabs=5e-12,limit=200)[0]
        return re+1j*im
    if n==3:
        return complex_quad(lambda x:inner((x,)),0,1)
    if n==4 and s==2:
        return complex_quad(lambda x: complex_quad(lambda y:inner((x,y)),0,1-x)+complex_quad(lambda y:inner((x,y)),1-x,1),0,1)
    raise ValueError('quadrature only set up in dimension 2 or central dimension 3')

def validate_numerical():
    tests = [(3,1,(1,1,0)),(3,2,(1,1,0)),(3,1,(1,2,0)),
       (4,2,(1,1,2,0)),(4,2,(1,2,3,0)),(4,2,(1,0,2,0)),
       (4,2,(3,4,3,0))]
    for n,s,k in tests:
        if len(set(k))==n:
            predicted=0j
        elif sum(comb(k.count(x),2) for x in set(k))==1:
            predicted=simple_double_formula(n,s,k)
        else:
            raise AssertionError('test requires no or exactly one collision')
        integral=direct_quadrature(n,s,k)
        err=abs(integral-predicted)
        assert err<5e-10,(n,s,k,integral,predicted,err)
    # Low-discrepancy independent cubature for the first non-simplex hypersimplices.
    # Integrate the fourth coordinate analytically and sample the first three.
    from scipy.stats import qmc
    import numpy as np
    xyz=qmc.Sobol(d=3,scramble=False).random_base2(m=18)
    sums=xyz.sum(axis=1)
    for s in (2,3):
        for k in ((1,1,2,3,0),(1,2,3,4,0)):
            lo=np.maximum(0,s-sums-1)
            hi=np.minimum(1,s-sums)
            interval=np.where(hi>lo,hi-lo,0.0)
            # The fourth frequency was deliberately selected as zero.
            assert k[3] in (3,4)
            w=k[3]
            v=(np.exp(-2j*pi*w*hi)-np.exp(-2j*pi*w*lo))/(-2j*pi*w)
            v=np.where(hi>lo,v,0j)
            direct=np.mean(np.exp(-2j*pi*(xyz @ np.asarray(k[:3])))*v)
            pred=simple_double_formula(5,s,k) if len(set(k))==4 else 0j
            assert abs(direct-pred)<5e-5, (s,k,direct,pred)
            tests.append((5,s,k))
    return len(tests)

if __name__=='__main__':
    a=validate_combinatorics()
    b=validate_numerical()
    print(f'PASS: {a} exact combinatorial checks and {b} direct numerical integrals')
