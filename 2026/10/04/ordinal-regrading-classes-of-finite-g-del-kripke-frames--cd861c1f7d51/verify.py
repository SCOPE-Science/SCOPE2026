#!/usr/bin/env python3
from itertools import product
from math import comb, factorial

def stirling2(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + j * dp[i - 1][j]
    return dp[n][k]

def ordered_bell(n):
    return sum(factorial(k) * stirling2(n, k) for k in range(n + 1))

def T(N):
    return sum(comb(N, s) * (2 ** (N - s)) * ordered_bell(s) for s in range(N + 1))

def signature(tup, top):
    # 0 and top are distinguished endpoints; interior values are rank-compressed.
    interiors = sorted({x for x in tup if x not in (0, top)})
    rank = {x: i + 1 for i, x in enumerate(interiors)}
    k = len(interiors)
    return (k, tuple(0 if x == 0 else (k + 1 if x == top else rank[x]) for x in tup))

expected = [None, 3, 11, 51, 299]
for N in range(1, 5):
    top = N + 1
    sigs = {signature(t, top) for t in product(range(top + 1), repeat=N)}
    assert len(sigs) == expected[N] == T(N), (N, len(sigs), T(N))

# Formula representation:
# ('p', i), ('bot',), ('and',a,b), ('or',a,b), ('imp',a,b), ('box',a), ('dia',a)
def gimp(a, b, top):
    return top if a <= b else b

def eval_formula(phi, w, R, val, top):
    tag = phi[0]
    if tag == 'p':
        return val[w][phi[1]]
    if tag == 'bot':
        return 0
    if tag == 'and':
        return min(eval_formula(phi[1], w, R, val, top),
                   eval_formula(phi[2], w, R, val, top))
    if tag == 'or':
        return max(eval_formula(phi[1], w, R, val, top),
                   eval_formula(phi[2], w, R, val, top))
    if tag == 'imp':
        a = eval_formula(phi[1], w, R, val, top)
        b = eval_formula(phi[2], w, R, val, top)
        return gimp(a, b, top)
    if tag == 'box':
        a = phi[1]
        return min(gimp(R[w][v], eval_formula(a, v, R, val, top), top)
                   for v in range(len(R)))
    if tag == 'dia':
        a = phi[1]
        return max(min(R[w][v], eval_formula(a, v, R, val, top))
                   for v in range(len(R)))
    raise ValueError(tag)

atoms = [('p',0), ('p',1), ('bot',)]
level1 = atoms + [('box',a) for a in atoms] + [('dia',a) for a in atoms]
for a in atoms:
    for b in atoms:
        level1 += [('and',a,b), ('or',a,b), ('imp',a,b)]
formulas = level1[:]
for a in level1[:8]:
    formulas += [('box',a), ('dia',a)]

# Exhaustive small semantic commutation test.
# Original truth chain: 0<1<2<3<4. Regraded chain: 0<2<5<7<9.
old_levels = [0,1,2,3,4]
new_levels = [0,2,5,7,9]
h = dict(zip(old_levels, new_levels))
m = 2
for rflat in product(old_levels, repeat=m*m):
    R = [list(rflat[i*m:(i+1)*m]) for i in range(m)]
    Rh = [[h[x] for x in row] for row in R]
    # Sample all one-variable valuations and a deterministic slice of two-variable valuations.
    vals = []
    for pvals in product(old_levels, repeat=m):
        vals.append([[pvals[w], (2*w + 1) % 5] for w in range(m)])
    for val in vals:
        valh = [[h[x] for x in row] for row in val]
        for phi in formulas:
            for w in range(m):
                lhs = eval_formula(phi, w, Rh, valh, 9)
                rhs = h[eval_formula(phi, w, R, val, 4)]
                assert lhs == rhs, (R, val, phi, w, lhs, rhs)

print("VERIFY_OK")
