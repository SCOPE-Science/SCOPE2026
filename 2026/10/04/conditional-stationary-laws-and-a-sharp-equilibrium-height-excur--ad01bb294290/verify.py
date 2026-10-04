from fractions import Fraction as F

# Sparse polynomials in x,y,z,a,b,c,k,h.
N = 8

def mon(*e):
    return {tuple(e): F(1)}

def con(q):
    return {(0,)*N: F(q)}

def add(p,q):
    r = dict(p)
    for m,v in q.items():
        r[m] = r.get(m,F(0)) + v
        if not r[m]:
            del r[m]
    return r

def neg(p):
    return {m:-v for m,v in p.items()}

def sub(p,q):
    return add(p,neg(q))

def mul(p,q):
    r = {}
    for e,u in p.items():
        for f,v in q.items():
            g = tuple(e[i]+f[i] for i in range(N))
            r[g] = r.get(g,F(0)) + u*v
    return {m:v for m,v in r.items() if v}

def sc(p,s):
    s = F(s)
    return {m:s*v for m,v in p.items() if s*v}

def der(p,i):
    r = {}
    for e,v in p.items():
        if e[i]:
            g = list(e)
            g[i] -= 1
            g = tuple(g)
            r[g] = r.get(g,F(0)) + v*e[i]
    return {m:v for m,v in r.items() if v}

def eq(p,q):
    return sub(p,q) == {}

x = mon(1,0,0,0,0,0,0,0)
y = mon(0,1,0,0,0,0,0,0)
z = mon(0,0,1,0,0,0,0,0)
a = mon(0,0,0,1,0,0,0,0)
b = mon(0,0,0,0,1,0,0,0)
c = mon(0,0,0,0,0,1,0,0)
k = mon(0,0,0,0,0,0,1,0)
h = mon(0,0,0,0,0,0,0,1)

fx = mul(a,sub(y,x))
fy = mul(x,sub(b,mul(k,z)))
fz = sub(mul(h,mul(x,x)),mul(c,z))
field = [fx,fy,fz,con(0),con(0),con(0),con(0),con(0)]

def L(p):
    r = {}
    for i in range(N):
        r = add(r,mul(der(p,i),field[i]))
    return r

assert eq(L(x), fx)
assert eq(L(z), fz)

Fcert = add(
    add(neg(mul(h,mul(x,y))), sc(mul(h,mul(x,x)), F(1,2))),
    add(mul(b,z), neg(sc(mul(k,mul(z,z)), F(1,2))))
)

target = sub(
    sub(mul(mul(k,c),mul(z,z)), mul(mul(b,c),z)),
    mul(mul(a,h), mul(sub(y,x),sub(y,x)))
)
assert eq(L(Fcert), target)

# Equilibria and canonical constants.
aa,bb,cc,kk,hh = F(10),F(40),F(5,2),F(1),F(4)
assert cc/hh == F(5,8)
assert aa*hh/(kk*cc) == F(16)
assert hh/(aa*kk*cc) == F(4,25)
assert bb*cc/(hh*kk) == F(25)

# Check equilibrium equations at x=y=0,z=0 and x=y=±5,z=40.
for X,Y,Z in [(F(0),F(0),F(0)),(F(5),F(5),F(40)),(F(-5),F(-5),F(40))]:
    assert aa*(Y-X) == 0
    assert X*(bb-kk*Z) == 0
    assert hh*X*X-cc*Z == 0

print("VERIFY_OK")
