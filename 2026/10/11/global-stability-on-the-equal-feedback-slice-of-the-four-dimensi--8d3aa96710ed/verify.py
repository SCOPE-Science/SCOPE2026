from collections import defaultdict

# Dependency-free exact commutative-polynomial checker.
def add(P, Q):
    R = defaultdict(int)
    R.update(P)
    for m, c in Q.items():
        R[m] += c
    return {m: c for m, c in R.items() if c}

def neg(P):
    return {m: -c for m, c in P.items()}

def sub(P, Q):
    return add(P, neg(Q))

def mul(P, Q):
    R = defaultdict(int)
    for m, c in P.items():
        for n, d in Q.items():
            R[tuple(sorted(m + n))] += c * d
    return {m: c for m, c in R.items() if c}

def scale(c, P):
    return {m: c * v for m, v in P.items() if c * v}

def atom(name):
    return {(name,): 1}

x, y, z, u, a, b, h, s, k = map(atom, ('x', 'y', 'z', 'u', 'a', 'b', 'h', 's', 'k'))
xd = add(add(add(mul(h, y), neg(mul(a, x))), mul(y, z)), mul(s, u))
yd = add(add(add(mul(h, x), neg(mul(b, y))), neg(mul(x, z))), mul(s, u))
ud = neg(mul(k, add(x, y)))

lhs = add(
    add(scale(2, mul(k, mul(x, xd))), scale(2, mul(k, mul(y, yd)))),
    scale(2, mul(s, mul(u, ud))),
)
Q = add(add(mul(a, mul(x, x)), scale(-2, mul(h, mul(x, y)))), mul(b, mul(y, y)))
rhs = scale(-2, mul(k, Q))
assert sub(lhs, rhs) == {}, sub(lhs, rhs)

left = sub(mul(add(a, b), add(a, b)), scale(4, mul(a, b)))
right = mul(sub(a, b), sub(a, b))
assert sub(left, right) == {}

print('VERIFY_OK')
