"""Reproducible integer-chain certificate for unordered two-point configurations on the Tutte eight-cage.
Requires Python 3 and SymPy only.  All graph data are constructed from duads and synthemes.
"""
import itertools
from collections import Counter
import sympy as sp

letters=tuple(range(6))
duads=tuple(itertools.combinations(letters,2))

def matchings(left):
    if not left:
        yield ()
        return
    a=left[0]
    for b in left[1:]:
        for rest in matchings(tuple(v for v in left if v not in (a,b))):
            yield tuple(sorted(((a,b),)+rest))

synthemes=tuple(sorted(set(matchings(letters))))
assert len(duads)==len(synthemes)==15
V=tuple(range(30))
E=tuple(sorted(tuple(sorted((duads.index(d),15+j))) for j,s in enumerate(synthemes) for d in s))
assert len(E)==45 and len(set(E))==45
edidx={e:i for i,e in enumerate(E)}
adj={v:set() for v in V}
for u,v in E:adj[u].add(v);adj[v].add(u)
assert all(len(adj[v])==3 for v in V)
# Canonical unoriented cyclic word starts at its minimum vertex, then takes lexicographically smaller direction.
def canon(path):
    j=path.index(min(path));p=tuple(path[j:]+path[:j]);return min(p,(p[0],)+p[:0:-1])
# Exhaustive simple cycles of length 8. One root is smallest vertex.
cycs=set()
for v in V:
    def explore(path):
        if len(path)==8:
            if v in adj[path[-1]]:cycs.add(canon(path))
            return
        for w in sorted(adj[path[-1]]):
            if w>v and w not in path:explore(path+[w])
    explore([v])
cycs=tuple(sorted(cycs));assert len(cycs)==90
# Girth exactly 8: rule out lengths 3-7 exhaustively via bounded DFS.
for length in range(3,8):
    for v in V:
        def no_short(path):
            if len(path)==length:
                assert v not in adj[path[-1]]
                return
            for w in adj[path[-1]]:
                if w>v and w not in path:no_short(path+[w])
        no_short([v])
cyclekeys={c:i for i,c in enumerate(cycs)}
cycle_sets=[set(c) for c in cycs]
pairs=tuple((i,j) for i in range(len(cycs)) for j in range(i+1,len(cycs)) if not cycle_sets[i].intersection(cycle_sets[j]))
assert len(pairs)==1125
pair_idx={p:i for i,p in enumerate(pairs)}
# The cellular model is the symmetric quotient of the graph deleted product.
C0=tuple(itertools.combinations(V,2))
C1=tuple((e,v) for e in E for v in V if v not in e)
C2=tuple((i,j) for i in range(len(E)) for j in range(i+1,len(E)) if len(set(E[i]+E[j]))==4)
assert (len(C0),len(C1),len(C2))==(435,1260,900)
one_idx={c:i for i,c in enumerate(C1)}
two_idx={c:i for i,c in enumerate(C2)}
# Integral incidence of oriented square (edge_i,edge_j), i<j: 
# (+ endpoint of edge_i, edge_j) - (- endpoint of edge_i,edge_j)
#  - (edge_i,+endpoint of edge_j) + (edge_i,-endpoint of edge_j).
def boundary2(c):
    ia,ib=c;a,b=E[ia];x,y=E[ib]
    return {one_idx[(E[ib],a)]:-1,one_idx[(E[ib],b)]:1,
            one_idx[(E[ia],x)]:1,one_idx[(E[ia],y)]:-1}
B2=tuple(boundary2(c) for c in C2)
# Boundary1 is the oriented displacement of the moving edge while the other particle stays at v.
zero_idx={c:i for i,c in enumerate(C0)}
def boundary1(cell):
    (a,b),v=cell
    return {zero_idx[tuple(sorted((a,v)))]:-1,zero_idx[tuple(sorted((b,v)))]:1}
B1=tuple(boundary1(c) for c in C1)
for col in B2:
    d={}
    for j,a in col.items():
        for k,b in B1[j].items():d[k]=d.get(k,0)+a*b
    assert not any(d.values()),'boundary composition must vanish'
# In each oriented cycle, edges use increasing endpoint orientation for the C2 basis.
def oriented_edges(c):
    ans=[]
    for k in range(8):
        a,b=c[k],c[(k+1)%8]
        ans.append((edidx[tuple(sorted((a,b)))],1 if a<b else -1))
    return ans
cyclE=tuple(oriented_edges(c) for c in cycs)
tori=[]
for i,j in pairs:
    coeff={}
    for a,sa in cyclE[i]:
        for b,sb in cyclE[j]:
            c=(a,b) if a<b else (b,a)
            idx=two_idx[c]
            assert idx not in coeff
            coeff[idx]=sa*sb*(1 if a<b else -1)
    assert len(coeff)==64
    chk={}
    for k,s in coeff.items():
        for q,v in B2[k].items():chk[q]=chk.get(q,0)+s*v
    assert not any(chk.values()),'product torus must be an integral 2-cycle'
    tori.append(coeff)
assert len(tori)==1125

def binary_rank_with_indices(vectors):
    b={};ids=[]
    for i,z in enumerate(vectors):
        x=z
        while x:
            p=x.bit_length()-1
            if p not in b:
                b[p]=x;ids.append(i);break
            x^=b[p]
    return len(b),ids
binary_tori=[sum(1<<k for k in t) for t in tori]
rankT,greedy90=binary_rank_with_indices(binary_tori)
assert rankT==len(greedy90)==90
# Row selection over F2 on the selected 90 cycles: earliest coordinates that add rank.
rowmasks=[sum(((k in tori[i])<<j) for j,i in enumerate(greedy90)) for k in range(len(C2))]
rowrank,pivotrows=binary_rank_with_indices(rowmasks)
assert rowrank==len(pivotrows)==90
minor=sp.Matrix([[tori[greedy90[j]].get(row,0) for j in range(90)] for row in pivotrows])
det=int(minor.det(method='domain-ge'))
assert abs(det)==1,det
# Since 90 primitive independent cycles in C2 and ker boundary2 is primitive,
# proving rank(boundary2) >=810 suffices for an integral basis.
def modular_rank(columns,p):
    pivots={}
    for col in columns:
        x={k:v%p for k,v in col.items() if v%p}
        while x:
            lead=max(x)
            if lead not in pivots:
                inv=pow(x[lead],-1,p)
                pivots[lead]={k:v*inv%p for k,v in x.items()}
                break
            mul=x[lead]
            for k,v in pivots[lead].items():
                val=(x.get(k,0)-mul*v)%p
                if val:x[k]=val
                else:x.pop(k,None)
    return len(pivots)
# A nonzero minor mod p gives a genuine characteristic-zero rank lower bound,
# and the 90 signed top cycles give the matching rank upper bound.
rank101=modular_rank(B2,101)
assert rank101==810
rank2=modular_rank(B2,2)
assert rank2==809
# The underlying graph has an evident faithful S6 action on its duads and synthemes.
def graph_action(p):
    mp=tuple(tuple(sorted((p[a],p[b]))) for a,b in duads)
    out=[duads.index(t) for t in mp]
    sy_idx={s:i for i,s in enumerate(synthemes)}
    for s in synthemes:
        transformed=tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in s))
        out.append(15+sy_idx[transformed])
    assert set(out)==set(V)
    return tuple(out)
# Adjacent transposition and 6-cycle generate all of S6.
perms=(tuple([1,0,2,3,4,5]),tuple([1,2,3,4,5,0]))
actions=[graph_action(p) for p in perms]
# There are exactly 720 distinct label-permutation maps, so this is a faithful S6 action.
assert len({graph_action(p) for p in itertools.permutations(letters)})==720
assert all({tuple(sorted((mp[a],mp[b]))) for a,b in E}==set(E) for mp in actions)
gens=[]
for mp in actions:
    ci=[cyclekeys[canon([mp[v] for v in c])] for c in cycs]
    gen=[pair_idx[tuple(sorted((ci[i],ci[j])))] for i,j in pairs]
    gens.append(gen)
rem=set(range(len(pairs)));orbits=[]
while rem:
    i=min(rem);q=[i];rem.remove(i)
    for a in q:
        for g in gens:
            b=g[a]
            if b in rem:rem.remove(b);q.append(b)
    orbits.append(tuple(sorted(q)))
orbits=tuple(sorted(orbits,key=lambda o:(len(o),o[0])))
print('S6_PAIR_ORBITS',tuple(len(o) for o in orbits))
for orb in orbits:
    rank,ids=binary_rank_with_indices(binary_tori[j] for j in orb)
    print('ORBIT',orb[0],len(orb),'RANK_MOD2',rank)
# This first-check rank over F2 is additional context, not a claim of integral orbit generation.
print('VERIFY_OK_TUTTE_COXETER_OCTAGON_PAIR_INTEGRAL_BASIS')
print('GRAPH_VERTICES_EDGES',len(V),len(E),'GIRTH',8,'EIGHT_CYCLES',len(cycs),'DISJOINT_PAIRS',len(pairs))
print('CUBICAL_CELLS',len(C0),len(C1),len(C2),'BOUNDARY2_RANK_MOD101',rank101,'BOUNDARY2_RANK_MOD2',rank2)
print('INTEGRAL_BASIS_TORI',len(greedy90),'PIVOT_ROWS',len(pivotrows),'DETERMINANT',det)
print('GREEDY_PAIRS',greedy90)
print('PIVOT_ROWS',pivotrows)
for orb in orbits:
    rank,ids=binary_rank_with_indices(binary_tori[j] for j in orb)
    if rank==90:
        orbsel=[orb[i] for i in ids]
        rowmask=[sum(((k in tori[j])<<a) for a,j in enumerate(orbsel)) for k in range(len(C2))]
        nr,rs=binary_rank_with_indices(rowmask);assert nr==90
        matr=sp.Matrix([[tori[orbsel[j]].get(row,0) for j in range(90)] for row in rs])
        d=int(matr.det(method='domain-ge'))
        print('RANK90_ORBIT_DETERMINANT',orb[0],len(orb),d)
for orb in orbits:
    i,j=pairs[orb[0]]
    U=set(cycs[i]);W=set(cycs[j]);cross=sum((a in U and b in W) or (a in W and b in U) for a,b in E)
    d2=sum(len(set(E[k]) & U)==1 and len(set(E[k]) & W)==1 for k in range(len(E)))
    assert cross==d2
    print('ORBIT_GEOMETRY_FIRST',orb[0],len(orb),'CROSS_EDGES',cross,'CYCLES',i,j,'CYCLE0',cycs[i],'CYCLE1',cycs[j])
    assert all(sum((a in set(cycs[pairs[t][0]]) and b in set(cycs[pairs[t][1]])) or (b in set(cycs[pairs[t][0]]) and a in set(cycs[pairs[t][1]])) for a,b in E)==cross for t in orb)
for orb in orbits:
 i,j=pairs[orb[0]];A=set(cycs[i]);B=set(cycs[j]);cross=[(u,v) if u in A else (v,u) for u,v in E if (u in A and v in B) or (u in B and v in A)]
 d=[]
 if len(cross)==2:
  for k,c in enumerate([cycs[i],cycs[j]]):
   p=c.index(cross[0][k]);q=c.index(cross[1][k]);dd=abs(p-q);d.append(min(dd,8-dd))
 print('ORBIT_CROSS_CHORD_DISTANCE',orb[0],len(orb),tuple(sorted(d)))

# The natural geometric separator identifies the distinguished orbit without using indices.
def bridge_profile(pair_id):
    i,j=pairs[pair_id]
    A=set(cycs[i]);B=set(cycs[j])
    crossing=[(u,v) if u in A else (v,u) for u,v in E if (u in A and v in B) or (u in B and v in A)]
    if not crossing:return (0,())
    assert len(crossing)==2
    def distance(c,u,v):
        d=abs(c.index(u)-c.index(v))
        return min(d,8-d)
    return (2,tuple(sorted((distance(cycs[i],crossing[0][0],crossing[1][0]),distance(cycs[j],crossing[0][1],crossing[1][1])))))
profiles=[bridge_profile(i) for i in range(len(pairs))]
assert Counter(profiles)==Counter({(0,()):45,(2,(2,4)):720,(2,(3,3)):360})
special_orbit=next(orb for orb in orbits if bridge_profile(orb[0])==(2,(3,3)))
assert len(special_orbit)==360 and all(profiles[i]==(2,(3,3)) for i in special_orbit)
special_rank,local_ids=binary_rank_with_indices(binary_tori[j] for j in special_orbit)
assert special_rank==90
special_ids=[special_orbit[i] for i in local_ids]
special_masks=[sum(((k in tori[j])<<a) for a,j in enumerate(special_ids)) for k in range(len(C2))]
special_row_rank,special_rows=binary_rank_with_indices(special_masks)
assert special_row_rank==90
special_minor=sp.Matrix([[tori[special_ids[j]].get(k,0) for j in range(90)] for k in special_rows])
special_det=int(special_minor.det(method='domain-ge'))
assert special_det==-1
print('GEOMETRIC_TYPES',dict(Counter(profiles)))
print('DISTINGUISHED_ORBIT_SIZE',len(special_orbit),'UNIT_MINOR',special_det)
print('SPECIAL_SELECTED_TORUS_INDICES',special_ids)
print('SPECIAL_SELECTED_SQUARE_ROWS',special_rows)
print('VERIFY_OK_DISTINGUISHED_S6_ORBIT_INTEGRAL_H2')
