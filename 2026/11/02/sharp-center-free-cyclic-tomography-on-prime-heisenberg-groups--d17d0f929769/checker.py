from itertools import product,combinations
from math import comb

def mul(p,g,h):
 a,b,c=g;u,v,w=h
 return ((a+u)%p,(b+v)%p,(c+w+a*v)%p)

def rows_for(p,split=None,vertical=0):
 if split is None:split=set(range((p+1)//2))
 G=list(product(range(p),repeat=3)); idx={g:j for j,g in enumerate(G)}
 for s in range(p):
  c=0 if s in split else 1
  yield from subgroup_rows(p,G,idx,(1,s,c))
 yield from subgroup_rows(p,G,idx,(0,1,vertical))

def subgroup_rows(p,G,idx,gen):
 H=[(0,0,0)];h=(0,0,0)
 for _ in range(p-1):h=mul(p,h,gen);H.append(h)
 unseen=set(G)
 while unseen:
  g=min(unseen); coset={mul(p,g,h) for h in H};unseen.difference_update(coset)
  mask=0
  for x in coset:mask|=1<<idx[x]
  yield mask

def bit_rank(masks):
 pivots={}
 for row in masks:
  while row:
   b=row.bit_length()-1
   if b not in pivots:pivots[b]=row;break
   row^=pivots[b]
 return len(pivots)

def run():
 for p in (3,5,7,11):
  splits=[set(range((p+1)//2))]
  if p<=7:splits=list(map(set,combinations(range(p),(p+1)//2)))
  for S in splits:
   rows=list(rows_for(p,S));r=bit_rank(rows)
   assert len(rows)==p*p*(p+1),(p,len(rows))
   assert r==p**3,(p,S,r)
  print('Exact integer mod-2 full-rank certificates:',p,'cases',len(splits),'size',len(rows),'x',p**3)
if __name__=='__main__':run()
