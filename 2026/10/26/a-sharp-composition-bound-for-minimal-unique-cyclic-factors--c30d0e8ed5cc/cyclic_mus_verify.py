#!/usr/bin/env python3
"""Direct independent cyclic-window enumeration for minimum uniquely occurring words."""
from collections import Counter
from itertools import product

def cyclic_mus(w):
 n=len(w); d=w+w
 freq=Counter(d[i:i+ell] for ell in range(1,n+1) for i in range(n))
 return {s for s,v in freq.items() if v==1 and (len(s)==1 or (freq[s[:-1]]>1 and freq[s[1:]]>1))}

def db(t,p,k,n,a):
 if t>n:
  if n%p==0:yield from a[1:p+1]
 else:
  a[t]=a[t-p]
  yield from db(t+1,p,k,n,a)
  for j in range(a[t-p]+1,k):
   a[t]=j
   yield from db(t+1,t,k,n,a)

def debruijn(k,n):
 a=[0]*(k*n+1)
 return ''.join(map(str,db(1,1,k,n,a)))

def test():
 cases=0;mus_count=0
 for q,maxn in [(2,15),(3,8),(4,6)]:
  alphabet='0123'[:q]
  for n in range(2,maxn+1):
   for tup in product(alphabet,repeat=n):
    w=''.join(tup); out=cyclic_mus(w)
    counts=Counter(w)
    if any(sum(s[0]==a for s in out)>min(cnt,n-cnt) for a,cnt in counts.items()):
     raise AssertionError(('per-letter-bound',w,out))
    if len(out)>sum(min(cnt,n-cnt) for cnt in counts.values()):
     raise AssertionError(('all-letter-bound',w,out))
    cases+=1;mus_count+=len(out)
  print('alphabet',q,'cases-so-far',cases)
 for q,nmax in [(2,6),(3,4)]:
  for r in range(1,nmax+1):
   w=debruijn(q,r)
   if len(w)!=q**r or Counter(w)!=Counter(dict((str(x),q**(r-1)) for x in range(q))):
    raise AssertionError(('deBruijn-shape',q,r,w))
   assert len({(w+w)[i:i+r] for i in range(len(w))})==q**r
   x=cyclic_mus(w)
   if len(x)!=len(w) or any(len(t)!=r for t in x):
    raise AssertionError(('deBruijn-muss',q,r,len(x)))
   print('deBruijn',q,r,len(w))
 print('ALL_PASS',cases,'word_cases',mus_count,'total_mus')
if __name__=='__main__':test()
