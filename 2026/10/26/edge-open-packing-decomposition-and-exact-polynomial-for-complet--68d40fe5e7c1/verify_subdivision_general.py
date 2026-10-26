from collections import Counter
from itertools import combinations
from functools import lru_cache
from random import Random

def prediction(n,edges):
 E=set(tuple(sorted(e)) for e in edges)
 out=Counter()
 def subsets(xs):
  for s in range(1<<len(xs)):
   yield {xs[i] for i in range(len(xs)) if s>>i&1}
 def enumerate_matching(rem, chosen):
  if not rem:
   unmatched=set(range(n))-set(sum((list(e) for e in chosen),[]))
   for C in subsets(sorted(unmatched)):
    U=unmatched-C
    factors=Counter({0:1})
    for c in C:
     d=sum((min(c,u),max(c,u)) in E for u in U)
     nxt=Counter()
     for power,count in factors.items():
      for bitmask in range(1,1<<d):
       nxt[power+bitmask.bit_count()]+=count
     factors=nxt
    for power,count in factors.items():out[power+2*len(chosen)]+=count
   return
  a=rem[0]
  enumerate_matching(rem[1:],chosen)
  for b in rem[1:]:
   if (min(a,b),max(a,b)) in E:
    enumerate_matching([u for u in rem if u not in (a,b)],chosen+[(a,b)])
 enumerate_matching(list(range(n)),[])
 return out

def brute(n,edges):
 e_orig=[tuple(sorted(e)) for e in edges]
 incidences=[(v,i) for i,(u,w) in enumerate(e_orig) for v in (u,w)]
 N=len(incidences)
 conflicts=[0]*N
 for i,(v,e) in enumerate(incidences):
  for j in range(i):
   u,f=incidences[j]
   # Is there a third incidence between an old endpoint of one and the subdivision endpoint of the other?
   bad=((v in e_orig[f] and (v,f) not in ((v,e),(u,f))) or
        (u in e_orig[e] and (u,e) not in ((v,e),(u,f))))
   if bad: conflicts[i]|=1<<j;conflicts[j]|=1<<i
 cnt=Counter()
 for mask in range(1<<N):
  i=mask
  ok=True
  while i:
   b=i&-i;idx=b.bit_length()-1
   if conflicts[idx]&mask:ok=False;break
   i^=b
  if ok:cnt[mask.bit_count()]+=1
 return cnt
rng=Random(11)
for n in range(1,5):
 poss=list(combinations(range(n),2))
 for m in range(1<<len(poss)):
  ed=[e for i,e in enumerate(poss) if m>>i&1]
  a=prediction(n,ed);b=brute(n,ed)
  if a!=b:raise Exception((n,ed,a,b))
 print('all graphs on',n,'vertices pass',1<<len(poss))
for n in [5]:
 poss=list(combinations(range(n),2));cases=[[],poss]+[rng.sample(poss,rng.randrange(0,len(poss)+1)) for _ in range(30)]
 for ed in cases:
  a=prediction(n,ed);b=brute(n,ed)
  if a!=b:raise Exception((n,ed,a,b))
 print('sample graph set on',n,'vertices pass',len(cases))
print('ALL_CHECKS_OK')
