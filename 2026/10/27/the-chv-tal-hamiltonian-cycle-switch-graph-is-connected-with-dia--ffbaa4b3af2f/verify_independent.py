"""Second, edge-subset exhaustive verifier for Chvatal Hamiltonian switches (Python 3, stdlib only)."""
from collections import Counter, deque
from itertools import combinations

E = ((0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),
     (2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),
     (5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11))

# Enumerate every 2-regular spanning edge subset by accept/reject decisions on edges;
# no Hamiltonian path enumeration is used in this independent implementation.
rem = [0]*12
for a,b in E: rem[a]+=1; rem[b]+=1
chosen = [0]*12
factors=set()
def extend(i,mask):
    if any(chosen[v]>2 or chosen[v]+rem[v]<2 for v in range(12)):
        return
    if i==len(E):
        assert all(x==2 for x in chosen)
        factors.add(mask)
        return
    a,b=E[i]
    rem[a]-=1;rem[b]-=1
    extend(i+1,mask)
    chosen[a]+=1;chosen[b]+=1
    extend(i+1,mask | (1<<i))
    chosen[a]-=1;chosen[b]-=1
    rem[a]+=1;rem[b]+=1
extend(0,0)
print('TWO_FACTORS_TOTAL', len(factors))

def connected(mask):
    nei=[[] for _ in range(12)]
    for j,(a,b) in enumerate(E):
        if mask>>j&1:
            nei[a].append(b);nei[b].append(a)
    seen={0}; todo=[0]
    for a in todo:
        for b in nei[a]:
            if b not in seen: seen.add(b);todo.append(b)
    return len(seen)==12

H=sorted(m for m in factors if connected(m))
assert len(H)==185
adj={m:[] for m in H}
for a,b in combinations(H,2):
    if (a^b).bit_count()==4:
        adj[a].append(b);adj[b].append(a)
assert sum(map(len,adj.values()))//2==382
cc=[];unseen=set(H)
while unseen:
    root=min(unseen);d={root:0};Q=deque([root]);unseen.remove(root)
    while Q:
        u=Q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v]=d[u]+1;Q.append(v);unseen.discard(v)
    cc.append(len(d))
assert cc==[185]
deg=Counter(map(len,adj.values()))
assert deg=={2:21,3:48,4:60,5:28,6:6,7:18,9:4}
ecc=Counter()
for root in H:
    d={root:0};Q=deque([root])
    while Q:
        u=Q.popleft()
        for v in adj[u]:
            if v not in d: d[v]=d[u]+1;Q.append(v)
    assert len(d)==185
    ecc[max(d.values())]+=1
assert ecc=={6:12,7:104,8:53,9:16}
print('INDEPENDENT_VERIFY_OK two_factor_filter_hamiltonian=185 switch_edges=382 diameter=9 radius=6 connected=1')
