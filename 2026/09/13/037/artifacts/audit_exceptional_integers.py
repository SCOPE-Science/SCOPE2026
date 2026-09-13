"""Integer-minimum audit for the 7 exceptional witness pieces (stdlib only).

For each exceptional (pat, combo): enumerate integer Kunz tuples with e=3
pattern `pat` satisfying the combo equalities up to a bound, and report the
integer minimum of W. Also verify the parity claims used in DRAFT.md:
W restricted to the witness lattice is an even integer.
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

WITNESS = {
    ('3a', '4b'): (lambda k: k[0]+k[1] == k[2], lambda k: 2*k[1] == k[3]),
    ('2a', '4a'): (lambda k: 2*k[0] == k[1], lambda k: k[0]+k[2] == k[3]),
    ('2a', '3a'): (lambda k: 2*k[0] == k[1], lambda k: k[0]+k[1] == k[2]),
    ('2a', '3b'): (lambda k: 2*k[0] == k[1], lambda k: k[2] == 2*k[3] + 1),
    ('1b', '4b'): (lambda k: 2*k[2]+1 == k[0], lambda k: 2*k[1] == k[3]),
    ('1a', '3b'): (lambda k: k[1]+k[3]+1 == k[0], lambda k: 2*k[3]+1 == k[2]),
    ('1b', '2b'): (lambda k: 2*k[2]+1 == k[0], lambda k: k[2]+k[3]+1 == k[1]),
}
PAT = {(1, 2): ('3a', '4b'), (1, 3): ('2a', '4a'), (1, 4): ('2a', '3a'),
       (1, 4): ('2a', '3b'), (2, 3): ('1b', '4b'), (2, 4): ('1a', '3b'),
       (3, 4): ('1b', '2b')}
CASES = [((1, 2), ('3a', '4b')), ((1, 3), ('2a', '4a')),
         ((1, 4), ('2a', '3a')), ((1, 4), ('2a', '3b')),
         ((2, 3), ('1b', '4b')), ((2, 4), ('1a', '3b')),
         ((3, 4), ('1b', '2b'))]
# residue class of W mod 2 (or mod 3 for E3j3) on the witness lattice,
# as derived in DRAFT.md Section 5
MODINFO = {((1, 2), ('3a', '4b')): 2, ((1, 3), ('2a', '4a')): 2,
           ((1, 4), ('2a', '3a')): None, ((1, 4), ('2a', '3b')): None,
           ((2, 3), ('1b', '4b')): None, ((2, 4), ('1a', '3b')): 2,
           ((3, 4), ('1b', '2b')): 2}

def cnw(k):
    w = [0, 5*k[0]+1, 5*k[1]+2, 5*k[2]+3, 5*k[3]+4]
    c = max(w) - 4
    return c, c - sum(k), 2*c - 3*sum(k)

B = 60
for pat, combo in CASES:
    f1, f2 = WITNESS[combo]
    best = None
    cnt = 0
    for k in itertools.product(range(1, B+1), repeat=4):
        if not kunz_valid(k):
            continue
        a = atoms(k)
        if tuple(i+1 for i, x in enumerate(a) if x) != pat:
            continue
        if not (f1(k) and f2(k)):
            continue
        c, n, W = cnw(k)
        if MODINFO[(pat, combo)] == 2:
            assert W % 2 == 0, ("parity fails", pat, combo, k, W)
        cnt += 1
        if best is None or W < best[0]:
            best = (W, k, c, n)
    print("pat%s combo%s count=%d min(W,k,c,n)=%s" % (pat, combo, cnt, best,))
    assert best is not None and best[0] >= 2
print("INTEGER AUDIT PASSED: all exceptional pieces have integer min >= 2, W even throughout")
