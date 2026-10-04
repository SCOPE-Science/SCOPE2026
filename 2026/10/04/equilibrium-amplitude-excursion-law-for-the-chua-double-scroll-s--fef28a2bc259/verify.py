from fractions import Fraction as F

# Sparse polynomial ring in x,y,z,alpha,beta,m0,m1.
N = 7

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

x,y,z,alpha,beta,m0,m1 = [v(i) for i in range(N)]

def L(p,h):
    fx = mul(alpha, sub(y,h))
    fy = add(sub(x,y),z)
    fz = neg(mul(beta,y))
    field = [fx,fy,fz,c(0),c(0),c(0),c(0)]
    r = {}
    for i in range(N):
        r = add(r,mul(der(p,i),field[i]))
    return r

# Three affine branches of h.
h_inner = mul(m0,x)
h_pos = add(mul(m1,x), sub(m0,m1))
h_neg = sub(mul(m1,x), sub(m0,m1))

x2_over_2 = scale(mul(x,x), F(1,2))
weighted = scale(add(mul(beta,mul(y,y)),mul(z,z)), F(1,2))
target_weighted = mul(beta, sub(mul(x,y),mul(y,y)))

for h in (h_inner,h_pos,h_neg):
    assert eq(L(x2_over_2,h), mul(alpha,mul(x,sub(y,h))))
    assert eq(L(weighted,h), target_weighted)

# Canonical double-scroll slopes from the rigorous source.
M0 = F(-1,7)
M1 = F(2,7)
r = (M1-M0)/M1
assert r == F(3,2)

def h_can(q):
    q = F(q)
    if q >= 1:
        return M1*q + (M0-M1)
    if q <= -1:
        return M1*q - (M0-M1)
    return M0*q

for q in (F(-3,2), F(0), F(3,2)):
    assert h_can(q) == 0

# Exact equilibrium equations at x in {-r,0,r}, y=0, z=-x.
A = F(9)
B = F(100,7)
for X in (-r,F(0),r):
    Y = F(0)
    Z = -X
    assert A*(Y-h_can(X)) == 0
    assert X-Y+Z == 0
    assert -B*Y == 0

# Canonical sign geometry of q=x*h(x).
assert F(1,2)*h_can(F(1,2)) < 0
assert F(5,4)*h_can(F(5,4)) < 0
assert F(2)*h_can(F(2)) > 0
assert F(-2)*h_can(F(-2)) > 0

print("VERIFY_OK")
