#!/usr/bin/env python3
from fractions import Fraction as F

# Polynomial in variables (x,y,z,a), represented by {exponent_tuple: coefficient}.
ZERO = {}
ONE = {(0,0,0,0): F(1)}

def clean(p):
    return {m:c for m,c in p.items() if c}

def add(*ps):
    out = {}
    for p in ps:
        for m,c in p.items():
            out[m] = out.get(m,F(0)) + c
    return clean(out)

def scale(c,p):
    c = F(c)
    return clean({m:c*v for m,v in p.items()})

def mul(p,q):
    out = {}
    for m,c in p.items():
        for n,d in q.items():
            e = tuple(m[i]+n[i] for i in range(4))
            out[e] = out.get(e,F(0)) + c*d
    return clean(out)

def diff(p,j):
    out = {}
    for m,c in p.items():
        if m[j]:
            e = list(m); e[j] -= 1; e = tuple(e)
            out[e] = out.get(e,F(0)) + c*m[j]
    return clean(out)

def var(j):
    e=[0,0,0,0]; e[j]=1
    return {tuple(e):F(1)}

x,y,z,a = [var(i) for i in range(4)]

f1 = z
f2 = add(scale(-1,x), scale(-1,z))
f3 = add(scale(F(1,10),x), scale(5,y), scale(-1,z), mul(x,y), scale(F(-3,10),mul(x,z)), a)
f = [f1,f2,f3]

def L(p):
    return add(mul(diff(p,0),f1), mul(diff(p,1),f2), mul(diff(p,2),f3))

def sq(p):
    return mul(p,p)

def assert_eq(name, got, want):
    got=clean(got); want=clean(want)
    if got != want:
        raise AssertionError((name,got,want))
    print(name+": OK")

H1 = scale(F(1,2),sq(x))
H2 = scale(F(1,2),sq(add(x,y)))
H3 = mul(x,y)
G = add(z, H2, scale(F(11,10),x), scale(F(1,10),y), scale(F(3,20),sq(x)))

assert_eq("L(x)", L(x), z)
assert_eq("L(y)", L(y), add(scale(-1,x),scale(-1,z)))
assert_eq("L(x^2/2)", L(H1), mul(x,z))
assert_eq("L((x+y)^2/2)", L(H2), add(scale(-1,sq(x)),scale(-1,mul(x,y))))
assert_eq("L(xy)", L(H3), add(mul(y,z),scale(-1,sq(x)),scale(-1,mul(x,z))))
assert_eq("L(G)", L(G), add(a,scale(5,y),scale(-1,sq(x))))
print("All exact polynomial identities verified.")
