"""Computational companion to the TARGET disproof (lane-706).

Verifies, on concrete Johnson-stable families (cyclic orbits of 5-sets),
the structural lemma used in the impossibility proof:
  For a rank-5 paving matroid on n>=12 whose nonbasis family H is
  Johnson-stable (|H1 cap H2| <= 3), EVERY 3-set C yields a U_{2,5} minor
  via contraction M/C (the pair-graph G_C is a matching, so alpha(G_C)>=5
  and the restriction (M/C)|I is U_{2,5} for any independent 5-set I).

Checks (stdlib only):
  1. Johnson stability of the chosen cyclic orbits.
  2. For EVERY 3-set C: max degree of G_C <= 1 (matching).
  3. For EVERY 3-set C: an explicit independent 5-set I with all 10 pairs
     giving 5-sets outside H (i.e. bases) -> certified U_{2,5} minor witness.
Exit 0 iff all checks pass.
"""
import itertools
import sys


def orbit(n, block):
    H = set()
    for t in range(n):
        H.add(tuple(sorted((x + t) % n for x in block)))
    return H


def find_stable_block(n, tries):
    for block in tries:
        H = orbit(n, block)
        ok = True
        L = list(H)
        for i in range(len(L)):
            si = set(L[i])
            for j in range(i + 1, len(L)):
                if len(si & set(L[j])) > 3:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return block, H
    return None, None


def check_all(n, H):
    Hset = set(H)
    nC = 0
    for C in itertools.combinations(range(n), 3):
        nC += 1
        cset = set(C)
        rest = [x for x in range(n) if x not in cset]
        adj = {x: [] for x in rest}
        for i, a in enumerate(rest):
            for b in rest[i + 1:]:
                key = tuple(sorted(cset | {a, b}))
                if key in Hset:
                    adj[a].append(b)
                    adj[b].append(a)
        if any(len(v) > 1 for v in adj.values()):
            print(f"FAIL(n={n}): G_C not a matching at C={C}")
            return False
        used = set()
        I = []
        for x in rest:
            if x in used:
                continue
            I.append(x)
            used.add(x)
            used.update(adj[x])
            if len(I) == 5:
                break
        if len(I) < 5:
            print(f"FAIL(n={n}): no independent 5-set at C={C}")
            return False
        for a, b in itertools.combinations(I, 2):
            if tuple(sorted(cset | {a, b})) in Hset:
                print(f"FAIL(n={n}): witness pair dependent at C={C}")
                return False
    print(f"OK n={n}: |H|={len(Hset)}, all {nC} 3-sets C: "
          f"G_C matching + explicit U_{{2,5}} witness")
    return True


CANDIDATES = [
    (0, 1, 2, 4, 9), (0, 1, 2, 3, 5), (0, 1, 3, 7, 12),
    (0, 1, 2, 5, 11), (0, 2, 3, 8, 13), (0, 1, 4, 10, 17),
    (0, 1, 2, 6, 15), (0, 3, 4, 9, 16),
]

ok = True
# n=17: representative small order (below target's primes, same mechanism)
b, H = find_stable_block(17, CANDIDATES)
assert b is not None, "no stable block at n=17"
print(f"n=17 stable base block: {b}")
ok &= check_all(17, H)
# n=41: smallest prime == 1 mod 20, squarely in the target's claimed class
b41, H41 = find_stable_block(41, CANDIDATES)
assert b41 is not None, "no stable block at n=41"
print(f"n=41 stable base block: {b41}")
ok &= check_all(41, H41)

print("VERIFY_DISPROOF:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
