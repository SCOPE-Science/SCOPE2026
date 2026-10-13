from itertools import combinations, permutations, product
from fractions import Fraction

# Source quadruple points for Komiya-Kuribayashi bitangent arrangement.
P=[
 (1,0,-1),(1,0,0),(1,0,1),
 (0,1,-1),(0,1,0),(0,1,1),
 (-1,1,0),(1,1,0),(0,0,1)
]
# The dual line to (a:b:c) is a*x+b*y+c*z=0; normalize integer triples up to scalar.
def norm(v):
    from math import gcd
    a,b,c=v
    g=0
    for q in (a,b,c): g=gcd(g,abs(q))
    if g: a,b,c=a//g,b//g,c//g
    for q in (a,b,c):
        if q:
            if q<0: a,b,c=-a,-b,-c
            break
    return (a,b,c)
L={norm(p) for p in P}
B3={norm(v) for v in [
 (1,0,0),(0,1,0),(0,0,1),
 (1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)
]}
assert L==B3

# Projective line intersections and multiplicities.
def cross(u,v):
    return norm((u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]))
pts={}
Ls=sorted(L)
for a,b in combinations(Ls,2):
    q=cross(a,b)
    pts.setdefault(q,set()).update([a,b])
# Replace by all lines through each point.
for q in list(pts):
    pts[q]={l for l in Ls if l[0]*q[0]+l[1]*q[1]+l[2]*q[2]==0}
mult={q:len(s) for q,s in pts.items()}
counts={m:sum(1 for q in mult if mult[q]==m) for m in sorted(set(mult.values()))}
assert counts=={2:6,3:4,4:3},counts
quad={q for q,m in mult.items() if m==4}
triple={q for q,m in mult.items() if m==3}
double={q for q,m in mult.items() if m==2}
assert quad=={(1,0,0),(0,1,0),(0,0,1)}
assert triple=={norm(q) for q in [(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1)]}

# Sign-permutation projective group: 6 permutations * 4 sign classes =24.
def mat_key(perm,sgn):
    # matrix M sends coordinates x_i -> s_i*x_{perm[i]}; normalize global sign.
    M=[[0]*3 for _ in range(3)]
    for i in range(3): M[i][perm[i]]=sgn[i]
    flat=tuple(sum(M,[]))
    # normalize first nonzero positive
    for a in flat:
        if a:
            if a<0: flat=tuple(-x for x in flat)
            break
    return flat
G=set()
for perm in permutations(range(3)):
    for sgn in product([1,-1], repeat=3):
        G.add(mat_key(perm,sgn))
assert len(G)==24

# Check every group element preserves B3 lines by contragredient action.
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def inv3(M):
    d=det3(M); assert d in (1,-1)
    C=[[0]*3 for _ in range(3)]
    for i in range(3):
      for j in range(3):
        rows=[r for r in range(3) if r!=j]; cols=[c for c in range(3) if c!=i]
        minor=M[rows[0]][cols[0]]*M[rows[1]][cols[1]]-M[rows[0]][cols[1]]*M[rows[1]][cols[0]]
        C[i][j]=((-1)**(i+j))*minor//d
    return C
for flat in G:
    M=[list(flat[3*i:3*i+3]) for i in range(3)]
    Mi=inv3(M)
    # line row l maps to l*M^{-1}
    image=set()
    for l in L:
        w=tuple(sum(l[k]*Mi[k][j] for k in range(3)) for j in range(3))
        image.add(norm(w))
    assert image==L

# Orbit sizes of line set under G: 3 coordinate + 6 diagonal.
def is_coord(l): return sum(1 for a in l if a!=0)==1
assert sum(is_coord(l) for l in L)==3
assert len(L)==9

# Pair count sanity.
assert 6*1 + 4*3 + 3*6 == 36 == 9*8//2
print('VERIFY_OK')
print('dual_arrangement=B3')
print('intersection_counts=t2:6,t3:4,t4:3')
print('projective_stabilizer_order=24=S4')
print('line_orbits=3_coordinate+6_diagonal')
