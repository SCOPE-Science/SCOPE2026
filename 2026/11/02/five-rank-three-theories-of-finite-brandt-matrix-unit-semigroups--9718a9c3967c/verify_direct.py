"""Direct element-level rank-3 EF-type enumerator for finite matrix-unit semigroups."""
from itertools import product
from functools import lru_cache

def semigroup(n):
 els=[None]+[(i,j) for i in range(n) for j in range(n)]
 tab=[]
 for a in els:
  row=[]
  for b in els:
   x=(a[0],b[1]) if a is not None and b is not None and a[1]==b[0] else None
   row.append(els.index(x))
  tab.append(row)
 return els,tab

def base(tup, tab):
 vals=(0,)+tup
 mask=0;k=len(vals)
 for i in range(k):
  for j in range(k):
   mask=(mask<<1)|(vals[i]==vals[j])
 for i in range(k):
  for j in range(k):
   for h in range(k):
    mask=(mask<<1)|(tab[vals[i]][vals[j]]==vals[h])
 return mask

intern={}
def label(sig):
 if sig not in intern:intern[sig]=len(intern)
 return intern[sig]

def signature(n,q=3):
 els,T=semigroup(n);size=len(els)
 # recursively for each chosen tuple of length from q down to 0
 prior={(a,b,c):label(('atom',base((a,b,c),T))) for a,b,c in product(range(size),repeat=3)}
 for k in [2,1,0]:
  curr={}
  for tup in product(range(size),repeat=k):
   nxt=frozenset(prior[tup+(x,)] for x in range(size))
   curr[tup]=label(('ext',base(tup,T),nxt))
  prior=curr
 return prior[()],len(intern)

if __name__=='__main__':
 for n in range(1,8):
  print(n,signature(n),flush=True)
