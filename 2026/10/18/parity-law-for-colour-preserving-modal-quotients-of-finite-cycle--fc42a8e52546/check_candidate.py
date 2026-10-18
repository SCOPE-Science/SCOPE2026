from itertools import product
from math import gcd

def divs(n): return [d for d in range(1,n+1) if n%d==0]
def per(w):
 n=len(w);return min(p for p in divs(n) if all(w[i]==w[i%p] for i in range(n)))
def refl(w):
 m=len(w);return any(all(w[i]==w[(2*s-i)%m] for i in range(m)) for s in range(m))
def canonical_path(w):return min(w,w[::-1])
def predicted(w):
 m=len(w);p=per(w)
 cyc=sum(1 for d in divs(m) if d>=3 and d%p==0)
 ps={}
 if refl(w) and m%2==0:
  for L in divs(m):
   if L%2==0 and L%p==0:
    k=L//p
    ps[L//2+1]=1 if (p%2 or k%2) else 2
 return cyc,ps

def actual(w):
 m=len(w);cyc=0;ps={}
 for d in divs(m):
  if d>=3:
   ts=set()
   for sign in [1,-1]:
    for s in range(d):
     target=[None]*d;ok=True
     for i in range(m):
      j=(s+sign*i)%d
      if target[j] is None: target[j]=w[i]
      elif target[j]!=w[i]:ok=False;break
     if ok: ts.add(tuple(target))
   if ts:cyc+=1
 for L in divs(m):
  if L%2==1:continue
  n=L//2+1
  ts=set()
  for s in range(L):
   target=[None]*n;ok=True
   for i in range(m):
    z=(i+s)%L;j=min(z,L-z)
    if target[j] is None:target[j]=w[i]
    elif target[j]!=w[i]:ok=False;break
   if ok:ts.add(canonical_path(tuple(target)))
  if ts:ps[n]=len(ts)
 return cyc,ps

if __name__=='__main__':
 tot=0;fold=0
 for m in range(3,15):
  for w in product(range(2),repeat=m):
   a=actual(w);p=predicted(w)
   assert a==p,(m,w,a,p)
   tot+=1
   if a[1]:fold+=1
 print('PASS binary length 3..14',tot,'words, with path images',fold)
 total3=0
 for m in range(3,10):
  for w in product(range(3),repeat=m):
   assert actual(w)==predicted(w),(m,w,actual(w),predicted(w))
   total3+=1
 print('PASS ternary length 3..9',total3,'words')
