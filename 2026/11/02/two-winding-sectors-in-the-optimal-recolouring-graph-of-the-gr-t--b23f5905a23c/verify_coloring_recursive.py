"""Complete proof-by-enumeration for the 4-color recoloring graph of mu(C5).

Run with Python >=3.9; no third-party dependencies. Graph vertices are
v_0,...,v_4,s_0,...,s_4,z, where indices on cycle vertices are mod 5.
"""
from collections import Counter, deque
from itertools import permutations

N = [set() for _ in range(11)]
def edge(i,j):
    N[i].add(j); N[j].add(i)
for i in range(5):
    edge(i,(i+1)%5)
    edge(5+i,10)
    edge(5+i,(i-1)%5)
    edge(5+i,(i+1)%5)
assert sum(map(len,N)) == 40
# Exhaustive depth-first assignment: each partial assignment is extended by
# all four allowable labels at the next vertex, so no proper coloring is lost.
order = sorted(range(11), key=lambda i: -len(N[i]))
work = [-1]*11
states = []
def extend(k):
    if k == 11:
        states.append(tuple(work)); return
    i = order[k]
    forbidden = {work[j] for j in N[i] if work[j] >= 0}
    for c in range(4):
        if c not in forbidden:
            work[i]=c
            extend(k+1)
    work[i]=-1
extend(0)
assert len(states) == 12480
index = {s:i for i,s in enumerate(states)}
assert len(index)==len(states)

def winding_sign(s):
    apex=s[10]
    remaining=[c for c in range(4) if c!=apex]
    ranking={c:i for i,c in enumerate(remaining)}
    reduced=[ranking[s[i] if s[i]!=apex else s[5+i]] for i in range(5)]
    assert all(reduced[i]!=reduced[(i+1)%5] for i in range(5))
    turns=sum(1 if (reduced[(i+1)%5]-reduced[i])%3==1 else -1
              for i in range(5))
    assert abs(turns)==3
    return (turns//3) * (-1 if apex%2 else 1)

signs=[winding_sign(s) for s in states]
assert Counter(signs)=={1:6240,-1:6240}
adj=[[] for _ in states]
for a,s in enumerate(states):
    for i in range(11):
        forbidden={s[j] for j in N[i]}
        for c in range(4):
            if c==s[i] or c in forbidden: continue
            t=list(s);t[i]=c
            b=index[tuple(t)]
            assert signs[a]==signs[b]
            adj[a].append(b)
assert sum(map(len,adj))==90480
assert Counter(len(x) for x in adj)=={5:480,6:2640,7:3840,8:4320,9:1200}
assert all(a in adj[b] for b,aa in enumerate(adj) for a in aa)

def flood(src, permitted=None):
    distance={src:0};q=deque([src])
    while q:
        a=q.popleft()
        for b in adj[a]:
            if b not in distance and (permitted is None or permitted(b)):
                distance[b]=distance[a]+1;q.append(b)
    return distance

components=[];unseen=set(range(len(states)))
while unseen:
    d=flood(next(iter(unseen)))
    components.append(set(d))
    unseen-=d.keys()
assert len(components)==2 and sorted(map(len,components))==[6240,6240]
assert {signs[i] for i in components[0]}!={signs[i] for i in components[1]}
# More detailed constructive connectivity certificate: fix the apex color.
# Exactly two induced connected pieces of 1560 configurations remain.
for apex in range(4):
    U={i for i,s in enumerate(states) if s[10]==apex}
    assert len(U)==3120
    local=[]
    while U:
        p=next(iter(U))
        block=set(flood(p,lambda j:states[j][10]==apex))
        local.append(block)
        U-=block
    assert sorted(map(len,local))==[1560,1560]
    assert all(len({signs[i] for i in z})==1 for z in local)
# Every pair of apex color classes is joined within each sign class.
apex_between=Counter()
for a,s in enumerate(states):
    for b in adj[a]:
        if s[10]<states[b][10]:
            apex_between[(s[10],states[b][10],signs[a])]+=1
assert len(apex_between)==12 and set(apex_between.values())=={190}
# Verify eccentricities for an orbit representative under S4 x D5.
# Those operations preserve recoloring distance exactly. Hence checking every
# orbit representative is equivalent to checking every one of 12480 roots.
color_perms=list(permutations(range(4)))
vertex_perms=[]
for offset in range(5):
    for orientation in (1,-1):
        vp=[(orientation*i+offset)%5 for i in range(5)]
        vp += [5+(orientation*i+offset)%5 for i in range(5)] + [10]
        vertex_perms.append(vp)
remaining=set(range(len(states)))
ecc_count=Counter(); orbit_count=0;orbit_sizes=Counter()
while remaining:
    a=next(iter(remaining));s=states[a]
    orbit=set()
    for cp in color_perms:
        for vp in vertex_perms:
            t=[None]*11
            for i in range(11):t[vp[i]]=cp[s[i]]
            orbit.add(index[tuple(t)])
    assert orbit<=remaining
    remaining-=orbit
    orbit_count+=1;orbit_sizes[len(orbit)]+=1
    distances=flood(a)
    assert len(distances)==6240
    ecc=max(distances.values())
    ecc_count[ecc]+=len(orbit)
assert orbit_count==56 and orbit_sizes=={240:48,120:8}
assert ecc_count=={15:2160,16:10200,17:120}
print('RECURSIVE_12480_45240_TWO_COMPONENTS_6240_PASS')
print('SIGNED_WINDING_INVARIANT_AND_FIXED_APEX_CONNECTIVITY_PASS')
print('DEGREE_POLYNOMIAL_AND_ALL_ORBIT_ECCENTRICITIES_15_17_PASS')
