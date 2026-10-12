#!/usr/bin/env python3
import math

def primes_upto(n):
    ps=[]
    for x in range(2,n+1):
        if all(x%p for p in ps if p*p<=x): ps.append(x)
    return ps

def inv_mod(a,p):
    for u in range(1,p):
        if (a*u)%p==1: return u
    raise AssertionError

def formula_pair(p,q):
    if p==2 or q%p==1: return None
    u=inv_mod(q%p,p)
    assert 2<=u<=p-1
    a=u-1
    b=q-1-(u*q-1)//p
    assert a>=1 and b>=1
    return a,b

def direct_pairs(p,q):
    out=[]
    # From aq+bp=(p-1)(q-1), both exponents are automatically bounded.
    rhs=(p-1)*(q-1)
    for a in range(1,p):
        rem=rhs-a*q
        if rem>0 and rem%p==0:
            b=rem//p
            if b>=1: out.append((a,b))
    return out

ps=primes_upto(200)
for p in ps:
    a=p-1
    assert a*p**(a-1) == p**(a-1)*(p-1)
for i,p in enumerate(ps):
    for q in ps[i+1:]:
        d=direct_pairs(p,q)
        f=formula_pair(p,q)
        expected=[] if f is None else [f]
        assert d==expected,(p,q,d,expected)

assert formula_pair(3,5)==(1,1)
assert formula_pair(5,7)==(2,2)
assert formula_pair(3,11)==(1,3)
assert formula_pair(7,11)==(1,7)
assert formula_pair(7,29) is None
print('VERIFY_OK prime_bound=200 squarefree=15 examples=1225,3993')
