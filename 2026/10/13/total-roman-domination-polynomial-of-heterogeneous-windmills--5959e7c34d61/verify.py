from itertools import product
from collections import Counter
from math import prod

CASES = [(2,2),(2,3),(3,3),(2,2,2),(2,2,3),(2,4)]


def conv(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def poly_pow(base, n):
    out = [1]
    for _ in range(n):
        out = conv(out, base)
    return out


def add(a, b, scale=1):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + scale*(b[i] if i < len(b) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def shift(a, k):
    return [0]*k + a


def T(m):
    return add(add(poly_pow([1,1,1], m), poly_pow([1,1], m), -1), [0]*m + [1])


def U(m):
    q = T(m)
    if len(q) <= 2:
        q += [0]*(3-len(q))
    q[2] -= m
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q


def formula(ms):
    M = sum(ms)
    c2 = shift(add(poly_pow([1,1,1], M), [1], -1), 2)
    c1 = shift(prod_poly(T(m) for m in ms), 1)
    c0 = add(prod_poly(U(m) for m in ms), [0]*M + [1], -1)
    return add(add(c2, c1), c0)


def prod_poly(polys):
    out = [1]
    for p in polys:
        out = conv(out, p)
    return out


def graph(ms):
    # vertex 0 is the universal center; blades occupy consecutive blocks
    blades = []
    v = 1
    for m in ms:
        B = list(range(v, v+m))
        blades.append(B)
        v += m
    n = v
    adj = [set() for _ in range(n)]
    for u in range(1, n):
        adj[0].add(u); adj[u].add(0)
    for B in blades:
        for i, u in enumerate(B):
            for w in B[i+1:]:
                adj[u].add(w); adj[w].add(u)
    return adj


def is_trdf(labels, adj):
    n = len(labels)
    for v in range(n):
        if labels[v] == 0 and not any(labels[u] == 2 for u in adj[v]):
            return False
    positive = {v for v, a in enumerate(labels) if a > 0}
    for v in positive:
        if not any(u in positive for u in adj[v]):
            return False
    return True


def brute(ms):
    adj = graph(ms)
    counts = Counter()
    valid = 0
    for labels in product((0,1,2), repeat=len(adj)):
        if is_trdf(labels, adj):
            w = sum(labels)
            counts[w] += 1
            valid += 1
    p = [0]*(2*len(adj)+1)
    for w,c in counts.items():
        p[w] = c
    return p, valid


def eval1(p):
    return sum(p)

labelings = 0
valid_functions = 0
coefficient_checks = 0
minimum_checks = 0
total_checks = 0
max_order = 0
for ms in CASES:
    M = sum(ms)
    n = M + 1
    max_order = max(max_order, n)
    labelings += 3**n
    b, valid = brute(ms)
    f = formula(ms)
    f += [0]*(len(b)-len(f))
    b += [0]*(len(f)-len(b))
    assert b == f, (ms, b, f)
    valid_functions += valid
    coefficient_checks += len(b)
    nz = [i for i,c in enumerate(b) if c]
    assert nz[0] == 3
    assert b[3] == M
    minimum_checks += 1
    total_formula = 3**M + prod(3**m - 2**m + 1 for m in ms) + prod(3**m - 2**m + 1 - m for m in ms) - 2
    assert valid == total_formula
    total_checks += 1

print(f"VERIFY_OK cases={len(CASES)} labelings={labelings} valid_functions={valid_functions} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} total_checks={total_checks} max_order={max_order}")
