"""Independent total-domination/reconfiguration census from an LCF model.

The 20-cycle and LCF shifts [10,7,4,-4,-7,10,-4,7,-7,4]^2
represent the ordinary dodecahedral graph. Python standard library only.
"""
from collections import Counter, deque
import json
N=20
shift=(10,7,4,-4,-7,10,-4,7,-7,4)*2
adj=[set() for _ in range(N)]
for i in range(N):
    for j in ((i+1)%N, (i+shift[i])%N):
        adj[i].add(j)
        adj[j].add(i)
assert all(len(nei)==3 for nei in adj)
assert sum(map(len,adj))//2==30

# Full 2^20-set scan, with open-neighborhood tests (not coverage OR).
# Only sets of size at most eight can improve or tie the claimed optimum.
best=[]
min_k=N+1
for m in range(1<<N):
    size=m.bit_count()
    if size>8:continue
    if all(any(m&(1<<j) for j in adj[i]) for i in range(N)):
        if size<min_k:min_k=size;best=[]
        if size==min_k:best.append(m)
assert min_k==8 and len(best)==190
index={m:i for i,m in enumerate(best)}
# Compute all unordered exchanges by scanning each pair of states;
# no transformation from the first checker is reused.
J=[set() for _ in best]
S=[set() for _ in best]
for i,a in enumerate(best):
    for j in range(i+1,len(best)):
        b=best[j]
        removed=a&~b
        added=b&~a
        if removed.bit_count()==1 and added.bit_count()==1:
            J[i].add(j);J[j].add(i)
            v=removed.bit_length()-1
            w=added.bit_length()-1
            if w in adj[v]:S[i].add(j);S[j].add(i)
assert sum(map(len,J))//2==360
assert not any(S)
assert Counter(map(len,J))==Counter({0:40,4:120,8:30})

def cc(graph, verts):
    todo=set(verts);out=[]
    while todo:
        a=min(todo);todo.remove(a);C={a};stack=[a]
        while stack:
            v=stack.pop()
            for w in graph[v]:
                if w in todo:todo.remove(w);C.add(w);stack.append(w)
        out.append(C)
    return out
all_components=cc(J,range(190))
assert Counter(map(len,all_components))==Counter({1:40,150:1})
big=next(x for x in all_components if len(x)==150)
maxdist=[]
for v in big:
    q=deque([v]);dist={v:0}
    while q:
        a=q.popleft()
        for b in J[a]:
            if b not in dist:dist[b]=dist[a]+1;q.append(b)
    assert len(dist)==150
    maxdist.append(max(dist.values()))
assert len(set(maxdist))==1 and maxdist[0]==10

low={v for v in big if len(J[v])==4}
lowadj=[J[v]&low for v in range(190)]
hexes=cc(lowadj,low)
assert len(hexes)==20 and all(len(H)==6 for H in hexes)
assert all(len(lowadj[v])==2 for v in low)
which={v:k for k,H in enumerate(hexes) for v in H}
quot=[set() for _ in range(20)]
hubs=[v for v in big if len(J[v])==8]
for h in hubs:
    incidences=Counter(which[v] for v in J[h])
    assert sorted(incidences.values())==[4,4]
    x,y=incidences
    quot[x].add(y);quot[y].add(x)
assert len(hubs)==30 and sum(map(len,quot))//2==30

# Direct exact graph-isomorphism search to GP(10,3), not a preloaded mapping.
ref=[set() for _ in range(20)]
for i in range(10):
    for a,b in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+3)%10)):
        ref[a].add(b);ref[b].add(a)
assert all(len(z)==3 for z in ref)

def find_iso(Q,T):
    n=len(Q);assigned={};used=set()
    def go():
        if len(assigned)==n:return assigned.copy()
        remain=[v for v in range(n) if v not in assigned]
        v=max(remain,key=lambda x:len(Q[x]&assigned.keys()))
        for w in range(n):
            if w in used or len(T[w])!=len(Q[v]):continue
            if any((u in Q[v])!=(assigned[u] in T[w]) for u in assigned):continue
            assigned[v]=w;used.add(w)
            r=go()
            if r is not None:return r
            used.remove(w);del assigned[v]
        return None
    return go()

mapping=find_iso(quot,ref)
assert mapping is not None and len(mapping)==20
assert all({mapping[v] for v in quot[u]}==ref[mapping[u]] for u in range(20))
report={'model':'LCF [10,7,4,-4,-7,10,-4,7,-7,4]^2',
 'total_domination_number':min_k,'minimum_total_domination_sets':len(best),
 'slide_edges':sum(map(len,S))//2,'jump_edges':sum(map(len,J))//2,
 'jump_degree_histogram':dict(sorted(Counter(map(len,J)).items())),
 'jump_component_size_histogram':dict(sorted(Counter(map(len,all_components)).items())),
 'nontrivial_component_radius':min(maxdist),'nontrivial_component_diameter':max(maxdist),
 'six_cycle_count':len(hexes),'hub_count':len(hubs),'quotient_isomorphic_to':'GP(10,3) = Desargues graph',
 'isomorphism_mapping': [mapping[i] for i in range(20)]}
print(json.dumps(report,sort_keys=True))
