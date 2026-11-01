#!/usr/bin/env python3
"""Exact combinatorial checks for the icosahedral independence complex.
Only the Python standard library is required.
"""
from collections import Counter, deque, defaultdict
from itertools import combinations

N, S = 10, 11
V = range(12)
E = set()
def edge(a, b):
    assert a != b
    E.add(tuple(sorted((a, b))))
for i in range(5):
    edge(N, i)
    edge(S, 5+i)
    edge(i, (i+1)%5)
    edge(5+i, 5+(i+1)%5)
    edge(i, 5+i)
    edge(i, 5+(i-1)%5)
adj = {v: set() for v in V}
for a,b in E:
    adj[a].add(b); adj[b].add(a)
assert len(E)==30 and all(len(adj[v])==5 for v in V)

def distance_from(a):
    d={a:0}; q=deque([a])
    while q:
        x=q.popleft()
        for y in sorted(adj[x]):
            if y not in d:
                d[y]=d[x]+1; q.append(y)
    assert len(d)==12
    return d
D={v:distance_from(v) for v in V}
assert Counter(D[10].values()) == {0:1,1:5,2:5,3:1}
assert all(Counter(D[v].values())=={0:1,1:5,2:5,3:1} for v in V)
D2={tuple(sorted((a,b))) for a,b in combinations(V,2) if D[a][b]==2}
D3={tuple(sorted((a,b))) for a,b in combinations(V,2) if D[a][b]==3}
assert len(D2)==30 and len(D3)==6
assert len(D2|D3|E)==66 and len((D2|D3)&E)==0
assert D3=={(10,11), (0,7), (1,8), (2,9), (3,5), (4,6)}

# A direct graph isomorphism from the distance-two graph to the original one.
phi={N:N,S:S}
phi.update({i:5+(2*i+1)%5 for i in range(5)})
phi.update({5+i:2*i%5 for i in range(5)})
assert len(set(phi.values()))==12
assert {tuple(sorted((phi[a],phi[b]))) for a,b in D2}==E

ind={k:tuple(t for t in combinations(V,k) if all(tuple(sorted((a,b))) not in E for a,b in combinations(t,2))) for k in range(1,5)}
assert tuple(map(len, (ind[1],ind[2],ind[3],ind[4])))==(12,36,20,0)
tri=ind[3]
assert all(all(tuple(sorted(e)) in D2 for e in combinations(f,2)) for f in tri)
assert set(ind[2]) == D2|D3
tri2=tuple(t for t in combinations(V,3) if all(tuple(sorted(e)) in D2 for e in combinations(t,2)))
assert tri == tri2
inc=defaultdict(list)
for f in tri:
    for e in combinations(f,2):inc[e].append(f)
assert set(inc)==D2 and all(len(ff)==2 for ff in inc.values())
# Verify every vertex link in the triangle subcomplex is a five-cycle.
for v in V:
    link_edges=[tuple(x for x in f if x!=v) for f in tri if v in f]
    L=defaultdict(set)
    for a,b in link_edges:L[a].add(b);L[b].add(a)
    assert len(L)==5 and len(link_edges)==5 and all(len(z)==2 for z in L.values())
    seen={next(iter(L))}; stack=list(seen)
    while stack:
        x=stack.pop()
        for y in L[x]:
            if y not in seen:seen.add(y);stack.append(y)
    assert len(seen)==5
assert len(V)-len(D2)+len(tri)==2

# A global integral orientation of the triangulated sphere.
def boundary_sign(face, edge):
    for j in range(3):
        if face[:j]+face[j+1:]==edge:return (-1)**j
    raise ValueError('not a face')
ori={tri[0]:1}; queue=deque([tri[0]])
while queue:
    f=queue.popleft()
    for e in combinations(f,2):
        for g in inc[e]:
            if g==f:continue
            desired=-ori[f]*boundary_sign(f,e)*boundary_sign(g,e)
            if g in ori:assert ori[g]==desired
            else:ori[g]=desired;queue.append(g)
assert len(ori)==20
assert all(sum(ori[f]*boundary_sign(f,e) for f in inc[e])==0 for e in D2)

def permutations_of_graph():
    # Backtracking over adjacency and non-adjacency; no external graph package.
    ans=[]
    def rec(p, used):
        if len(p)==12:
            ans.append(tuple(p[i] for i in V));return
        vv=None; opts=None
        for v in V:
            if v in p:continue
            choices=[w for w in V if w not in used and all((u in adj[v]) == (p[u] in adj[w]) for u in p)]
            if not choices:return
            if opts is None or len(choices)<len(opts):vv,opts=v,choices
        for w in opts:
            p[vv]=w;used.add(w)
            rec(p,used)
            used.remove(w);del p[vv]
    rec({},set())
    return sorted(ans)
G=permutations_of_graph()
assert len(G)==120 and len(set(G))==120
idp=tuple(V)
assert idp in G

def compose(p,q):return tuple(p[q[i]] for i in V)
def inverse(p):return tuple(p.index(i) for i in V)
def order(p):
    x=idp
    for k in range(1,121):
        x=compose(p,x)
        if x==idp:return k
    raise RuntimeError('unbounded order')
def sign(values):
    return -1 if sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))%2 else 1

def sphere_degree(p):
    vals=set()
    for f in tri:
        image=tuple(p[x] for x in f)
        to=tuple(sorted(image))
        vals.add(ori[f]*sign(image)*ori[to])
    assert len(vals)==1
    return vals.pop()

def h1_trace(p):
    ans=0
    for a,b in D3:
        if tuple(sorted((p[a],p[b])))==(a,b):
            ans+=1 if p[a]==a else -1
    return ans

t=tuple(next(j for j in V if D[i][j]==3) for i in V)
assert order(t)==2 and all(compose(t,p)==compose(p,t) for p in G)
assert sphere_degree(t)==-1 and h1_trace(t)==-6
assert len([p for p in G if sphere_degree(p)==1])==60
stats=Counter((sphere_degree(p),order(p),h1_trace(p)) for p in G)
expected={(1,1,6):1,(1,2,-2):15,(1,3,0):20,(1,5,1):24,
          (-1,2,-6):1,(-1,2,2):15,(-1,6,0):20,(-1,10,-1):24}
assert dict(stats)==expected, (stats,expected)
assert sum(h1_trace(p) for p in G)==0
assert sum(h1_trace(p) for p in G if sphere_degree(p)==1)==0
assert sum(sphere_degree(p) for p in G)==0
assert sum(sphere_degree(p) for p in G if sphere_degree(p)==1)==60

# Independent chain check: exact simplicial boundary ranks over several fields.
def rankmod(mat,prime):
    rows=[list(map(lambda x:x%prime,r)) for r in mat]
    m=len(rows); n=len(rows[0]) if m else 0
    rank=0
    for j in range(n):
        i=next((i for i in range(rank,m) if rows[i][j]),None)
        if i is None:continue
        rows[rank],rows[i]=rows[i],rows[rank]
        sc=pow(rows[rank][j],-1,prime)
        rows[rank][j:]=[(sc*x)%prime for x in rows[rank][j:]]
        for i in range(rank+1,m):
            if rows[i][j]:
                fac=rows[i][j]
                rows[i][j:]=[(x-fac*y)%prime for x,y in zip(rows[i][j:],rows[rank][j:])]
        rank+=1
    return rank
v_ix={v:i for i,v in enumerate(V)}
e_ix={e:i for i,e in enumerate(ind[2])}
d1=[[0]*len(ind[2]) for _ in V]
for j,(a,b) in enumerate(ind[2]):d1[v_ix[a]][j]=-1;d1[v_ix[b]][j]=1
d2=[[0]*len(tri) for _ in ind[2]]
for j,f in enumerate(tri):
    for k in range(3):d2[e_ix[f[:k]+f[k+1:]]][j]=(-1)**k
for p in (2,3,5,101):
    assert rankmod(d1,p)==11
    assert rankmod(d2,p)==19

print('independent_face_counts', (12,36,20,0))
print('independent_edge_partition distance_2=30 antipodal=6')
print('distance_two_graph_is_icosahedron', True)
print('sphere_links_and_orientation', '12 five-cycles, 20 oriented triangles')
print('antipodal_edges',sorted(D3))
print('automorphism_group_order',len(G))
print('degree_order_h1trace_counts')
for row,num in sorted(stats.items(),reverse=True):print(' ',row,num)
print('rational_homology_rotational_fixed_dimensions', (0,1))
print('rational_homology_full_fixed_dimensions', (0,0))
print('H1_A5_character_by_order', {1:6,2:-2,3:0,5:1})
print('H2_A5_character_by_order', {1:1,2:1,3:1,5:1})
print('VERIFIED_OK')
