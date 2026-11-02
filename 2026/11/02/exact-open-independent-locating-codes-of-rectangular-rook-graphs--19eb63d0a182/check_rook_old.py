"""Independent direct checker for open-independent OLD sets on rectangular rook graphs."""
import math
from itertools import product

def theorem_count(m,n):
  total=0
  if (2*m-n)%3==0 and (2*n-m)%3==0:
    a=(2*m-n)//3
    b=(2*n-m)//3
    if a>=0 and b>=0 and a+b>=1:
      total+=math.comb(n,a)*math.comb(m,b)*math.factorial(2*a)*math.factorial(2*b)//(2**(a+b))
  if n==2*m+1:
    total+=math.factorial(n)//(2**m)
  if m==2*n+1:
    total+=math.factorial(m)//(2**n)
  return total

def direct_count(m,n):
  v=m*n;neigh=[]
  for i in range(m):
    for j in range(n):
      neigh.append(sum(1<<(a*n+b) for a in range(m) for b in range(n) if (a==i or b==j) and (a,b)!=(i,j)))
  result=0
  for mask in range(1<<v):
    if mask.bit_count()%2:continue
    x=mask;good=True
    while x:
      t=x&-x;idx=t.bit_length()-1;x-=t
      if (mask&neigh[idx]).bit_count()!=1:
        good=False;break
    if not good:continue
    seen=set()
    for s in neigh:
      sig=s&mask
      if not sig or sig in seen:
        good=False;break
      seen.add(sig)
    if good:result+=1
  return result

def run():
  pairs=[(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)]
  checked=0
  for m,n in pairs:
    actual=direct_count(m,n)
    predicted=theorem_count(m,n)
    assert actual==predicted,(m,n,actual,predicted)
    checked+=(1<<(m*n))
    print(f'{m}x{n}: {actual} codes (checked {1<<(m*n)} subsets)')
  print(f'PASS {len(pairs)} board sizes, {checked} labeled subsets')
if __name__=='__main__':run()
