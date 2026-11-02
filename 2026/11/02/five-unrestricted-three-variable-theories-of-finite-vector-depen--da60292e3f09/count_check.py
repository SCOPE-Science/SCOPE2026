"""Independent finite arithmetic check of the two-anchor extension-count formula.

The theorem itself follows from the general algebraic formulas, not from
finite testing. This program checks those formulas on representative pairs.
"""
from itertools import product
from collections import Counter

def add(a,b,q):return (a^b) if q==4 else (a+b)%q

def mul(a,b,q):
 if q!=4:return a*b%q
 r=0
 for i in range(2):
  if (b>>i)&1:r^=a
  a=((a<<1)&3)^((a>>1)*3)
 return r

def scalar(a,x,q):return tuple(mul(a,u,q) for u in x)
def sumv(x,y,q):return tuple(add(a,b,q) for a,b in zip(x,y))

def label(x,y,q):
 zero=(0,)*len(x)
 if x==zero:return 'ZZ' if y==zero else 'ZX'
 if y==zero:return 'XZ'
 if x==y:return 'XX'
 if any(scalar(a,x,q)==y for a in range(1,q)):return 'PP'
 return 'II'

def expected(q,d,state):
 n=q**d
 if state=='ZZ':return {('ZZ','ZZ',1):1,('ZX','ZX',1):n-1}
 if state=='ZX':return {('ZZ','XZ',1):1,('ZX','XX',1):1,('ZX','PP',1):q-2,('ZX','II',1):n-q}
 if state=='XZ':return {('XZ','ZZ',1):1,('XX','ZX',1):1,('PP','ZX',1):q-2,('II','ZX',1):n-q}
 if state=='XX':return {('XZ','XZ',1):1,('XX','XX',1):1,('PP','PP',1):q-2,('II','II',1):n-q}
 if state=='PP':return {('XZ','XZ',1):1,('XX','PP',1):1,('PP','XX',1):1,('PP','PP',1):q-3,('II','II',1):n-q}
 assert state=='II'
 return {('XZ','XZ',1):1,('XX','II',1):1,('II','XX',1):1,('PP','II',1):q-2,('II','PP',1):q-2,('II','II',1):(q-1)**2,('II','II',0):n-q*q}

def verify(q,d):
 zero=(0,)*d;e1=(1,)+(0,)*(d-1);e2=(0,1)+(0,)*(d-2)
 reps=[(zero,zero),(zero,e1),(e1,zero),(e1,e1),(e1,e2)]
 for a in range(2,q):reps.append((e1,scalar(a,e1,q)))
 V=list(product(range(q), repeat=d)); seen=set()
 for x,y in reps:
  st=label(x,y,q); seen.add(st)
  c=Counter()
  span={sumv(scalar(a,x,q),scalar(b,y,q),q) for a in range(q) for b in range(q)}
  for z in V:
   dep=1 if st!='II' or z in span else 0
   c[(label(x,z,q),label(y,z,q),dep)]+=1
  exp={k:v for k,v in expected(q,d,st).items() if v>0}
  assert dict(c)==exp,(q,d,st,c,exp)
 return seen

if __name__=='__main__':
 for q,d in [(2,3),(2,4),(3,3),(3,4),(4,3),(5,3),(7,3)]:
  seen=verify(q,d)
  print(f'q={q} d={d}: exact extension-count formulas hold for {len(seen)} pair status classes')
 print('INDEPENDENT EXTENSION-COUNT CHECK PASSED')
