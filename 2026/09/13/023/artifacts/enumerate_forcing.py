"""Exact enumeration + forcing numbers for equiangular degree-8 vertex A8.
Pure integer combinatorics (no floating point). Family P = all {+1,-1}^8
vectors with sum +-2 (Maekawa |M-V|=2): 112 assignments.
Checks: |P|=112; dihedral orbits; forcing number of every mu over P and
over the parity-mixed subfamily F (96); explicit 4-subset distinguishers.
"""
import itertools

EVENS = (0, 2, 4, 6)
ODDS = (1, 3, 5, 7)

P = []
for combo in itertools.combinations(range(8), 3):
    s = [1] * 8
    for i in combo:
        s[i] = -1
    P.append(tuple(s))
    P.append(tuple(-x for x in s))
assert len(P) == 112 and len(set(P)) == 112
print("|P| =", len(P))


def dihedral_canonical(mu):
    rots = []
    for k in range(8):
        rots.append(tuple(mu[(i + k) % 8] for i in range(8)))
    m2 = mu[::-1]
    for k in range(8):
        rots.append(tuple(m2[(i + k) % 8] for i in range(8)))
    return min(rots)


orbits = {}
for mu in P:
    orbits.setdefault(dihedral_canonical(mu), []).append(mu)
print("dihedral orbits:", len(orbits))
for c in sorted(orbits):
    print("  ", c, "size", len(orbits[c]))
assert len(orbits) == 10
assert sorted(len(v) for v in orbits.values()) == [8, 8, 8, 8, 8, 8, 16, 16, 16, 16]


def mixed(mu):
    e = {mu[i] for i in EVENS}
    o = {mu[i] for i in ODDS}
    return len(e) > 1 and len(o) > 1


F = [mu for mu in P if mixed(mu)]
G = [mu for mu in P if not mixed(mu)]
print("|F| =", len(F), "|G| =", len(G))
assert len(F) == 96 and len(G) == 16


def forcing_number(mu, fam):
    for k in range(9):
        for S in itertools.combinations(range(8), k):
            n = 0
            for nu in fam:
                if all(nu[i] == mu[i] for i in S):
                    n += 1
                    if n > 1:
                        break
            if n == 1:
                return k, S
    raise AssertionError


from collections import Counter
distP = Counter()
for mu in P:
    k, _ = forcing_number(mu, P)
    distP[k] += 1
print("forcing distribution over P:", dict(distP))
assert distP == {5: 112}

distF = Counter()
for mu in F:
    k, _ = forcing_number(mu, F)
    distF[k] += 1
print("forcing distribution over F:", dict(distF))
assert distF == {5: 96}

# Minimality witness: canonical example mu0; every 4-subset fails (distinguisher shown for first 5).
mu0 = (-1, -1, -1, 1, 1, 1, 1, 1)
k0, S0 = forcing_number(mu0, P)
print("example:", mu0, "forcing number", k0, "witness S", S0)
assert k0 == 5
shown = 0
for S in itertools.combinations(range(8), 4):
    alt = next(nu for nu in P if nu != mu0 and all(nu[i] == mu0[i] for i in S))
    if shown < 5:
        print("  4-subset", S, "distinguisher", alt)
        shown += 1
print("ALL EXACT CHECKS PASSED")
