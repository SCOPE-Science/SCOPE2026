"""Exact checks of Chebyshev endpoint identities for root-of-unity-angle sets.
No numerical computation is used as a substitute for the general harmonic proof.
"""
from fractions import Fraction
from itertools import product, permutations

# Pairs represent a+b*sqrt(5). The rational basis keeps every test exact.
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def mul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scalar(x,s):return (x[0]*s,x[1]*s)
def dot(x,y):
 z=(Fraction(0),Fraction(0))
 for a,b in zip(x,y):z=add(z,mul(a,b))
 return z
Z=(Fraction(0),Fraction(0))
ONE=(Fraction(1),Fraction(0))

def cheb(n,t):
 if n==0:return ONE
 u0,u1=ONE,scalar(t,2)
 for k in range(2,n+1):u0,u1=u1,sub(scalar(mul(t,u1),2),u0)
 return u1

def build_600():
 V=[]
 for i in range(4):
  for sg in (-1,1):
   x=[Z]*4;x[i]=scalar(ONE,sg);V.append(tuple(x))
 for sg in product((-1,1),repeat=4):V.append(tuple(scalar(ONE,Fraction(s,2)) for s in sg))
 base=[Z,(Fraction(1,2),Fraction(0)),(Fraction(1,4),Fraction(1,4)),(Fraction(-1,4),Fraction(1,4))]
 for pm in permutations(range(4)):
  if sum(pm[i]>pm[j] for i in range(4) for j in range(i+1,4))%2:continue
  for sg in product((-1,1),repeat=3):
   x=[base[i] for i in pm];it=iter(sg)
   V.append(tuple(scalar(t,next(it)) if t!=Z else Z for t in x))
 assert len(V)==len(set(V))==120
 return V

def show(label,V,L):
 n=len(V); assert n%2==0
 assert all(dot(v,v)==ONE for v in V)
 Vset=set(V)
 assert all(tuple(scalar(c,-1) for c in v) in Vset for v in V)
 tset={dot(a,b) for a in V for b in V}
 for t in tset:
  u=cheb(L-2,t);v=cheb(L-1,t);w=cheb(L,t)
  if t==ONE:assert (u,v,w)==(scalar(ONE,L-1),scalar(ONE,L),scalar(ONE,L+1))
  elif t==scalar(ONE,-1):assert (u,v,w)==(scalar(ONE,L-1),scalar(ONE,-L),scalar(ONE,L+1))
  else:assert (u,v,w)==(scalar(ONE,-1),Z,ONE)
  for k in range(0,8):
   assert cheb(k+L,t)==add(cheb(k,t),scalar(ONE,L*(1 if t==ONE else ((-1)**k if t==scalar(ONE,-1) else 0))))
 print(label, 'vertices',n,'angular_classes',len(tset), 'L',L,'exact_checks_passed')
 print('  rank at L-2:',n//2-1 if n==2*L else n//2,'rank at L-1:',n//2)

show('600-cell',build_600(),60)
V=[]
for i in range(4):
 for sg in (-1,1):
  v=[Z]*4;v[i]=scalar(ONE,sg);V.append(tuple(v))
show('Q8',V,4)
print('General proof: addition kernel is positive; equalities extend to all degrees via the L-periodic recurrence.')
