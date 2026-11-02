"""Exact finite cellular checks for two unordered particles on G(8,3).

Requires Python 3.9 or newer; no third-party packages.
The rational homology argument uses a lower bound from lifted graph
cycles and an upper bound from a finite-field matrix rank.
"""
from collections import Counter, deque
from itertools import combinations
from math import lcm

N=16
edges=set()
def edge(a,b):return (a,b) if a<b else (b,a)
for i in range(8):
    edges.add(edge(i,(i+1)%8))
    edges.add(edge(i,8+i))
    edges.add(edge(8+i,8+(i+3)%8))
E=sorted(edges); edge_idx={e:i for i,e in enumerate(E)}
adj=[set() for _ in range(N)]
for a,b in E:adj[a].add(b);adj[b].add(a)
assert len(E)==24 and all(len(s)==3 for s in adj)

# Every simplex of the graph is a vertex or an edge; unordered pairs
# with pairwise disjoint closures form a regular cubical model.
C0=list(combinations(range(N),2)); I0={c:i for i,c in enumerate(C0)}
C1=[(v,i) for v in range(N) for i,e in enumerate(E) if v not in e]
I1={c:i for i,c in enumerate(C1)}
C2=[(i,j) for i in range(len(E)) for j in range(i+1,len(E))
    if not (set(E[i])&set(E[j]))]
assert (len(C0),len(C1),len(C2))==(120,336,228)

# Sparse columns of the cellular boundary operators.
d1=[]
for v,i in C1:
    a,b=E[i]
    d1.append({I0[edge(v,b)]:1,I0[edge(v,a)]:-1})
d2=[]
for i,j in C2:
    a,b=E[i];c,d=E[j]
    d2.append({I1[(b,j)]:1,I1[(a,j)]:-1,
               I1[(d,i)]:-1,I1[(c,i)]:1})
for column in d2:
    c=Counter()
    for k,s in column.items():
        for j,t in d1[k].items():c[j]+=s*t
    assert all(v==0 for v in c.values())

def rank_mod(columns,prime):
    pivots={}
    for column in columns:
        v={k:a%prime for k,a in column.items() if a%prime}
        while v:
            k=min(v);a=v[k]
            if k not in pivots:
                inv=pow(a,-1,prime)
                pivots[k]={i:(b*inv)%prime for i,b in v.items()}
                break
            q=pivots[k]
            v={i:(v.get(i,0)-a*q.get(i,0))%prime for i in v.keys()|q.keys()}
            v={i:b for i,b in v.items() if b}
    return len(pivots)

assert [(p,rank_mod(d1,p),rank_mod(d2,p)) for p in (2,3,5,101)] == [
    (2,119,207),(3,119,208),(5,119,208),(101,119,208)]
# A second orientation of matrix elimination over a different field.
rows=[{} for _ in range(len(C1))]
for j,column in enumerate(d2):
    for i,sgn in column.items():rows[i][j]=sgn
assert rank_mod(rows,5)==208

# A fundamental cycle basis for the graph, lifted with a stationary
# particle at a vertex outside each cycle. Such cycles show that the
# rational first Betti number is at least the graph cycle rank nine.
root=0;parent={root:None};Q=deque([root]);tree=set()
while Q:
    v=Q.popleft()
    for w in sorted(adj[v]):
        if w not in parent:
            parent[w]=v;tree.add(edge(v,w));Q.append(w)
assert len(parent)==N and len(tree)==N-1

def tree_path(a,b):
    pa=[a]
    while parent[pa[-1]] is not None:pa.append(parent[pa[-1]])
    pb=[b]
    while parent[pb[-1]] is not None:pb.append(parent[pb[-1]])
    meet=next(v for v in pa if v in set(pb))
    return pa[:pa.index(meet)+1]+list(reversed(pb[:pb.index(meet)]))
non_tree=[e for e in E if e not in tree]
assert len(non_tree)==9
for a,b in non_tree:
    path=tree_path(a,b);used=set(path)
    outside=next(v for v in range(N) if v not in used)
    walk=list(zip(path,path[1:]))+[(b,a)]
    z=Counter()
    for x,y in walk:
        i=edge_idx[edge(x,y)]
        z[I1[(outside,i)]] += 1 if x<y else -1
    boundary=Counter()
    for i,t in z.items():
        for j,s in d1[i].items():boundary[j]+=t*s
    assert all(q==0 for q in boundary.values())
    assert z[I1[(outside,edge_idx[edge(a,b)])]]!=0
# Rank over Q of d2 is 208: 208 by the mod-3 minor;
# at most 208 since these nine H1 cycles map independently onto H1(G).
# Consequently b1=9 and b2=20, and no chains exist above degree two.

# Automorphisms: backtrack along BFS order, preserving adjacency and
# nonadjacency with the already assigned vertices.
order=[];seen={0};Q=deque([0])
while Q:
    v=Q.popleft();order.append(v)
    for w in sorted(adj[v]):
        if w not in seen:seen.add(w);Q.append(w)
assert len(order)==N
perms=[]
def extend(k,mapping,used):
    if k==N:
        perms.append(tuple(mapping[i] for i in range(N)))
        return
    v=order[k]
    neigh=[u for u in mapping if u in adj[v]]
    opts=set(range(N)) if not neigh else set.intersection(*(adj[mapping[u]] for u in neigh))
    for x in sorted(opts-used):
        if all((u in adj[v]) == (mapping[u] in adj[x]) for u in mapping):
            mapping[v]=x;extend(k+1,mapping,used|{x});del mapping[v]
extend(0,{},set())
assert len(perms)==96 and len(set(perms))==96
assert all({edge(g[a],g[b]) for a,b in E}==edges for g in perms)

def order_of(g):
    seen=set();ans=1
    for v in range(N):
        if v not in seen:
            u=v;k=0
            while u not in seen:seen.add(u);u=g[u];k+=1
            ans=lcm(ans,k)
    return ans

def on_0(g,k):
    a,b=C0[k];return I0[edge(g[a],g[b])]
def on_1(g,k):
    v,i=C1[k];a,b=E[i]
    return I1[(g[v],edge_idx[edge(g[a],g[b])])],(1 if g[a]<g[b] else -1)
def on_2(g,k):
    i,j=C2[k];a,b=E[i];c,d=E[j]
    ei=edge_idx[edge(g[a],g[b])];ej=edge_idx[edge(g[c],g[d])]
    mapped=(ei,ej) if ei<ej else (ej,ei)
    s=(1 if g[a]<g[b] else -1)*(1 if g[c]<g[d] else -1)*(1 if ei<ej else -1)
    return C2.index(mapped),s

# Chain maps are checked cell by cell for every automorphism.
char_counts=Counter(); char_total=[0,0]
for g in perms:
    for k,col in enumerate(d1):
        image=Counter()
        for i,s in col.items():image[on_0(g,i)]+=s
        j,sgn=on_1(g,k)
        for i,s in d1[j].items():image[i]-=sgn*s
        assert all(x==0 for x in image.values())
    c2_map=[]
    for k,col in enumerate(d2):
        image=Counter()
        for i,s in col.items():
            j,sgn=on_1(g,i);image[j]+=s*sgn
        j,sgn=on_2(g,k);c2_map.append((j,sgn))
        for i,s in d2[j].items():image[i]-=sgn*s
        assert all(x==0 for x in image.values())
    t0=sum(on_0(g,i)==i for i in range(len(C0)))
    t1=sum(sign for i in range(len(C1)) for j,sign in [on_1(g,i)] if j==i)
    t2=sum(sign for i,(j,sign) in enumerate(c2_map) if j==i)
    fixed_vertices=sum(g[v]==v for v in range(N))
    graph_edges=sum(1 if (g[a],g[b])==(a,b) else -1
        for a,b in E if edge(g[a],g[b])==(a,b))
    h1=graph_edges-fixed_vertices+1
    h2=t0-t1+t2-1+h1
    char_counts[(order_of(g),h1,h2)]+=1
    char_total[0]+=h1;char_total[1]+=h2
expected={(1,9,20):1,(2,-3,0):6,(2,-1,-4):12,
          (2,-1,0):12,(2,1,-4):1,(3,-3,2):8,
          (4,1,0):8,(6,1,2):8,(8,1,0):24,(12,1,0):16}
assert dict(char_counts)==expected
assert char_total==[0,0]
rot=tuple([(i+1)%8 for i in range(8)]+[8+(i+1)%8 for i in range(8)])
r=tuple(range(N));rotation_char=[]
for k in range(8):
    assert r in perms
    n0=sum(on_0(r,i)==i for i in range(len(C0)))
    n1=sum(s for i in range(len(C1)) for j,s in [on_1(r,i)] if i==j)
    n2=sum(s for i in range(len(C2)) for j,s in [on_2(r,i)] if i==j)
    nv=sum(r[i]==i for i in range(N))
    ne=sum(1 if (r[a],r[b])==(a,b) else -1 for a,b in E
           if edge(r[a],r[b])==(a,b))
    h1=ne-nv+1;h2=n0-n1+n2-1+h1
    rotation_char.append((h1,h2));r=tuple(rot[r[i]] for i in range(N))
assert rotation_char==[(9,20),(1,0),(1,0),(1,0),(1,-4),(1,0),(1,0),(1,0)]
print('MOBIUS_KANTOR_TWO_POINT_CHARACTER_CERTIFICATE_OK')
print('cells',len(C0),len(C1),len(C2),'rank3',rank_mod(d2,3),'automorphisms',len(perms))
print('character classes',sorted(char_counts.items()))
print('full invariants',tuple(x//96 for x in char_total),'rotation invariants',(2,2))
