from fractions import Fraction as F

# Exact sparse polynomials in variables x,y,z,a.
N = 4

def mon(*e):
    return {tuple(e): F(1)}

def const(q):
    return {(0,)*N: F(q)}

def add(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, F(0)) + v
        if not r[k]:
            del r[k]
    return r

def neg(p):
    return {k: -v for k, v in p.items()}

def sub(p, q):
    return add(p, neg(q))

def mul(p, q):
    r = {}
    for e, u in p.items():
        for f, v in q.items():
            g = tuple(e[i] + f[i] for i in range(N))
            r[g] = r.get(g, F(0)) + u*v
    return {k:v for k,v in r.items() if v}

def scale(p, s):
    s = F(s)
    return {k:s*v for k,v in p.items() if s*v}

def deriv(p, i):
    r = {}
    for e, v in p.items():
        if e[i]:
            g = list(e)
            g[i] -= 1
            g = tuple(g)
            r[g] = r.get(g, F(0)) + v*e[i]
    return {k:v for k,v in r.items() if v}

def equal(p, q):
    return sub(p, q) == {}

x = mon(1,0,0,0)
y = mon(0,1,0,0)
z = mon(0,0,1,0)
a = mon(0,0,0,1)

fx = y
fy = sub(neg(x), mul(y,z))
fz = sub(mul(y,y), a)
field = [fx, fy, fz, const(0)]

def L(p):
    r = {}
    for i in range(N):
        r = add(r, mul(deriv(p,i), field[i]))
    return r

Q = add(add(mul(x,x), mul(y,y)), mul(z,z))

assert equal(L(z), sub(mul(y,y), a))
assert equal(L(Q), scale(mul(a,z), -2))

target_zQ = sub(mul(sub(mul(y,y),a), Q), scale(mul(a,mul(z,z)), 2))
assert equal(L(mul(z,Q)), target_zQ)

target_xy = add(sub(mul(y,y), mul(x,x)), neg(mul(mul(x,y),z)))
assert equal(L(mul(x,y)), target_xy)

print("VERIFY_OK")
