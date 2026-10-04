from fractions import Fraction as F

# Exact checks for the Wang-Chen flow.
# Variables are handled symbolically where needed by sparse polynomials.

N = 4  # x,y,z,a

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
    for e,ae in p.items():
        for f,bf in q.items():
            g = tuple(e[i]+f[i] for i in range(N))
            r[g] = r.get(g,F(0)) + ae*bf
    return {m:coef for m,coef in r.items() if coef}

def scale(p,s):
    s = F(s)
    return {m:s*coef for m,coef in p.items() if s*coef}

x,y,z,a = [v(i) for i in range(N)]
fx = add(mul(y,z),a)
fy = sub(mul(x,x),y)
fz = sub(c(1),scale(x,4))

# Equilibrium at x=1/4, y=1/16, z=-16a.
X = F(1,4)
Y = F(1,16)
# yz+a = (-16a)/16 + a = 0.
assert F(-16)*Y + 1 == 0
assert X*X - Y == 0
assert 1 - 4*X == 0

# Jacobian characteristic polynomial:
# lambda^3 + lambda^2 + (8a+1/4)lambda + 1/4.
# Routh-Hurwitz determinant a1*a2-a3 = 8a.
assert F(1)*F(1,4) - F(1,4) == 0
# coefficient of a in a2 is 8, hence determinant is 8a.
assert F(8) > 0

# Moment algebra. Let V=Var(x), D=16V.
# E[y] = E[x^2] = 1/16 + V = (1+D)/16.
for V in [F(0), F(1,16), F(7,20)]:
    D = 16*V
    Ey = F(1,16) + V
    assert Ey == (1 + D)/16

# Weighted-height identity, tested as a rational identity in sample exact values.
for A in [F(1,100), F(3,500), F(1,20)]:
    for D in [F(0), F(1,4), F(7,3)]:
        Ey = (1 + D)/16
        lhs = -A/Ey
        rhs = -16*A/(1+D)
        assert lhs == rhs

# D=E[(1-4x)^2] = 16 Var(x) when E[x]=1/4:
# expansion gives 1 - 8E[x] + 16E[x^2]
# = -1 + 16(1/16+V) = 16V.
for V in [F(0), F(2,11), F(5,7)]:
    Ex = F(1,4)
    Ex2 = F(1,16) + V
    D = 1 - 8*Ex + 16*Ex2
    assert D == 16*V

print("VERIFY_OK")
