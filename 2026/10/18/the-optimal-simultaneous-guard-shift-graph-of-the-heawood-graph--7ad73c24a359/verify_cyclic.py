"""Complete enumeration for simultaneous shifts among minimum dominating sets of the Fano incidence graph."""
from itertools import combinations, permutations
from collections import Counter, deque
import json

N=14
lines=[{j,(j+1)%7,(j+3)%7} for j in range(7)]
adj=[set() for _ in range(N)]
for j,L in enumerate(lines):
    for p in L:
        adj[p].add(j+7)
        adj[j+7].add(p)

def dominating(S):
    return all(v in S or not adj[v].isdisjoint(S) for v in range(N))

def movable(A,B):
    return any(all(a==b or b in adj[a] for a,b in zip(A,perm)) for perm in permutations(B))

doms3=[c for c in combinations(range(N),3) if dominating(set(c))]
doms4=[c for c in combinations(range(N),4) if dominating(set(c))]
assert len(doms3)==0 and len(doms4)==21
flags={}
for j,L in enumerate(lines):
    for r in L:
        s=tuple(sorted((L-{r})|{h+7 for h,H in enumerate(lines) if h!=j and r in H}))
        flags[(r,j)]=s
assert set(flags.values())==set(doms4) and len(flags)==21
flag_at={v:k for k,v in flags.items()}
shifts={a:set() for a in doms4}
for a,b in combinations(doms4,2):
    move=movable(a,b)
    fa,fb=flag_at[a],flag_at[b]
    assert move == (fa[0]!=fb[0] and fa[1]!=fb[1])
    if move:
        shifts[a].add(b); shifts[b].add(a)
assert all(len(shifts[a])==16 for a in doms4)
assert sum(len(shifts[a]) for a in doms4)//2==168
hist=Counter()
for a in doms4:
    dist={a:0}; Q=deque([a])
    while Q:
        u=Q.popleft()
        for v in shifts[u]:
            if v not in dist:
                dist[v]=dist[u]+1; Q.append(v)
    assert len(dist)==21 and max(dist.values())==2
    hist.update(dist.values())
    for attack in range(N):
        if attack not in a:
            assert any(attack in b for b in shifts[a])
assert hist == Counter({0:21,1:336,2:84})
print(json.dumps({"verification":"VERIFY_OK","graph":"Fano incidence/Heawood","dominating_three_sets":0,"minimum_dominating_sets":21,"flags":21,"shift_edges":168,"degree":16,"diameter":2,"distance_pair_histogram":dict(sorted(hist.items())),"winning_initial_sets":21},sort_keys=True))
