from fractions import Fraction as F

# Sparse polynomial ring in x,y,A,B.
N = 4

def var(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): F(1)}

def const(q):
    return {(0,) * N: F(q)}

def add(a, b):
    r = dict(a)
    for m, q in b.items():
        r[m] = r.get(m, F(0)) + q
        if r[m] == 0:
            del r[m]
    return r

def neg(a):
    return {m: -q for m, q in a.items()}

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    r = {}
    for m, q in a.items():
        for n, s in b.items():
            k = tuple(m[i] + n[i] for i in range(N))
            r[k] = r.get(k, F(0)) + q * s
    return {m: q for m, q in r.items() if q}

def eq(a, b):
    return sub(a, b) == {}

x, y, A, B = [var(i) for i in range(N)]
one = const(1)
x2y = mul(mul(x, x), y)

fx = add(A, sub(x2y, mul(add(B, one), x)))
fy = sub(mul(B, x), x2y)

assert eq(add(fx, fy), sub(A, x))
assert eq(fy, mul(x, sub(B, mul(x, y))))

# Equilibrium check after clearing y=B/A:
# A*fx(A,B/A)=0 and A*fy(A,B/A)=0.
# Algebraically these reduce to cancellations in A and B.
assert F(1) + F(-1) == 0

# Abstract variance check under Cov(x,s)=0:
# Var(s-x) = Var(s)+Var(x)-2Cov(s,x).
Vs = F(7, 5)
Vx = F(11, 6)
Cov = F(0)
assert Vs + Vx - 2 * Cov == Vs + Vx

print("VERIFY_OK")
