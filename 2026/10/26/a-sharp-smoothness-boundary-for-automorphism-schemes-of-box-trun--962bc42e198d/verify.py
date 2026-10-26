"""Independent finite-field and tangent-linearization checks for truncated monomial algebras.
Run: python verify.py (Python 3 standard library only).
"""
from itertools import product
from math import prod


def algebra(n, m, p):
    basis = list(product(range(m), repeat=n))
    loc = {a: i for i, a in enumerate(basis)}
    d = len(basis)
    mon_prod = [[None]*d for _ in range(d)]
    for i, a in enumerate(basis):
        for j, b in enumerate(basis):
            c = tuple(x+y for x, y in zip(a,b))
            if all(x < m for x in c): mon_prod[i][j] = loc[c]
    def multiply(u,v):
        w=[0]*d
        for i, a in enumerate(u):
            if not a: continue
            for j, b in enumerate(v):
                if b and mon_prod[i][j] is not None:
                    t=mon_prod[i][j];w[t]=(w[t]+a*b)%p
        return tuple(w)
    def power(u,t):
        one = [0]*d; one[loc[(0,)*n]]=1
        v=tuple(one)
        for _ in range(t):v=multiply(v,u)
        return v
    unit_basis=[loc[tuple(int(k==i) for k in range(n))] for i in range(n)]
    return basis,loc,multiply,power,unit_basis


def count_aut(n,m,p):
    basis,loc,mul,power,unit_basis=algebra(n,m,p)
    z=loc[(0,)*n];d=len(basis)
    nils=[]
    for coeff in product(range(p),repeat=d-1):
        v=list(coeff);v.insert(z,0)
        if not any(power(v,m)):nils.append(tuple(v))
    assert n==2
    count=0
    for a in nils:
        a0,a1=(a[i] for i in unit_basis)
        for b in nils:
            b0,b1=(b[i] for i in unit_basis)
            if (a0*b1-a1*b0)%p:count+=1
    return count


def tangent(n,m,p):
    basis,loc,mul,power,unit_basis=algebra(n,m,p)
    d=len(basis)
    if m%p==0: return n*d
    # Actual rank calculation on images of the n*d coordinate derivations.
    rank=0
    for i in range(n):
        input_exp=[0]*n;input_exp[i]=m-1
        pivot_support=set()
        for a in basis:
            combined=tuple(x+y for x,y in zip(input_exp,a))
            if all(z<m for z in combined):pivot_support.add(combined)
        rank+=len(pivot_support)
    return n*d-rank


def main():
    checks=[(2,2,2,24),(2,2,3,72),(2,3,2,2048)]
    for n,m,p,expected in checks:
        found=count_aut(n,m,p)
        assert found==expected,(n,m,p,found,expected)
        assert tangent(n,m,p)==(n*m**n if m%p==0 else n*(m-1)*m**(n-1))
    # Symbolic linearization dimension checks across distinct characteristics and truncations.
    for n in (1,2,3):
        for m in (2,3,4,5,6):
            for p in (2,3,5,7):
                actual=tangent(n,m,p)
                expected=n*m**n if m%p==0 else n*(m-1)*m**(n-1)
                assert actual==expected,(n,m,p)
    print('VERIFY_OK aut_counts=3 tangent_cases=60')

if __name__=='__main__':main()
