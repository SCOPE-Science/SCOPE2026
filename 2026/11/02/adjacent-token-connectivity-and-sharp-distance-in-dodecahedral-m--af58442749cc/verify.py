"""Exhaustive finite certificate for minimum decycling-set token reconfiguration of GP(10,2).
Python 3 standard library only: python3 verify.py
"""
from itertools import combinations
from collections import Counter, deque

N=20
E=set()
for i in range(10):
    for x,y in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)):
        E.add(tuple(sorted((x,y))))
assert len(E)==30
adj=[set() for _ in range(N)]
for x,y in E:
    adj[x].add(y);adj[y].add(x)
assert all(len(v)==3 for v in adj)

def is_acyclic_after_removal(S):
    # Union-find: repeated edge cannot close a circuit.
    par=list(range(N))
    def root(x):
        while par[x]!=x:
            par[x]=par[par[x]];x=par[x]
        return x
    for a,b in E:
        if (S>>a)&1 or (S>>b)&1:continue
        ra,rb=root(a),root(b)
        if ra==rb:return False
        par[ra]=rb
    return True

# For a 3-regular graph with 20 vertices and 30 edges, every feedback
# vertex set has size >=ceil((30-19)/2)=6. Checking all 6-sets is exhaustive.
states=sorted(sum(1<<v for v in t) for t in combinations(range(N),6)
              if is_acyclic_after_removal(sum(1<<v for v in t)))
assert len(states)==2520,len(states)
index={S:i for i,S in enumerate(states)}
type_of=[]
for S in states:
    m=sum(((S>>a)&1) and ((S>>b)&1) for a,b in E)
    assert m in (0,1)
    type_of.append(m)
assert Counter(type_of)=={0:660,1:1860}

def exchange(sliding):
    graph=[set() for S in states]
    for i,S in enumerate(states):
        for x in range(N):
            if not (S>>x)&1:continue
            for y in (adj[x] if sliding else range(N)):
                if (S>>y)&1:continue
                T=(S^(1<<x))|(1<<y)
                j=index.get(T)
                if j is not None:
                    graph[i].add(j)
    assert all(i not in graph[i] for i in range(len(states)))
    assert all(i in graph[j] for i,ns in enumerate(graph) for j in ns)
    return graph

def component_sizes(graph,allowed=None):
    allow=set(range(len(graph))) if allowed is None else set(allowed)
    seen=set(); sizes=[]
    for start in allow:
        if start in seen:continue
        seen.add(start);q=[start]
        for i in q:
            for j in graph[i]:
                if j in allow and j not in seen:
                    seen.add(j);q.append(j)
        sizes.append(len(q))
    return sorted(sizes)

def metric(graph):
    hist=Counter()
    for source in range(len(graph)):
        distances=[-1]*len(graph); distances[source]=0
        q=deque([source])
        while q:
            i=q.popleft()
            for j in graph[i]:
                if distances[j]==-1:
                    distances[j]=distances[i]+1;q.append(j)
        assert all(x>=0 for x in distances)
        hist[max(distances)]+=1
    return hist

ts=exchange(True);tj=exchange(False)
assert component_sizes(ts)==[2520]
assert component_sizes(tj)==[2520]
assert component_sizes(ts,[i for i,k in enumerate(type_of) if k==0])==[660]
assert component_sizes(ts,[i for i,k in enumerate(type_of) if k==1])==[1860]
for name,graph,expectededges,expdist in [
    ('SLIDING',ts,8880,{8:120,9:2340,10:60}),
    ('JUMPING',tj,23940,{6:2520})]:
    edges=sum(len(ns) for ns in graph)//2
    assert edges==expectededges,(name,edges)
    ec=Counter()
    for i,ns in enumerate(graph):
        for j in ns:
            if i<j:ec[tuple(sorted((type_of[i],type_of[j])))]+=1
    assert ec==({(0,0):1620,(0,1):3120,(1,1):4140} if name=='SLIDING' else
                {(0,0):3180,(0,1):9600,(1,1):11160})
    h=metric(graph)
    assert h==expdist,(name,h)
    print('%s_OK states=%d edges=%d eccentricities=%s type_edges=%s'%(
        name,len(states),edges,dict(sorted(h.items())),dict(sorted(ec.items()))))
print('GRAPH_OK GP(10,2), n=20, m=30, degree=3')
print('DECVCLING_OK lower_bound=6 minsets=2520, independent=660, one_internal_edge=1860')
print('FINITE_CERTIFICATE_OK')
