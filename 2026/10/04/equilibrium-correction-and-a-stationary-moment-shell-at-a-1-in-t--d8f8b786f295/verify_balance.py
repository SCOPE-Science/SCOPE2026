#!/usr/bin/env python3
from collections import defaultdict

# Sparse polynomials in variables (x,y,z,b), keyed by exponent tuples.
def add(*ps):
    out = defaultdict(int)
    for p in ps:
        for m, c in p.items():
            out[m] += c
    return {m:c for m,c in out.items() if c}

def scale(p, k):
    return {m:k*c for m,c in p.items() if k*c}

def mul(p, q):
    out = defaultdict(int)
    for m,c in p.items():
        for n,d in q.items():
            out[tuple(a+b for a,b in zip(m,n))] += c*d
    return {m:c for m,c in out.items() if c}

def deriv(p, i):
    out = defaultdict(int)
    for m,c in p.items():
        if m[i]:
            n = list(m)
            out[tuple(n[:i]+[n[i]-1]+n[i+1:])] += c*m[i]
    return {m:c for m,c in out.items() if c}

def var(i):
    m=[0,0,0,0]; m[i]=1
    return {tuple(m):1}

one={(0,0,0,0):1}
x,y,z,b = (var(i) for i in range(4))
x2=mul(x,x); x3=mul(x2,x)

xd = add(scale(x,-1), y, z)
yd = add(mul(x,y), scale(z,-1))
zd = add(scale(mul(x,z),-1), y, b)
F = add(x2, scale(x,-2), scale(y,-2), scale(z,2))
lie = add(mul(deriv(F,0),xd), mul(deriv(F,1),yd), mul(deriv(F,2),zd))
expected = scale(add(x2, scale(x,-1), scale(b,-1)),-2)
assert lie == expected

cubic = add(x3, scale(mul(b,x),-1), scale(x,-1), scale(b,-1))
quadratic = add(x2, scale(x,-1), scale(b,-1))
factored = mul(add(x,one), quadratic)
assert cubic == factored

print('VERIFY_OK')
