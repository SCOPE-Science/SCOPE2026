from itertools import combinations,product
from collections import Counter
from math import comb

def rref_subspaces(n,q):
  yield ()
  for k in range(1,n+1):
    for piv in combinations(range(n),k):
      frees=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
      for vals in product(range(q),repeat=len(frees)):
        rows=[[0]*n for _ in range(k)]
        for i,p in enumerate(piv): rows[i][p]=1
        for (i,j),v in zip(frees,vals): rows[i][j]=v
        yield tuple(tuple(r) for r in rows)

def belongs(v,R,p):
  v=list(v)
  for row in R:
    pivot=next(i for i,x in enumerate(row) if x)
    m=v[pivot]
    if m:
      for j in range(pivot,len(v)): v[j]=(v[j]-m*row[j])%p
  return not any(v)

# a=0,b=1,c=2,d=3,e=4,f=5
mul={(0,1):3,(1,2):4,(0,4):5,(3,2):5}
def times(x,y,p):
  z=[0]*6
  for (i,j),k in mul.items(): z[k]=(z[k]+x[i]*y[j])%p
  return tuple(z)

def main(p):
  es=[tuple(int(i==k) for i in range(6)) for k in range(6)]
  count=Counter(); N=0
  for R in rref_subspaces(6,p):
    N+=1
    for x in R:
      if any(not belongs(times(e,x,p),R,p) or not belongs(times(x,e,p),R,p) for e in es):break
    else:count[len(R)]+=1
  return N,count

if __name__=='__main__':
 for p in [2,3]:
  N,counts=main(p)
  expected=[1,1,p+1,2*p+1,p*p+p+1,p*p+p+1,1]
  print('q=',p,'spaces=',N,'ideals=',dict(sorted(counts.items())),'expected',expected,'MATCH',list(counts.get(i,0) for i in range(7))==expected,flush=True)
