"""Reproducible finite checks of the icosahedral graph and its two representation spheres."""
import itertools
import networkx as nx
import numpy as np

phi=(1+5**.5)/2
V=[]
for a,b in itertools.product((-1.,1.),repeat=2):
    V.extend([(0.,a,b*phi),(a,b*phi,0.),(a*phi,0.,b)])
V=np.asarray(V)
assert V.shape==(12,3)
norm=np.linalg.norm(V[0]); V=V/norm
G=nx.Graph();G.add_nodes_from(range(12))
for i in range(12):
 for j in range(i+1,12):
  if abs(np.sum((V[i]-V[j])**2)-4/norm**2)<1e-7:
   G.add_edge(i,j)
assert G.number_of_edges()==30
assert sorted(set(dict(G.degree).values()))==[5]
dist=dict(nx.all_pairs_shortest_path_length(G))
assert set(d for row in dist.values() for d in row.values())=={0,1,2,3}
opp={i:next(j for j in range(12) if dist[i][j]==3) for i in range(12)}
assert len(opp)==12 and all(opp[opp[i]]==i for i in range(12))
assert all(np.allclose(V[i]+V[opp[i]],0) for i in range(12))
assert all(dist[i][j]!=3 for i in range(12) for j in range(12) if j!=opp[i])
faces=[c for c in itertools.combinations(range(12),3) if all(G.has_edge(a,b) for a,b in itertools.combinations(c,2))]
assert len(faces)==20
assert all(not all(G.has_edge(a,b) for a,b in itertools.combinations(c,2)) for c in itertools.combinations(range(12),4))
assert all(min(np.dot(np.sum(V[list(f)],axis=0),p) for p in V[list(f)])>0 for f in faces)

reps=[]
seen=set()
for i in range(12):
 if i in seen:continue
 j=opp[i];seen|={i,j};reps.append(i)
assert len(reps)==6
E=np.zeros((12,6))
for col,i in enumerate(reps):E[i,col]=1;E[opp[i],col]=-1
X=V[reps,:]
assert np.allclose(X.T@X,2*np.eye(3),atol=1e-10)
perms=[tuple(f[i] for i in range(12)) for f in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()]
assert len(perms)==120 and len(set(perms))==120
B=[0,1,2]
assert abs(np.linalg.det(V[B,:]))>1e-9
base=V[B,:]
proper_types={}
dets={}
chars=[]
for f in perms:
    mapped=V[[f[i] for i in B],:]
    M=np.linalg.solve(base,mapped) # V(row) @ M = transformed coordinates
    assert np.allclose(V@M,V[list(f),:],atol=1e-9)
    assert np.allclose(M@M.T,np.eye(3),atol=1e-9)
    det=round(np.linalg.det(M))
    assert det in (-1,1)
    # Signed permutation on the six antipodal lines
    S=np.zeros((6,6),dtype=int)
    for j,i in enumerate(reps):
        fi=f[i]
        if fi in reps:S[reps.index(fi),j]=1
        else:S[reps.index(opp[fi]),j]=-1
    assert np.array_equal(S.T@S,np.eye(6,dtype=int))
    assert np.allclose(S.T@X,X@M,atol=1e-9)  # checks the equivariance of the canonical 3D subspace
    trace6=int(np.trace(S));trace3=float(np.trace(M))
    assert round(np.linalg.det(S))==1, 'orientation of 5-sphere must be preserved'
    if det==1:
        def ord_perm(p):
            tmp=tuple(range(12)); k=0
            while True:
                tmp=tuple(p[tmp[i]] for i in range(12));k+=1
                if tmp==tuple(range(12)):return k
        order=ord_perm(f)
        proper_types.setdefault(order,[]).append((trace6,trace3))
    chars.append((trace6,trace3,det))
    dets[det]=dets.get(det,0)+1
assert dets=={1:60,-1:60}
assert {o:len(v) for o,v in proper_types.items()}=={1:1,2:15,3:20,5:24}
assert all(x[0]=={1:6,2:-2,3:0,5:1}[o] for o,li in proper_types.items() for x in li)
assert all(abs(x[1]-{1:3,2:-1,3:0}[o])<1e-8 for o,li in proper_types.items() if o in (1,2,3) for x in li)
print('ICOSAHEDRAL_GRAPH_AND_ACTION_VERIFIED',len(perms),len(faces),len(reps),dets)
for o,li in sorted(proper_types.items()):
 print('ROTATION_ORDER_AND_SIX_AXIS_TRACE',o,len(li),sorted(set(x[0] for x in li)))
print('CANONICAL_EQUIVARIANT_THREE_PLUS_THREE_SPLITTING_VERIFIED')
print('PROJECTION_NONZERO_ON_ALL_TWENTY_FACE_SIMPLICES_VERIFIED')
# Exhaustively check the fixed-subspace dimension doubling against the full subgroup lattice.
index={p:i for i,p in enumerate(perms)}
comp=[[index[tuple(q[p[i]] for i in range(12))] for q in perms] for p in perms]
idindex=index[tuple(range(12))]
assert all(comp[idindex][i]==i and comp[i][idindex]==i for i in range(120))

def closure(gens):
    vis={idindex};todo=[idindex]
    while todo:
        i=todo.pop()
        for g in gens:
            k=comp[i][g]
            if k not in vis:
                vis.add(k);todo.append(k)
    return frozenset(vis)

known={frozenset([idindex]):()}
queue=[frozenset([idindex])]
while queue:
    H=queue.pop()
    if len(H)==120:continue
    old=known[H]
    for g in range(120):
        if g in H:continue
        K=closure(old+(g,))
        if K not in known:
            known[K]=old+(g,)
            queue.append(K)
assert len(known)<1000
for H in known:
    d3=sum(chars[g][1] for g in H)/len(H)
    d6=sum(chars[g][0] for g in H)/len(H)
    assert abs(d3-round(d3))<1e-8
    assert abs(d6-round(d6))<1e-8
    assert round(d6)==2*round(d3), (len(H),d3,d6)
    assert round(d3) in (0,1,2,3)
from collections import Counter
print('ALL_SUBGROUP_FIXED_DIMENSION_DOUBLING_VERIFIED',len(known),sorted(Counter(int(round(sum(chars[g][1] for g in H)/len(H))) for H in known).items()))
