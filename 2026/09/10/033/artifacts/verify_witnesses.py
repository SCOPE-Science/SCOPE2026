"""Direct verification of separation witnesses and the n=6/n=7 difference census.

Uses only full pattern matching on explicit permutations (no insertion logic):
every claim below is checkable by hand or by re-running this script.
"""
import itertools

def std(p):
    s = sorted(p)
    r = {v: i + 1 for i, v in enumerate(s)}
    return tuple(r[v] for v in p)

def contains(p, q):
    for idx in itertools.combinations(range(len(p)), len(q)):
        if std([p[i] for i in idx]) == q:
            return True
    return False

P2413 = (2, 4, 1, 3)
P3142 = (3, 1, 4, 2)
T1 = (1, 2, 3, 6, 5, 4)
T2 = (3, 2, 1, 6, 5, 4)

def status(w):
    sep = not contains(w, P2413) and not contains(w, P3142)
    return sep, contains(w, T1), contains(w, T2)

ok = True

# Minimal (n=7) two-sided witnesses: each must be separable and lie in exactly one class.
w12 = (4, 3, 2, 7, 6, 5, 1)  # claimed in C1 \ C2
w21 = (2, 3, 4, 7, 6, 5, 1)  # claimed in C2 \ C1
for w, want1, want2, tag in ((w12, False, True, "C1\\C2"), (w21, True, False, "C2\\C1")):
    sep, h1, h2 = status(w)
    good = sep and (h1 == want1) and (h2 == want2)
    ok &= good
    print(f"{w} sep={sep} hasT1={h1} hasT2={h2} expected {tag}: {'OK' if good else 'FAIL'}")

# Higher-order witnesses from the insertion log (each in the stated difference).
pairs = [
    ((5, 4, 3, 8, 7, 6, 2, 1), False, True),
    ((3, 4, 5, 8, 7, 6, 2, 1), True, False),
    ((6, 5, 4, 9, 8, 7, 3, 2, 1), False, True),
    ((4, 5, 6, 9, 8, 7, 3, 2, 1), True, False),
    ((7, 6, 5, 10, 9, 8, 4, 3, 2, 1), False, True),
    ((5, 6, 7, 10, 9, 8, 4, 3, 2, 1), True, False),
]
for w, want1, want2 in pairs:
    sep, h1, h2 = status(w)
    good = sep and (h1 == want1) and (h2 == want2)
    ok &= good
    print(f"{w} sep={sep} hasT1={h1} hasT2={h2}: {'OK' if good else 'FAIL'}")

# n=6: exactly the two forbidden singletons are removed (agreement 393 = 394 - 1 each side).
hits = []
for p in itertools.permutations(range(1, 7)):
    if contains(p, P2413) or contains(p, P3142):
        continue
    h1, h2 = contains(p, T1), contains(p, T2)
    if h1 or h2:
        hits.append((p, h1, h2))
good6 = hits == [((1, 2, 3, 6, 5, 4), True, False), ((3, 2, 1, 6, 5, 4), False, True)]
ok &= good6
print(f"n=6 hits: {hits}: {'OK' if good6 else 'FAIL'}")

# n=7 full difference census: both differences nonempty (two-sided split at first index).
d12 = d21 = 0
for p in itertools.permutations(range(1, 8)):
    if contains(p, P2413) or contains(p, P3142):
        continue
    h1, h2 = contains(p, T1), contains(p, T2)
    if not h1 and h2:
        d12 += 1
    if h1 and not h2:
        d21 += 1
good7 = (d12, d21) == (21, 25)
ok &= good7
print(f"n=7 |C1\\C2|={d12} |C2\\C1|={d21} (expect 21, 25): {'OK' if good7 else 'FAIL'}")

print("VERIFY:", "OK" if ok else "FAIL")
assert ok
