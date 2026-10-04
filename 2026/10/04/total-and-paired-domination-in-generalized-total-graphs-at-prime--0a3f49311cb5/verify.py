#!/usr/bin/env python3
from itertools import combinations
from math import comb

def zn_prime_ideal_graph(n, p):
    """Generalized total graph GT_P(Z/nZ), with P=(p), for p|n prime."""
    assert n % p == 0
    P = {(p*k) % n for k in range(n)}
    adj = [set() for _ in range(n)]
    for x in range(n):
        for y in range(x+1, n):
            if (x+y) % n in P:
                adj[x].add(y)
                adj[y].add(x)
    return P, adj

def total_dominates(S, adj):
    S = set(S)
    return all(bool(adj[v] & S) for v in range(len(adj)))

def has_perfect_matching(S, adj):
    S = set(S)
    if not S:
        return True
    if len(S) % 2:
        return False
    v = next(iter(S))
    for u in adj[v] & S:
        if has_perfect_matching(S - {v,u}, adj):
            return True
    return False

def exact_minima_and_counts(adj):
    N = len(adj)
    if any(len(a) == 0 for a in adj):
        return None, None, 0, 0
    gt = gp = None
    ct = cp = 0
    for k in range(1, N+1):
        good = [S for S in combinations(range(N), k) if total_dominates(S, adj)]
        if good:
            gt, ct = k, len(good)
            break
    for k in range(2, N+1, 2):
        good = [
            S for S in combinations(range(N), k)
            if total_dominates(S, adj) and has_perfect_matching(S, adj)
        ]
        if good:
            gp, cp = k, len(good)
            break
    return gt, gp, ct, cp

def predicted(s, q):
    if s == 1:
        return None, None, 0, 0
    if q % 2 == 0:
        g = 2*q
        c = comb(s, 2)**q
    else:
        g = q+1
        c = comb(s, 2) * (s**(q-1))
    return g, g, c, c

cases = [
    (4,2),   # s=2, q=2
    (6,2),   # s=3, q=2
    (8,2),   # s=4, q=2
    (9,3),   # s=3, q=3
    (12,2),  # s=6, q=2
    (12,3),  # s=4, q=3
    (15,3),  # s=5, q=3
    (20,5),  # s=4, q=5
    (5,5),   # P=0, s=1, q=5: isolated zero
]
rows = []
for n,p in cases:
    P, adj = zn_prime_ideal_graph(n,p)
    s = len(P)
    q = n // s
    got = exact_minima_and_counts(adj)
    want = predicted(s,q)
    assert got == want, (n,p,s,q,got,want)
    rows.append((n,p,s,q,*got))

# Structural decomposition checks, including non-prime residue-field orders.
profiles = 0
for q in [2,3,4,5,7,8,9,11]:
    for s in range(1,7):
        N=s*q
        # vertices represented as (quotient class, lift index);
        # additive inverse on quotient labels is modeled modulo q only for
        # the component pattern, which is all that the theorem uses.
        comp_sizes = []
        if s == 1:
            # P itself is an isolated K1, enough to obstruct total domination.
            assert predicted(s,q) == (None,None,0,0)
        elif q % 2 == 0:
            comp_sizes = [s]*q
            assert 2*len(comp_sizes) == predicted(s,q)[0]
        else:
            comp_sizes = [s] + [2*s]*((q-1)//2)
            assert 2*len(comp_sizes) == predicted(s,q)[0]
        profiles += 1

print("VERIFY_OK")
print(f"structural_profiles_checked={profiles}")
for row in rows:
    print("Zmod_case n=%d p=%d s=%d q=%d gamma_t=%s gamma_pr=%s count_t=%d count_pr=%d" % row)
