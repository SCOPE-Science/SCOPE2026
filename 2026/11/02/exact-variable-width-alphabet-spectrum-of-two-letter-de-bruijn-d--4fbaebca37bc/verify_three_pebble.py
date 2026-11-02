#!/usr/bin/env python3
"""Exact non-counting three-pebble refinement for B(q,2), q=1,...,7.
Uses only Python's standard library.  Fixed-point colors describe all
unrestricted-depth three-variable types, not merely a chosen game length.
"""

def initial(q):
    w = [(a, b) for a in range(q) for b in range(q)]
    n = len(w)
    E = [[x[1] == y[0] for y in w] for x in w]
    col = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                bits = (
                    i == j, i == k, j == k,
                    E[i][i], E[j][j], E[k][k],
                    E[i][j], E[j][i], E[i][k], E[k][i],
                    E[j][k], E[k][j],
                )
                v = 0
                for b in bits:
                    v = v * 2 + b
                col.append(v)
    return n, col


def supports(n, c):
    s0 = []
    s1 = []
    s2 = []
    for j in range(n):
        for k in range(n):
            s0.append(tuple(sorted({c[(i*n+j)*n+k] for i in range(n)})))
    for i in range(n):
        for k in range(n):
            s1.append(tuple(sorted({c[(i*n+j)*n+k] for j in range(n)})))
    for i in range(n):
        for j in range(n):
            base = (i*n+j)*n
            s2.append(tuple(sorted(set(c[base:base+n]))))
    return s0, s1, s2


def triples(n, c, sp):
    s0, s1, s2 = sp
    for i in range(n):
        for j in range(n):
            for k in range(n):
                yield (c[(i*n+j)*n+k], s0[j*n+k], s1[i*n+k], s2[i*n+j])


params = list(range(1, 8))
data = [initial(q) for q in params]
for round_index in range(12):
    oldtypes = len({z for n,c in data for z in c})
    subs = [supports(n,c) for n,c in data]
    signatures = set()
    for (n,c),sp in zip(data,subs):
        signatures.update(triples(n,c,sp))
    canon = {sig:i for i,sig in enumerate(sorted(signatures))}
    updated = []
    for (n,c),sp in zip(data,subs):
        updated.append((n, [canon[sig] for sig in triples(n,c,sp)]))
    data = updated
    if len(canon) == oldtypes:
        break
else:
    raise AssertionError('refinement did not stabilize')

classes = [frozenset(c) for n,c in data]
for a,qa in enumerate(params):
    for b,qb in enumerate(params):
        expected = min(qa,6) == min(qb,6)
        assert (classes[a] == classes[b]) == expected, (qa,qb)
print('VERIFY_THREE_PEBBLE_OK: q=1..7, fixed-point rounds=%d, color counts=%s' %
      (round_index+1, [len(c) for c in classes]))
