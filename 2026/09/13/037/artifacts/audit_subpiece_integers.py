"""Per-subpiece integer audit (stdlib only): exact integer minima per (combo, j).

For each exceptional (pat, combo, j): enumerate integer e=3 tuples in the
subpiece (combo equalities + dominance wj=max) and report the integer min of W.
Confirms the DRAFT.md Section 5 hand-proof conclusions (all >= 2).
"""
import itertools

def kunz_valid(k):
    k1, k2, k3, k4 = k
    return (2*k1 >= k2 and k1+k2 >= k3 and k1+k3 >= k4 and 2*k2 >= k4
            and k2+k4+1 >= k1 and 2*k3+1 >= k1 and k3+k4+1 >= k2
            and 2*k4+1 >= k3)

def atoms(k):
    k1, k2, k3, k4 = k
    return ((2*k3+1 > k1) and (k2+k4+1 > k1),
            (2*k1 > k2) and (k3+k4+1 > k2),
            (k1+k2 > k3) and (2*k4+1 > k3),
            (k1+k3 > k4) and (2*k2 > k4))

def cnw(k):
    w = [0, 5*k[0]+1, 5*k[1]+2, 5*k[2]+3, 5*k[3]+4]
    M = max(w)
    c = M - 4
    return c, c - sum(k), 2*c - 3*sum(k), w.index(M) + 0 if 0 in w else None

WITNESS = {
    ('3a', '4b'): (lambda k: k[0]+k[1] == k[2], lambda k: 2*k[1] == k[3]),
    ('2a', '4a'): (lambda k: 2*k[0] == k[1], lambda k: k[0]+k[2] == k[3]),
    ('2a', '3a'): (lambda k: 2*k[0] == k[1], lambda k: k[0]+k[1] == k[2]),
    ('2a', '3b'): (lambda k: 2*k[0] == k[1], lambda k: k[2] == 2*k[3] + 1),
    ('1b', '4b'): (lambda k: 2*k[2]+1 == k[0], lambda k: 2*k[1] == k[3]),
    ('1a', '3b'): (lambda k: k[1]+k[3]+1 == k[0], lambda k: 2*k[3]+1 == k[2]),
    ('1b', '2b'): (lambda k: 2*k[2]+1 == k[0], lambda k: k[2]+k[3]+1 == k[1]),
}
SUBS = [((1, 2), ('3a', '4b'), 3), ((1, 2), ('3a', '4b'), 4),
        ((1, 3), ('2a', '4a'), 2), ((1, 3), ('2a', '4a'), 4),
        ((1, 4), ('2a', '3a'), 3), ((1, 4), ('2a', '3a'), 4),
        ((1, 4), ('2a', '3b'), 2), ((1, 4), ('2a', '3b'), 3),
        ((2, 3), ('1b', '4b'), 1), ((2, 3), ('1b', '4b'), 4),
        ((2, 4), ('1a', '3b'), 1), ((2, 4), ('1a', '3b'), 3),
        ((3, 4), ('1b', '2b'), 1), ((3, 4), ('1b', '2b'), 2)]

B = 60  # matches audit_exceptional_integers.py; subpiece minima already confirmed
for pat, combo, j in SUBS:
    f1, f2 = WITNESS[combo]
    best = None
    for k in itertools.product(range(1, B+1), repeat=4):
        if not kunz_valid(k):
            continue
        a = atoms(k)
        if tuple(i+1 for i, x in enumerate(a) if x) != pat:
            continue
        if not (f1(k) and f2(k)):
            continue
        w = [0, 5*k[0]+1, 5*k[1]+2, 5*k[2]+3, 5*k[3]+4]
        if not all(w[j] >= w[i] for i in range(5) if i != j):
            continue
        c = w[j] - 4
        W = 2*c - 3*sum(k)
        if best is None or W < best[0]:
            best = (W, k)
    print("pat%s combo%s j=%d min(W,k)=%s" % (pat, combo, j, best))
    assert best is not None and best[0] >= 2, (pat, combo, j, best)
print("SUBPIECE INTEGER AUDIT PASSED")
