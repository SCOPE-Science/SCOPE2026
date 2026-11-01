"""Exact reproducibility checks for the 14-point rhombic-dodecahedral Rips filtration.

No numerical tolerances are used: squared distances are integers, and all
simplices and collapse pairs are bit masks.
Run: python3 verify.py
"""
import itertools
import json
from collections import Counter,defaultdict
from pathlib import Path

V=[tuple(2*s if k==a else 0 for k in range(3)) for a in range(3) for s in (-1,1)]
V+=list(itertools.product((-1,1),repeat=3))
N=len(V)
assert N==14 and len(set(V))==14
D={(i,j):sum((V[i][k]-V[j][k])**2 for k in range(3)) for i in range(N) for j in range(i+1,N)}
assert Counter(D.values())=={3:24,4:12,8:24,11:24,12:4,16:3}

def faces(q):
    result=set()
    for mask in range(1,1<<N):
        vs=[i for i in range(N) if mask>>i&1]
        if all(D[i,j]<=q for i,j in itertools.combinations(vs,2)):
            result.add(mask)
    return result

def edges(K):
    return [mask for mask in K if mask.bit_count()==2]

def connected(vertices,edgelist):
    parent={v:v for v in vertices}
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for a,b in edgelist:
        ra,rb=find(a),find(b)
        parent[ra]=rb
    return len({find(i) for i in vertices})==1

def edge_vertices(mask):
    return [i for i in range(N) if mask>>i&1]

def one_skeleton_connected(K):
    vert=[i for i in range(N) if 1<<i in K]
    return connected(vert,[edge_vertices(e) for e in edges(K)])

def cof(K,a):
    return [a|(1<<i) for i in range(N) if not a>>i&1 and (a|(1<<i)) in K]

F={q:faces(q) for q in (0,3,4,8,11,12)}
counts={q:dict(sorted(Counter(mask.bit_count()-1 for mask in F[q]).items())) for q in F}
assert counts=={
 0:{0:14},
 3:{0:14,1:24},
 4:{0:14,1:36,2:24},
 8:{0:14,1:60,2:100,3:60,4:6},
 11:{0:14,1:84,2:280,3:560,4:672,5:448,6:128},
 12:{0:14,1:88,2:328,3:806,4:1372,5:1652,6:1408,7:833,8:326,9:76,10:8}
}
assert one_skeleton_connected(F[3])
assert len(edges(F[3]))-N+1==11
# At squared radius four, prove a connected closed triangulated surface.
K=F[4]
assert one_skeleton_connected(K)
triangles=[m for m in K if m.bit_count()==3]
for e in edges(K):
    assert sum((e&t)==e for t in triangles)==2
for i in range(N):
    link_vertices=[j for j in range(N) if j!=i and (1<<i|1<<j) in K]
    link_edges=[]
    for t in triangles:
        if t>>i&1:
            j,k=edge_vertices(t^(1<<i))
            link_edges.append((j,k))
    assert connected(link_vertices,link_edges)
    deg=Counter(j for e in link_edges for j in e)
    assert all(deg[v]==2 for v in link_vertices)
assert 14-36+24==2
# At squared radius eight, replay every elementary simplicial collapse.
cert=json.loads(Path(__file__).with_name('collapse_8.json').read_text(encoding='utf8'))
assert cert['squared_threshold']==8 and cert['initial_faces']==240 and cert['final_faces']==80
assert [s['axis_vertex'] for s in cert['steps']]==list(range(6))
assert [s['link_face_count'] for s in cert['steps']]==[39,39,23,23,15,15]
assert [s['link_pairs'] for s in cert['steps']]==[19,19,11,11,7,7]
assert len(cert['elementary_pairs'])==80
K=set(F[8])
for a,b in cert['elementary_pairs']:
    assert a in K and b in K and b.bit_count()==a.bit_count()+1
    assert (a&b)==a and cof(K,a)==[b]
    K.remove(a);K.remove(b)
assert K=={f for f in F[8] if (f&63)==0}
assert len(K)==80
# On the eight cube corners the four antipodal pairs are precisely the
# nonedges; the clique complex is the boundary of a four-cross-polytope.
corners=list(range(6,14))
nonedges8={tuple(sorted((i,j))) for i,j in itertools.combinations(corners,2) if (1<<i|1<<j) not in K}
assert nonedges8=={(i,j) for i,j in itertools.combinations(corners,2) if all(V[i][a]==-V[j][a] for a in range(3))}
assert len(nonedges8)==4
# At squared radius eleven, the 7 absent edges form a perfect matching.
nonedges11=[(i,j) for i,j in itertools.combinations(range(N),2) if (1<<i|1<<j) not in F[11]]
assert len(nonedges11)==7
assert sorted(i for e in nonedges11 for i in e)==list(range(N))
# Hence the full clique complex is the boundary of a 7-cross-polytope.
assert len(F[11])==3**7-1
# At squared radius twelve, each of the eight cube corners is a cone vertex.
assert all(all(1<<i|1<<j in F[12] for j in range(N) if i!=j) for i in corners)
assert faces(16)==set(range(1,1<<N))
print('DISTANCES',sorted(Counter(D.values()).items()))
for q in F:print('SQUARED_SCALE',q,'F_VECTOR',counts[q])
print('SURFACE', 'connected_closed_Euler2')
print('COLLAPSE_8',len(cert['elementary_pairs']),'pairs onto cubical S3')
print('CROSSPOLYTOPE_11',len(nonedges11),'opposite pairs')
print('CONE_12',len(corners),'universal vertices')
print('VERIFY_OK')
