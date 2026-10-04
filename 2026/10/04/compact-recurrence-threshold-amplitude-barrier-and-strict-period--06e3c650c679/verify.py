from fractions import Fraction as F

# Exact sparse polynomials in variables x,y,z,a,b.
N = 5

def mon(*e):
    return {tuple(e): F(1)}

def con(q):
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

def sc(p, s):
    s = F(s)
    return {k:s*v for k,v in p.items() if s*v}

def der(p, i):
    r = {}
    for e, v in p.items():
        if e[i]:
            g = list(e)
            g[i] -= 1
            g = tuple(g)
            r[g] = r.get(g, F(0)) + v*e[i]
    return {k:v for k,v in r.items() if v}

def eq(p, q):
    return sub(p, q) == {}

x = mon(1,0,0,0,0)
y = mon(0,1,0,0,0)
z = mon(0,0,1,0,0)
a = mon(0,0,0,1,0)
b = mon(0,0,0,0,1)

fx = neg(mul(a,y))
fy = add(x,z)
fz = sub(add(x,mul(y,y)),mul(b,z))
field = [fx,fy,fz,con(0),con(0)]

def L(p):
    r = {}
    for i in range(N):
        r = add(r,mul(der(p,i),field[i]))
    return r

v = add(x,z)

# Six times H1, avoiding fractions.
H1s = add(
    add(
        add(sc(mul(add(b,con(1)),mul(x,y)),6), sc(mul(mul(y,y),y),2)),
        sc(mul(a,mul(y,y)),-3)
    ),
    sc(mul(v,v),-3)
)
target1 = sub(sc(mul(b,mul(v,v)),6),
              sc(mul(mul(a,add(b,con(1))),mul(y,y)),6))
assert eq(L(H1s), target1)

# Denominator-free cubic certificate.
K = {}
for term in [
    sc(mul(mul(a,b),mul(y,z)),6),
    sc(mul(a,mul(x,y)),-6),
    sc(mul(a,mul(mul(y,y),y)),-2),
    sc(mul(mul(a,add(a,mul(b,b))),mul(y,y)),3),
    sc(mul(a,mul(v,v)),3),
    sc(mul(mul(b,add(b,con(1))),mul(x,x)),3),
]:
    K = add(K,term)
target2 = sc(mul(mul(a,mul(y,y)),add(a,mul(b,y))),6)
assert eq(L(K), target2)

# Eliminate x,z to obtain the exact jerk equation for y.
y1 = fy
y2 = L(y1)
y3 = L(y2)
jerk = add(
    add(
        add(y3, mul(b,y2)),
        mul(a,y1)
    ),
    sub(mul(mul(a,add(b,con(1))),y), sc(mul(y,y1),2))
)
assert jerk == {}

print("VERIFY_OK")
