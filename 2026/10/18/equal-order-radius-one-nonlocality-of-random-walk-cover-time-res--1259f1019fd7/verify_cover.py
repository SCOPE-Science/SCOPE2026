"""Exact rational finite-state verifier for fixed-start cover-time edge response in two trees."""
from fractions import Fraction as Q
from collections import deque
import sys,time
EDGES_A=[(0,3),(1,6),(2,3),(3,9),(4,5),(4,9),(5,7),(5,8),(6,9),(9,10)]
EDGES_B=[(0,2),(0,6),(1,6),(2,3),(2,9),(2,10),(3,5),(3,8),(4,10),(7,8)]
S_U_V_A=(1,10,0)
S_U_V_B=(4,9,5)

def mat_solve(a,b):
 n=len(b)
 for k in range(n):
  pivot=next(i for i in range(k,n) if a[i][k]);a[k],a[pivot]=a[pivot],a[k];b[k],b[pivot]=b[pivot],b[k]
  pk=a[k][k]
  for j in range(k+1,n):a[k][j]/=pk
  b[k]/=pk;a[k][k]=Q(1)
  for i in range(k+1,n):
   fac=a[i][k]
   if fac:
    for j in range(k+1,n):a[i][j]-=fac*a[k][j]
    b[i]-=fac*b[k]
    a[i][k]=Q(0)
 for k in range(n-1,-1,-1):
  for i in range(k):
   b[i]-=a[i][k]*b[k];a[i][k]=Q(0)
 return b

def cover_time(edges,start,n=11):
 adj=[[] for i in range(n)]
 for u,v in edges:adj[u].append(v);adj[v].append(u)
 assert all(adj)
 deg=list(map(len,adj))
 full=(1<<n)-1
 F={full:{v:Q(0) for v in range(n)}}
 for mask in range(full-1,0,-1):
  if not(mask>>start&1):continue
  V=[v for v in range(n) if mask>>v&1];k=len(V);ind={v:i for i,v in enumerate(V)}
  a=[[Q(0)]*k for _ in V]; b=[Q(0)]*k
  for i,v in enumerate(V):
   a[i][i]=Q(deg[v]);b[i]=Q(deg[v])
   for w in adj[v]:
    if mask>>w&1:a[i][ind[w]]-=Q(1)
    else:b[i]+=F[mask|(1<<w)][w]
  result=mat_solve(a,b)
  F[mask]={v:result[ind[v]] for v in V}
 return F[1<<start][start]

def bfs(edges,origin,n=11):
 a=[[] for _ in range(n)]
 for x,y in edges:a[x].append(y);a[y].append(x)
 ds={origin:0};q=deque([origin])
 while q:
  x=q.popleft()
  for y in a[x]:
   if y not in ds:ds[y]=ds[x]+1;q.append(y)
 assert len(ds)==n
 return ds

def invariants(edges,markers):
 s,u,v=markers
 a=[[] for _ in range(11)]
 for x,y in edges:a[x].append(y);a[y].append(x)
 dist={z:bfs(edges,z) for z in markers}
 assert len(edges)==10
 return {'order':11,'degrees':tuple(map(lambda z:len(a[z]),markers)), 'pair_distances':(dist[s][u],dist[s][v],dist[u][v]), 'radius_one_degree_balls':tuple((len(a[z]),tuple(sorted(len(a[w]) for w in a[z]))) for z in markers)}

def cover_hit_ie(edges,start,n=11):
    """Separate inclusion-exclusion computation via first hitting times."""
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    deg=[len(a) for a in adj]
    other=[v for v in range(n) if v!=start]
    total=Q(0)
    for mask in range(1,1<<(n-1)):
        target={other[i] for i in range(n-1) if (mask>>i)&1}
        rest=[v for v in range(n) if v not in target]
        at={v:i for i,v in enumerate(rest)}
        a=[[Q(0)]*len(rest) for _ in rest]; b=[Q(0)]*len(rest)
        for i,v in enumerate(rest):
            a[i][i]=Q(deg[v]); b[i]=Q(deg[v])
            for w in adj[v]:
                if w not in target:a[i][at[w]]-=1
        hit=mat_solve(a,b)[at[start]]
        total+=hit if (mask.bit_count()%2) else -hit
    return total

EXPECTED={
    'A':(Q(1409284291,16327080),Q(16056931351603,189157385340),Q(-1162717427,813580152)),
    'B':(Q(3046636,33495),Q(1722497083,18929460),Q(3127,83076)),
}

def verify():
    inv=[]
    for name,edges,marks in [('A',EDGES_A,S_U_V_A),('B',EDGES_B,S_U_V_B)]:
        n=11;s,u,v=marks
        assert len(edges)==10 and len({tuple(sorted(e)) for e in edges})==10
        assert tuple(sorted((u,v))) not in {tuple(sorted(e)) for e in edges}
        obj=invariants(edges,marks)
        inv.append(obj)
        assert obj['order']==11
        assert obj['degrees']==(1,1,1)
        assert obj['pair_distances']==(3,4,3)
        assert obj['radius_one_degree_balls']==((1,(2,)),(1,(4,)),(1,(3,)))
        before=cover_time(edges,s);after=cover_time(edges+[(u,v)],s)
        assert (before,after,after-before)==EXPECTED[name]
        assert (cover_hit_ie(edges,s),cover_hit_ie(edges+[(u,v)],s))==(before,after)
        assert (after-before<0) if name=='A' else (after-before>0)
        print(name,'cover_before=',before,'cover_after=',after,'change=',after-before)
    assert inv[0]==inv[1]
    print('VERIFY_OK: two independent exact rational cover-time methods agree')

if __name__=='__main__':verify()
