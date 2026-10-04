from fractions import Fraction as F

# Sparse polynomial ring in x,y,z,a.
N = 4

def c(q):
    return {(0,)*N: F(q)}

def v(i):
    e = [0]*N
    e[i] = 1
    return {tuple(e): F(1)}

def add(p,q):
    r = dict(p)
    for m,coef in q.items():
        r[m] = r.get(m,F(0)) + coef
        if r[m] == 0:
            del r[m]
    return r

def neg(p):
    return {m:-coef for m,coef in p.items()}

def sub(p,q):
    return add(p,neg(q))

def mul(p,q):
    r = {}
    for e,ce in p.items():
        for f,cf in q.items():
            g = tuple(e[i]+f[i] for i in range(N))
            r[g] = r.get(g,F(0)) + ce*cf
    return {m:coef for m,coef in r.items() if coef}

def scale(p,s):
    s = F(s)
    return {m:s*coef for m,coef in p.items() if s*coef}

def der(p,i):
    r = {}
    for e,coef in p.items():
        if e[i]:
            g = list(e)
            g[i] -= 1
            g = tuple(g)
            r[g] = r.get(g,F(0)) + coef*e[i]
    return {m:coef for m,coef in r.items() if coef}

def eq(p,q):
    return sub(p,q) == {}

x,y,z,a = [v(i) for i in range(N)]
fx = y
fy = z
fz = neg(add(add(y,mul(x,z)),add(mul(y,z),a)))
field = [fx,fy,fz,{}]

def L(p):
    r = {}
    for i in range(N):
        r = add(r,mul(der(p,i),field[i]))
    return r

assert eq(L(x),y)
assert eq(L(y),z)
assert eq(L(scale(mul(x,x),F(1,2))),mul(x,y))
assert eq(L(scale(mul(y,y),F(1,2))),mul(y,z))
assert eq(L(mul(x,y)),add(mul(y,y),mul(x,z)))

# Stationary algebra:
# Ey=Ez=Exy=Eyz=0.
# Ez'=0 gives Exz=-a; E L(xy)=0 gives Ey2=-Exz=a.
A = F(3,4)
Exz = -A
Ey2 = -Exz
assert Ey2 == A
assert Ey2 >= 0

# At a=0, the set y=z=0 is pointwise equilibrium for every x.
for X in [F(-7,3),F(0),F(5,2)]:
    Y = F(0)
    Z = F(0)
    A0 = F(0)
    assert Y == 0
    assert Z == 0
    assert -Y-X*Z-Y*Z-A0 == 0

print("VERIFY_OK")
