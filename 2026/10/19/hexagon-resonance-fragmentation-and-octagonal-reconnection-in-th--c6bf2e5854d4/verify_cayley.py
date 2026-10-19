#!/usr/bin/env python3
"""Independent exhaustive Cayley S4 calculation; no third-party packages."""
from itertools import permutations,combinations
from collections import defaultdict,Counter,deque
P=list(permutations(range(4)));lab={p:i for i,p in enumerate(P)}
E=set()
for p in P:
    for i in (1,2,3):
        q=list(p);q[0],q[i]=q[i],q[0]
        E.add(tuple(sorted((lab[p],lab[tuple(q)]))))
E=sorted(E);assert len(E)==36
near=[set() for _ in P]
for a,b in E:near[a].add(b);near[b].add(a)
assert len(P)==24 and set(map(len,near))=={3}
assert not any(len(near[a]&near[b])>=2 for a,b in combinations(range(24),2)) # no 4-cycles
M=[]
def walk(remaining,selection):
    if not remaining:
        M.append(tuple(sorted(selection)));return
    v=min(remaining)
    for w in sorted(near[v]&remaining):
        walk(remaining-{v,w},selection+[(min(v,w),max(v,w))])
walk(set(range(len(P))),[])
M.sort();assert len(M)==120 and len(set(M))==120

def flip_length(a,b):
    extra=set(a)^set(b)
    if not extra:return 0
    inc=defaultdict(list)
    for v,w in extra:inc[v].append(w);inc[w].append(v)
    if any(len(x)!=2 for x in inc.values()):raise AssertionError('noncycle union')
    start=next(iter(inc));seen={start};stack=[start]
    while stack:
        for w in inc[stack.pop()]:
            if w not in seen:seen.add(w);stack.append(w)
    return len(extra) if len(seen)==len(inc) else -1
adj6=[set() for _ in M];adj68=[set() for _ in M]
bylength=Counter()
for i,j in combinations(range(len(M)),2):
    n=flip_length(M[i],M[j]);bylength[n]+=1
    if n==6:adj6[i].add(j);adj6[j].add(i)
    if n in (6,8):adj68[i].add(j);adj68[j].add(i)
def graph_info(adj):
    seen=set();size=[]; ecc=Counter();profiles=[]
    for s in range(len(adj)):
        if s in seen:continue
        q=[s];seen.add(s);comp=[]
        while q:
            v=q.pop();comp.append(v)
            for w in adj[v]-seen:seen.add(w);q.append(w)
        size.append(len(comp))
        e=[]
        for v in comp:
            dd={v:0};queue=deque([v])
            while queue:
                x=queue.popleft()
                for y in adj[x]:
                    if y not in dd:dd[y]=dd[x]+1;queue.append(y)
            assert len(dd)==len(comp)
            e.append(max(dd.values()))
        profiles.append((len(comp),min(e),max(e)))
        ecc.update(e)
    return {'edges':sum(map(len,adj))//2,'components':sorted(size,reverse=True),
      'degrees':dict(sorted(Counter(map(len,adj)).items())),
      'radius':min(ecc) if len(size)==1 else None,
      'diameter':max(ecc) if len(size)==1 else None,
      'eccentricities':dict(sorted(ecc.items())) if len(size)==1 else None,
      'profiles':sorted(profiles,reverse=True)}
a=graph_info(adj6);b=graph_info(adj68)
assert a['edges']==192 and a['components']==[57,18,18,18]+[1]*9
assert a['degrees']=={0:9,2:48,4:36,5:24,8:3}
assert b['edges']==606 and b['components']==[120]
assert (b['radius'],b['diameter'])==(4,6)
assert b['eccentricities']=={4:96,5:18,6:6}
print('model=Cayley_S4_star_generators degree=3 vertices=24 edges=36')
print('perfect_matchings=',len(M),'six_cycle_switch_edges=',a['edges'],'eight_cycle_switch_edges=',b['edges']-a['edges'])
print('six=',a)
print('six_or_eight=',b)
print('all_matching_pair_difference_lengths=',dict(sorted(bylength.items())))
print('independent_enumeration=PASSED')
