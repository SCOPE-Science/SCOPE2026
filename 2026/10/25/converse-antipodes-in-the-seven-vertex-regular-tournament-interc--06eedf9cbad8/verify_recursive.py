"""Second exact checker: construct balanced tournaments recursively and BFS every state.
Representation is oriented adjacency rows, independent of bit-mask enumeration.
Python 3.10+; no third-party dependencies.
"""
from collections import Counter,defaultdict,deque
from itertools import combinations

N=7

def generate(rows,at):
    if at==N:
        if all(r.bit_count()==3 for r in rows): yield tuple(rows)
        return
    known=rows[at].bit_count()
    later=list(range(at+1,N))
    needed=3-known
    if not (0 <= needed <= len(later)):return
    for won in combinations(later,needed):
        won=set(won)
        new=rows.copy()
        for j in later:
            if j in won:new[at] |= (1<<j)
            else:new[j] |= (1<<at)
        if all(new[j].bit_count()<=3 for j in range(N)):
            yield from generate(new,at+1)

T=list(generate([0]*N,0)); assert len(T)==2640 and len(set(T))==2640
V={x:i for i,x in enumerate(T)}

# Directed-triangle reversal directly on rows, without an edge-index encoding.
def neighbours(rows):
    for i,j,k in combinations(range(N),3):
        if rows[i]&(1<<j) and rows[j]&(1<<k) and rows[k]&(1<<i):
            x=list(rows)
            for u,v in ((i,j),(j,k),(k,i)):
                x[u]^=1<<v; x[v]^=1<<u
            yield tuple(x)
        elif rows[j]&(1<<i) and rows[k]&(1<<j) and rows[i]&(1<<k):
            x=list(rows)
            for u,v in ((j,i),(k,j),(i,k)):
                x[u]^=1<<v; x[v]^=1<<u
            yield tuple(x)

G=[]
for x in T:
    y=list(neighbours(x))
    assert len(y)==14 and len(set(y))==14
    G.append([V[z] for z in y])
assert sum(map(len,G))//2==18480

ALL = (1<<N)-1
classes=defaultdict(lambda:[0,None,0,0]); maximal_pairs=set()
for r,t in enumerate(T):
    ds=[-1]*len(T);ds[r]=0;queue=deque([r])
    while queue:
        u=queue.popleft()
        for v in G[u]:
            if ds[v]==-1:ds[v]=ds[u]+1;queue.append(v)
    assert -1 not in ds
    ecc=max(ds)
    shell=tuple(Counter(ds).get(k,0) for k in range(ecc+1))
    classes[shell][0]+=1
    opposite=tuple(ALL ^ (1<<i) ^ t[i] for i in range(N))
    od=ds[V[opposite]]
    if classes[shell][1] is None:classes[shell][1]=od
    assert classes[shell][1]==od
    far=sum(v==ecc for v in ds)
    if classes[shell][2]==0:classes[shell][2]=far
    assert classes[shell][2]==far
    if ecc==9:
        assert far==1 and ds[V[opposite]]==9
        maximal_pairs.add(tuple(sorted((r,V[opposite]))))
    classes[shell][3]+=far
expected={
(1,14,91,336,721,822,485,147,22,1):(720,9,1,720),
(1,14,91,340,739,853,483,113,6):(1680,7,6,10080),
(1,14,91,343,749,871,476,92,3):(240,7,3,720)}
assert {k:tuple(v) for k,v in classes.items()}==expected
assert len(maximal_pairs)==360
print('recursive_vertices=2640 undirected_edges=18480 components=1 radius=8 diameter=9')
print('distance_9_unordered_pairs=360 all_are_converse_tournaments')
for shell,v in sorted(classes.items(),key=lambda e:e[1][0]): print('count=',v[0],'converse_distance=',v[1],'farthest_count=',v[2],'shell=',shell)
print('PASS')
