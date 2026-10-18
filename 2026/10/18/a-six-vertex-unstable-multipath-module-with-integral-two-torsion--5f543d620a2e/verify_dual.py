"""Independent recursive enumeration and nonorientability certificate for the multipath complex."""
from collections import defaultdict,deque,Counter

arcs=[(a,b) for a in (0,1) for b in (2,3,4,5)]+[(b,a) for b in (2,3,4,5) for a in (0,1)]
faces={():None}
# Build legal edge sets recursively; no exhaustive 2^16 scan.
for k in range(4):
    new={}
    for f in tuple(face for face in faces if len(face)==k):
        nxtstart=(f[-1]+1) if f else 0
        for j in range(nxtstart,16):
            trial=f+(j,)
            outgoing={};incoming={};valid=True
            for i in trial:
                u,v=arcs[i]
                if u in outgoing or v in incoming:valid=False;break
                outgoing[u]=v;incoming[v]=u
            if not valid:continue
            for x in range(6):
                seen=set();u=x
                while u in outgoing:
                    if u in seen:valid=False;break
                    seen.add(u);u=outgoing[u]
                if not valid:break
            if valid:new[trial]=None
    faces.update(new)
by_size=[sorted(f for f in faces if len(f)==k) for k in range(5)]
assert tuple(map(len,by_size))==(1,16,80,144,72)
facets=by_size[4]
tri_inc=defaultdict(list)
for i,f in enumerate(facets):
    for k in range(4):tri_inc[f[:k]+f[k+1:]].append((i,(-1)**k))
assert len(tri_inc)==144
assert all(len(lst)==2 for lst in tri_inc.values())
adj=defaultdict(list)
for f,lst in tri_inc.items():
    (a,pa),(b,pb)=lst
    edge_sign=-pa*pb
    adj[a].append((b,edge_sign,f))
    adj[b].append((a,edge_sign,f))
seen={0};q=deque([0])
while q:
    i=q.popleft()
    for j,_,_ in adj[i]:
        if j not in seen:seen.add(j);q.append(j)
assert len(seen)==72

# A 7-cycle in the facet-adjacency graph has orientation product -1.
orientation_obstruction=[(0,6,9,10),(3,6,9,10),(3,5,9,10),
 (2,5,9,10),(2,5,10,15),(0,5,10,15),(0,6,10,15)]
assert all(f in facets for f in orientation_obstruction)
prod=1
for f,g in zip(orientation_obstruction,orientation_obstruction[1:]+orientation_obstruction[:1]):
    i,j=facets.index(f),facets.index(g)
    edge=[sgn for dest,sgn,_ in adj[i] if dest==j]
    assert len(edge)==1
    prod*=edge[0]
assert prod==-1

# Independently calculate mod-two boundary ranks by integer bit elimination.
def rank_two(rows,cols):
    idx={f:i for i,f in enumerate(rows)}
    basis={}
    for f in cols:
        vec=0
        for k in range(len(f)):vec ^= (1<<idx[f[:k]+f[k+1:]])
        while vec:
            lead=vec.bit_length()-1
            if lead in basis:vec^=basis[lead]
            else:basis[lead]=vec;break
    return len(basis)
ranks=[rank_two(by_size[k-1],by_size[k]) for k in range(1,5)]
assert ranks==[1,15,65,71],ranks
b=[len(by_size[i])- (ranks[i-1] if i else 0) - (ranks[i] if i<4 else 0) for i in range(5)]
assert b==[0,0,0,8,1],b
print('face_counts',[len(f) for f in by_size])
print('facet_adjacency_connected',len(seen))
print('triangle_incidence',dict(Counter(map(len,tri_inc.values()))))
print('nonorientable_seven_cycle_product',prod)
print('mod2_boundary_ranks',ranks)
print('mod2_reduced_homology_dims',b)
print('torsion_consequence','H_3(Z)=0, H_3(F2)=F2, hence H_2(Z) has 2-torsion')

# Directed cycle-overlap connectivity is a certificate of dynamical-module minimality.
cycle_edges=[]
for i,(u,v) in enumerate(arcs):
    for j,(v2,w) in enumerate(arcs):
        if v2==v and w==u and i!=j:cycle_edges.append((i,j))
for a in (0,1):
    b=1-a
    for x in (2,3,4,5):
        for y in (2,3,4,5):
            if x==y:continue
            ordered=[(a,x),(x,b),(b,y),(y,a)]
            cyc=tuple(arcs.index(e) for e in ordered)
            cycle_edges.append(cyc)
edge_reach={0}
while True:
    nxt=edge_reach|set(i for cyc in cycle_edges if any(j in edge_reach for j in cyc) for i in cyc)
    if nxt==edge_reach:break
    edge_reach=nxt
assert len(edge_reach)==16
print('cycle_overlap_component_arcs',len(edge_reach))
