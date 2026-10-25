#!/usr/bin/env python3
"""Exact matching-complex and integral involution-lattice certificate for the Tietze graph.

Python 3, NetworkX 3.6.1 and SymPy 1.14.0. No input files or network access.
Edges are numbered from zero in lexicographic order. A face is its edge-bitmask.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import gcd
import networkx as nx
from sympy import Matrix, eye
from sympy.matrices.normalforms import hermite_normal_form

E = [(1,2),(1,6),(1,10),(2,3),(2,7),(3,4),(3,8),(4,9),(4,11),
     (5,7),(5,8),(5,12),(6,8),(6,9),(7,9),(10,11),(10,12),(11,12)]
assert E == sorted(E)
n=len(E)
G=nx.Graph();G.add_edges_from(E)
assert (len(G),len(E))==(12,18)
assert all(d==3 for v,d in G.degree())
conflict=[sum((1<<j) for j,ej in enumerate(E) if j!=i and bool(set(ei)&set(ej)))
          for i,ei in enumerate(E)]
face=set()
by_dim=defaultdict(list)
for mask in range(1,1<<n):
    if all(not(mask>>i&1) or not(mask&conflict[i]) for i in range(n)):
        face.add(mask)
        by_dim[mask.bit_count()-1].append(mask)
for d in by_dim:by_dim[d].sort()
assert [len(by_dim[k]) for k in range(6)]==[18,117,335,408,165,8]
assert len(face)==1051

# A complete elementary matching. Order is fixed certificate data, not a heuristic search.
vertex_order=[1,10,2,13,6,3,17,0,14,11,16,8,7,12,9,4,15,5]
remaining=set(face)
pairs=[]
for v in vertex_order:
    bit=1<<v
    for lo in sorted(remaining):
        up=lo|bit
        if not(lo&bit) and up in remaining:
            remaining.remove(lo); remaining.remove(up)
            pairs.append((lo,up))
assert len(pairs)==517
crit=Counter(x.bit_count()-1 for x in remaining)
assert crit=={0:1,3:16}

# Verify all directed Hasse incidences, with paired arrows reversed.
D=nx.DiGraph();D.add_nodes_from(face)
matched=set(pairs)
for up in face:
    for i in range(n):
        if up>>i&1:
            lo=up^(1<<i)
            if lo in face:
                D.add_edge(up,lo) if (lo,up) in matched else D.add_edge(lo,up)
assert D.number_of_edges()==3744
assert nx.is_directed_acyclic_graph(D)
assert len(list(nx.topological_sort(D)))==1051
critical3=sorted(f for f in remaining if f.bit_count()==4)
critical3_index={f:i for i,f in enumerate(critical3)}
upward3={lo:up for lo,up in pairs if lo.bit_count()==4}

def bd_face(up):
    return [(up^(1<<i),(-1)**k) for k,i in enumerate(i for i in range(n) if up>>i&1)]

# Topologically sorted unit eliminations of 3/4 face pairs.
G3=nx.DiGraph();G3.add_nodes_from(upward3)
for lo,up in upward3.items():
    for another,coefficient in bd_face(up):
        if another!=lo and another in upward3:G3.add_edge(lo,another)
assert nx.is_directed_acyclic_graph(G3)
order3=list(nx.topological_sort(G3))
def project_cycle(c):
    c=defaultdict(int,c)
    for lo in order3:
        a=c.get(lo,0)
        if not a:continue
        up=upward3[lo]
        bd=bd_face(up)
        pivot=next(s for f,s in bd if f==lo)
        for f,s in bd:c[f]-=a*pivot*s
    assert all(c[f]==0 for f in upward3)
    return [c.get(f,0) for f in critical3]

# The projection vanishes on every simplicial 4-boundary.
for f in by_dim[4]:
    assert project_cycle(dict(bd_face(f))) == [0]*16

def boundary(c):
    result=defaultdict(int)
    for f,a in c.items():
        for sub,coeff in bd_face(f):result[sub]+=a*coeff
    return {f:a for f,a in result.items() if a}

def sphere_cycle(mask):
    # The intersection graph of eight edges has four independent conflict pairs.
    ids=[i for i in range(n) if mask>>i&1]
    used=set();pairs4=[]
    for i in ids:
        if i in used:continue
        con=conflict[i]&mask
        assert con.bit_count()==1
        j=con.bit_length()-1
        assert j!=i
        used.add(i);used.add(j)
        pairs4.append((min(i,j),max(i,j)))
    pairs4.sort()
    assert len(pairs4)==4 and len(used)==8
    c=defaultdict(int)
    for selectors in product((0,1),repeat=4):
        seq=[pairs4[k][selectors[k]] for k in range(4)]
        m=sum(1<<x for x in seq)
        inversions=sum(seq[i]>seq[j] for i in range(4) for j in range(i+1,4))
        c[m]+=(-1)**(sum(selectors)+inversions)
    assert len(c)==16 and not boundary(c)
    return dict(c)

supports=[]
for ids in combinations(range(n),8):
    m=sum(1<<i for i in ids)
    if all((conflict[i]&m).bit_count()==1 for i in ids):supports.append(m)
assert len(supports)==63
cycles={m:sphere_cycle(m) for m in supports}
columns={m:project_cycle(cycles[m]) for m in supports}
assert all(gcd(*map(abs,columns[m]))==1 for m in supports)

# Exhaustively identify automorphisms, their center, and carrier orbits.
autos=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(autos)==12
edge_id={e:i for i,e in enumerate(E)}
perms=[[edge_id[tuple(sorted((p[a],p[b])))] for a,b in E] for p in autos]
identity=list(range(n))
def compose(p,q):return [p[q[i]] for i in range(n)]
center=[p for p in perms if all(compose(p,q)==compose(q,p) for q in perms)]
assert len(center)==2
involution=next(p for p in center if p!=identity)
assert compose(involution,involution)==identity

def element_order(p):
    q=identity[:]
    for k in range(1,13):
        q=compose(p,q)
        if q==identity:return k
    raise AssertionError('automorphism order did not divide 12')
three=[p for p in perms if element_order(p)==3]
reflection=[p for p in perms if element_order(p)==2 and p!=involution]
assert any(compose(compose(b,a),b)==compose(a,a)
           and len({tuple(compose(compose(pow_a,pow_b),pow_t))
                    for pow_a in (identity,a,compose(a,a))
                    for pow_b in (identity,b)
                    for pow_t in (identity,involution)})==12
           for a in three for b in reflection)
# Thus the full group has the S_3 x C_2 presentation.

def apply_mask(m,p):return sum(1<<p[i] for i in range(n) if m>>i&1)

remaining_supports=set(supports)
orbits=[]
while remaining_supports:
    m=min(remaining_supports)
    orbit={apply_mask(m,p) for p in perms}
    assert orbit <= remaining_supports
    orbits.append(sorted(orbit))
    remaining_supports-=orbit
assert [len(o) for o in orbits]==[6,12,12,3,12,12,6]

# The following eight pairs have orbit representatives selected from the 63 supports.
central_pairs=[(115299,115907),(180835,181443),(157797,149710),
               (15141,3486),(27941,3022),(7109,19766),
               (47881,44314),(80177,72090)]
assert all(a in columns and b in columns and apply_mask(a,involution)==b
           for a,b in central_pairs)
reps=[m for a,b in central_pairs for m in (a,b)]
B=Matrix(16,16,lambda i,j:columns[reps[j]][i])
assert B.det()==-1

# Therefore the 16 octahedral cycles form an integral basis, exchanged in eight pairs
# by the central involution, up to each carrier's chosen orientation.
Binv=B.inv()
def transport_chain(c,p):
    result=defaultdict(int)
    for f,a in c.items():
        images=[p[i] for i in range(n) if f>>i&1]
        sign=(-1)**sum(images[i]>images[j] for i in range(len(images))
                        for j in range(i+1,len(images)))
        result[sum(1<<i for i in images)]+=sign*a
    return dict(result)

characters=[]
for p in perms:
    represented=Matrix(16,16,lambda i,j:project_cycle(transport_chain(cycles[reps[j]],p))[i])
    action=Binv*represented
    assert all(a.q==1 for a in action)
    assert abs(action.det())==1
    q=identity[:]
    for order in range(1,13):
        q=compose(p,q)
        if q==identity:break
    characters.append((order,int(action.trace())))
assert Counter(characters)=={(1,16):1,(2,0):7,(3,-2):2,(6,0):2}

# Optional orbit-lattice comparisons via integer Hermite forms.
A=Matrix(16,len(supports),lambda i,j:columns[supports[j]][i])
assert hermite_normal_form(A)==eye(16)
index={m:i for i,m in enumerate(supports)}
generating_pairs=[]
for a,b in combinations(range(len(orbits)),2):
    mat=A[:,[index[m] for j in (a,b) for m in orbits[j]]]
    H=hermite_normal_form(mat)
    if H.shape[1]==16:
        assert abs(H.det())==1
        generating_pairs.append((a,b))
assert generating_pairs==[(1,4),(1,5),(1,6)]
fixed=sum(apply_mask(m,involution)==m for m in supports)
assert fixed==3
print('VERIFY_OK_TIETZE_SHORTEST_OCTAHEDRAL_REGULAR_C2_LATTICE')
print('VERTICES_EDGES',len(G),len(E),'FACE_VECTOR',[len(by_dim[d]) for d in range(6)])
print('MORSE_PAIRS',len(pairs),'CRITICAL_CELLS',dict(crit),'HASSE',D.number_of_edges())
print('WEDGE_16_THREE_SPHERES_INTEGRAL')
print('SHORTEST_EIGHT_VERTEX_OCTAHEDRAL_CARRIERS',len(supports))
print('ALL_63_CLASSES_PRIMITIVE',True)
print('AUT_ORDER',len(autos),'CARRIER_ORBITS',[len(o) for o in orbits])
print('CENTRAL_FIXED_CARRIERS',fixed,'EXCHANGED_PAIRS',(len(supports)-fixed)//2)
print('EIGHT_CENTRAL_PAIRS_INTEGRAL_BASIS_DET',B.det())
print('INTEGRAL_C2_MODULE_EIGHT_REGULAR_SUMMANDS')
print('PLUS_MINUS_LATTICE_QUOTIENT',(2,)*8)
print('FULL_AUTOMORPHISM_CHARACTERS',dict(Counter(characters)))
print('GENERATING_TWO_ORBIT_UNIONS',generating_pairs)
