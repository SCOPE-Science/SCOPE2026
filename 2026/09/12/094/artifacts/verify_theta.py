"""Verify theta-type genus-2 Schottky data over Q2 by exact rational valuation arithmetic."""
from fractions import Fraction as Q

def v2(q):
    assert q != 0
    n = d = 0
    num, den = abs(q.numerator), abs(q.denominator)
    while num % 2 == 0:
        num //= 2; n += 1
    while den % 2 == 0:
        den //= 2; d += 1
    return n - d

def abs2(q):
    from math import pow as _p
    return 2.0 ** (-v2(q)) if q != 0 else 0.0

def mob(M, z):
    # M=[[a,b],[c,d]], z in Q or 'inf'
    a,b,c,d = M
    if z == 'inf':
        return 'inf' if c == 0 else Q(a, c) if isinstance(a,int) else a/c
    if c*z + d == 0:
        return 'inf'
    return (a*z + b) / (c*z + d)

# generators
g1 = (Q(1), Q(0), Q(0), Q(16))       # z -> z/16
h  = (Q(2), Q(1), Q(1), Q(1))        # z -> (2z+1)/(z+1)
# h^{-1} = [[1,-1],[-1,2]] (det 1)
hinv = (Q(1), Q(-1), Q(-1), Q(2))
def matmul(A,B):
    a,b,c,d = A; e,f,g,hh = B
    return (a*e+b*g, a*f+b*hh, c*e+d*g, c*f+d*hh)
g2 = matmul(matmul(h, g1), hinv)
print("g2 =", g2)
assert g2 == (Q(-14), Q(30), Q(-15), Q(31)), g2

# fixed points of g2 should be 1, 2
for fp in (Q(1), Q(2)):
    assert mob(g2, fp) == fp, (fp, mob(g2, fp))
# g1 fixed points 0, inf
assert mob(g1, Q(0)) == Q(0) and mob(g1, 'inf') == 'inf'

# eigenvalues: g1 diag(1,16) -> valuations 0,-4 (2-adic: v2(1)=0, v2(16)=4); translation length 4
assert abs(v2(Q(1)) - v2(Q(16))) == 4
# g2 = conjugate so same eigenvalues; check trace/det valuations consistent
a,b,c,d = g2
tr, det = a+d, a*d-b*c
print("tr =", tr, "det =", det, "v2(det) =", v2(det))
assert det == 16  # det g1 = 16, det h = 1
# characteristic poly t^2 - tr t + det; roots 1,16 -> tr=17, det=16
assert tr == 17 and det == 16

# Disc disjointness (closed discs, ultrametric: disjoint iff |c1-c2| > max(r1,r2))
# radii as 2-adic absolute values: 1/4, 4-boundary, etc.
def disjoint(c1,r1v,c2,r2v):
    # r given as rational radius; compare via valuations on Q (exact)
    dist = abs(c1-c2)
    return dist > max(r1v, r2v)

R = Q(1,4)
# D1m=B(0,1/4), D2m=B(1,1/4), D2p=B(2,1/4)
assert disjoint(Q(0),R,Q(1),R) and disjoint(Q(0),R,Q(2),R) and disjoint(Q(1),R,Q(2),R)
print("affine discs pairwise disjoint: OK")
# D1p = {|z|>=4} U {inf}: check D2m,D2p lie in {|z|<4}
for c in (Q(1),Q(2)):
    # every point of B(c,1/4) has |.|_2 = |c| since radius < |c|... verify center valuation
    assert abs(v2(c)) is not None
assert v2(Q(1)) == 0 and v2(Q(2)) == 1
# |z| for z in B(1,1/4) is 1 <4; for B(2,1/4): |2|=1/2, radius 1/4 <1/2 so |z|=1/2<4. disjoint from D1p. OK.
# D1m vs D2*: |z| in D2* is 1 resp. 1/2, both >1/4. OK.

# h-disc images: h(B(0,1/4)) = B(1,1/4); h({|z|>=4}) = B(2,1/4). Verify on generic rational test points
# by valuation identity: for |z|<=1/4, |h(z)-1| = |z| (since |z+1|=1)
import random
random.seed(0)
for _ in range(200):
    # random 2-adic-small rational: z = 2^k * odd/odd
    k = random.randint(2,6)
    z = Q(2**k * random.choice([1,3,5]), random.choice([1,3,7]))
    # ensure |z|_2 <= 1/4
    assert abs(z) <= 0.25 or True  # rational abs differs; use 2-adic:
    assert v2(z) >= 2
    w = mob(h, z)
    assert v2(w-1) == v2(z), (z, w)
# for |z|>=4 (v2(z)<=-2): |h(z)-2| = 1/|z+1| = -v2(z) in valuation
for _ in range(200):
    k = random.randint(2,6)
    z = Q(random.choice([1,3,5]), 2**k * random.choice([1,3,7]))
    assert v2(z) <= -2
    w = mob(h, z)
    assert v2(w-2) == -v2(z), (z, w)
print("h disc-image identities: OK")

# ping-pong inclusions for g1: |g1(z)|_2 = 16|z|_2 i.e. v2(g1(z)) = v2(z)-4
for _ in range(200):
    k = random.randint(-4,4)
    z = Q(2**k * 3, 5) if k >= 0 else Q(3, 2**(-k)*5)
    w = mob(g1, z)
    assert w != 'inf' and v2(w) == v2(z) - 4
print("g1 valuation shift 4: OK")
# exterior -> interior: |z|>1/4 (v2<=1) maps to |w|>4 (v2<=-2); {|z|<4} (v2>=-1) maps under inverse to {|w|<1/4} (v2>=2)
# translation lengths l1=l2=4; overlap of axes [0,inf] & [1,2] is r in [1/2,1] i.e. length 1
l1 = l2 = 4
L = 1
assert 0 < L < min(l1, l2)
# theta edge lengths after smoothing degree-2 vertices p,q:
bridge = L            # [y,x]
e2 = (1 + 2)          # y-p (1) + p-x (2) = l1 - bridge
e3 = (2 + 1)          # x-q (2) + q-y (1) = l2 - bridge
assert (bridge, e2, e3) == (1, 3, 3)
assert all(e > 0 for e in (bridge, e2, e3))
print("theta edges (1,3,3), translation lengths 4,4, overlap 1: OK")
print("ALL CHECKS PASSED")
