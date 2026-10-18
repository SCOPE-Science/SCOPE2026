"""Exact affine toric divisor-class calculation for box-section face fans.

Run with Python 3 and SymPy (tested with SymPy 1.13+).
For a facet d_0=c, enumerate its primitive ray generators and compare
its Smith normal form with the closed theorem. Nothing probabilistic is used.
"""
from itertools import combinations
from math import comb, gcd
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def formula(n, A, B, c):
    assert n >= 2 and A >= B >= 1 and A <= n*B and gcd(A,B)==1
    assert c in (-A, B)
    L=A+B
    S=n*A-c
    if not (0 < S < n*L):
        return None  # d_0=c is not a facet
    k,h=divmod(S,L)
    if h==0:
        D=L
        r=comb(n,k)
    else:
        D=h if k==0 else (L-h if k==n-1 else gcd(L,h))
        r=n*comb(n-1,k)
    assert D > 0 and r >= n
    factors=sorted([1]+[D]*(n-2)+[D*abs(c)])
    return r, factors, k, h, D


def enumerated_rays(n,A,B,c):
    # d_0=c. Choose n-1 of the remaining n coordinates at bounds.
    rays=set()
    for fixed in combinations(range(1,n+1),n-1):
        free=next(i for i in range(1,n+1) if i not in fixed)
        for count_upper in range(n):
            for upper in combinations(fixed,count_upper):
                upper=set(upper)
                d=[None]*(n+1)
                d[0]=c
                for j in fixed:
                    d[j]=B if j in upper else -A
                d[free]=-sum(v for v in d if v is not None)
                if -A<=d[free]<=B:
                    rays.add(tuple(d))
    return sorted(rays)


def smith_data(n,rays):
    # Basis of the trace-zero lattice given by coordinates d_1,...,d_n.
    m=Matrix(n,len(rays),lambda i,j:rays[j][i+1])
    snf=smith_normal_form(m,domain=ZZ)
    return sorted(abs(int(snf[i,i])) for i in range(n))


def check(n,A,B):
    for c in (-A,B):
        pred=formula(n,A,B,c)
        if pred is None: continue
        r,factors,k,h,D=pred
        rays=enumerated_rays(n,A,B,c)
        assert len(rays)==r,(n,A,B,c,r,len(rays))
        for v in rays:
            assert sum(v)==0
            assert gcd(*v)==1
        observed=smith_data(n,rays)
        assert observed==factors,(n,A,B,c,pred,observed)
    return True

if __name__=='__main__':
    tests=0
    for n in range(2,7):
        for B in range(1,6):
            for A in range(B,min(n*B,12)+1):
                if gcd(A,B)!=1: continue
                check(n,A,B)
                tests+=1
    assert formula(3,5,2,-5)[:2]==(3,[1,1,5])
    assert formula(3,5,2,2)[:2]==(6,[1,1,2])
    assert formula(2,3,2,-3)[:2]==(2,[1,3])
    assert formula(2,3,2,2)[:2]==(2,[1,8])
    print('VERIFY_OK checked_parameter_triples=%d n_range=2..6 Liu_Zhu_specialization=matched' % tests)
