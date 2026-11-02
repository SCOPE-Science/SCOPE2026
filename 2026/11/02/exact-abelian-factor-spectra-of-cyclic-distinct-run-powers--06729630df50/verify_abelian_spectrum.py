from itertools import product
from collections import Counter

def direct(lens,k):
 q=len(lens)
 p=sum(lens)
 P=sum(([j]*lens[j] for j in range(q)),[])
 W=P*k
 profiles=[]
 for L in range(1,len(W)+1):
  cs=[0]*q
  for x in W[:L]:cs[x]+=1
  ss={tuple(cs)}
  for start in range(len(W)-L):
   cs[W[start]]-=1;cs[W[start+L]]+=1
   ss.add(tuple(cs))
  profiles.append(len(ss))
 return profiles

def formula(lens,k):
 p=sum(lens);S=sum(x*y for i,x in enumerate(lens) for y in lens[i+1:]);out=[]
 for L in range(1,k*p+1):
  if L<=(k-1)*p:
   h=L%p
   v=1 if h==0 else p-sum(max(0,r-h)+max(0,r-(p-h)) for r in lens)
  else:
   h=L-(k-1)*p
   v=p-h+1-sum(max(0,r-h) for r in lens)
  out.append(v)
 assert sum(out)==p+S+(k-1)*(1+2*S)
 return out

checked=0; prof=0
for q,maxr,kmax in [(3,6,5),(4,4,4),(5,3,3),(6,2,3)]:
 for lens in product(range(1,maxr+1),repeat=q):
  for k in range(1,kmax+1):
   actual=direct(lens,k);exp=formula(lens,k)
   assert actual==exp, (q,lens,k,actual,exp)
   checked+=1;prof+=len(actual)
 print('verified q=',q,'cases so far',checked,'lengths',prof)
print(f'VERIFY_OK cases={checked} length_profiles={prof} q=3..6 exact_P_profiles=True circular_Hamming_formula=True total_formula=True')
