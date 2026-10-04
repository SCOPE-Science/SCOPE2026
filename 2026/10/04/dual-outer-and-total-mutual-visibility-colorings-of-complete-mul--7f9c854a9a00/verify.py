from itertools import product
from collections import deque

def build(parts):
    labels=[]
    for i,n in enumerate(parts): labels += [i]*n
    N=len(labels)
    adj=[[False]*N for _ in range(N)]
    for u in range(N):
        for v in range(N):
            adj[u][v]=(u!=v and labels[u]!=labels[v])
    return labels,adj

def distances(adj):
    N=len(adj); D=[[10**9]*N for _ in range(N)]
    for s in range(N):
        D[s][s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v,a in enumerate(adj[u]):
                if a and D[s][v]>D[s][u]+1:
                    D[s][v]=D[s][u]+1; q.append(v)
    return D

def visible(adj,D,M,x,y):
    if x==y: return True
    target=D[x][y]
    q=deque([(x,0)]); seen={(x,0)}
    while q:
        u,d=q.popleft()
        if d>=target: continue
        for v,a in enumerate(adj[u]):
            if not a: continue
            nd=d+1
            if nd>target: continue
            if v==y and nd==target: return True
            if v!=x and v!=y and v in M: continue
            state=(v,nd)
            if state not in seen:
                seen.add(state); q.append(state)
    return False

def is_set(parts,M,kind):
    _,adj=build(parts); D=distances(adj); N=len(adj); M=set(M)
    for x in range(N):
        for y in range(x+1,N):
            if kind=='total': need=True
            elif kind=='outer': need=(x in M or y in M)
            elif kind=='dual': need=((x in M and y in M) or (x not in M and y not in M))
            else: raise ValueError(kind)
            if need and not visible(adj,D,M,x,y): return False
    return True

def chi(parts,kind):
    N=sum(parts)
    for k in range(1,N+1):
        for assignment in product(range(k), repeat=N):
            if set(assignment)!=set(range(k)): continue
            if all(is_set(parts,{v for v,c in enumerate(assignment) if c==j},kind) for j in range(k)):
                return k
    return float('inf')

def predicted(parts,kind):
    r=len(parts); complete=all(n==1 for n in parts)
    if complete: return 1
    if kind=='outer': return 2
    if kind=='dual':
        if r==2 and min(parts)==1 and max(parts)>=3: return float('inf')
        return 2
    if kind=='total':
        if r==2 and min(parts)==1 and max(parts)>=2: return float('inf')
        return 2

profiles=[]
for r in range(2,5):
    for parts in product(range(1,5), repeat=r):
        if tuple(sorted(parts))!=parts: continue
        if sum(parts)>8: continue
        profiles.append(parts)
for parts in profiles:
    for kind in ('outer','dual','total'):
        got=chi(parts,kind); want=predicted(parts,kind)
        if got!=want:
            raise SystemExit(f'FAIL parts={parts} kind={kind} got={got} want={want}')
print(f'ALL CHECKS PASSED; profiles={len(profiles)}; parameter_cases={3*len(profiles)}; max_order=8')
