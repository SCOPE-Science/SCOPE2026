from fractions import Fraction as F
from itertools import combinations, product
from math import gcd

V = [
(-72,84,18),(-36,112,102),(72,-84,18),(36,-112,102),(0,300,234),(-84,48,-18),
(9,147,207),(0,-300,234),(84,-48,-18),(-112,-36,-102),(48,84,18),(-147,9,-207),
(-9,-147,207),(84,72,-18),(112,36,-102),(-48,-84,18),(147,-9,-207),(-18,126,144),
(-126,-18,-144),(-300,0,-234),(-84,-72,-18),(18,-126,144),(126,18,-144),(300,0,-234)
]
FACES = [
[6,10,16,22,18,7,5,1,2],
[9,15,11,18,22,13,8,3,4],
[7,5,8,3,17,23,9,15,14],
[13,8,5,1,12,19,6,10,21],
[1,2,11,18,7,14,24,20,12],
[3,4,16,22,13,21,20,24,17],
[14,24,17,23,19,6,2,11,15],
[10,21,20,12,19,23,9,4,16]
]
PLANES = [
((21,3,-10),-1440),((21,3,10),1440),((3,0,1),234),((3,0,-1),-234),
((0,3,-1),234),((0,3,1),-234),((3,-21,10),-1440),((3,-21,-10),1440)
]

B = [[-1,2,4],[-3,-4,2],[3,0,0]]
A = [
[F(0),F(0),F(1,3)],
[F(1,10),F(-1,5),F(-1,6)],
[F(1,5),F(1,10),F(1,6)]
]
T = [[0,1,0],[-1,0,0],[0,0,-1]]
C = [
[F(1,10),F(3,10),F(0)],
[F(-3,10),F(1,10),F(0)],
[F(0),F(0),F(1,3)]
]

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def mm(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def trans(M):
    return [list(r) for r in zip(*M)]

def inv3(M):
    d=det3(M)
    assert d != 0
    cof=[
        [M[1][1]*M[2][2]-M[1][2]*M[2][1], -(M[1][0]*M[2][2]-M[1][2]*M[2][0]), M[1][0]*M[2][1]-M[1][1]*M[2][0]],
        [-(M[0][1]*M[2][2]-M[0][2]*M[2][1]), M[0][0]*M[2][2]-M[0][2]*M[2][0], -(M[0][0]*M[2][1]-M[0][1]*M[2][0])],
        [M[0][1]*M[1][2]-M[0][2]*M[1][1], -(M[0][0]*M[1][2]-M[0][2]*M[1][0]), M[0][0]*M[1][1]-M[0][1]*M[1][0]]
    ]
    return [[F(cof[j][i],d) for j in range(3)] for i in range(3)]

def apply(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))

def primitive_sign(q):
    g=0
    for x in q:
        g=gcd(g,abs(x))
    q=tuple(x//g for x in q)
    for x in q:
        if x:
            if x<0:
                q=tuple(-y for y in q)
            return q
    raise ValueError

def orthogonal(M):
    return mm(trans(M),M)==[[F(i==j) for j in range(3)] for i in range(3)]

# Source incidences.
assert all(sum(n[k]*V[j-1][k] for k in range(3))==c
           for (n,c),face in zip(PLANES,FACES) for j in face)

# Difference lattice index is the gcd of full-rank 3x3 minors.
diffs=[tuple(V[i][j]-V[0][j] for j in range(3)) for i in range(1,len(V))]
minor_gcd=0
for inds in combinations(range(len(diffs)),3):
    M=[[diffs[inds[col]][row] for col in range(3)] for row in range(3)]
    minor_gcd=gcd(minor_gcd,abs(det3(M)))
assert minor_gcd==60
assert abs(det3(B))==60
assert mm(A,B)==[[F(i==j) for j in range(3)] for i in range(3)]

P=[apply(A,v) for v in V]
assert all(all(x.denominator==1 for x in p) for p in P)
P=[tuple(int(x) for x in p) for p in P]
# Hence the difference lattice is exactly B Z^3: it is contained there and both have index 60.

# Width of a dual-lattice covector q^T A.
def width(q):
    z=[sum(q[j]*p[j] for j in range(3)) for p in P]
    return max(z)-min(z)

# A finite certificate that all relevant short covectors lie in [-3,3]^3.
# The columns are p_8-p_1, p_20-p_1, p_24-p_1.
D=[[P[i-1][r]-P[0][r] for i in (8,20,24)] for r in range(3)]
assert D==[[72,-84,-84],[48,36,96],[12,-96,24]]
R=inv3(trans(D))
row_sums=[sum(abs(x) for x in row) for row in R]
assert max(row_sums)==F(157,7980)
assert 180*max(row_sums)<4

short_lt_168=[]
short_lt_180={}
for q in product(range(-3,4),repeat=3):
    if q==(0,0,0):
        continue
    w=width(q)
    if w<168:
        short_lt_168.append((q,w))
    if w<180:
        u=primitive_sign(q)
        short_lt_180[u]=min(short_lt_180.get(u,10**9),w)
assert short_lt_168==[((-1,0,0),156),((1,0,0),156)]
expected_dirs={
    (1,0,0):156,
    (0,1,0):168,
    (0,0,1):168,
    (1,0,-1):168,
    (1,1,0):168,
}
assert short_lt_180==expected_dirs

# Radius-84 optimal affine integer copy.
t=(0,15,15)
Q=[(p[0]+t[0],p[1]+t[1],p[2]+t[2]) for p in P]
assert max(max(abs(x) for x in q) for q in Q)==84
expected_Q=[
(6,-12,12),(34,-28,36),(6,36,24),(34,24,28),(78,-84,84),(-6,0,0),
(69,-48,66),(78,36,24),(-6,36,24),(-34,28,-28),(6,0,36),(-69,33,-48),
(69,9,33),(-6,12,36),(-34,36,24),(6,24,0),(-69,66,9),(48,-36,48),
(-48,30,-36),(-78,24,-84),(-6,24,-12),(48,18,30),(-48,48,18),(-78,84,36)
]
assert Q==expected_Q

new_planes=[]
for n,c in PLANES:
    a=tuple(sum(n[k]*B[k][j] for k in range(3)) for j in range(3))
    rhs=c+sum(a[j]*t[j] for j in range(3))
    g=0
    for z in a+(rhs,):
        g=gcd(g,abs(z))
    a=tuple(z//g for z in a); rhs//=g
    new_planes.append((a,rhs))
assert new_planes==[
((-2,1,3),12),((0,1,3),108),((0,1,2),84),((-1,1,2),6),
((-2,-2,1),24),((-1,-2,1),-54),((3,3,-1),-18),((1,3,-1),78)
]
assert all(sum(n[k]*Q[j-1][k] for k in range(3))==c
           for (n,c),face in zip(new_planes,FACES) for j in face)

# Symmetry-preserving radius-90 copy; C commutes with T.
S=[apply(C,v) for v in V]
assert all(all(x.denominator==1 for x in s) for s in S)
S=[tuple(int(x) for x in s) for s in S]
assert max(max(abs(x) for x in s) for s in S)==90
assert mm(C,T)==mm(T,C)

# Any hypothetical radius <90 has all three row widths <180, so its row directions
# must come from the five directions above. Up to row signs and permutation, test
# every independent triple; none conjugates T to an orthogonal matrix.
dirs=list(expected_dirs)
triples=0
for comb in combinations(dirs,3):
    if det3([list(q) for q in comb])==0:
        continue
    triples+=1
    M=[]
    for q in comb:
        M.append([sum(F(q[k])*A[k][j] for k in range(3)) for j in range(3)])
    O=mm(mm(M,T),inv3(M))
    assert not orthogonal(O)
assert triples==8

print('source_incidence: OK')
print('difference_lattice_index:', minor_gcd)
print('dual_short_width_lt_168:', short_lt_168)
print('dual_projective_width_lt_180:', sorted(short_lt_180.items()))
print('optimal_affine_integer_radius:', 84)
print('compressed_vertices:', Q)
print('compressed_planes:', new_planes)
print('symmetry_preserving_radius:', 90)
print('low_radius_independent_triples_checked:', triples)
print('all_exact_checks: OK')
