from itertools import combinations, permutations
from collections import deque, Counter
from fractions import Fraction

CONNECTED_EXPECTED = {1:1,2:1,3:4,4:38,5:728,6:26704}
SET_DIFF_EXPECTED = {1:0,2:0,3:0,4:0,5:400,6:18480}
UNIQUE_CONFLICT_EXPECTED = {1:0,2:0,3:0,4:0,5:0,6:720}
REP_EXPECTED = {
    122: {(0,2),(0,4),(0,5),(1,2),(1,3)},
    760: {(0,4),(0,5),(1,2),(1,3),(1,4),(2,3)},
}

def edge_list(n):
    return list(combinations(range(n),2))

def adj_from_mask(n, mask):
    es=edge_list(n)
    adj=[0]*n
    for k,(u,v) in enumerate(es):
        if (mask>>k)&1:
            adj[u]|=1<<v; adj[v]|=1<<u
    return adj

def connected_bfs(adj):
    n=len(adj)
    seen=1; q=[0]
    for u in q:
        bits=adj[u]
        for v in range(n):
            if (bits>>v)&1 and not ((seen>>v)&1):
                seen|=1<<v; q.append(v)
    return seen==(1<<n)-1

def connected_union_find(n, mask):
    es=edge_list(n)
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b:p[b]=a
    for k,(u,v) in enumerate(es):
        if (mask>>k)&1: union(u,v)
    r=find(0)
    return all(find(i)==r for i in range(n))

def bfs_distances(adj,s):
    n=len(adj); d=[-1]*n; d[s]=0; q=deque([s])
    while q:
        u=q.popleft(); bits=adj[u]
        for v in range(n):
            if (bits>>v)&1 and d[v]<0:
                d[v]=d[u]+1; q.append(v)
    return d

def all_pairs_bfs(adj):
    return [bfs_distances(adj,s) for s in range(len(adj))]

def floyd(adj):
    n=len(adj); inf=99
    d=[[0 if i==j else (1 if (adj[i]>>j)&1 else inf) for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            dik=d[i][k]
            for j in range(n):
                z=dik+d[k][j]
                if z<d[i][j]: d[i][j]=z
    return d

def canonical_mask(n,mask,perms=None):
    es=edge_list(n)
    idx={e:i for i,e in enumerate(es)}
    if perms is None: perms=list(permutations(range(n)))
    best=None
    for p in perms:
        bm=0
        for k,(a,b) in enumerate(es):
            u,v=p[a],p[b]
            e=(u,v) if u<v else (v,u)
            if (mask>>idx[e])&1: bm|=1<<k
        if best is None or bm<best: best=bm
    return best

def orbit(n,mask):
    es=edge_list(n); idx={e:i for i,e in enumerate(es)}; vals=set()
    for p in permutations(range(n)):
        bm=0
        for k,(a,b) in enumerate(es):
            u,v=p[a],p[b]
            e=(u,v) if u<v else (v,u)
            if (mask>>idx[e])&1: bm|=1<<k
        vals.add(bm)
    return vals

all_conflicts={}
for n in range(1,7):
    es=edge_list(n)
    connected=0; setdiff=0; uniq=0; conflicts=set()
    for mask in range(1<<len(es)):
        adj=adj_from_mask(n,mask)
        c1=connected_bfs(adj); c2=connected_union_find(n,mask)
        assert c1==c2
        if not c1: continue
        connected+=1
        db=all_pairs_bfs(adj); df=floyd(adj)
        assert db==df
        deg=[x.bit_count() for x in adj]
        ecc1=[max(row) for row in db]
        ecc2=[max(row) for row in df]
        assert ecc1==ecc2
        D={i for i,x in enumerate(deg) if x==max(deg)}
        C={i for i,x in enumerate(ecc1) if x==min(ecc1)}
        if D!=C: setdiff+=1
        if len(D)==len(C)==1 and D!=C:
            uniq+=1; conflicts.add(mask)
    assert connected==CONNECTED_EXPECTED[n], (n,connected)
    assert setdiff==SET_DIFF_EXPECTED[n], (n,setdiff)
    assert uniq==UNIQUE_CONFLICT_EXPECTED[n], (n,uniq)
    all_conflicts[n]=conflicts

conf=all_conflicts[6]
perms=list(permutations(range(6)))
classes=Counter(canonical_mask(6,m,perms) for m in conf)
assert classes==Counter({122:360,760:360}), classes
for rep,c in classes.items():
    orb=orbit(6,rep)
    assert len(orb)==360
    assert orb<=conf
    assert c==360
assert orbit(6,122).isdisjoint(orbit(6,760))
assert orbit(6,122)|orbit(6,760)==conf

# Exact representative checks, including the closeness tie between the two leaders.
for rep,edges in REP_EXPECTED.items():
    adj=adj_from_mask(6,rep)
    got={e for k,e in enumerate(edge_list(6)) if (rep>>k)&1}
    assert got==edges
    d=all_pairs_bfs(adj)
    deg=[x.bit_count() for x in adj]
    ecc=[max(row) for row in d]
    farness=[sum(row) for row in d]
    D=[i for i,x in enumerate(deg) if x==max(deg)]
    C=[i for i,x in enumerate(ecc) if x==min(ecc)]
    assert len(D)==len(C)==1 and D[0]!=C[0]
    assert farness[D[0]]==farness[C[0]]==min(farness)
    if rep==122:
        assert deg==[3,2,2,1,1,1]
        assert ecc==[3,3,2,4,4,4]
        assert farness==[8,10,8,14,12,12]
        assert D==[0] and C==[2]
        assert sum(deg)//2==5
    else:
        assert deg==[2,3,2,2,2,1]
        assert ecc==[3,3,4,4,2,4]
        assert farness==[10,8,11,11,8,14]
        assert D==[1] and C==[4]
        assert sum(deg)//2==6

print('VERIFY_OK')
print('connected_counts', [CONNECTED_EXPECTED[n] for n in range(1,7)])
print('maxset_vs_center_set_differences', [SET_DIFF_EXPECTED[n] for n in range(1,7)])
print('distinct_unique_leader_conflicts', [UNIQUE_CONFLICT_EXPECTED[n] for n in range(1,7)])
print('six_vertex_classes', dict(sorted(classes.items())))
print('representatives', {k:sorted(v) for k,v in REP_EXPECTED.items()})
