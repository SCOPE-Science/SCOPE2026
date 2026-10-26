from itertools import combinations,permutations
from collections import Counter
from math import comb

def B(L,k):
  v=[{0:1}]+[{} for _ in range(k-1)]
  for _ in range(L):
    w=[{} for _ in range(k)]
    for j,poly in enumerate(v):
      for r,num in poly.items():
        w[0][r]=w[0].get(r,0)+num
        if j+1<k:w[j+1][r+1]=w[j+1].get(r+1,0)+num
    v=w
  out=Counter()
  for p in v:out.update(p)
  return out

def conv(a,b):
  o=Counter()
  for r,x in a.items():
    for s,y in b.items():o[r+s]+=x*y
  return o

def prediction(n,k):
  assert k>=2
  ans=Counter({0:1})
  for d in range(1,n):
    p=Counter({0:1})
    for j in range(1,d+1):p=conv(p,B((n-j)//d,k))
    p[0]-=1
    for r,x in p.items():ans[r]+=2*x
  for c in range(2,2*n+1):
    L=min(c-1,2*n+1-c)
    m=L//2
    for r in range(1,m+1):ans[r]+=comb(m,r)*2**r
  ans[1]-=n*(n-1)
  return +ans

def direct(n):
  ans=Counter()
  for r in range(n+1):
    for dom in combinations(range(1,n+1),r):
      if r==0:
        ans[0,1]+=1
        continue
      for img in combinations(range(1,n+1),r):
        for values in permutations(img):
          if any(abs(dom[i]-dom[j])!=abs(values[i]-values[j]) for i in range(r) for j in range(i+1,r)):
            continue
          f=dict(zip(dom,values))
          maxind=0
          is_nilpotent=True
          for x in dom:
            step=0;y=x;seen=set()
            while y in f:
              if y in seen:
                is_nilpotent=False
                break
              seen.add(y)
              y=f[y];step+=1
            if not is_nilpotent:
              break
            maxind=max(maxind,step+1)
          if is_nilpotent:
            ans[r,maxind]+=1
  return ans

if __name__=='__main__':
 for n in range(1,9):
  actual=direct(n)
  prev=Counter({0:1})
  pred=Counter({(0,1):1})
  for k in range(2,n+1):
    current=prediction(n,k)
    for r,v in current.items():pred[r,k]=v-prev[r]
    prev=current
  assert pred==actual,(n,actual,pred,actual-pred,pred-actual)
  print(n, sum(actual.values()),'index_counts',dict(sorted((k,sum(v for (r,j),v in actual.items() if j==k)) for k in range(1,n+1))),'rank_counts',dict(sorted((r,sum(v for (i,j),v in actual.items() if i==r)) for r in range(n))))
 for n in range(1,101):
  row=prediction(n,max(2,n))
  h=n//2
  delta=1 if n%2==0 else 3
  wanted_total=2**(n+1)-n*n-3*n-4+(3**(h+1) if n%2==0 else 5*3**h)
  assert sum(row.values())==wanted_total,(n,'total')
  for r in range(n+1):
   closed=(1 if r==0 else n*(n-1) if r==1 else
       2*comb(n,r+1)+2**r*(4*(comb(h,r+1) if r+1<=h else 0)+delta*(comb(h,r) if r<=h else 0)))
   assert row[r]==closed,(n,r,row[r],closed)
 print('VERIFY_OK_CHAIN_PARTIAL_ISOMETRY_RANK_INDEX')
