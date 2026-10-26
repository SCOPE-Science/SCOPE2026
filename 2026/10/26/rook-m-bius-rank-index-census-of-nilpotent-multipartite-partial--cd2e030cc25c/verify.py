from itertools import combinations, permutations
from functools import lru_cache
from math import factorial, comb, prod
from collections import defaultdict

def all_maps(k):
  for t in range(k+1):
    for ss in combinations(range(k),t):
      for tt in combinations(range(k),t):
        for pp in permutations(tt):
          yield dict(zip(ss,pp))

def mu(h):return sum((-1)**j*comb(h,j)**2*factorial(j) for j in range(h+1))

def fg(n,pi,L):
  k=len(n)
  words=[]
  for start in range(k):
    word=[start]
    for ell in range(1,L+1):
      c=tuple(word.count(i) for i in range(k))
      if all(c[i]<=n[i] for i in range(k)):
        words.append((c,ell-1))
      if word[-1] not in pi:break
      word.append(pi[word[-1]])
  @lru_cache(None)
  def rec(m):
    if sum(m)==0:return {0:1}
    a=next(i for i in range(k) if m[i]>0)
    ans=defaultdict(int)
    for counts,rank in words:
      if not counts[a] or any(counts[i]>m[i] for i in range(k)):continue
      ways=counts[a]
      for j in range(1,counts[a]):ways*=m[a]-j
      for i in range(k):
        if i!=a:
          for j in range(counts[i]):ways*=m[i]-j
      rem=tuple(m[i]-counts[i] for i in range(k))
      for r,v in rec(rem).items():ans[r+rank]+=v*ways
    return dict(ans)
  return rec(tuple(n))

def spec(n,L):
 out=defaultdict(int);k=len(n)
 for pi in all_maps(k):
  fac=mu(k-len(pi))
  if not fac:continue
  for r,v in fg(n,pi,L).items():out[r]+=fac*v
 return dict(out)

def brute(n):
 N=sum(n);cs=sum(([i]*c for i,c in enumerate(n)),[]); out=defaultdict(int)
 for r in range(N+1):
  for dd in combinations(range(N),r):
   for rr in combinations(range(N),r):
    for tt in permutations(rr):
     f=dict(zip(dd,tt))
     if any((cs[a]==cs[b])!=(cs[f[a]]==cs[f[b]]) for a,b in combinations(dd,2)):continue
     cur=[i for i in range(N)]
     # check nilpotent and index as max path length
     nu=1;good=True
     for x in range(N):
      y=x;seen={x};ell=1
      while y in f:
       y=f[y]
       if y in seen:
        good=False;break
       seen.add(y);ell+=1
      nu=max(nu,ell)
      if not good:break
     if good:out[(r,nu)]+=1
 return dict(out)

if __name__=='__main__':
 for n in [(2,2),(3,2),(2,2,2),(3,2,2)]:
  k=len(n);lim=sum(n)
  print('case',n, 'mu', [mu(i) for i in range(k+1)],flush=True)
  lens={j:spec(n,j) for j in range(1,lim+1)}
  theoretical={}
  for L in range(1,lim+1):
   for r,v in lens[L].items():
    dif=v-lens.get(L-1,{}).get(r,0)
    if dif:theoretical[r,L]=dif
  b=brute(n)
  assert b==theoretical,(b,theoretical)
  if len(n)>=3:
    sizes={j:sum(c>=j for c in n) for j in range(1,max(n)+2)}
    M=max(j*sizes[j]+sizes[j+1] for j in range(1,max(n)+1))
    assert max(index for rank,index in b)==M
    if M==sum(n):
      m=min(n);h=sum(c==m+1 for c in n)
      assert all(c in (m,m+1) for c in n)
      assert b.get((sum(n)-1,M))==factorial(h)*factorial(len(n)-h)*prod(factorial(c) for c in n)
  print('PASS',n,'nilpotents',sum(b.values()),'max_index',max(idx for rank,idx in b),flush=True)

print('VERIFY_OK: exact coefficient recurrence and independent metric-map enumeration')
