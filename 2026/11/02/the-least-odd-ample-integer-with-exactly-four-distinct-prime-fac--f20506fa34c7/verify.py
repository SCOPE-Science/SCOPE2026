from itertools import product
from math import prod
P=(3,5,7,11); N=3**11*5**5*7**3*11**2
lim=[]
for p in P:
 t=N//prod(x for x in P if x!=p);a=0
 while p**(a+1)<=t:a+=1
 lim.append(a)
assert lim==[22,15,13,10],lim
D={}; κ={};count=0;best=None
for a in range(lim[0]+1):
 for b in range(lim[1]+1):
  for c in range(lim[2]+1):
   for d in range(lim[3]+1):
    E=(a,b,c,d);q=0
    for mask in range(1,16):
     E2=tuple(E[j]-((mask>>j)&1) for j in range(4))
     if min(E2)>=0:q+= (1 if mask.bit_count()%2 else -1)*D[E2]
    κ[E]=q+1;D[E]=2*q+1
    if min(E)>0:
     n=3**a*5**b*7**c*11**d
     if n<=N:
      count+=1
      if κ[E]>n:
       if best is None or n<best[0]:best=(n,E,κ[E])
assert best==(22975412315625,(11,5,3,2),24786437787648),best
assert count==2757,count
# independent proper-subdivisor recursion for every subtuple of minimizer
cache={}
for e0 in range(12):
 for e1 in range(6):
  for e2 in range(4):
   for e3 in range(3):
    E=(e0,e1,e2,e3)
    val=1+sum(cache[es] for es in product(*(range(x+1) for x in E)) if es!=E)
    cache[E]=val
    assert val==κ[E],(E,val,κ[E])
assert len(cache)==864
print('VERIFY_OK candidate_tuples=2757 direct_subvectors=864')
