#!/usr/bin/env python3
"""Exact, reproducible homology and octahedral-character certificate.

Dependencies: Python 3.10+ and SymPy. Every calculation is finite and exact.
The model is the cubical unordered two-point discretized configuration space
of the octahedral graph, with original vertices labelled 0,...,5.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from sympy import Matrix, zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

V = tuple(range(6))
E = tuple(combinations(V, 2))
E = tuple(e for e in E if e[0] // 2 != e[1] // 2)
C0 = tuple(combinations(V, 2))
C1 = tuple(sorted((v, e) for v in V for e in E if v not in e))
C2 = tuple((e, f) for e, f in combinations(E, 2) if not set(e) & set(f))
assert (len(C0), len(C1), len(C2)) == (15, 48, 30)
I0, I1, I2 = ({x: i for i, x in enumerate(c)} for c in (C0, C1, C2))
d1 = zeros(15, 48)
d2 = zeros(48, 30)
for j, (v, (a, b)) in enumerate(C1):
    d1[I0[tuple(sorted((v, b)))], j] = 1
    d1[I0[tuple(sorted((v, a)))], j] = -1
for j, ((a, b), (c, d)) in enumerate(C2):
    for (v, edge), s in (((b, (c,d)),1), ((a,(c,d)),-1),
                          ((d,(a,b)),-1), ((c,(a,b)),1)):
        d2[I1[(v, edge)], j] = s
assert d1 * d2 == zeros(15, 30)
assert d1.rank() == 14 and d2.rank() == 26
smith = smith_normal_form(d2, domain=ZZ)
nonzeros = [abs(int(smith[i,i])) for i in range(min(smith.shape)) if smith[i,i]]
assert nonzeros == [1] * 26   # no integral torsion in H_1

# Four unordered products of disjoint triangular boundary loops.
faces = tuple(tuple(2*a+s for a,s in enumerate((0,b,c)))
              for b,c in product((0,1), repeat=2))
assert faces == ((0,2,4),(0,2,5),(0,3,4),(0,3,5))

def oriented_edges(face):
    for a,b in zip(face, face[1:] + face[:1]):
        yield tuple(sorted((a,b))), (1 if a < b else -1)

def torus(face):
    other = tuple(x ^ 1 for x in face)
    cycle = zeros(30,1)
    for (e,se),(f,sf) in product(oriented_edges(face),oriented_edges(other)):
        ef = tuple(sorted((e,f)))
        cycle[I2[ef]] += se*sf*(1 if ef == (e,f) else -1)
    assert d2*cycle == zeros(48,1)
    return cycle

tori = Matrix.hstack(*(torus(face) for face in faces))
# Four coordinate squares provide an integral unimodular minor;
# because kernel(d2) has rank four this establishes an integral basis.
assert int(tori[[0,1,5,6], :].det()) == 1
assert tori.rank() == 4

def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def act_vertices(p, flips):
    return tuple(2*p[v//2]+((v%2)^flips[p[v//2]]) for v in V)

def act_edge(m, e):
    ends = (m[e[0]], m[e[1]])
    return tuple(sorted(ends)), (1 if ends[0]<ends[1] else -1)

def image_c1(m, ve):
    v,e = ve
    ee,s = act_edge(m,e)
    return I1[(m[v],ee)],s

def image_c2(m, ef):
    e,f = ef
    ee,se=act_edge(m,e);ff,sf=act_edge(m,f)
    pair=tuple(sorted((ee,ff)))
    return I2[pair],se*sf*(1 if pair == (ee,ff) else -1)

def image_c0(m, pair):
    return I0[tuple(sorted(m[x] for x in pair))]

def mapped_chain(m, c, source, target):
    res=zeros(len(target),1)
    action={C0:image_c0,C1:image_c1,C2:image_c2}[source]
    for i,coef in enumerate(c):
        if not coef:continue
        if source is C0:
            res[action(m,source[i])]+=coef
        else:
            j,sign=action(m,source[i]);res[j]+=sign*coef
    return res

# Character table of rational irreducibles of the proper rotation group S4.
S4_CHARS={
  'trivial':{(1,1,1,1):1,(2,1,1):1,(2,2):1,(3,1):1,(4,):1},
  'sign':{(1,1,1,1):1,(2,1,1):-1,(2,2):1,(3,1):1,(4,):-1},
  'standard':{(1,1,1,1):3,(2,1,1):1,(2,2):-1,(3,1):0,(4,):-1},
  'signed_standard':{(1,1,1,1):3,(2,1,1):-1,(2,2):-1,(3,1):0,(4,):1},
  'two_dimensional':{(1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0}}
records=[]
orientation_gauge=(-1,1,1,-1)
for p in permutations(range(3)):
 for flips in product((0,1),repeat=3):
    m=act_vertices(p,flips)
    # Entire cubical chain complex is equivariant, not merely its Euler trace.
    for j in range(48):
        assert mapped_chain(m,d1[:,j],C0,C0) == \
            d1[:,image_c1(m,C1[j])[0]]*image_c1(m,C1[j])[1]
    for j in range(30):
        assert mapped_chain(m,d2[:,j],C1,C1) == \
            d2[:,image_c2(m,C2[j])[0]]*image_c2(m,C2[j])[1]
    faceperm=[];signs=[]
    for f in faces:
        mapped=tuple(m[v] for v in f)
        sign_vector=[0]*3
        for x in mapped:sign_vector[x//2]=x%2
        normalized=tuple(2*a+(s^sign_vector[0]) for a,s in enumerate(sign_vector))
        destination=faces.index(normalized)
        faceperm.append(destination)
        signs.append((-1)**sign_vector[0])
    assert sorted(faceperm) == [0,1,2,3]
    for j in range(4):
        assert mapped_chain(m,tori[:,j],C2,C2) == signs[j]*tori[:,faceperm[j]]
    det=(-1)**sum(flips)*parity(p)  # parity of physical octahedral isometry
    # Wreath product B3 is the direct product S4 (proper rotations) x C2 (central inversion).
    sgn4=parity(faceperm)
    assert all(signs[i]==det*sgn4*orientation_gauge[faceperm[i]]*orientation_gauge[i]
               for i in range(4))
    visited=set();cyc=[]
    for i in range(4):
        if i not in visited:
            length=0;j=i
            while j not in visited:
                visited.add(j);j=faceperm[j];length+=1
            cyc.append(length)
    shape=tuple(sorted(cyc,reverse=True))
    char0=sum(image_c0(m,x)==j for j,x in enumerate(C0))
    char1=sum(s for j,x in enumerate(C1) for k,s in [image_c1(m,x)] if k==j)
    char2=sum(s for j,x in enumerate(C2) for k,s in [image_c2(m,x)] if k==j)
    hom2=sum(signs[j] for j in range(4) if j==faceperm[j])
    hom1=1+hom2-(char0-char1+char2)  # equivariant Hopf trace
    records.append((shape,det,hom1,hom2))
assert len(records)==48 and len(set((r[0],r[1]) for r in records))==10
CLASS_ORDER=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
TABLE={}
for shape in CLASS_ORDER:
  for det in (1,-1):
    vals={(h1,h2) for s,d,h1,h2 in records if s==shape and d==det}
    assert len(vals)==1
    TABLE[(shape,det)]=next(iter(vals))
assert TABLE == {
 ((1,1,1,1),1):(8,4),((1,1,1,1),-1):(0,-4),
 ((2,1,1),1):(0,-2),((2,1,1),-1):(-4,2),
 ((2,2),1):(0,0),((2,2),-1):(0,0),
 ((3,1),1):(2,1),((3,1),-1):(0,-1),
 ((4,),1):(0,0),((4,),-1):(0,0),
}
expected={
  0:{('trivial',-1):1,('sign',1):1,('standard',-1):1,('signed_standard',1):1},
  1:{('sign',-1):1,('signed_standard',-1):1}}
for degree in (0,1):
 actual={}
 for name,ir in S4_CHARS.items():
    for eps in (1,-1):
       total=sum(row[2+degree]*ir[row[0]]*(1 if eps==1 else row[1]) for row in records)
       assert total%48==0
       mult=total//48
       assert mult>=0
       if mult:actual[(name,eps)]=mult
 assert actual==expected[degree],(degree,actual)
print('PASS: cells 15/48/30; boundary ranks 14/26; Smith invariants 1^26.')
print('PASS: integral homology Z in H0, Z^8 in H1, Z^4 in H2.')
print('PASS: four disjoint triangular-face tori are an integral H2 basis.')
print('PASS: all 48 automorphisms commute with chain differentials and act on tori.')
print('PASS: full rational S4 x C2 character, 10 classes, and irreducible multiplicities.')
for shape in CLASS_ORDER:
 print('CLASS',shape,'proper',TABLE[(shape,1)],'improper',TABLE[(shape,-1)])
