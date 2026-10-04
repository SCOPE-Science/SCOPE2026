#!/usr/bin/env python3
from itertools import product, combinations

def elements(p, d, q):
    return [v + (y,) for v in product(range(p), repeat=d) for y in range(q)]

def add(a, b, p, d, q):
    return tuple((a[i] + b[i]) % p for i in range(d)) + ((a[d] + b[d]) % q,)

def cyclic_subgroup(a, p, d, q):
    zero = tuple(0 for _ in range(d + 1))
    H = {zero}
    cur = zero
    while True:
        cur = add(cur, a, p, d, q)
        if cur in H:
            break
        H.add(cur)
    return H

def proper_power_graph(p, d, q):
    zero = tuple(0 for _ in range(d + 1))
    V = [x for x in elements(p, d, q) if x != zero]
    cyclic = [cyclic_subgroup(x, p, d, q) for x in V]
    adj = [set() for _ in V]
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            if V[i] in cyclic[j] or V[j] in cyclic[i]:
                adj[i].add(j)
                adj[j].add(i)
    return V, adj

def dominates(S, adj, total=False):
    S = set(S)
    for v in range(len(adj)):
        if total:
            if not (adj[v] & S):
                return False
        else:
            if v not in S and not (adj[v] & S):
                return False
    return True

def perfect_matching(S, adj):
    S = set(S)
    if not S:
        return True
    if len(S) % 2:
        return False
    v = next(iter(S))
    for u in adj[v] & S:
        if perfect_matching(S - {v, u}, adj):
            return True
    return False

def exact_minima(p, d, q):
    V, adj = proper_power_graph(p, d, q)
    t = (p ** d - 1) // (p - 1)
    targets = (t, t + 1, 2 * t)
    found = []
    for kind, target in enumerate(targets):
        answer = None
        for k in range(1, target + 1):
            if kind == 2 and k % 2:
                continue
            for S in combinations(range(len(V)), k):
                if kind == 0:
                    ok = dominates(S, adj, False)
                elif kind == 1:
                    ok = dominates(S, adj, True)
                else:
                    ok = dominates(S, adj, False) and perfect_matching(S, adj)
                if ok:
                    answer = k
                    break
            if answer is not None:
                break
        assert answer == target, (p, d, q, kind, answer, target)
        found.append(answer)
    return len(V), tuple(found)

cases = [
    (2, 1, 3),
    (3, 1, 2),
    (2, 2, 3),
    (2, 2, 5),
    (3, 2, 2),
]
for p, d, q in cases:
    n, vals = exact_minima(p, d, q)
    print(f"p={p} d={d} q={q}: vertices={n} gamma={vals[0]} gamma_t={vals[1]} gamma_pr={vals[2]}")
print("VERIFY_OK")
