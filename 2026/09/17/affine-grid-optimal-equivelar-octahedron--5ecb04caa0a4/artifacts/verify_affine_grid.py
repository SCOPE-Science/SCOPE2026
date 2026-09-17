from fractions import Fraction
from itertools import combinations, product
from math import gcd

V = [
(-72,84,18),(-36,112,102),(72,-84,18),(36,-112,102),(0,300,234),(-84,48,-18),
(9,147,207),(0,-300,234),(84,-48,-18),(-112,-36,-102),(48,84,18),(-147,9,-207),
(-9,-147,207),(84,72,-18),(112,36,-102),(-48,-84,18),(147,-9,-207),(-18,126,144),
(-126,-18,-144),(-300,0,-234),(-84,-72,-18),(18,-126,144),(126,18,-144),(300,0,-234)
]

P_expected = [
(6,-12,-24),(34,-28,-28),(6,36,-12),(34,24,-36),(78,-84,-24),(-6,0,-24),
(69,-48,-33),(78,36,-84),(-6,36,0),(-34,28,-24),(6,0,0),(-69,33,-9),
(69,9,-66),(-6,12,12),(-34,36,28),(6,24,-36),(-69,66,48),(48,-36,-30),
(-48,30,-18),(-78,24,-36),(-6,24,-36),(48,18,-48),(-48,48,36),(-78,84,84)
]

def phi(v):
    x,y,z = v
    return (
        Fraction(z,3),
        Fraction(x,10)-Fraction(y,5)-Fraction(z,6)+15,
        Fraction(x,5)+Fraction(y,10)-Fraction(z,6)-15,
    )

P = []
for v in V:
    q = phi(v)
    assert all(t.denominator == 1 for t in q)
    P.append(tuple(int(t) for t in q))
assert P == P_expected

def det3(rows):
    (a,b,c),(d,e,f),(g,h,i)=rows
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

M = [
    [Fraction(0), Fraction(0), Fraction(1,3)],
    [Fraction(1,10), Fraction(-1,5), Fraction(-1,6)],
    [Fraction(1,5), Fraction(1,10), Fraction(-1,6)],
]
detM = (
    M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
    -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
    +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
)
assert detM == Fraction(1,60)

base = P[0]
D = [tuple(P[i][j]-base[j] for j in range(3)) for i in range(1,len(P))]
minor_gcd = 0
for rows in combinations(D,3):
    minor_gcd = gcd(minor_gcd, abs(det3(rows)))
assert minor_gcd == 1

def width(a):
    vals = [sum(a[j]*p[j] for j in range(3)) for p in P]
    return max(vals)-min(vals)

mins = [min(p[j] for p in P) for j in range(3)]
maxs = [max(p[j] for p in P) for j in range(3)]
spans = [maxs[j]-mins[j] for j in range(3)]
assert mins == [-78,-84,-84]
assert maxs == [78,84,84]
assert spans == [156,168,168]

D0 = [
    tuple(P[6][j]-P[7][j] for j in range(3)),
    tuple(P[15][j]-P[19][j] for j in range(3)),
    tuple(P[11][j]-P[23][j] for j in range(3)),
]
assert D0 == [(-9,-84,51),(84,0,0),(9,-51,-93)]

bounds = [
    Fraction(1,84),
    Fraction(33,2314),
    Fraction(465,32396),
]
assert Fraction(167)*bounds[0] < 2
assert Fraction(167)*bounds[1] < 3
assert Fraction(167)*bounds[2] < 3

small = []
for a in product(range(-1,2), range(-2,3), range(-2,3)):
    if a != (0,0,0) and width(a) <= 167:
        small.append((a,width(a)))
assert small == [((-1,0,0),156),((1,0,0),156)]

print("det(linear part) =", detM)
print("transformed coordinate minima =", mins)
print("transformed coordinate maxima =", maxs)
print("coordinate spans =", spans)
print("difference-lattice index =", minor_gcd)
print("nonzero integer covectors of width <= 167 =", small)
print("affine-integer cube span = 168; centered radius = 84")
