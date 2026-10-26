"""Exact finite verification of fixed-size subset span/adjacency laws."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import comb
checks=0
for n in range(3,13):
 for k in range(2,n):
  counts={r:Counter() for r in range(k-1,n)}
  for s in combinations(range(1,n+1),k):
   r=s[-1]-s[0]
   a=sum(s[i+1]-s[i]==1 for i in range(k-1))
   counts[r][a]+=1
  for r in range(k-1,n):
   z=r+1-k
   tot=sum(counts[r].values())
   assert tot==(n-r)*comb(r-1,k-2)
   checks+=1
   for a in range(k):
    h=k-a
    if z==0: expected=1 if a==k-1 else 0
    else: expected= (comb(k-1,h-1)*comb(z-1,h-2) if 1<=h<=k and 2<=h<=z+1 else 0)
    assert counts[r][a]==(n-r)*expected,(n,k,r,a,counts[r][a],expected)
    checks+=1
   ea=Fraction(sum(a*v for a,v in counts[r].items()),tot)
   expected=Fraction((k-1)*(k-2),r-1) if k>=3 else int(r==1)
   assert ea==expected,(n,k,r,ea,expected)
   checks+=1
   if r<n-1:
    nxt=counts[r+1]; nt=sum(nxt.values())
    for cut in range(k):
     p=sum(v for a,v in counts[r].items() if a>=cut)
     pn=sum(v for a,v in nxt.items() if a>=cut)
     assert Fraction(p,tot)>=Fraction(pn,nt)
     checks+=1
  ex=lambda var: Fraction(sum((s[-1]-s[0] if var=='r' else sum(s[i+1]-s[i]==1 for i in range(k-1))) for s in combinations(range(1,n+1),k)),comb(n,k))
  er=ex('r');ea=ex('a')
  era=Fraction(sum((s[-1]-s[0])*sum(s[i+1]-s[i]==1 for i in range(k-1)) for s in combinations(range(1,n+1),k)),comb(n,k))
  assert era-er*ea<0
  checks+=1
print('PASS',checks,'exact assertions; all subsets n<=12')
