#!/usr/bin/env python3
from itertools import product, combinations
from math import ceil

Q = 3

def canon(v):
    for x in v:
        x %= Q
        if x:
            inv = 1 if x == 1 else 2
            return tuple((inv*y) % Q for y in v)
    raise ValueError("zero vector")

POINTS = sorted({canon(v) for v in product(range(Q), repeat=3) if any(v)})
assert len(POINTS) == 13
INDEX = {p:i for i,p in enumerate(POINTS)}
LINES = []
for normal in POINTS:
    line = tuple(i for i,p in enumerate(POINTS)
                 if sum(a*b for a,b in zip(normal,p)) % Q == 0)
    LINES.append(line)
assert len(set(LINES)) == 13
assert all(len(L) == 4 for L in LINES)

def rank_mod3(rows):
    a = [list(r) for r in rows]
    r = 0
    for c in range(3):
        pivot = next((i for i in range(r, len(a)) if a[i][c] % 3), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = 1 if a[r][c] % 3 == 1 else 2
        a[r] = [(inv*x) % 3 for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c] % 3:
                f = a[i][c] % 3
                a[i] = [(a[i][j] - f*a[r][j]) % 3 for j in range(3)]
        r += 1
    return r

def local2(mult):
    support = {i for i,m in enumerate(mult) if m > 0}
    for p in support:
        if mult[p] >= 2:
            continue
        if not any(p in L and len(support.intersection(L)) >= 3 for L in LINES):
            return False
    return True

def line_distance(mult):
    n = sum(mult)
    return n - max(sum(mult[i] for i in L) for L in LINES)

def direct_distance(mult):
    cols = []
    for i,m in enumerate(mult):
        cols.extend([POINTS[i]] * m)
    best = len(cols) + 1
    for u in product(range(3), repeat=3):
        if u == (0,0,0):
            continue
        w = sum(1 for p in cols if sum(a*b for a,b in zip(u,p)) % 3 != 0)
        best = min(best, w)
    return best

def griesmer(d):
    return d + ceil(d/3) + ceil(d/9)

U = set(range(13))
L_INF = set(range(4))       # x = 0
a, b = 4, 5
A = {0, 1, 4}               # three noncollinear points
ARC4 = {0, 1, 4, 8}         # four points, no three collinear

def indicator(S, value=1):
    return [value if i in S else 0 for i in range(13)]

BASE = {}
BASE[4] = indicator(U - (L_INF | {a,b}))
BASE[5] = indicator(U - (L_INF | {a}))
BASE[6] = indicator(U - L_INF)
BASE[7] = indicator(U - {a,b})
BASE[8] = indicator(U - {a})
BASE[9] = indicator(U)
BASE[10] = [1 + (1 if i in A else 0) for i in range(13)]
BASE[11] = [1 + (1 if i in ARC4 else 0) for i in range(13)]
BASE[12] = indicator(U - L_INF, 2)

# Check the geometric descriptions used by the proof.
assert rank_mod3([POINTS[i] for i in A]) == 3
for L in LINES:
    assert len(ARC4.intersection(L)) <= 2

base_summary = []
for s in range(4,13):
    m = BASE[s]
    n = sum(m)
    d1 = line_distance(m)
    d2 = direct_distance(m)
    support = [POINTS[i] for i,x in enumerate(m) if x]
    assert rank_mod3(support) == 3
    assert n == griesmer(s)
    assert d1 == s == d2
    assert local2(m)
    base_summary.append((s,n))

# Small-distance witnesses.
L1 = set(LINES[4])  # x = 0
L2 = set(LINES[1])  # y = 0
P = next(iter(L1.intersection(L2)))
SMALL2 = indicator((L1 - {3}) | (L2 - {6}))
SMALL3 = indicator((L1 | L2) - {P})
for d,m,n in [(2,SMALL2,5),(3,SMALL3,6)]:
    support = [POINTS[i] for i,x in enumerate(m) if x]
    assert rank_mod3(support) == 3
    assert sum(m) == n
    assert line_distance(m) == d == direct_distance(m)
    assert local2(m)

# Finite check of the small lower-bound geometry:
# there are only four projective one-spaces in F_3^2, so a 2 x 5
# parity-check matrix cannot have five nonzero pairwise nonproportional columns.
def canon2(v):
    for x in v:
        if x % 3:
            inv = 1 if x % 3 == 1 else 2
            return tuple((inv*y) % 3 for y in v)
P1 = sorted({canon2(v) for v in product(range(3), repeat=2) if any(v)})
assert len(P1) == 4

# Lift every residue class by copies of the ternary simplex multiset.
# Adding one full PG(2,3) increases length by 13 and distance by 9.
lift_checks = 0
for d in range(4,1001):
    s = 4 + ((d - 4) % 9)
    t = (d - s) // 9
    m = [BASE[s][i] + t for i in range(13)]
    assert sum(m) == griesmer(d)
    assert line_distance(m) == d
    assert local2(m)
    assert rank_mod3([POINTS[i] for i,x in enumerate(m) if x]) == 3
    lift_checks += 1

# Algebraic recurrence underlying the lift.
for d in range(1,1001):
    assert griesmer(d+9) == griesmer(d) + 13

print(
    "VERIFY_OK "
    f"pg_points={len(POINTS)} pg_lines={len(LINES)} "
    f"bases={len(base_summary)} small_witnesses=2 "
    f"lift_d=4..1000 lift_checks={lift_checks} "
    f"projective_line_points={len(P1)}"
)
