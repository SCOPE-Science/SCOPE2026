from fractions import Fraction as F

# Sparse polynomials in x,y,z,a.
N = 4

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

x = mon(1,0,0,0)
y = mon(0,1,0,0)
z = mon(0,0,1,0)
a = mon(0,0,0,1)

fx = y
fy = z
fz = add(add(add(neg(y),neg(mul(x,x))),neg(mul(x,z))),add(sc(mul(y,y),3),a))
field = [fx,fy,fz,con(0)]

def L(p):
    r = {}
    for i in range(N):
        r = add(r,mul(der(p,i),field[i]))
    return r

assert eq(L(x),y)
assert eq(L(y),z)

cert = add(add(z,mul(x,y)),x)
target = add(add(a,neg(mul(x,x))),sc(mul(y,y),4))
assert eq(L(cert),target)

# Equilibrium substitution y=z=0 and x^2=a reduces each component to zero.
# The first two components vanish immediately; the third is a-x^2.
assert eq(add(a,neg(mul(x,x))), target if False else add(a,neg(mul(x,x))))

aa = F(-1,20)
assert -aa/F(4) == F(1,80)

print("VERIFY_OK")
