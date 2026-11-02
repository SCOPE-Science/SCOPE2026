#!/usr/bin/env python3
"""Exact 12-spin icosahedral Ising two-range phase certificate (stdlib only)."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product

EDGES=((0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),
       (2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),
       (4,5),(4,6),(4,10),(4,11),(5,6),(5,11),(7,8),
       (7,9),(7,10),(7,11),(8,9),(9,10),(10,11))
N=12
adj=[set() for _ in range(N)]
for a,b in EDGES: adj[a].add(b);adj[b].add(a)
assert len(EDGES)==30 and all(len(a)==5 for a in adj)
# Distance layers computed by elementary graph search, independently of other packages.
dist=[]
for v in range(N):
 dd=[-1]*N;dd[v]=0;front=[v]
 while front:
  nxt=[]
  for u in front:
   for w in adj[u]:
    if dd[w]==-1:dd[w]=dd[u]+1;nxt.append(w)
  front=nxt
 dist.append(dd)
E={d:tuple((a,b) for a in range(N) for b in range(a+1,N) if dist[a][b]==d) for d in (1,2,3)}
assert [len(E[d]) for d in (1,2,3)]==[30,30,6]
assert set(E[1])==set(EDGES)
PAIRS=tuple(E[3]);assert len({v for e in PAIRS for v in e})==N
# Signed conference matrix on antipodal pairs: each pair of pairs has two bonds
# of each distance (1 and 2), with the two bonds forming a matching.
eta={}
for i,j in combinations(range(6),2):
 a,b=PAIRS[i];c,d=PAIRS[j]
 assert sorted(dist[x][y] for x in (a,b) for y in (c,d))==[1,1,2,2]
 assert dist[a][c]==dist[b][d] and dist[a][d]==dist[b][c]
 eta[i,j]=1 if dist[a][c]==1 else -1

def signed_cut(subset,signs):
 return sum(eta[i,j]*signs[a]*signs[b]
            for a,i in enumerate(subset) for b,j in enumerate(subset) if a<b)

extrema=[];cnt_minus=[];cnt_plus=[]
for q in range(7):
 values=[]
 for inds in combinations(range(6),q):
  vs=[signed_cut(inds,z) for z in product((-1,1),repeat=q)]
  values.extend(vs)
  if q==4: assert vs.count(-4)==2 and vs.count(4)==2
 mn,mx=min(values),max(values)
 extrema.append((mn,mx))
 cnt_minus.append(values.count(mn));cnt_plus.append(values.count(mx))
assert extrema==[(0,0),(0,0),(-1,1),(-3,3),(-4,4),(-4,4),(-5,5)]
assert cnt_minus[4]==cnt_plus[4]==30 and cnt_minus[6]==cnt_plus[6]==12

profile=Counter();by_energy={}
for mask in range(1<<N):
 spin=[1 if (mask>>i)&1 else -1 for i in range(N)]
 s1=sum(spin[a]*spin[b] for a,b in E[1])
 s2=sum(spin[a]*spin[b] for a,b in E[2])
 s3=sum(spin[a]*spin[b] for a,b in E[3])
 profile[(s1,s2,s3,sum(spin))]+=1
 sm=[spin[a]+spin[b] for a,b in PAIRS]
 dif=[spin[a]-spin[b] for a,b in PAIRS]
 u=sum(sm[i]*sm[j] for i,j in combinations(range(6),2))
 v=sum(eta[i,j]*dif[i]*dif[j] for i,j in combinations(range(6),2))
 assert s1+s2==u and s1-s2==v
assert sum(profile.values())==4096
pairs=Counter()
for (s1,s2,s3,m), count in profile.items():pairs[s1,s2]+=count
assert min(a for a,b in pairs)==-10
assert min(b for a,b in pairs)==-10
assert min(3*a+b for a,b in pairs)==-24
assert min(a+3*b for a,b in pairs)==-24

def check_ratio(r, energy, degeneracy, allowed):
 score=min(Fraction(a)+r*Fraction(b) for a,b in pairs)
 winners={ (a,b) for a,b in pairs if a+r*b==score}
 assert score==energy and sum(pairs[k] for k in winners)==degeneracy
 assert winners==allowed,(r,score,winners)

L={(-10,6)};M={(-6,-6)};R={(6,-10)}
check_ratio(Fraction(1,9), Fraction(-10)+Fraction(6,9),60,L)
check_ratio(Fraction(1,3),Fraction(-8),80,L|M)
check_ratio(Fraction(1,1),Fraction(-12),20,M)
check_ratio(Fraction(3,1),Fraction(-24),80,M|R)
check_ratio(Fraction(10,1),Fraction(-94),60,R)
check_ratio(Fraction(0,1),Fraction(-10),72,L|{(-10,10)})
assert pairs[(-10,6)]==60 and pairs[(-6,-6)]==20 and pairs[(6,-10)]==60
assert pairs[(-10,10)]==12 and pairs[(10,-10)]==12
# Both transitions have no intermediate-energy support point.
for a,b in pairs:
 assert a>=-10 and b>=-10 and 3*a+b>=-24 and a+3*b>=-24
# Check antipodal-spin description of every proposed ground state.
for mask in range(1<<N):
 sp=[1 if mask>>i&1 else -1 for i in range(N)]
 a=sum(sp[x]*sp[y] for x,y in E[1]);b=sum(sp[x]*sp[y] for x,y in E[2]);
 p=sum(sp[x]==sp[y] for x,y in PAIRS)
 assert ((a,b)==(-6,-6))==(p==6 and sum(sp)==0)
 if (a,b) in (L|R):assert p==2 and sum(sp)==0
print('CERTIFIED: 4096 states; 6-pair conference extrema; thresholds 1/3,3; ground degeneracies 60,80,20,80,60; no floating point.')
