"""Exact certificate for tetrahedra in the snub cube, with algebraic root isolation.
Only Python standard-library modules are used. Run: python snub_exact_verifier.py
"""
from collections import defaultdict, Counter
from fractions import Fraction as F
from itertools import permutations, product, combinations
from math import comb

ZERO=(0,0,0); ONE=(1,0,0); T=(0,1,0); INV_T=(-1,-1,1)

def add(a,b): return tuple(a[i]+b[i] for i in range(3))
def neg(a): return tuple(-z for z in a)
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    t=[0]*5
    for i in range(3):
        for j in range(3):t[i+j]+=a[i]*b[j]
    c=t[4]; t[0]+=c;t[1]+=2*c;t[2]+=2*c
    c=t[3]; t[0]+=c;t[1]+=c;t[2]+=c
    return tuple(t[:3])
def vsub(a,b): return tuple(sub(a[i],b[i]) for i in range(3))
def cross(a,b):
    return (sub(mul(a[1],b[2]),mul(a[2],b[1])),
            sub(mul(a[2],b[0]),mul(a[0],b[2])),
            sub(mul(a[0],b[1]),mul(a[1],b[0])))
def dot(a,b):
    r=ZERO
    for i in range(3):r=add(r,mul(a[i],b[i]))
    return r

def det4(a,b,c,d):
    return dot(vsub(b,a),cross(vsub(c,a),vsub(d,a)))

def pol(x): return x[0]+x[1]*F(1839286755214,10**12)+x[2]*F(1839286755214,10**12)**2
L=F(1839286755214,10**12)
U=F(1839286755215,10**12)
def cubic(x):return x*x*x-x*x-x-1
assert 1<L<U<2 and cubic(L)<0<cubic(U)
def lower(a):
    return F(a[0])+min(a[1]*L,a[1]*U)+min(a[2]*L*L,a[2]*U*U)
def upper(a):
    return F(a[0])+max(a[1]*L,a[1]*U)+max(a[2]*L*L,a[2]*U*U)
def sign(a):
    if a==ZERO:return 0
    if lower(a)>0:return 1
    if upper(a)<0:return -1
    raise ArithmeticError('root enclosure insufficient for '+str(a))

basis=(ONE,INV_T,T)
V=[]
for perm in permutations(range(3)):
    parity=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2
    for signs in product((-1,1),repeat=3):
        if sum(s>0 for s in signs)%2 != parity:continue
        V.append(tuple(basis[perm[j]] if signs[j]>0 else neg(basis[perm[j]]) for j in range(3)))
assert len(V)==24 and len(set(V))==24

MAX=(8,4,4) # maximal oriented determinant predicted by the exact computation
maxima=[]; diffs=[]; mult=Counter(); positive_gaps=[]
for I in combinations(range(24),4):
    v=det4(*(V[i] for i in I))
    mult[v]+=1
    if sign(sub(MAX,v))<0 or sign(add(MAX,v))<0:
        raise AssertionError(('exceeds maximum',I,v))
    if v==MAX or v==neg(MAX): maxima.append(I)
    else:
        for z in [sub(MAX,v),add(MAX,v)]:
            assert sign(z)==1
            positive_gaps.append(z)
assert len(maxima)==24
assert sum(mult.values())==comb(24,4)==10626
assert len(mult)>3

apices=defaultdict(set)
for I in maxima:
    for triple in combinations(I,3):
        apices[triple].add(next(i for i in I if i not in triple))
assert Counter(map(len,apices.values()))=={1:72,3:8}
base_triples={a:tuple(sorted(b)) for a,b in apices.items() if len(b)==3}
assert len(base_triples)==8
assert len(set((tuple(sorted(set(a)|{b}))) for a,B in base_triples.items() for b in B))==24
for I in maxima:
    assert sum(tuple(j for j in I if j!=k) in base_triples for k in I)==1
# A size-24 rotation group acts on the vertex set; these eight families form one orbit.
rotations=[]
for perm in permutations(range(3)):
    parity=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2
    for sig in product((-1,1),repeat=3):
        if (sum(z<0 for z in sig)%2)!=parity:continue
        def image_vertex(v,perm=perm,sig=sig):
            return tuple(v[perm[i]] if sig[i]>0 else neg(v[perm[i]]) for i in range(3))
        pmap=tuple(V.index(image_vertex(v)) for v in V)
        rotations.append(pmap)
assert len(rotations)==24 and len(set(rotations))==24
seed_A=min(base_triples)
seed_B=base_triples[seed_A]
orbit={(
    tuple(sorted(g[i] for i in seed_A)),
    tuple(sorted(g[i] for i in seed_B))) for g in rotations}
assert len(orbit)==8 and orbit==set(base_triples.items())

# Geometric side lengths: every fixed long base is equilateral; every movable
# apex face is a smaller equilateral triangle. Both are nondegenerate.
def sqdist(i,j):
    a=vsub(V[i],V[j]);return dot(a,a)
for A,B in base_triples.items():
    assert len({sqdist(i,j) for i,j in combinations(A,2)})==1
    assert len({sqdist(i,j) for i,j in combinations(B,2)})==1
    assert {sqdist(i,j) for i,j in combinations(A,2)}=={(-2,4,2)}
    assert {sqdist(i,j) for i,j in combinations(B,2)}=={(2,4,-2)}

# The eight variable-apex triples are genuine triangular support faces.
for B in base_triples.values():
    normal=cross(vsub(V[B[1]],V[B[0]]),vsub(V[B[2]],V[B[0]]))
    vals=[dot(normal,vsub(v,V[B[0]])) for v in V]
    sgn={sign(v) for v in vals if v!=ZERO}
    assert len(sgn)==1
    assert [i for i,v in enumerate(vals) if v==ZERO]==list(B)
# For each three-point fixed base, all vertex maximal apices give same oriented determinant.
for A,B in base_triples.items():
    vals=[det4(V[A[0]],V[A[1]],V[A[2]],V[j]) for j in B]
    assert len(set(vals))==1 and abs(float(lower(vals[0])))>0

print('vertex_count=24')
print('four_vertex_subsets=10626')
print('distinct_oriented_det_polynomials='+str(len(mult)))
print('max_abs_det=8+4*t+4*t^2')
print('max_vertex_tetrahedra=24')
print('nontrivial_fixed_base_triangles=8')
print('support_counts='+str(dict(Counter(map(len,apices.values())))))
print('root_interval='+str(L)+' < t < '+str(U))
print('eight_fixed_base_and_variable_triangular_face_groups:')
for A,B in sorted(base_triples.items()):print(A,'->',B)
print('all_exact_checks_passed')
