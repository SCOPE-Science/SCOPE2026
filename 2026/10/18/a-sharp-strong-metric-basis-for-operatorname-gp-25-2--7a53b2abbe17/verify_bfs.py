"""Independent breadth-first exact check of the GP(25,2) strong metric dimension certificate."""
import collections
import json

n=25
N=2*n
adj=[set() for _ in range(N)]
def add(a,b):
    adj[a].add(b);adj[b].add(a)
for i in range(n):
    add(i,(i+1)%n)
    add(i,n+i)
    add(n+i,n+(i+2)%n)
assert all(len(z)==3 for z in adj)
dist=[]
for a in range(N):
    row=[-1]*N;row[a]=0
    q=collections.deque([a])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if row[v]<0:
                row[v]=row[u]+1;q.append(v)
    assert -1 not in row
    dist.append(row)
U=[dist[0][d] for d in range(13)]
UV=[dist[0][n+d] for d in range(13)]
V=[dist[n][n+d] for d in range(13)]
MMD=set()
for x in range(N):
 for y in range(x+1,N):
    if all(dist[w][y]<=dist[x][y] for w in adj[x]) and all(dist[x][w]<=dist[x][y] for w in adj[y]):
        MMD.add((x,y))
outer={5,7,9,11,12};inner={9,11}
expected=set()
for layer,steps in ((0,outer),(n,inner)):
  for i in range(n):
    for d in steps:
      a=layer+i;b=layer+(i+d)%n
      expected.add(tuple(sorted((a,b))))
assert MMD==expected, (len(MMD),len(expected),MMD^expected)
IU={0,2,4,6,8,10}
IV={0,2,5,7,10,12,15,17,20,22}
I=IU|{n+i for i in IV}
assert len(I)==16 and not any(a in I and b in I for a,b in MMD)
S=set(range(N))-I
assert len(S)==34
for x in range(N):
 for y in range(x+1,N):
    assert any(dist[s][x]==dist[s][y]+dist[x][y] or dist[s][y]==dist[s][x]+dist[x][y] for s in S),(x,y)
print(json.dumps({'n':n,'vertices':N,'graph_edges':sum(map(len,adj))//2,'distance_UU':U,'distance_UV':UV,'distance_VV':V,'MMD_edges':len(MMD),'MMD_outer_edges':len([1 for a,b in MMD if b<n]),'MMD_inner_edges':len([1 for a,b in MMD if a>=n]),'independent_outer':sorted(IU),'independent_inner':sorted(IV),'independent_total':len(I),'strong_resolving_size':len(S),'strong_resolution_pairs_checked':N*(N-1)//2},sort_keys=True))
