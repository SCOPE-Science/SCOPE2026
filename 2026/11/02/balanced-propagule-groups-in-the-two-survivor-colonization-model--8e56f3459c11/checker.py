#!/usr/bin/env python3
"""Exact-arithmetic consistency checks for binomial two-survivor founding allocations.
The written analytic proof, rather than this finite program, covers arbitrary N and p.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb

checks = 0

def check(assertion, description):
    global checks
    checks += 1
    if not assertion:
        raise AssertionError(description)

def f(n, p):
    assert n >= 0 and 0 < p < 1
    if n < 2:
        return Fraction(0)
    q = 1-p
    return 1-q**n-n*p*q**(n-1)

@lru_cache(maxsize=None)
def partitions(n, lower=2):
    if n == 0:
        return ((),)
    if n < lower:
        return ()
    out=[]
    for k in range(lower,n+1):
        for rest in partitions(n-k,k):
            out.append((k,)+rest)
    return tuple(out)

def balanced(N,k):
    a,r=divmod(N,k)
    assert a>=2
    return (a,)*(k-r)+(a+1,)*r

def poly_add(a,b):
    n=max(len(a),len(b)); return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n))

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return tuple(c)

def poly_scale(a,k):return tuple(k*x for x in a)

def polynomial_f(n):
    # (1-p)^n and n*p*(1-p)^(n-1) via exact binomial coefficients
    qn=tuple(comb(n,i)*(-1)**i for i in range(n+1))
    qnp=poly_mul((0,n),tuple(comb(n-1,i)*(-1)**i for i in range(n))) if n else (0,)
    return poly_add((1,),poly_scale(poly_add(qn,qnp),-1))

f2,f3,f6=(polynomial_f(n) for n in (2,3,6))
lhs=poly_add(f6,poly_scale(f3,-2))
rhs=poly_mul((0,0,1),poly_mul((3,-3,1),(3,-9,5)))
check(lhs==rhs, 'six-versus-two-three factorization')
check(poly_add(poly_scale(f3,2),poly_scale(f2,-3))==(0,0,3,-4), 'two-three-versus-three-pairs factorization')

for p in (Fraction(i,41) for i in range(1,41)):
    for N in range(2,19):
        entries=partitions(N)
        allvals=[(sum((f(x,p) for x in v),Fraction(0)),v) for v in entries]
        best=max(v for v,_ in allvals)
        candidates=[balanced(N,k) for k in range(1,N//2+1)]
        candidates_best=max(sum((f(x,p) for x in v),Fraction(0)) for v in candidates)
        check(best==candidates_best, f'balanced maximum N={N},p={p}')
        for value,v in allvals:
            if value==best:
                check(max(v)-min(v)<=1, f'unbalanced maximizer N={N},p={p}: {v}')

for p in [Fraction(1,101),Fraction(1,8),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(4,5),Fraction(99,100)]:
    for S in range(4,60):
        h=lambda a:f(a,p)+f(S-a,p)
        endpoint=max(h(0),h(S//2))
        for a in range(1,S//2):
            check(h(a)<endpoint, f'pair-endpoint S={S},p={p},a={a}')

p0_lower=Fraction(44,100)
p0_upper=Fraction(45,100)
check(f(6,p0_lower)>2*f(3,p0_lower)>3*f(2,p0_lower), 'low-survival order')
check(2*f(3,p0_upper)>f(6,p0_upper), 'intermediate-survival order')
check(2*f(3,Fraction(3,4))==3*f(2,Fraction(3,4)), '3/4 tie')
print(f'PASS: {checks} exact-rational assertions; max checked N=18; finite checks are not the general proof.')
