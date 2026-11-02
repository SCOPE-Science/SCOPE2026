from itertools import product, permutations, combinations
from collections import Counter

def codes(b):
 d=(b-1).bit_length();K=d+1
 return ['0'*K+'1'+''.join(a)+'1'*K for a in list(product('01',repeat=d))[:b]]
def first_hit(w,ws):
 best=None
 for i,c in enumerate(ws):
  j=w.find(c)
  if j>=0 and (best is None or j<best[0]):best=(j,i)
 return None if best is None else best[1]
for b in range(1,9):
 ws=codes(b)
 for a in ws:
  for c in ws:
   for i in range(1,len(a)):
    assert a[-i:]!=c[:i]
 L=len(ws[0]);N=L+4
 if b<=4 and N<=18:
  h=Counter(first_hit(''.join(w),ws) for w in product('01',repeat=N))
  assert len({h[i] for i in range(b)})==1,(b,h)
 print('CROSS_BIFIX_OK',b,L)
for n in range(1,8):
 m={}
 for bits in product('01',repeat=n):
  s=[i+1 for i,x in enumerate(bits) if x=='1']
  t=[i+1 for i,x in enumerate(bits) if x=='0']
  perm=tuple(s+t)
  assert sum(perm[i]>perm[i+1] for i in range(n-1))<=1
  m.setdefault(perm,[]).append(bits)
 assert len(m)==2**n-n,(n,len(m))
 nonid=[p for p in m if p!=tuple(range(1,n+1))]
 assert len(nonid)==2**n-n-1
 for p in nonid:
  cut=next(i for i in range(n-1) if p[i]>p[i+1])+1
  rec=tuple('1' if i in p[:cut] else '0' for i in range(1,n+1))
  assert m[p]==[rec]
 print('BIJECTION_OK',n,len(m))
print('ALL_CHECKS_OK')
