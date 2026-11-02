#!/usr/bin/env python3
"""Independent finite-field, Lie-bracket-matrix checks of a cyclicly labeled 2-step Lie family."""
from collections import Counter
from itertools import product
from math import gcd


def field(q):
    """Arithmetic for small prime fields and GF(4) in basis 1,alpha (alpha^2=alpha+1)."""
    if q == 4:
        def mul(a, b):
            z = 0
            for i in range(2):
                for j in range(2):
                    if ((a >> i)&1) and ((b >> j)&1):
                        z ^= (1 << (i+j))
            if z & 8:
                z ^= 0b1110
            if z & 4:
                z ^= 0b111
            return z
        plus = lambda a, b: a ^ b
        negative = lambda a: a
        inverse = lambda a: next(b for b in range(1, 4) if mul(a,b)==1)
    else:
        assert q in (2,3,5,7,11)
        plus = lambda a,b:(a+b)%q
        negative = lambda a:(-a)%q
        mul = lambda a,b:(a*b)%q
        inverse = lambda a:pow(a,-1,q)
    return plus,negative,mul,inverse


def matrix_rank(columns,n,q):
    plus,negative,mul,inverse=field(q)
    pivots={}
    for col in columns:
        vec=list(col)
        for i in range(n):
            if not vec[i]:
                continue
            if i in pivots:
                coeff=negative(vec[i])
                ref=pivots[i]
                vec=[plus(v,mul(coeff,ref[j])) for j,v in enumerate(vec)]
            else:
                k=inverse(vec[i]); pivots[i]=[mul(k,v) for v in vec]; break
    return len(pivots)


def columns_from_brackets(a,b,w,n,q):
    """Columns of ad_(a*u0+b*u1+w) against u0,u1,v0,...,v(n-1)."""
    plus,negative,_,_=field(q)
    columns=[]
    columns.append([negative(w[j]) for j in range(n)])
    columns.append([negative(w[(j-1)%n]) for j in range(n)])
    for k in range(n):
        col=[0]*n
        col[k]=plus(col[k],a)
        col[(k+1)%n]=plus(col[(k+1)%n],b)
        columns.append(col)
    return columns


def predicted_counts(n,q):
    g=gcd(n,q-1)
    return {0:1,1:g*(q-1),2:q**n-1-g*(q-1),n-1:g*(q-1)*q**(n-1),n:(q*q-1)*q**n-g*(q-1)*q**(n-1)}


def exhaustive(n,q):
    found=Counter()
    for tup in product(range(q), repeat=n+2):
        a,b=tup[:2];w=tup[2:]
        rank=matrix_rank(columns_from_brackets(a,b,w,n,q),n,q)
        found[rank]+=1
    expected=predicted_counts(n,q)
    if any(found[k]!=expected.get(k,0) for k in set(found)|set(expected)):
        raise AssertionError((n,q,dict(found),expected))
    print(f"PASS n={n} q={q} noncentral={q**(n+2)} ranks={dict(sorted(found.items()))}")


def arithmetic_nonpolynomial_check():
    for q,g in [(3,2),(9,4),(27,2),(81,4)]:
        assert gcd(4,q-1)==g
        assert predicted_counts(4,q)[3] == g*(q-1)*q**3

if __name__ == '__main__':
    configs=[(4,2),(4,3),(4,4),(4,5),(4,7),(5,2),(5,3),(6,2)]
    for n,q in configs:
        exhaustive(n,q)
    arithmetic_nonpolynomial_check()
    print('VERIFY_OK')
