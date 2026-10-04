from fractions import Fraction as F

# Exact sparse polynomials in variables x,y,z,a,b,c,d,m.
N = 8

def mon(*e):
    return {tuple(e): F(1)}

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

x = mon(1,0,0,0,0,0,0,0)
y = mon(0,1,0,0,0,0,0,0)
z = mon(0,0,1,0,0,0,0,0)
a = mon(0,0,0,1,0,0,0,0)
b = mon(0,0,0,0,1,0,0,0)
c = mon(0,0,0,0,0,1,0,0)
d = mon(0,0,0,0,0,0,1,0)
m = mon(0,0,0,0,0,0,0,1)

fx = add(add(y, neg(mul(a,x))), mul(b,mul(y,z)))
fy = add(add(mul(c,y), neg(mul(x,z))), z)
fz = add(mul(d,mul(x,y)), neg(mul(m,z)))
field = [fx, fy, fz, {}, {}, {}, {}, {}]

def L(p):
    r = {}
    for i in range(N):
        r = add(r, mul(deriv(p,i), field[i]))
    return r

z2 = mul(z,z)
x2 = mul(x,x)

assert equal(L(z), fz)
assert equal(L(z2), add(scale(mul(d,mul(mul(x,y),z)), 2),
                        scale(mul(m,z2), -2)))
assert equal(L(x2), add(add(scale(mul(x,y), 2),
                            scale(mul(a,x2), -2)),
                        scale(mul(b,mul(mul(x,y),z)), 2)))

lhs = add(add(scale(mul(d,L(x2)), F(1,2)),
              neg(L(z))),
          scale(mul(b,L(z2)), F(-1,2)))
rhs = add(add(mul(m,z), mul(b,mul(m,z2))),
          neg(mul(a,mul(d,x2))))
assert equal(lhs, rhs)

print("VERIFY_OK")
