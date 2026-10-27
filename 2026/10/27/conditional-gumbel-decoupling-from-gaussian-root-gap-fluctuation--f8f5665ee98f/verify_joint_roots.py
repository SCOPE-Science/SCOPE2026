"""Exact finite checks for conditional late-root decoupling in cyclic deposition.
This is supporting finite arithmetic, not a proof of asymptotic convergence.
Python 3 standard library only.
"""
from itertools import permutations, product
from fractions import Fraction as F
from math import factorial

checks=0
# Five consecutive clocks: simultaneous strict valleys at positions 1 and 3.
num=sum(1 for r in permutations(range(5)) if r[1]<r[0] and r[1]<r[2] and r[3]<r[2] and r[3]<r[4])
assert num==16 and F(num,factorial(5))==F(2,15)
checks+=1

# Cyclic root count: exact means and variances, for all permutations through K=8.
for k in range(5,9):
  hist={}
  for r in permutations(range(k)):
    roots=tuple(j for j in range(k) if r[j]<r[(j-1)%k] and r[j]<r[(j+1)%k])
    z=len(roots)
    hist[z]=hist.get(z,0)+1
  total=factorial(k)
  mean=sum(F(z*h,total) for z,h in hist.items())
  var=sum(F((z*z)*h,total) for z,h in hist.items())-mean*mean
  assert mean==F(k,3),(k,mean)
  assert var==F(2*k,45),(k,var)
  checks+=2

# Exact Bernoulli-survival three-site block count S, for K=7,8.
# This verifies the conditional Poisson parameter's variance formula.
for k in (7,8):
 for p in (F(1,2),F(1,3)):
  es=es2=F(0)
  for flags in product([0,1],repeat=k):
    z=sum(flags[j-1]*flags[j]*flags[(j+1)%k] for j in range(k))
    q=p**sum(flags)*(1-p)**(k-sum(flags))
    es+=q*z
    es2+=q*z*z
  proposed=k*(p**3-p**6)+2*k*((p**4-p**6)+(p**5-p**6))
  assert es==k*p**3 and es2-es*es==proposed,(k,p,es,es2)
  checks+=2

# Inserting a late root changes the count of any fixed gap length by <=2.
def gap_count(R,k,d):
  if len(R)<=1:
    return 0
  a=sorted(R)
  return sum((a[(j+1)%len(a)]-a[j])%k==d for j in range(len(a)))
for k in (5,6,7):
 for mask in product((0,1),repeat=k):
  old={j for j in range(k) if mask[j]}
  if not old:
    continue
  for j in range(k):
    if j in old:
      continue
    for d in range(2,k):
      assert abs(gap_count(old|{j},k,d)-gap_count(old,k,d))<=2
      checks+=1
print('VERIFY_OK',checks,'checks; 5-clock joint-valley probability',F(num,120))
