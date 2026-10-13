from collections import Counter
from itertools import product

ROWS = [
    "100011111111111111000",
    "010000112233012311110",
    "001010000000132122311",
    "000111200000102313022",
]
EXPECTED_SPECTRUM = {1:2,2:4,3:12,4:12,5:22,6:16,7:6,8:4,9:3,10:4}
EXPECTED_LOCAL_DEPTH = {0:2,1:1,2:16,3:9,4:25,5:23,6:2,7:7}

# GF(4) = GF(2)[a]/(a^2+a+1), encoded 0,1,a,a^2 as 0,1,2,3.
def add(x,y):
    return x ^ y

def mul(x,y):
    c0=c1=c2=0
    for i in range(2):
        if (x>>i)&1:
            for j in range(2):
                if (y>>j)&1:
                    if i+j==0: c0 ^= 1
                    elif i+j==1: c1 ^= 1
                    else: c2 ^= 1
    if c2:  # a^2 = a+1
        c0 ^= 1
        c1 ^= 1
    return c0 | (c1<<1)

def inv(x):
    if x == 0: raise ZeroDivisionError
    for y in (1,2,3):
        if mul(x,y)==1:
            return y
    raise AssertionError

def scale(v,s):
    return tuple(mul(s,x) for x in v)

def normalize(v):
    for x in v:
        if x:
            return scale(v,inv(x))
    raise ValueError("zero vector")

def dot(u,v):
    z=0
    for x,y in zip(u,v):
        z=add(z,mul(x,y))
    return z

points = sorted({normalize(v) for v in product(range(4), repeat=4) if any(v)})
assert len(points)==85
cols=[tuple(int(ROWS[i][j]) for i in range(4)) for j in range(21)]
column_mult=Counter(normalize(c) for c in cols)

# Normalized nonzero linear forms parameterize all projective planes.
planes=points
plane_mult={h:sum(column_mult[p] for p in points if dot(h,p)==0) for h in planes}
spectrum=Counter(plane_mult.values())
assert dict(sorted(spectrum.items()))==EXPECTED_SPECTRUM

# For n=21 and q=4, the exceptional residue in a locally-three-weight test is 0 mod 4.
exceptional=[h for h in planes if plane_mult[h] % 4 == 0]
assert Counter(plane_mult[h] for h in exceptional)==Counter({4:12,8:4})

depth={p:sum(dot(h,p)==0 for h in exceptional) for p in points}
depth_hist=Counter(depth.values())
assert dict(sorted(depth_hist.items()))==EXPECTED_LOCAL_DEPTH

P=(0,0,1,3)
H=(1,1,0,0)
assert column_mult[P]==0
assert depth[P]==1
assert [p for p in points if depth[p]==1]==[P]
assert plane_mult[H]==8 and dot(H,P)==0
assert sum(1 for p in points if depth[p]==2)==16

# Incidence checksum: each of the 16 exceptional planes contains q^2+q+1=21 points.
assert sum(depth.values()) == 16*21

print("PROJECTIVE_POINTS", len(points))
print("PLANE_SPECTRUM", dict(sorted(spectrum.items())))
print("EXCEPTIONAL_PLANES", len(exceptional), dict(sorted(Counter(plane_mult[h] for h in exceptional).items())))
print("LOCAL_DEPTH_HISTOGRAM", dict(sorted(depth_hist.items())))
print("UNIQUE_1_LOCAL_CENTER", P, "COLUMN_MULTIPLICITY", column_mult[P])
print("TWO_LOCAL_CENTERS", sum(1 for p in points if depth[p]==2))
print("INCIDENCE_CHECKSUM", sum(depth.values()))
print("VERIFY_OK")
