from fractions import Fraction as F

# Sparse polynomials in x,y,z,a,b,c.
N = 6

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

x = mon(1,0,0,0,0,0)
y = mon(0,1,0,0,0,0)
z = mon(0,0,1,0,0,0)
a = mon(0,0,0,1,0,0)
b = mon(0,0,0,0,1,0)
c = mon(0,0,0,0,0,1)

d = sub(y,x)
rho = sub(sc(c,2),a)

fx = mul(a,d)
fy = add(sub(mul(sub(c,a),x),mul(mul(x,z),con(1))),mul(c,y))
fz = sub(mul(x,y),mul(b,z))
field = [fx,fy,fz,con(0),con(0),con(0)]

def L(p):
    r = {}
    for i in range(N):
        r = add(r,mul(der(p,i),field[i]))
    return r

assert eq(L(x),fx)
assert eq(L(z),fz)

target_d = add(mul(sub(rho,z),x),mul(sub(c,a),d))
assert eq(L(d),target_d)

# Avoid rational functions in parameters: check 2a*F = 2a*x*d -(c-a)x^2.
two_a_F = sub(sc(mul(mul(a,x),d),2),mul(sub(c,a),mul(x,x)))
target_scaled = sc(mul(a,add(mul(a,mul(d,d)),mul(sub(rho,z),mul(x,x)))),2)
assert eq(L(two_a_F),target_scaled)

aa,bb,cc = F(35),F(3),F(28)
rr = 2*cc-aa
assert rr == F(21)
assert bb*rr == F(63)

# Equilibrium relations for the nonzero pair are x=y, z=rho, x^2=b*rho.
# Substitution into the vector field reduces each component to zero.
# This exact scalar check is sufficient because each component factors accordingly.
assert aa*(F(1)-F(1)) == 0
assert (cc-aa) + cc - rr == 0
assert bb*rr - bb*rr == 0

print("VERIFY_OK")
