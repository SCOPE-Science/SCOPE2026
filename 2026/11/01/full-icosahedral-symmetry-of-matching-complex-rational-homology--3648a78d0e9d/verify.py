#!/usr/bin/env python3
"""Reproducible exact calculations for an icosahedral graph matching complex.
No external packages required.  Vertex labels are fixed in this file.
"""
from collections import Counter, defaultdict
from itertools import combinations

V = tuple(range(12))
E = set()
def edge(a,b):
    assert a != b
    E.add(tuple(sorted((a,b))))
for j in range(5):
    k=(j+1)%5
    u=1+j; v=6+j
    edge(0,u); edge(11,v)
    edge(u,1+k); edge(v,6+k)
    edge(u,v); edge(u,6+(j-1)%5)
E=tuple(sorted(E)); assert len(E)==30
adj=[set() for _ in V]
for u,v in E:adj[u].add(v);adj[v].add(u)
assert all(len(x)==5 for x in adj)
tri=[x for x in combinations(V,3) if all(tuple(sorted((a,b))) in E for a,b in combinations(x,2))]
assert len(tri)==20

# Every nonempty matching, in a canonical edge-index order.
used=[(0,())]
for i,(u,v) in enumerate(E):
    bit=(1<<u)|(1<<v)
    used += [(mask|bit,ids+(i,)) for mask,ids in used if mask&bit==0]
F={k:[] for k in range(1,7)}
for mask,ids in used:
    if ids:F[len(ids)].append(ids)
assert [len(F[k]) for k in range(1,7)]==[30,315,1400,2535,1482,125]
assert len(used)==5888

# Exhaustive graph automorphisms by adjacency-preserving backtracking.
# Choose the next domain vertex with the most already mapped neighbors.
automorphisms=[]
def backtrack(mapping, taken):
    if len(mapping)==12:
        automorphisms.append(tuple(mapping[v] for v in V));return
    choices=[]
    for x in V:
        if x in mapping:continue
        possible=[y for y in V if y not in taken and all((y in adj[mapping[v]])==(x in adj[v]) for v in mapping)]
        choices.append((len(possible), -sum(v in adj[x] for v in mapping), x, possible))
    _,_,x,possible=min(choices)
    for y in possible:
        mapping[x]=y;taken.add(y)
        backtrack(mapping,taken)
        taken.remove(y);del mapping[x]
backtrack({},set())
assert len(automorphisms)==120 and len(set(automorphisms))==120

def compose(g,h):return tuple(g[h[i]] for i in V)
idmap=V
def order(g):
    x=idmap
    for j in range(1,121):
        x=compose(g,x)
        if x==idmap:return j
    raise AssertionError('nonfinite-order')
orders={g:order(g) for g in automorphisms}
odd=[g for g in automorphisms if orders[g] in (3,5)]
rot={idmap};stack=[idmap]
for h in stack:
    for g in odd:
        a=compose(g,h)
        if a not in rot:rot.add(a);stack.append(a)
assert len(rot)==60

# Unique antipodal map, determined by graph distance three.
def distances(a):
    dist={a:0}; todo=[a]
    for u in todo:
        for v in adj[u]:
            if v not in dist:dist[v]=dist[u]+1;todo.append(v)
    return dist
D=[distances(v) for v in V]
zlist=[g for g in automorphisms if orders[g]==2 and all(D[v][g[v]]==3 for v in V)]
assert len(zlist)==1
z=zlist[0];assert z not in rot
assert all(compose(z,g)==compose(g,z) for g in automorphisms)
assert {compose(z,g) for g in rot}==set(automorphisms)-rot

# A modular certificate of rational homology in one degree.
def boundary_rank(k,p):
    # boundary maps the (k-1)-simplices to the (k-2)-simplices.
    rows={es:j for j,es in enumerate(F[k-1])}
    piv={}
    for es in F[k]:
        col={rows[es[:j]+es[j+1:]]:(1 if j%2==0 else p-1) for j in range(k)}
        while col:
            i=max(col); val=col[i]
            if i not in piv:
                inv=pow(val,-1,p)
                piv[i]={j:(v*inv)%p for j,v in col.items()}
                break
            for j,v in piv[i].items():
                new=(col.get(j,0)-val*v)%p
                if new:col[j]=new
                else:col.pop(j,None)
    return len(piv)

rank101={k:boundary_rank(k,101) for k in range(2,7)}
assert rank101=={2:29,3:286,4:1114,5:1357,6:125},rank101
b101={1:len(F[1])-1-rank101[2]}
for k in range(2,6):b101[k]=len(F[k])-rank101[k]-rank101[k+1]
b101[6]=len(F[6])-rank101[6]
assert b101=={1:0,2:0,3:0,4:64,5:0,6:0}
# Euler gives reduced Q-H_3 of rank 64, and all other Q homology zero.
# In degree notation: F[4] is dimension-three chains.
chi_red=sum((-1)**(k-1)*len(F[k]) for k in range(1,7))-1
assert chi_red==-64

# Two completely different exact trace algorithms.
edge_id={e:i for i,e in enumerate(E)}
def induced_edges(g):
    return tuple(edge_id[tuple(sorted((g[u],g[v])))] for u,v in E)
def lefschetz_faces(ep):
    out=0
    for k in range(1,7):
        tr=0
        for face in F[k]:
            im=[ep[i] for i in face]
            if set(im)!=set(face):continue
            sign=-1 if sum(im[i]>im[j] for i in range(k) for j in range(i+1,k))%2 else 1
            tr+=sign
        out+=(-1)**(k-1)*tr
    return 1-out

def orbit_poly_minus_one(ep):
    visited=set(); masks=[]
    for i in range(30):
        if i in visited:continue
        cyc=[]; j=i
        while j not in visited:
            visited.add(j);cyc.append(j);j=ep[j]
        covered=0;good=True
        for t in cyc:
            u,v=E[t]; bit=(1<<u)|(1<<v)
            if covered&bit:good=False;break
            covered|=bit
        if good:masks.append(covered)
    # sum over subsets of internally disjoint edge orbits with alternating signs
    def rec(i,mask):
        if i==len(masks):return 1
        v=rec(i+1,mask)
        if mask&masks[i]==0:v-=rec(i+1,mask|masks[i])
        return v
    return rec(0,0)

records=[]
for g in automorphisms:
    ep=induced_edges(g)
    c1=lefschetz_faces(ep)
    c2=orbit_poly_minus_one(ep)
    assert c1==c2,(g,c1,c2)
    # the rotation part is g if g in R, and zg otherwise
    r=g if g in rot else compose(z,g)
    records.append((g in rot,order(r),c1))
classes={}
for grp in (True,False):
    for k in (1,2,3,5):
        x=[t for isrot,o,t in records if isrot==grp and o==k]
        assert len(set(x))<=1
        classes[(grp,k)]=(len(x),x[0])
assert classes=={
 (True,1):(1,64),(True,2):(15,0),(True,3):(20,-2),(True,5):(24,-1),
 (False,1):(1,16),(False,2):(15,0),(False,3):(20,-2),(False,5):(24,1)
}
# For the two irreducible 3-dimensional representations, their sum has
# character [6,-2,0,1,1] on [1,2A,3A,5A,5B].
# Standard rational A5 characters [trivial, 3+3', 4, 5].
A5={'one':(1,1,1,1),'three_pair':(6,-2,0,1),
    'four':(4,0,1,-1),'five':(5,1,-1,0)}
def char(mults):
    return tuple(sum(mults[name]*A5[name][j] for name in A5) for j in range(4))
# inversion-even and inversion-odd characters
Cp=tuple((classes[(True,o)][1]+classes[(False,o)][1])//2 for o in (1,2,3,5))
Cm=tuple((classes[(True,o)][1]-classes[(False,o)][1])//2 for o in (1,2,3,5))
assert Cp==(40,0,-2,0) and Cm==(24,0,0,-1)
even={'one':0,'three_pair':2,'four':2,'five':4}
oddm={'one':0,'three_pair':1,'four':2,'five':2}
assert char(even)==Cp and char(oddm)==Cm
for cl in sorted(classes,reverse=True):print('class',cl,'size,trace',classes[cl])
print('vector',tuple(len(F[k]) for k in range(1,7)))
print('rank_F101',rank101)
print('betti_F101',b101)
print('eigenspaces_40_24',Cp,Cm)
print('A5_even_multiplicities',even)
print('A5_odd_multiplicities',oddm)
print('icosahedral_matching_symmetry_PASS')
