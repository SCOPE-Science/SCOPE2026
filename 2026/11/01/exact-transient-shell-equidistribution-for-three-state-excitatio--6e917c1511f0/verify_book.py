"""Self-contained verification of the book-graph CCA/GHM first-entry census.

Python 3, standard library.  Enumerated reduced classes are a complete
finite proof device for arbitrary positive numbers of labelled pages.
"""
from collections import Counter
from itertools import product
from math import comb

SUPPORTS=((0,),(1,),(2,),(0,1),(0,2),(1,2),(0,1,2))
HUBS=tuple(product(range(3), repeat=2))

# Each table entry is (first periodic entry time, least period).
# Columns 00 01 02 10 11 12 20 21 22, rows 0 1 2 01 02 12 012.
TABLE={
 'CCA':(
  ('0/1','1/1','1/1','1/1','1/1','0/3','1/1','0/3','1/1'),
  ('1/1','1/1','0/3','1/1','0/1','1/1','0/3','1/1','1/1'),
  ('1/1','0/3','1/1','0/3','1/1','1/1','1/1','1/1','0/1'),
  ('2/1','1/1','1/3','1/1','1/1','0/3','1/3','0/3','2/1'),
  ('1/1','0/3','1/1','0/3','2/1','1/3','1/1','1/3','2/1'),
  ('2/1','1/3','0/3','1/3','2/1','1/1','0/3','1/1','1/1'),
  ('2/1','1/3','1/3','1/3','2/1','1/3','1/3','1/3','2/1')),
 'GHM':(
  ('0/1','3/1','1/1','3/1','3/1','0/3','1/1','0/3','1/1'),
  ('3/1','3/1','0/3','3/1','2/1','2/1','0/3','2/1','2/1'),
  ('1/1','0/3','1/1','0/3','2/1','2/1','1/1','2/1','1/1'),
  ('4/1','3/1','1/3','3/1','3/1','0/3','1/3','0/3','2/1'),
  ('1/1','0/3','1/1','0/3','3/1','2/3','1/1','2/3','1/1'),
  ('4/1','3/3','0/3','3/3','2/1','2/1','0/3','2/1','2/1'),
  ('4/1','3/3','1/3','3/3','3/1','2/3','1/3','2/3','2/1'))
}

def local(old,neighbor_colors,model):
 if model=='CCA':
  return (old+1)%3 if ((old+1)%3 in neighbor_colors) else old
 return (old+1)%3 if (old in (1,2) or 1 in neighbor_colors) else 0

def reduced_step(st,model):
 a,b,*leaves=st
 return (local(a,(b,*leaves),model),local(b,(a,*leaves),model),
         *(local(x,(a,b),model) for x in leaves))

def full_step(st,model):
 n=len(st)
 adj=[tuple(j for j in range(n) if j!=i and (i<2 or j<2)) for i in range(n)]
 return tuple(local(st[i],(st[j] for j in adj[i]),model) for i in range(n))

def entry_period(start,step,model):
 seen={};st=start
 while st not in seen:
  seen[st]=len(seen)
  st=step(st,model)
  assert len(seen)<100
 return seen[st],len(seen)-seen[st]

def surj(m,k):
 return sum((-1)**(k-j)*comb(k,j)*j**m for j in range(k+1))

def expected(m,model):
 p=3**m;q=2**m
 if model=='CCA':
  return {(0,1):3,(0,3):6*(q-1),(1,1):9*q,
          (1,3):6*(p-2*q+1),(2,1):3*(p-q-1)}
 return {(0,1):1,(0,3):6*(q-1),(1,1):4*q-1,
         (1,3):2*(p-2*q+1),(2,1):p+2*q,
         (2,3):2*(p-2*q+1),(3,1):p+q+1,
         (3,3):2*(p-2*q+1),(4,1):p-q-1}

for model in TABLE:
 counts_by_size=Counter()
 for idx,support in enumerate(SUPPORTS):
  for j,(a,b) in enumerate(HUBS):
   t,p=entry_period((a,b,*support),reduced_step,model)
   assert '%d/%d'%(t,p)==TABLE[model][idx][j],(model,support,a,b,t,p)
   counts_by_size[(len(support),t,p)]+=1
 # This comparison proves formula identities for all m through the
 # three-dimensional basis of functions 1, 2**m, and 3**m.
 for m in range(1,13):
  census=Counter()
  for (k,t,p),c in counts_by_size.items():census[(t,p)]+=c*surj(m,k)
  assert {key:val for key,val in census.items() if val}=={
      key:val for key,val in expected(m,model).items() if val}
  assert sum(census.values())==9*3**m
  if model=='GHM':
   assert census[(1,3)]==census[(2,3)]==census[(3,3)]
 print('REDUCED_TABLE_OK',model,'63 classes; exact exponential coefficients')

for m in range(1,9):
 cycles={}
 for model in TABLE:
  census=Counter();c3=set()
  for st in product(range(3),repeat=m+2):
   t,p=entry_period(st,full_step,model)
   census[(t,p)]+=1
   if t==0 and p==3:c3.add(st)
  assert {k:v for k,v in census.items() if v}=={
      k:v for k,v in expected(m,model).items() if v}
  cycles[model]=c3
 assert cycles['CCA']==cycles['GHM']
 assert len(cycles['CCA'])==6*(2**m-1)
 for st in cycles['CCA']:
  a,b,*leaves=st
  missing=next(c for c in range(3) if c not in (a,b))
  assert a!=b and set(leaves)<={missing,(missing+1)%3} and missing in leaves
  assert full_step(st,'CCA')==full_step(st,'GHM')
 print('MICROSCOPIC_OK','pages=',m,'colorings=',3**(m+2))
print('BOOK_CCA_GHM_VERIFY_OK')
