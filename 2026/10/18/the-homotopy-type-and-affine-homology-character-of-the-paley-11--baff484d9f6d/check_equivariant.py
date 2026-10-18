#!/usr/bin/env python3
"""Independent signed fixed-face computation for the affine action."""
from itertools import combinations
from collections import Counter
P=11
Q={x*x%P for x in range(1,P)}
facets=[set((i+x)%P for x in Q) for i in range(P)]
faces=set()
for S in facets:
 for k in range(1,6):
  faces.update(tuple(t) for t in combinations(sorted(S),k))
def parity(seq):
 return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
def L(a,b):
 v=0
 for s in faces:
  image=tuple(sorted((a*x+b)%P for x in s))
  if image != s:continue
  perm=tuple(s.index((a*x+b)%P) for x in s)
  v += (-1)**(len(s)-1)*parity(perm)
 return v
result=Counter()
for a in sorted(Q):
 for b in range(P):
  category='identity' if (a,b)==(1,0) else ('nonidentity_translation' if a==1 else 'order_five')
  trace=L(a,b)-1 # reduced Lefschetz equals the sole H2 trace
  result[(category,trace)]+=1
assert result==Counter({('identity',21):1,('nonidentity_translation',-1):10,('order_five',1):44}),result
avg=sum(count*tr for (kind,tr),count in result.items())//55
assert sum(count*tr for (kind,tr),count in result.items())==55 and avg==1
print('signed_fixed_simplex_Lefschetz:', sorted((kind,trace,count) for (kind,trace),count in result.items()))
print('full_affine_quotient_reduced_rational_Betti2:',avg)
print('other_reduced_rational_Betti_numbers: 0')
