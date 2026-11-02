from itertools import product
from fractions import Fraction
from math import comb

def comps(n):
 for a in range(1,n-2):
  for b in range(1,n-a-1):
   for c in range(1,n-a-b):
    d=n-a-b-c
    if d>0: yield (a,b,c,d)

def e_formula(x,q):
 n=sum(x);a,b,c,d=x
 c1=q+q**3-q**4;c2=2*q*q-q**4
 return (sum(v*v for v in x)+2*c1*(a*b+b*c+c*d+d*a)+2*c2*(a*c+b*d))/n

def brute(x,q):
 n=sum(x); ss=Fraction(0)
 for mask in product((0,1),repeat=4):
  prob=Fraction(1)
  for m in mask:prob*=q if m else (1-q)
  # make segment graph: 0--1--2--3--0
  par=list(range(4))
  def root(i):
   while par[i]!=i:i=par[i]
   return i
  for i,m in enumerate(mask):
   if m: par[root(i)]=root((i+1)%4)
  c={}
  for i,v in enumerate(x):c[root(i)]=c.get(root(i),0)+v
  ss+=prob*sum(v*v for v in c.values())/n
 return ss

def predicted(x,n):
 k=n//4
 r=n%4
 if r==0:return sorted(x)==[k]*4
 if r==1:return sorted(x)==[k]*3+[k+1]
 if r==3:return sorted(x)==[k]+[k+1]*3
 return tuple(x) in [(k,k+1,k,k+1),(k+1,k,k+1,k)]

for q in (Fraction(1,9),Fraction(1,2),Fraction(9,10)):
 for n in range(4,17):
  xs=list(comps(n));vals=[e_formula(x,q) for x in xs]; mn=min(vals)
  opt={x for x,v in zip(xs,vals) if v==mn}
  target={x for x in xs if predicted(x,n)}
  assert opt==target, (n,q,opt,target)
  for x in xs[:8]:assert brute(x,q)==e_formula(x,q),(n,q,x)
 print('q',q,'all n4..16 PASS')
for n in range(4,11):
 for x in comps(n):
  assert brute(x,Fraction(2,5)) == e_formula(x,Fraction(2,5))
print('all configurations n4..10 exact 2/5 PASS')
q=Fraction(1,2)
for x in [(2,1,2,1),(2,2,1,1),(1,2,1,2)]: print(x,e_formula(x,q))
