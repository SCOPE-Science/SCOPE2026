#!/usr/bin/env python3
"""Finite exact checks for the oriented-line extension of the Fano matroid complex.
Uses only the Python standard library. All arithmetic is over integers.
"""
from collections import Counter
from itertools import combinations, product
from math import gcd

P = tuple(range(1, 8))
TRI = tuple(combinations(P, 3))
EDGES = tuple(combinations(P, 2))
LINES = tuple(t for t in TRI if t[0] ^ t[1] ^ t[2] == 0)
BASES = tuple(t for t in TRI if t not in LINES)
assert len(LINES) == 7 and len(BASES) == 28
assert all(sum((e[0] in L and e[1] in L) for L in LINES) == 1 for e in EDGES)

# A linear map on F_2^3 is determined by its columns, each nonzero.
G = []
for a, b, c in product(P, repeat=3):
    if a ^ b == c or len({a,b,c}) < 3:
        continue
    def map_point(x):
        return ((a if x & 1 else 0) ^ (b if x & 2 else 0)
                ^ (c if x & 4 else 0))
    G.append(tuple(map_point(x) for x in P))
assert len(G) == 168 and len(set(G)) == 168
ID = P

def sign(xs):
    return -1 if sum(x > y for i,x in enumerate(xs) for y in xs[i+1:]) % 2 else 1

def act(p, t):
    x = tuple(p[i-1] for i in t)
    return tuple(sorted(x)), sign(x)

def compose(p, q):
    return tuple(p[q[i-1]-1] for i in P)

def order(p):
    q, k = p, 1
    while q != ID:
        q = compose(p,q); k += 1
    return k

def trace_on_faces(p, faces):
    return sum(s for face in faces for dest,s in (act(p,face),) if dest == face)

# Augmented chain-Lefschetz formula: H_2 is the only nonzero
# reduced homology because the matroid independence complex is shellable.
chars = Counter()
for g in G:
    top = -1 + trace_on_faces(g, [(i,) for i in P]) - trace_on_faces(g, EDGES) + trace_on_faces(g, BASES)
    line = trace_on_faces(g, LINES)
    alltop = top + line
    chars[(order(g), top, line, alltop)] += 1
assert chars == Counter({
    (1, 13, 7, 20):1,
    (2, -3, -1, -4):21,
    (3, 1, 1, 2):56,
    (4, 1, -1, 0):42,
    (7, -1, 0, -1):48,
})
assert sum(s*(c*c) for (_,c,_,_),s in chars.items()) == 3*168 # 7 + 3 + conjugate 3
assert sum(s*(l*l) for (_,_,l,_),s in chars.items()) == 168   # signed line module irreducible
# The GL(3,2)=PSL(2,7) character table identifies the 13-character as 7+3+3bar.

# The topological relative map H_2(S) -> H_2(S,K) is the restriction
# of coefficients of oriented triangles to Fano lines.
# For every line L, a 4-subset L + p has only this one dependent triple,
# so the boundary of the tetrahedron maps to +/- a basis vector.
for line in LINES:
    external = next(i for i in P if i not in line)
    quad = tuple(sorted(line + (external,)))
    dependent_faces = [face for face in combinations(quad, 3) if face in LINES]
    assert dependent_faces == [line], (line, dependent_faces)

# Local integral obstruction to an equivariant splitting.
L = (1,2,3)
H = [g for g in G if act(g,L)[0] == L]
assert len(H) == 24
EPS = lambda g: act(g,L)[1]

def signed_orbits(faces):
    seen = set(); result=[]
    for f in faces:
        if f in seen:continue
        orb = {act(h,f)[0] for h in H}
        seen.update(orb)
        coefficients={}; consistent=True
        for h in H:
            target, orient=act(h,f)
            coefficient=EPS(h)*orient
            if target in coefficients and coefficients[target]!=coefficient:
                consistent=False
            coefficients[target]=coefficient
        result.append((f,len(orb),consistent, coefficients if consistent else None))
    return result

orbits = signed_orbits(TRI)
assert [(f,n,ok) for f,n,ok,_ in orbits] == [
    ((1,2,3),1,True), ((1,2,4),12,True),
    ((1,4,5),6,False),((1,4,6),12,False),((4,5,6),4,True)]
coeffs=[z for _,_,ok,z in orbits if ok]

def boundary(z):
    out={e:0 for e in EDGES}
    for face,coefficient in z.items():
        for j in range(3):
            out[face[:j]+face[j+1:]]+=(-1)**j*coefficient
    return out
borders=[boundary(z) for z in coeffs]
E={e:0 for e in EDGES}
E[(1,2)]=1;E[(1,3)]=-1;E[(2,3)]=1
assert borders[0]==E
assert borders[1]=={e:4*v for e,v in E.items()}
assert borders[2]=={e:0 for e in EDGES}
assert [z.get(L,0) for z in coeffs]==[1,0,0]
# Thus H-sign vectors in the triangle cycle lattice have line coefficient -4b.
# Explicit cycle z (12 outer triangles minus four times the line triangle).
cycle={t:coeffs[1].get(t,0)-4*coeffs[0].get(t,0) for t in TRI}
assert all(v==0 for v in boundary({t:v for t,v in cycle.items() if v}).values())
assert cycle[L]==-4
assert all(cycle.get(other,0)==0 for other in LINES if other!=L)
for h in H:
    actcycle={}
    for t,val in cycle.items():
        if val:
            target,s=act(h,t)
            actcycle[target]=val*s
    assert all(actcycle.get(t,0)==EPS(h)*cycle.get(t,0) for t in TRI)
# The rational equivariant extension splits by averaging, but any integral
# G-section would restrict to an H-sign cycle with line coefficient one.
# The displayed integral orbit basis forces that coefficient divisible by 4.
# Conversely the cycle here gives a G-map with projection -4*identity.
print('FANO_FACETS', len(BASES),'FANO_LINES',len(LINES),'FULL_GROUP',len(G))
print('CHARACTER_BY_ORDER_H2_LINE_FULL', sorted(chars.items()))
print('LINE_STABILIZER',len(H),'TRIPLE_ORBITS',[(f,n,ok) for f,n,ok,_ in orbits])
print('SIGNED_ORBIT_BOUNDARY_MULTIPLIERS',(1,4,0),'EXACT_LOCAL_INDEX',4)
print('RATIONAL_DECOMPOSITION', '7 + 3 + conjugate_3')
print('VERIFY_OK_FANO_MATROID_ORIENTED_LINE_EXTENSION')
