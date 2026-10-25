"""Independent-set token reconfiguration on the 24-vertex McGee graph.
Run: python3 verify_a.py  (Python standard library only).
"""
from collections import Counter, deque
N=24
EDGES={tuple(sorted((i,(i+1)%N))) for i in range(N)}
EDGES|={tuple(sorted((i,(i+(12,7,-7)[i%3])%N))) for i in range(N)}
assert len(EDGES)==36
ADJ=[0]*N
for u,v in EDGES:ADJ[u]|=1<<v;ADJ[v]|=1<<u
assert set(map(int.bit_count,ADJ))=={3}
# Enumeration over all independent sets by a binary decision recursion.
SIZES=Counter(); STATES={9:[],10:[]}
def visit(v,s,forbid):
    if v==N:
        k=s.bit_count(); SIZES[k]+=1
        if k in STATES:STATES[k].append(s)
        return
    visit(v+1,s,forbid)
    if not (forbid>>v)&1:
        visit(v+1,s|(1<<v),forbid|ADJ[v]|(1<<v))
visit(0,0,0)
assert [SIZES[i] for i in range(11)]==[1,24,240,1304,4212,8328,10024,7072,2668,424,8]
assert not any(k>10 for k in SIZES)
def report(k, mode):
    S=sorted(STATES[k]); ix={s:i for i,s in enumerate(S)}; adj=[set() for s in S]
    for i,s in enumerate(S):
        for u in range(N):
            if not s>>u&1:continue
            for v in range(N):
                if s>>v&1:continue
                if mode=='TS' and not ADJ[u]>>v&1:continue
                j=ix.get(s^(1<<u)^(1<<v))
                if j is not None:adj[i].add(j)
    assert all(i in adj[j] for i,nb in enumerate(adj) for j in nb)
    unseen=set(range(len(S))); comps=[]; ecc=[]
    while unseen:
        start=min(unseen);q=deque([start]);seen={start};unseen.remove(start)
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v not in seen:seen.add(v);unseen.remove(v);q.append(v)
        comps.append(seen)
    for comp in comps:
        for start in comp:
            dist={start:0}; q=deque([start])
            while q:
                u=q.popleft()
                for v in adj[u]:
                    if v not in dist: dist[v]=dist[u]+1;q.append(v)
            assert len(dist)==len(comp)
            ecc.append(max(dist.values()))
    sizes=Counter(map(len,comps)); degrees=Counter(map(len,adj)); ecs=Counter(ecc)
    print(f'{mode} k={k}: states={len(S)} edges={sum(map(len,adj))//2} comps={sorted(sizes.items())} degrees={sorted(degrees.items())} eccentricity={sorted(ecs.items())}')
    return S,comps
S9, tj9=report(9,'TJ'); _,ts9=report(9,'TS'); S10,tj10=report(10,'TJ'); _,ts10=report(10,'TS')
assert list(map(len,tj9))==[424]
assert sorted(map(len,ts9))==[2,2,2,2,416]
assert sorted(map(len,tj10))==[4,4]
assert sorted(map(len,ts10))==[4,4]
print('MAXIMUM_MASKS:',[hex(s) for s in S10]);print('ALL ASSERTIONS PASSED')
