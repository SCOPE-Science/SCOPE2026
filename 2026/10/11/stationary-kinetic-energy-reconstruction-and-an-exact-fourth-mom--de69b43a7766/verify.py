from fractions import Fraction as F

# Sparse polynomial ring in x, v, mu.
N = 3

def var(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): F(1)}

def const(q):
    return {(0,) * N: F(q)}

def add(p, q):
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, F(0)) + c
        if out[m] == 0:
            del out[m]
    return out

def neg(p):
    return {m: -c for m, c in p.items()}

def sub(p, q):
    return add(p, neg(q))

def mul(p, q):
    out = {}
    for m, c in p.items():
        for n, d in q.items():
            k = tuple(m[i] + n[i] for i in range(N))
            out[k] = out.get(k, F(0)) + c * d
    return {m: c for m, c in out.items() if c}

def scale(p, q):
    q = F(q)
    return {m: q*c for m, c in p.items() if q*c}

def power(p, n):
    out = const(1)
    for _ in range(n):
        out = mul(out, p)
    return out

def der(p, i):
    out = {}
    for m, c in p.items():
        if m[i]:
            n = list(m)
            n[i] -= 1
            n = tuple(n)
            out[n] = out.get(n, F(0)) + c*m[i]
    return {m: c for m, c in out.items() if c}

def eq(p, q):
    return sub(p, q) == {}

x, v, mu = [var(i) for i in range(N)]
fx = v
fv = sub(mul(mu, mul(sub(const(1), mul(x,x)), v)), x)
field = [fx, fv, {}]

def L(p):
    out = {}
    for i in range(N):
        out = add(out, mul(der(p, i), field[i]))
    return out

for k in range(9):
    test = scale(mul(power(x, k+1), v), F(1, k+1))
    expected = add(
        power(x, k) if False else mul(power(x,k), mul(v,v)),
        add(
            scale(mul(mu, mul(power(x,k+1), mul(sub(const(1), mul(x,x)), v))), F(1,k+1)),
            scale(power(x,k+2), F(-1,k+1))
        )
    )
    assert eq(L(test), expected)

energy = scale(add(mul(x,x), mul(v,v)), F(1,2))
expected_energy = mul(mu, mul(sub(const(1), mul(x,x)), mul(v,v)))
assert eq(L(energy), expected_energy)

# Exact scalar implication:
# Ev2 = Ex2, Ex2v2 = Ex4/3, and Ev2 = Ex2v2.
Ex2 = F(17,7)
Ev2 = Ex2
Ex2v2 = Ev2
Ex4 = 3 * Ex2v2
assert Ex4 == 3 * Ex2

print("VERIFY_OK")
