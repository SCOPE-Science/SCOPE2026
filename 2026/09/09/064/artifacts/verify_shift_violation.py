"""Independent verifier for the shifting-violation certificate.
Replays from committed integer inputs with stdlib only:
1. H on {0..5} is C5-free (checks all 6 5-sets x 12 tight-C5 patterns).
2. S_01(H) per Frankl definition contains a tight C5 (prints cyclic order).
3. Edge count preserved.
Usage: python3 verify_shift_violation.py  -> prints VERIFY_OK / VERIFY_FAIL
"""
import itertools

H_EDGES = [(0, 3, 5), (0, 4, 5), (1, 2, 4), (2, 3, 4), (2, 3, 5)]
I, J = 0, 1
N = 6

def frankl_shift(edges, i, j):
    E = set(tuple(sorted(e)) for e in edges)
    out = set(E)
    for e in E:
        if j in e and i not in e:
            e2 = tuple(sorted((i if x == j else x) for x in e))
            if e2 not in E:
                out.discard(e)
                out.add(e2)
    return out

def tight_c5_patterns(verts5):
    pats = set()
    for p in itertools.permutations(verts5):
        if p[0] != min(p) or p[1] > p[4]:
            continue
        pats.add(frozenset(tuple(sorted((p[k], p[(k+1) % 5], p[(k+2) % 5]))) for k in range(5)))
    return pats

def find_c5(edges, n):
    E = set(tuple(sorted(e)) for e in edges)
    for verts in itertools.combinations(range(n), 5):
        for pat in tight_c5_patterns(verts):
            if pat <= E:
                return verts, pat
    return None

S = frankl_shift(H_EDGES, I, J)
print("H =", sorted(set(H_EDGES)))
print("S_%d%d(H) =" % (I, J), sorted(S))
print("|H|=%d |S|=%d" % (len(H_EDGES), len(S)))

ok1 = find_c5(H_EDGES, N) is None
print("H C5-free:", ok1)
hit = find_c5(S, N)
ok2 = hit is not None
print("S contains C5:", ok2)
if hit:
    verts, pat = hit
    print("witness 5-set:", verts, "edges:", sorted(pat))
    # recover cyclic order
    for p in itertools.permutations(verts):
        e = frozenset(tuple(sorted((p[k], p[(k+1) % 5], p[(k+2) % 5]))) for k in range(5))
        if e == pat:
            print("cyclic order:", p)
            break
# minimality: S(H) has exactly 5 edges = the C5 itself
ok3 = len(S) == 5 and len(H_EDGES) == 5
print("minimal (5 edges, single-edge move (1,2,4)->(0,2,4)):", ok3,
      ((1, 2, 4) in set(H_EDGES)) and ((0, 2, 4) in S))
if ok1 and ok2 and ok3:
    print("VERIFY_OK")
else:
    print("VERIFY_FAIL")
