"""Exact cubic-pair incidence enumeration over F_2 (Python 3 stdlib only)."""
from collections import Counter
from itertools import combinations
from math import comb

# A coefficient vector c = sum c_i M_i, in this fixed order.
MON3 = ((3,0,0),(0,3,0),(0,0,3),(2,1,0),(2,0,1),
        (1,2,0),(0,2,1),(1,0,2),(0,1,2),(1,1,1))
MON2 = tuple((i,j,2-i-j) for i in range(3) for j in range(3-i))
MON4 = tuple((i,j,4-i-j) for i in range(5) for j in range(5-i))
I2 = {e:i for i,e in enumerate(MON2)}
I4 = {e:i for i,e in enumerate(MON4)}
POINTS = tuple(tuple((p >> i) & 1 for i in range(3)) for p in range(1,8))

def gf2_rank(rows):
    pivots = {}
    for v in rows:
        while v:
            k = v.bit_length()-1
            if k in pivots:
                v ^= pivots[k]
            else:
                pivots[k] = v
                break
    return len(pivots)

def smooth(c):
    # Smooth iff the Jacobian ideal of the three quadrics is
    # irrelevant-primary, equivalently its degree-four part is all R_4.
    # For a regular sequence of three quadrics, the quotient Hilbert
    # series is (1+t)^3; hence the necessary degree-four condition.
    derivatives = []
    for var in range(3):
        d = 0
        for i,e in enumerate(MON3):
            if (c >> i) & 1 and (e[var] & 1):
                v = list(e);v[var] -= 1
                d ^= 1 << I2[tuple(v)]
        derivatives.append(d)
    rows = []
    for d in derivatives:
        for a in MON2:
            row = 0
            for i,b in enumerate(MON2):
                if (d >> i) & 1:
                    row ^= 1 << I4[tuple(a[j]+b[j] for j in range(3))]
            rows.append(row)
    return gf2_rank(rows)==len(MON4)

def vanishes(c,p):
    v = 0
    for i,e in enumerate(MON3):
        if (c>>i)&1 and all(p[j] or not e[j] for j in range(3)):
            v ^= 1
    return v == 0

def rational_mask(c):
    return sum(1<<i for i,p in enumerate(POINTS) if vanishes(c,p))

SMOOTH = [(c,rational_mask(c)) for c in range(1,1024) if smooth(c)]
counts = Counter((mask & other).bit_count()
                 for i,(_,mask) in enumerate(SMOOTH)
                 for _,other in SMOOTH[i+1:])
assert len(SMOOTH)==336
assert Counter(mask.bit_count() for _,mask in SMOOTH)=={1:42,2:84,3:84,4:84,5:42}
assert dict(counts)=={0:12740,1:22575,2:14448,3:5488,4:1008,5:21}
assert sum(counts.values())==comb(336,2)==56280

# Chosen five-point configuration; the two excluded points are [0:0:1], [0:1:1].
selected = ((1,0,0),(0,1,0),(1,1,0),(1,0,1),(1,1,1))
through = [c for c in range(1024) if all(vanishes(c,p) for p in selected)]
assert len(through)==32
assert [c for c in through if smooth(c)]==[60,172]
assert 60^172==144  # xyz-factorized difference x*z*(x+z)
assert sum(1 for i,(a,pa) in enumerate(SMOOTH) for b,pb in SMOOTH[i+1:]
           if (pa&pb).bit_count()==5)==21
print('smooth_cubics',len(SMOOTH))
print('point_count_distribution',dict(sorted(Counter(m.bit_count() for _,m in SMOOTH).items())))
print('unordered_pair_distribution',dict(sorted(counts.items())))
print('five_point_configuration_forms',through)
print('five_point_configuration_smooth_forms',[60,172])
print('total_unordered_pairs',sum(counts.values()))
print('VERIFY_OK')
