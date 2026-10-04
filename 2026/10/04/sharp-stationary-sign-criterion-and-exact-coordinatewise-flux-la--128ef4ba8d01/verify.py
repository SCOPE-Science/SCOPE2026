from fractions import Fraction as F

# Sparse polynomial ring in x,y,z,a,b,c.
N = 6

def c(q):
    return {(0,)*N: F(q)}

def v(i):
    e = [0]*N
    e[i] = 1
    return {tuple(e): F(1)}

def add(p,q):
    r = dict(p)
    for m,a in q.items():
        r[m] = r.get(m,F(0)) + a
        if r[m] == 0:
            del r[m]
    return r

def neg(p):
    return {m:-a for m,a in p.items()}

def sub(p,q):
    return add(p,neg(q))

def mul(p,q):
    r = {}
    for e,a in p.items():
        for f,b in q.items():
            g = tuple(e[i]+f[i] for i in range(N))
            r[g] = r.get(g,F(0)) + a*b
    return {m:a for m,a in r.items() if a}

def scale(p,s):
    s = F(s)
    return {m:s*a for m,a in p.items() if s*a}

def der(p,i):
    r = {}
    for e,a in p.items():
        if e[i]:
            g = list(e)
            g[i] -= 1
            g = tuple(g)
            r[g] = r.get(g,F(0)) + a*e[i]
    return {m:a for m,a in r.items() if a}

def eq(p,q):
    return sub(p,q) == {}

x,y,z,a,b,cc = [v(i) for i in range(N)]
fx = add(neg(mul(y,z)), mul(a,x))
fy = add(mul(x,z), mul(b,y))
fz = add(scale(mul(x,y), F(1,3)), mul(cc,z))
field = [fx,fy,fz,{}, {}, {}]

def L(p):
    r = {}
    for i in range(N):
        r = add(r,mul(der(p,i),field[i]))
    return r

half_x2 = scale(mul(x,x),F(1,2))
half_y2 = scale(mul(y,y),F(1,2))
half_z2 = scale(mul(z,z),F(1,2))
xyz = mul(mul(x,y),z)

assert eq(L(half_x2), add(neg(xyz), mul(a,mul(x,x))))
assert eq(L(half_y2), add(xyz, mul(b,mul(y,y))))
assert eq(L(half_z2), add(scale(xyz,F(1,3)), mul(cc,mul(z,z))))

# Classical parameters a=5, b=-10, c=-19/5.
A = F(5)
B = F(-10)
C = F(-19,5)
assert A == 5
assert -B == 10
assert -3*C == F(57,5)

# Nonzero equilibrium square relations.
X2 = 3*B*C
Y2 = -3*A*C
Z2 = -A*B
assert X2 == 114
assert Y2 == 57
assert Z2 == 50

# Common equilibrium cubic product Q = 3abc.
Qeq = 3*A*B*C
assert Qeq == A*X2
assert Qeq == (-B)*Y2
assert Qeq == (-3*C)*Z2

print("VERIFY_OK")
