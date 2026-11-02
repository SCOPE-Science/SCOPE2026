"""Independent enumeration on the Fano plane represented by F_2^3.

Run with Python 3: python verify_secondary.py
All state spaces and legal transfers are enumerated rather than sampled.
"""
from collections import Counter
from functools import lru_cache
from math import comb

N=14
lines=sorted({tuple(sorted((a,b,a^b))) for a in range(1,8) for b in range(a+1,8)})
assert len(lines)==7 and all(len(q)==3 for q in lines)
assert all(sum({a,b}.issubset(q) for q in lines)==1 for a in range(1,8) for b in range(a+1,8))
neighbors=[set() for _ in range(N)]
for k,line in enumerate(lines):
    for x in line:
        u=x-1; v=7+k
        neighbors[u].add(v); neighbors[v].add(u)
assert all(len(n)==3 for n in neighbors)

@lru_cache(maxsize=None)
def reachable(c):
    # Recurrence exhausts all states after zero or more legal pebbling moves.
    output=sum(1<<i for i,z in enumerate(c) if z)
    for u,z in enumerate(c):
        if z<2:continue
        for v in neighbors[u]:
            x=list(c)
            x[u]-=2; x[v]+=1
            output|=reachable(tuple(x))
        if output==(1<<N)-1:break
    return output

def compositions(total,places=N):
    if places==1:
        yield (total,)
    else:
        for i in range(total+1):
            for tail in compositions(total-i,places-1):
                yield (i,)+tail

def count_components(states, slides_only):
    look={x:i for i,x in enumerate(states)}
    parent=list(range(len(states)))
    size=[1]*len(states)
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]
            a=parent[a]
        return a
    edges=0
    for i,x in enumerate(states):
        for u in range(N):
            if not x[u]:continue
            for v in (neighbors[u] if slides_only else range(N)):
                if v==u:continue
                y=list(x);y[u]-=1;y[v]+=1
                j=look.get(tuple(y))
                if j is not None and j>i:
                    edges+=1
                    a,b=find(i),find(j)
                    if a!=b:
                        parent[a]=b;size[b]+=size[a]
    cnt=Counter(size[i] for i in range(len(states)) if parent[i]==i)
    return edges,dict(sorted(cnt.items()))

EXPECTED={
    5:(0,0,{},0,{}),
    6:(161,42,{1:98,3:21},42,{1:98,3:21}),
    7:(5936,33726,{2576:1,3360:1},11970,{24:21,74:28,3360:1}),
    8:(71323,1145396,{71323:1},314496,{71323:1}),
}
for t in range(5,9):
    valid=[];all_count=0
    for x in compositions(t):
        all_count+=1
        if reachable(x)==(1<<N)-1:valid.append(x)
    assert all_count==comb(t+N-1,N-1)
    ej,cj=count_components(valid,False)
    es,cs=count_components(valid,True)
    assert (len(valid),ej,cj,es,cs)==EXPECTED[t],(t,len(valid),ej,cj,es,cs)
    print(f'T={t} total={all_count} solvable={len(valid)} jump_edges={ej} jump_components={cj} slide_edges={es} slide_components={cs}')
    if t==6:
        profiles=Counter(tuple(sorted((a for a in x if a),reverse=True)) for x in valid)
        assert profiles=={(4,2):98,(4,1,1):42,(3,3):21}
        print("OPTIMUM_PROFILES_OK",profiles)
    if t==7:
        bounded=sum(max(x)<=2 for x in valid)
        assert bounded==2576 and len(valid)-bounded==3360
        print("CAPACITY_BARRIER_OK",bounded,len(valid)-bounded)
print('INDEPENDENT_FANO_CERTIFICATE_OK states_cached=',reachable.cache_info().currsize)
