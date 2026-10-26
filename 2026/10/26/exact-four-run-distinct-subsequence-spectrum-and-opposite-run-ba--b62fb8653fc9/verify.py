#!/usr/bin/env python3
"""Check four-run distinct-subsequence counting and conditional maxima."""
from itertools import product

def formula(a,b,c,d):
 n=a+b+c+d
 return n+(a+c)*(b+d)+b*c*(a+d)+a*b*c*d

def independent_count(w):
 # Number including empty obtained from classic last-occurrence recurrence.
 dp=[1]
 previous={}
 for pos,ch in enumerate(w):
  z=2*dp[-1]
  if ch in previous:
   z-=dp[previous[ch]]
  dp.append(z)
  previous[ch]=pos
 return dp[-1]-1

def phi(n,p):
 q=n-p
 H16=16*n+4*n*n+p*q*q*(p+4)
 if p%2==0 and q%2==0:D16=0
 elif p%2==1 and q%2==1:D16=p*p+q*q+4*p-1
 elif p%2==0:D16=(p+2)**2
 else:D16=q*q+4
 val=H16-D16
 assert val%16==0
 return val//16

count=0
for a,b,c,d in product(range(1,10),repeat=4):
 w='0'*a+'1'*b+'0'*c+'1'*d
 assert formula(a,b,c,d)==independent_count(w),(a,b,c,d)
 count+=1
for n in range(4,49):
 byp={}
 for p in range(2,n-1):
  q=n-p
  best=-1; winners=[]
  for a in range(1,p):
   d=p-a
   for b in range(1,q):
    c=q-b
    value=formula(a,b,c,d)
    if value>best:best=value;winners=[(a,b,c,d)]
    elif value==best:winners.append((a,b,c,d))
  assert best==phi(n,p),(n,p,best,phi(n,p))
  assert all(abs(a-d)<=1 and abs(b-c)<=1 and (p%2==0 or q%2==0 or (a-d)*(b-c)>0) for a,b,c,d in winners)
  byp[p]=best
 assert max(byp.values())==max(phi(n,p) for p in range(2,n-1))
print('VERIFY_OK parameter_grid=6561 lengths=4..48 conditional_maxima=checked')
