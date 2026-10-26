#!/usr/bin/env python3
"""Exact anti-forcing census of the Möbius--Kantor graph. Pure Python 3."""
from collections import Counter
from itertools import combinations

N=16
adj=[set() for _ in range(N)]
for i in range(8):
    for a,b in ((i,(i+1)%8),(i,i+8),(i+8,8+(i+3)%8)):
        adj[a].add(b);adj[b].add(a)
assert all(len(a)==3 for a in adj)
E={tuple(sorted((u,v))) for u in range(N) for v in adj[u]}
assert len(E)==24

color=[-1]*N
for root in range(N):
    if color[root]>=0:continue
    color[root]=0; queue=[root]
    for u in queue:
        for v in adj[u]:
            if color[v]==-1:color[v]=1-color[u];queue.append(v)
            else:assert color[v]==1-color[u]
L=[i for i in range(N) if color[i]==0]
R=[i for i in range(N) if color[i]==1]
assert len(L)==len(R)==8
idxR={v:i for i,v in enumerate(R)}
options=[tuple(sorted(idxR[v] for v in adj[u])) for u in L]

perms=[]
def perm_match(i,taken,p):
    if i==8:perms.append(tuple(p));return
    for j in options[i]:
        if not(taken>>j&1):perm_match(i+1,taken|1<<j,p+[j])
perm_match(0,0,[])
matchings=[]
def matching(remaining,chosen):
    if not remaining:matchings.append(frozenset(chosen));return
    u=min(remaining)
    for v in adj[u]&remaining:
        matching(remaining-{u,v},chosen+[tuple(sorted((u,v)))])
matching(set(range(N)),[])
matchset={frozenset(tuple(sorted((L[i],R[j]))) for i,j in enumerate(p)) for p in perms}
assert len(matchset)==len(perms)==len(matchings)==len(set(matchings))==33
assert matchset==set(matchings)

# Permanent via subsets, independent of the backtracking routines.
ways=[0]*256;ways[0]=1
for mask in range(1,256):
    i=mask.bit_count()-1
    # This recurrence is transposed: sum over injections of first |mask| rows
    # into the |mask| chosen columns, assigning its last row.
    ways[mask]=sum(ways[mask^(1<<j)] for j in options[i] if mask>>j&1)
assert ways[255]==33

autos=[];mapping={};inverse={}
def automorphism():
    if len(mapping)==N:
        autos.append(tuple(mapping[i] for i in range(N)));return
    u=min((i for i in range(N) if i not in mapping),key=lambda i:(-len(adj[i]&mapping.keys()),i))
    for v in range(N):
        if v in inverse:continue
        if all((x in adj[u])==(mapping[x] in adj[v]) for x in mapping):
            mapping[u]=v;inverse[v]=u
            automorphism()
            del mapping[u];del inverse[v]
automorphism()
assert len(autos)==96==len(set(autos))
lookup={m:i for i,m in enumerate(matchings)}
orbits=[];remaining=set(range(33))
while remaining:
    r=min(remaining);m=matchings[r]
    orb=set()
    for a in autos:
        image=frozenset(tuple(sorted((a[u],a[v]))) for u,v in m)
        orb.add(lookup[image])
    assert orb<=remaining
    orbits.append(orb);remaining-=orb
assert sorted(map(len,orbits))==[3,6,24]

def cycle_type(M):
    sub=[adj[i]-{next(v if u==i else u for u,v in M if u==i or v==i)} for i in range(N)]
    assert all(len(a)==2 for a in sub)
    unseen=set(range(N));out=[]
    while unseen:
        q=[min(unseen)];unseen.remove(q[0])
        for u in q:
            for v in sub[u]:
                if v in unseen:unseen.remove(v);q.append(v)
        out.append(len(q))
    return tuple(sorted(out))

def digraph(M):
    p=next(p for p in perms if frozenset(tuple(sorted((L[i],R[j]))) for i,j in enumerate(p))==M)
    inv={j:i for i,j in enumerate(p)}
    edges=[(i,inv[j]) for i in range(8) for j in options[i] if j!=p[i]]
    assert len(edges)==16 and all(a!=b for a,b in edges)
    return edges

def dp_antiforcing(arcs):
    outgoing=[0]*8
    for u,v in arcs:outgoing[u]|=1<<v
    dp=[100]*256;dp[0]=0
    for mask in range(1,256):
        for v in range(8):
            if mask>>v&1:
                others=mask^(1<<v)
                dp[mask]=min(dp[mask],dp[others]+(outgoing[v]&others).bit_count())
    return dp[255]

def acyclic_after_deletions(arcs, deleted):
    deg=[0]*8;successors=[[] for _ in range(8)]
    for i,(a,b) in enumerate(arcs):
        if (deleted>>i)&1:continue
        deg[b]+=1;successors[a].append(b)
    stack=[v for v,d in enumerate(deg) if d==0];cnt=0
    while stack:
        u=stack.pop();cnt+=1
        for v in successors[u]:
            deg[v]-=1
            if deg[v]==0:stack.append(v)
    return cnt==8

def direct_antiforcing(arcs):
    for k in range(7):
        for take in combinations(range(16),k):
            mask=sum(1<<i for i in take)
            if acyclic_after_deletions(arcs,mask):return k,mask
    raise AssertionError('no solution')



def directed_cycle_packing(arcs):
    """List every directed simple cycle and maximize arc-disjoint cycle packing."""
    adjdir=[[] for _ in range(8)]
    for i,(u,v) in enumerate(arcs):adjdir[u].append((v,i))
    cycles=set()
    def dfs(root,x,seen,path):
        for y,e in adjdir[x]:
            if y==root and len(seen)>=2:
                cycles.add(sum(1<<a for a in path+(e,)))
            elif y>root and y not in seen:
                dfs(root,y,seen|{y},path+(e,))
    for root in range(8):dfs(root,root,{root},())
    assert cycles
    memo={}
    def solve(used):
        if used in memo:return memo[used]
        best=()
        for cyc in sorted(cycles):
            if used&cyc==0:
                candidate=(cyc,)+solve(used|cyc)
                if len(candidate)>len(best):best=candidate
        memo[used]=best
        return best
    return len(cycles),solve(0)

profile=Counter(); afs={}
for m in matchings:
    c=cycle_type(m); af=dp_antiforcing(digraph(m))
    profile[(c,af)]+=1;afs[m]=af
assert profile=={((8,8),4):3,((16,),5):6,((6,10),5):24},profile
for orb in orbits:
    reps=[matchings[i] for i in orb]
    assert len({(cycle_type(m),afs[m]) for m in reps})==1
    rep=reps[0];a=digraph(rep)
    brute,witness=direct_antiforcing(a)
    assert brute==afs[rep]
    cycle_total,packed=directed_cycle_packing(a)
    assert len(packed)==brute
    assert all(not(x&y) for i,x in enumerate(packed) for y in packed[i+1:])
    print('CYCLE_PACKING',len(orb),cycle_total,len(packed),packed)
    print('ORBIT',len(orb),'CYCLES',cycle_type(rep),'AF',afs[rep],
          'WITNESS_MASK',witness)
print('PERMANENT',ways[255], 'MATCHINGS',len(matchings), 'AUTOMORPHISMS',len(autos))
print('PROFILE',dict(sorted(profile.items())))
print('POLYNOMIAL',dict(sorted(Counter(afs.values()).items())))
print('VERIFY_OK')
