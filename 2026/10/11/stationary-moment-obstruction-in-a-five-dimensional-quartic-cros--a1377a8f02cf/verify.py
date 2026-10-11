#!/usr/bin/env python3
from fractions import Fraction as Q
N = 10
def var(i):
    ex = [0]*N
    ex[i] = 1
    return {tuple(ex): Q(1)}
def add(p,q):
    r = dict(p)
    for m,c in q.items():
        r[m] = r.get(m,Q(0)) + c
        if not r[m]:
            del r[m]
    return r
def neg(p):
    return {m:-c for m,c in p.items()}
def sub(p,q):
    return add(p,neg(q))
def mul(p,q):
    r = {}
    for m,c in p.items():
        for n,d in q.items():
            k = tuple(m[i]+n[i] for i in range(N))
            r[k] = r.get(k,Q(0)) + c*d
    return {m:c for m,c in r.items() if c}
a,b,c,d,e,x,y,z,u,v = [var(i) for i in range(N)]
P = mul(mul(mul(mul(x,y),z),u),v)
Fx = sub(mul(a,x), mul(mul(mul(y,z),u),v))
Fy = add(neg(mul(b,y)), mul(mul(mul(x,z),u),v))
Fz = add(neg(mul(c,z)), mul(mul(mul(x,y),u),v))
Fu = add(neg(mul(d,u)), mul(mul(mul(x,y),z),v))
Fv = add(neg(mul(e,v)), mul(mul(mul(x,y),z),u))
assert mul(x,Fx) == sub(mul(mul(a,x),x), P)
assert mul(y,Fy) == add(neg(mul(mul(b,y),y)), P)
assert mul(z,Fz) == add(neg(mul(mul(c,z),z)), P)
assert mul(u,Fu) == add(neg(mul(mul(d,u),u)), P)
assert mul(v,Fv) == add(neg(mul(mul(e,v),v)), P)
print("VERIFY_OK")
