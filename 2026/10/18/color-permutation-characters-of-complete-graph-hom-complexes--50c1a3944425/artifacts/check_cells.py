from itertools import product,permutations
from math import comb

def parity(seq):return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
def cycles(p):
 seen=set();c=0
 for i in range(len(p)):
  if i not in seen:
   c+=1;j=i
   while j not in seen:seen.add(j);j=p[j]
 return c

def cells(m,n):
 out={}
 for z in product(range(m+1),repeat=n):
  if not set(range(1,m+1)).issubset(set(z)):continue
  tup=tuple(tuple(j for j,v in enumerate(z) if v==i) for i in range(1,m+1))
  d=sum(map(len,tup))-m
  out.setdefault(d,[]).append(tup)
 return out

def target(m,n,p):
 c=cycles(p)
 # complete-cell trace formula
 return ((-1)**m)*parity(p)*sum((-1)**j*comb(m,j)*(j-1)**c for j in range(2,m+1))

def cell_trace(cel,p):
 s=0
 for tup in cel:
  image=tuple(tuple(sorted(p[x] for x in A)) for A in tup)
  if image!=tup:continue
  sign=1
  for A in tup:sign*=parity(tuple(p[x] for x in A))
  s+=sign
 return s

def verify(m,n):
 cs=cells(m,n)
 print('m,n=',m,n,'cell-count', {k:len(v) for k,v in cs.items()})
 bycycle={}
 for p in permutations(range(n)):
  L=sum((-1)**d*cell_trace(row,p) for d,row in cs.items())
  h=(-1)**(n-m)*(L-1)
  f=target(m,n,p)
  assert h==f,(m,n,p,h,f)
  bycycle.setdefault((cycles(p),parity(p)),set()).add(h)
 assert all(len(v)==1 for v in bycycle.values())
 print('cycle-sign->char', {str(k): next(iter(v)) for k,v in sorted(bycycle.items())})

if __name__=='__main__':
 for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4),(4,5)]:verify(m,n)
 print('CHECK_CELLS_OK')
