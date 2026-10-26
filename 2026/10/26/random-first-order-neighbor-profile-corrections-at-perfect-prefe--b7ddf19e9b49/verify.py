from fractions import Fraction as F
from itertools import product
checks=0
for m,K,C,i0 in product((2,4),range(1,8),range(1,8),(0,1)):
 if C>K or (i0 and C<1) or (not i0 and C==K):continue
 a=F(2,5); b=1-a*i0
 q0=b*F(C,K)
 for nums in product(range(K-C+1), repeat=m-1):
  if sum(nums)>K-C:continue
  ns=list(nums)+[K-C-sum(nums)]
  for j in range(m):
   D=F(ns[j],1)-F(K-C,m)
   R=D/C
   probs=[b*F(x,K)+a*i0/F(m) for x in ns]
   assert sum(probs)+q0==1
   # conditional expectation of ratio after next step
   er=q0*D/(C+1)+sum(p*(D+F(int(k==j),1)-F(1,m))/C for k,p in enumerate(probs))
   assert er==R*(1+b/F(K*(C+1)))
   checks+=1
print('EXACT_CONDITIONAL_IDENTITIES_OK',checks)
