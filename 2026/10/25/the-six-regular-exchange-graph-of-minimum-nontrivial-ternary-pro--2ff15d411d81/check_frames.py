"""Independent incidence-dual checker using four-line projective frames.
Builds the exchange edges by pair intersections rather than six-subset swaps.
Requires only Python 3 standard library.
"""
from itertools import product,combinations
from collections import Counter,deque

vectors=[]
for i in product(range(3),repeat=3):
    if i==(0,0,0):continue
    for k in range(3):
        if i[k]:
            if i[k]==1:vectors.append(i)
            break
V=sorted(vectors)
assert len(V)==13
L=[]
for a,b,c in V:
    L.append(frozenset(j for j,(x,y,z) in enumerate(V) if (a*x+b*y+c*z)%3==0))
assert len({tuple(sorted(x)) for x in L})==13

F={}
for ids in combinations(range(13),4):
    if any(len(L[i]&L[j]&L[k]) for i,j,k in combinations(ids,3)):
        continue
    meets=frozenset(next(iter(L[i]&L[j])) for i,j in combinations(ids,2))
    assert len(meets)==6
    assert meets not in F
    F[meets]=ids
assert len(F)==234
assert all(all(B&line for line in L) and not any(line<=B for line in L) for B in F)
S=sorted(F,key=lambda B:tuple(sorted(B)))
A=[set() for _ in S]
for i in range(len(S)):
    for j in range(i+1,len(S)):
        if len(S[i]&S[j])==5:
            A[i].add(j);A[j].add(i)
assert all(len(n)==6 for n in A)
assert sum(map(len,A))==1404
assert Counter(len(set(F[S[i]])&set(F[S[j]])) for i in range(len(S)) for j in A[i] if i<j)=={2:702}

def bfs(i):
    d=[-1]*len(S);d[i]=0; queue=deque([i])
    while queue:
        x=queue.popleft()
        for y in A[x]:
            if d[y]<0:d[y]=d[x]+1;queue.append(y)
    return d

hists={tuple(Counter(bfs(i)).get(k,0) for k in range(7)) for i in range(len(S))}
assert hists=={(1,6,24,72,116,12,3)}
# Exact frame total from PGL(3,3) orbit size = 5616/24.
assert (27-1)*(27-3)*(27-9)//(2*24)==len(F)
print('FRAME_CHECK_PASS')
print('frames',len(F),'frame_graph_edges',sum(map(len,A))//2)
print('each_exchange_preserves_two_frame_lines',True)
print('distance_layers',(1,6,24,72,116,12,3),'diameter',6)
print('PGL_order',5616,'frame_stabilizer',24)
