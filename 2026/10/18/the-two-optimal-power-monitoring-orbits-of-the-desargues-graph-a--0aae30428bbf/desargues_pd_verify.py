#!/usr/bin/env python3
"""Exact power-domination and optimal-placement reconfiguration on H(5,2).
Requires Python >=3.9, standard library only. Run: python3 desargues_pd_verify.py.
"""
from itertools import combinations, permutations
from collections import Counter, deque

V=tuple(x for x in range(32) if x.bit_count() in (2,3))
assert len(V)==20
I={x:i for i,x in enumerate(V)}
N=[0]*20
for i,x in enumerate(V):
    for j,y in enumerate(V):
        if i != j and (x & y == x if x.bit_count()==2 else x & y == y):
            N[i] |= 1<<j
assert all(z.bit_count()==3 for z in N)
ALL=(1<<20)-1

def levels(seed):
    obs=seed
    for v in range(20):
        if seed>>v & 1:obs |= N[v]
    sizes=[obs.bit_count()]
    while obs != ALL:
        nxt=obs
        for v in range(20):
            if obs>>v & 1:
                left=N[v]&~obs
                if left and left&(left-1)==0:nxt |= left
        if nxt==obs:break
        obs=nxt; sizes.append(obs.bit_count())
    return obs==ALL,tuple(sizes)

def dist(a,b):
    q=deque([a]); d={a:0}
    while q:
        v=q.popleft()
        for w in range(20):
            if N[v]>>w&1 and w not in d:d[w]=d[v]+1;q.append(w)
    return d[b]
D=[[dist(i,j) for j in range(20)] for i in range(20)]
assert all(len(row)==20 for row in D)

def profile(s):
    return tuple(sorted(D[a][b] for a,b in combinations(s,2)))

# Explicit subgroup of Aut(H(5,2)): permute underlying five symbols,
# then optionally complement each subset. Distinct maps (120*2=240).
SYMS=[]
for p in permutations(range(5)):
    translated={x:sum(1<<p[k] for k in range(5) if x>>k&1) for x in V}
    for rev in (0,31):
        t=tuple(I[translated[x]^rev] for x in V)
        assert len(set(t))==20
        assert all((N[i]>>j & 1)==(N[t[i]]>>t[j]&1) for i in range(20) for j in range(20))
        SYMS.append(t)
assert len(SYMS)==len(set(SYMS))==240

def mask_of(s):return sum(1<<i for i in s)
def image(b,t):return sum(1<<t[i] for i in range(20) if b>>i&1)

# All triples: exact exhaustive orbit disjointification, not sampling.
all3={mask_of(s) for s in combinations(range(20),3)}
assert len(all3)==1140
orbits=[]
while all3:
    seed=min(all3)
    orb={image(seed,t) for t in SYMS}
    assert orb<=all3
    all3-=orb
    orbits.append((seed,orb))
assert len(orbits)==12 and sum(len(o) for _,o in orbits)==1140

# Lower bound is exhaustive on sizes 0,1,2; for triples classify all members.
for k in range(3):
    assert not any(levels(mask_of(s))[0] for s in combinations(range(20),k))
GOOD=set()
print('orbit  size  profile  closed-neighborhood-and-forcing-level-sizes  power-dominating')
for idx,(seed,orb) in enumerate(orbits,1):
    rep=tuple(v for v in range(20) if seed>>v&1)
    sig=profile(rep)
    accepted,obs=levels(seed)
    assert all(profile(tuple(v for v in range(20) if b>>v&1))==sig for b in orb)
    assert all(levels(b)[0]==accepted and levels(b)[1]==obs for b in orb)
    if accepted:GOOD |= orb
    print('%02d %3d %-12s %-22s %s rep=%s'%(idx,len(orb),str(sig),str(obs),accepted,tuple(V[v] for v in rep)))
assert len(GOOD)==240
SHAPES={profile(tuple(i for i in range(20) if b>>i&1)) for b in GOOD}
assert SHAPES=={(2,3,5),(3,3,4)}
assert Counter(profile(tuple(i for i in range(20) if b>>i&1)) for b in GOOD)==Counter({(2,3,5):120,(3,3,4):120})

def mkgraph(slide=False):
    graph={s:set() for s in GOOD}
    for s in GOOD:
        for old in range(20):
            if not s>>old&1:continue
            for new in range(20):
                if s>>new&1:continue
                if slide and not N[old]>>new&1:continue
                t=s^(1<<old)^(1<<new)
                if t in GOOD:graph[s].add(t)
    assert all(s in graph[t] for s,adj in graph.items() for t in adj)
    return graph

def bfs(g,seed):
    q=deque([seed]);out={seed:0}
    while q:
        s=q.popleft()
        for t in g[s]:
            if t not in out:out[t]=out[s]+1;q.append(t)
    return out

reps={profile(tuple(i for i in range(20) if seed>>i&1)):seed for seed,o in orbits if seed in GOOD}
assert len(reps)==2
for kind,sliding in [('TJ',False),('TS',True)]:
    R=mkgraph(sliding)
    degrees=Counter(len(a) for a in R.values())
    edgecount=sum(map(len,R.values()))//2
    assert len(bfs(R,next(iter(GOOD))))==240
    ecc={}
    for sig,seed in sorted(reps.items()):
        d=bfs(R,seed)
        assert len(d)==240
        ecc[sig]=max(d.values())
        print(kind,'from',sig,'distance_levels',tuple(Counter(d.values()).get(i,0) for i in range(ecc[sig]+1)))
    print(kind,'states',len(R),'edges',edgecount,'degrees',sorted(degrees.items()),'radius',min(ecc.values()),'diameter',max(ecc.values()))
    if kind=='TJ':
        assert edgecount==1800 and degrees==Counter({17:120,13:120})
        assert ecc=={(2,3,5):4,(3,3,4):4}
        assert all(len(R[b])==(17 if profile(tuple(i for i in range(20) if b>>i&1))==(2,3,5) else 13) for b in GOOD)
    else:
        assert edgecount==480 and degrees==Counter({4:240})
        assert ecc=={(2,3,5):7,(3,3,4):8}
        assert all((sum(V[i].bit_count()==2 for i in range(20) if s>>i&1)%2)!=(sum(V[i].bit_count()==2 for i in range(20) if t>>i&1)%2) for s in GOOD for t in R[s])
        ec=Counter(tuple(sorted((profile(tuple(i for i in range(20) if s>>i&1)),profile(tuple(i for i in range(20) if t>>i&1))))) for s in GOOD for t in R[s] if s<t)
        assert sorted(ec.values())==[120,120,240]
        print('TS edge-class-counts',sorted(ec.items()))
print('VERIFY_OK')
