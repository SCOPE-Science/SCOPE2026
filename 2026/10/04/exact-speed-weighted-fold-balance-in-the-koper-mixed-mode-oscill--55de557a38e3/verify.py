from fractions import Fraction as F
import math

# Sparse polynomial ring in x,y,z,eps,delta,k,lam.
N = 7

def var(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): F(1)}

def const(q):
    return {(0,) * N: F(q)}

def add(p, q):
    out = dict(p)
    for m, a in q.items():
        out[m] = out.get(m, F(0)) + a
        if out[m] == 0:
            del out[m]
    return out

def neg(p):
    return {m: -a for m, a in p.items()}

def sub(p, q):
    return add(p, neg(q))

def mul(p, q):
    out = {}
    for e, a in p.items():
        for f, b in q.items():
            g = tuple(e[i] + f[i] for i in range(N))
            out[g] = out.get(g, F(0)) + a * b
    return {m: a for m, a in out.items() if a}

def powp(p, n):
    out = const(1)
    for _ in range(n):
        out = mul(out, p)
    return out

def der(p, i):
    out = {}
    for m, a in p.items():
        if m[i]:
            n = list(m)
            n[i] -= 1
            n = tuple(n)
            out[n] = out.get(n, F(0)) + a * m[i]
    return {m: a for m, a in out.items() if a}

def eq(p, q):
    return sub(p, q) == {}

x, y, z, eps, delta, k, lam = [var(i) for i in range(N)]
c = sub(powp(x, 3), mul(const(3), x))

# Clear eps in xdot: eps*xdot = y-c.
X = sub(y, c)  # eps * xdot
Y = add(add(mul(k, x), neg(mul(const(2), add(y, lam)))), z)  # ydot
Z = mul(delta, add(add(lam, y), neg(z)))  # zdot

# Check the identity after multiplying by eps:
# eps*yddot + (2+d)*eps*ydot + d*eps*y
# = k*(eps*xdot) + d*k*eps*x - d*eps*lam.
# eps*yddot = k*(eps*xdot) - 2*eps*ydot + eps*zdot.
eps_yddot = add(add(mul(k, X), neg(mul(const(2), mul(eps, Y)))), mul(eps, Z))
lhs = add(add(eps_yddot, mul(add(const(2), delta), mul(eps, Y))), mul(delta, mul(eps, y)))
rhs = add(add(mul(k, X), mul(delta, mul(k, mul(eps, x)))), neg(mul(delta, mul(eps, lam))))
assert eq(lhs, rhs)

# Abstract regression variance algebra.
EA = F(7, 5)
EB = EA
EB2 = F(19, 6)
EAB = EB2
EA2 = F(23, 5)
lhs_v = (EA2 - EA*EA) - (EB2 - EB*EB)
rhs_v = EA2 - 2*EAB + EB2
assert lhs_v == rhs_v

r1sq = F(1) + F(1, 10) / 3
r2sq = F(1) + F(1, 100) / 3
assert r1sq == F(31, 30)
assert r2sq == F(301, 300)
assert abs(math.sqrt(float(r1sq)) - 1.016530) < 1e-6
assert abs(math.sqrt(float(r2sq)) - 1.001665) < 1e-6

print("VERIFY_OK")
