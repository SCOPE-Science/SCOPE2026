from fractions import Fraction
from itertools import permutations, combinations
from math import gcd

# P^1 points [u:v] for t=u/v: 0, infinity, 1, -1.
S = [(0,1),(1,0),(1,1),(-1,1)]

def det(p,q):
    return p[0]*q[1]-p[1]*q[0]

def cr(a,b,c,d):
    return Fraction(det(a,c)*det(b,d), det(a,d)*det(b,c))

base = cr(*S)
assert base == -1
# A permutation of four distinct marked points is induced by a unique Mobius
# map iff it preserves the ordered cross-ratio of one base quadruple.
G = [p for p in permutations(range(4)) if cr(*(S[i] for i in p)) == base]
assert len(G) == 8

# The maps r(t)=(t-1)/(t+1) and s(t)=-t act on the marked set as follows.
r = (3,2,0,1)  # 0->-1, inf->1, 1->0, -1->inf
s = (0,1,3,2)  # 0->0, inf->inf, 1<->-1
assert r in G and s in G

def compose(p,q):
    return tuple(p[q[i]] for i in range(4))

def power(p,n):
    out=(0,1,2,3)
    for _ in range(n): out=compose(p,out)
    return out
assert power(r,4)==(0,1,2,3) and power(r,2)!=(0,1,2,3)
assert power(s,2)==(0,1,2,3)
assert compose(compose(s,r),s)==power(r,3)
H={(0,1,2,3)}
changed=True
while changed:
    changed=False
    for a in list(H):
        for b in (r,s):
            c=compose(a,b)
            if c not in H:
                H.add(c); changed=True
assert len(H)==8 and H==set(G)

# Conic parameterization nu([u:v])=[2uv:v^2-u^2:v^2+u^2].
# The six line components of Q6 and the marked pairs they cut on the conic.
lines = {
    'x': (1,0,0),
    'y': (0,1,0),
    'y+x-z': (1,1,-1),
    'y-x-z': (-1,1,-1),
    'y+x+z': (1,1,1),
    'y-x+z': (-1,1,1),
}

def nu(p):
    u,v=p
    return (2*u*v, v*v-u*u, v*v+u*u)
def eval_line(L,P):
    return sum(a*b for a,b in zip(L,P))
inc={name:tuple(i for i,p in enumerate(S) if eval_line(L,nu(p))==0) for name,L in lines.items()}
expected_pairs=set(combinations(range(4),2))
assert set(inc.values())==expected_pairs
assert all(len(pair)==2 for pair in inc.values())

# Exact line-line intersections: four marked points carry three chords each,
# while the three disjoint-edge pairs meet in three additional nodes.
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def norm(P):
    vals=list(P); g=0
    for v in vals: g=gcd(g,abs(v))
    vals=[v//g for v in vals]
    for v in vals:
        if v:
            if v<0: vals=[-w for w in vals]
            break
    return tuple(vals)
I={}
items=list(lines.items())
for (na,la),(nb,lb) in combinations(items,2):
    I.setdefault(norm(cross(la,lb)), []).append((na,nb))
triple_line_pts=[P for P,pairs in I.items() if len(pairs)==3]
simple_line_pts=[P for P,pairs in I.items() if len(pairs)==1]
assert set(triple_line_pts)=={norm(nu(p)) for p in S}
assert len(simple_line_pts)==3
# Conic q=x^2+y^2-z^2 vanishes at the four chord vertices and not at the 3 others.
def q(P): return P[0]*P[0]+P[1]*P[1]-P[2]*P[2]
assert all(q(P)==0 for P in triple_line_pts)
assert all(q(P)!=0 for P in simple_line_pts)

# Explicit plane generators induced from r,s under the quadratic Veronese model:
# R[x:y:z]=[-y:x:z], S[x:y:z]=[-x:y:z]. Both preserve the conic and permute line factors.
def mat_apply(M,L):
    # pullback of line coefficient row L under point map M: L*M
    return tuple(sum(L[i]*M[i][j] for i in range(3)) for j in range(3))
def canon(L):
    vals=list(L); g=0
    for v in vals: g=gcd(g,abs(v))
    vals=[v//g for v in vals]
    for v in vals:
        if v:
            if v<0: vals=[-w for w in vals]
            break
    return tuple(vals)
R=((0,-1,0),(1,0,0),(0,0,1))
Sm=((-1,0,0),(0,1,0),(0,0,1))
line_set={canon(L) for L in lines.values()}
for M in (R,Sm):
    assert {canon(mat_apply(M,L)) for L in lines.values()}==line_set

print('VERIFY_OK')
print('cross_ratio=-1')
print('mobius_stabilizer_order=8')
print('group=dihedral_order_8')
print('line_chords=6 quadruple_points=4 nodes=3')
