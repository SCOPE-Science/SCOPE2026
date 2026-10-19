"""Exhaustive finite-field certificate for three-dimensional unital commutative algebras over F3.

Run: python verify.py. Pure Python 3 standard library, no inputs.
All structure constants, quadrics, and basis changes are enumerated exactly.
"""
from itertools import product

P = 3
POINTS = [v for v in product(range(P), repeat=3)
          if any(v) and next(x for x in v if x) == 1]
SQUARES = [(x*x % P, 2*x*y % P, 2*x*z % P,
            y*y % P, 2*y*z % P, z*z % P) for x,y,z in POINTS]
assert len(POINTS) == 13


def dot(a, b):
    return sum(x*y for x,y in zip(a,b)) % P


def rank(rows):
    a = [list(row) for row in rows]
    if not a: return 0
    r = 0
    for col in range(len(a[0])):
        i = next((k for k in range(r,len(a)) if a[k][col] % P),None)
        if i is None: continue
        a[r],a[i] = a[i],a[r]
        inv = pow(a[r][col], -1, P)
        a[r] = [inv*x % P for x in a[r]]
        for k in range(len(a)):
            if k != r:
                h = a[k][col]
                a[k] = [(x-h*y)%P for x,y in zip(a[k],a[r])]
        r += 1
        if r == len(a): break
    return r


def nullspace(rows):
    a = [list(row) for row in rows]
    pivots = []
    r = 0
    for col in range(6):
        i = next((k for k in range(r,len(a)) if a[k][col] % P),None)
        if i is None:continue
        a[r],a[i] = a[i],a[r]
        inv = pow(a[r][col], -1, P)
        a[r] = [inv*x % P for x in a[r]]
        for k in range(len(a)):
            if k != r:
                h = a[k][col]
                a[k] = [(x-h*y)%P for x,y in zip(a[k],a[r])]
        pivots.append(col)
        r += 1
    out = []
    for k in range(6):
        if k not in pivots:
            v = [0]*6
            v[k] = 1
            for i,j in enumerate(pivots):v[j] = (-a[i][k])%P
            out.append(tuple(v))
    return out


def product_in_algebra(c, a, b):
    A, B, C = c[:3], c[3:6], c[6:9]
    return tuple((a[0]*b[0]*A[i] + (a[0]*b[1]+a[1]*b[0])*B[i]
                  +a[1]*b[1]*C[i] + a[2]*b[i]+b[2]*a[i]
                  - a[2]*b[2]*(i==2)) % P for i in range(3))


def quadric_rows(c):
    A, B, C = c[:3],c[3:6],c[6:9]
    return [tuple(v % P for v in (A[i], 2*B[i], 2*(i==0),
                                 C[i], 2*(i==1), i==2))
            for i in range(3)]


def maximal(c):
    f = quadric_rows(c)
    assert rank(f)==3 # the identity forces the image of squaring to span
    n = nullspace(f)
    assert len(n)==3
    for t in POINTS:
        form = tuple(sum(t[i]*n[i][j] for i in range(3)) % P
                     for j in range(6))
        if sum(dot(form,s)==0 for s in SQUARES)>=5:
            return False
    return True


def associative(c):
    basis = [(1,0,0), (0,1,0), (0,0,1)]
    for a in basis:
        for b in basis:
            for d in basis:
                if product_in_algebra(c,product_in_algebra(c,a,b),d) != \
                   product_in_algebra(c,a,product_in_algebra(c,b,d)):
                    return False
    return True

# Every conic having >=5 rational points supplies five independent square vectors.
# This verifies the finite geometric lemma for all projective ternary quadrics.
conic_profiles = {}
for n in product(range(P), repeat=6):
    if not any(n) or next(x for x in n if x) != 1: continue
    zero_squares = [s for s in SQUARES if dot(n,s)==0]
    profile = (len(zero_squares), rank(zero_squares))
    conic_profiles[profile] = conic_profiles.get(profile,0)+1
    if len(zero_squares)>=5:assert rank(zero_squares)==5
assert conic_profiles == {(4,3):13,(7,5):78,(1,1):39,(4,4):234}

# Six square vectors span the full quadratic space, giving the universal upper bound.
upper = [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1)]
assert rank([(x*x%P,2*x*y%P,2*x*z%P,y*y%P,2*y*z%P,z*z%P)
             for x,y,z in upper])==6

all_sharp = {c for c in product(range(P), repeat=9) if maximal(c)}
assert len(all_sharp)==288
assert sum(associative(c) for c in all_sharp)==144
# Verify the structural equivalence: maximal rank iff every nonzero
# multiplication operator is invertible, across all 19,683 tables.
def is_division(c):
    basis = [(1,0,0),(0,1,0),(0,0,1)]
    for v in product(range(P),repeat=3):
        if any(v) and rank([product_in_algebra(c,v,e) for e in basis]) != 3:
            return False
    return True
assert all(is_division(c) == (c in all_sharp)
           for c in product(range(P), repeat=9))

# All invertible linear basis changes that fix the identity (0,0,1).
transformations=[]
for a,b,d,e in product(range(P),repeat=4):
    determinant = (a*e-b*d)%P
    if determinant:
        inv=pow(determinant,-1,P)
        for z,w in product(range(P),repeat=2):
            transformations.append((a,b,z,d,e,w,inv))
assert len(transformations)==432

def change_basis(c,g):
    a,b,z,d,e,w,inv=g
    v0=(a,b,z)
    v1=(d,e,w)
    def reduce(v):
        x=inv*(e*v[0]-d*v[1])%P
        y=inv*(-b*v[0]+a*v[1])%P
        return (x,y,(v[2]-z*x-w*y)%P)
    return (reduce(product_in_algebra(c,v0,v0))
           +reduce(product_in_algebra(c,v0,v1))
           +reduce(product_in_algebra(c,v1,v1)))

remaining = set(all_sharp)
orbits=[]
while remaining:
    representative = min(remaining)
    orbit = {change_basis(representative, g) for g in transformations}
    assert orbit <= all_sharp
    orbits.append((representative,len(orbit),associative(representative)))
    remaining-=orbit
assert orbits == [
 ((0,1,0,0,1,2,2,0,2),144,False),
 ((0,1,0,0,1,2,2,1,2),144,True)]
# Directly verify division and the five-square lower bound for both orbit representatives.
from itertools import combinations
for representative, _, _ in orbits:
    basis = [(1,0,0),(0,1,0),(0,0,1)]
    for v in product(range(P),repeat=3):
        if any(v):
            assert rank([product_in_algebra(representative,v,e) for e in basis]) == 3
    forms = quadric_rows(representative)
    for five in combinations(SQUARES,5):
        assert rank(list(five)+forms) > rank(five)
print('VERIFY_OK: 19683 tables; 288 maximal; 144 associative; '
      'two isomorphism orbits of 144; all 364 projective quadrics checked')
