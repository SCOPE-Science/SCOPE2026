from collections import Counter
from itertools import product

P=2
mul_table=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))  # GF4: alpha^2=alpha+1

def multiply(x,y):
 a,b,c,d,e,f=[(x>>(2*i))&3 for i in range(6)]
 A,B,C,D,E,F=[(y>>(2*i))&3 for i in range(6)]
 return (mul_table[a][B]<<6)^(mul_table[b][C]<<8)^((mul_table[a][E]^mul_table[d][C])<<10)

def normal(vs):
 # Canonical reduced row echelon F2, highest-index pivot first
 v={}
 for a in vs:
  x=a
  for i in sorted(v,reverse=True):
   if (x>>i)&1: x^=v[i]
  if x:
   j=x.bit_length()-1
   for i in list(v):
    if (v[i]>>j)&1: v[i]^=x
   v[j]=x
 return tuple(v[i] for i in sorted(v,reverse=True))

ES=[1<<i for i in range(12)]

def principal(v):
 if not v:return ()
 basis=normal([v]);done={basis};queue=[v]
 while queue:
  x=queue.pop()
  for e in ES:
   for a in (multiply(x,e),multiply(e,x)):
    if not a:continue
    next_basis=normal((*basis,a))
    if next_basis!=basis:
     basis=next_basis;queue.append(a)
 return basis

def allideals():
 ps={principal(x) for x in range(1<<12)}
 print('distinct principal',len(ps),flush=True)
 ideals={()};todo=[()]
 # do closure under join with *principal* elements
 ps=sorted(ps,key=lambda b:(len(b),b))
 while todo:
  u=todo.pop()
  for v in ps:
   s=normal((*u,*v))
   if s not in ideals:
    ideals.add(s);todo.append(s)
  if len(ideals)>12000:raise RuntimeError('too many ideals')
 print('all ideals',len(ideals),flush=True)
 return ideals

if __name__=='__main__':
 x=allideals()
 dist=Counter(len(v) for v in x)
 print('distribution',sorted(dist.items()),flush=True)
 assert len(x)==3011
 assert [dist.get(i,0) for i in range(13)] == [1,3,1,15,35,39,69,87,651,1395,651,63,1]
 # Independently test full ideal multiplication closure, beyond the generation procedure.
 for basis in x:
  for v in basis:
   for unit in ES:
    assert normal((*basis,multiply(v,unit))) == basis
    assert normal((*basis,multiply(unit,v))) == basis
 # Exactly the F4-linear ideals remain closed under multiplication by alpha.
 def alpha(v):
  return sum(mul_table[2][(v>>(2*i))&3] << (2*i) for i in range(6))
 linear=sum(all(normal((*basis,alpha(v)))==basis for v in basis) for basis in x)
 assert linear==59,linear
 print('F4 linear ideals',linear)


# This independent integer-arithmetic expansion reconstructs the universal
# Gaussian-binomial formula, and compares its F4 coefficients with the ideal
# enumeration obtained from ring multiplication above.
def gaussian(n,k,p):
 if k<0 or k>n:return 0
 num=1;den=1
 for j in range(k):
  num*=p**(n-j)-1
  den*=p**(j+1)-1
 return num//den

def formula(p,m):
 from collections import defaultdict
 ans=defaultdict(int)
 def addG(d,shift,scale=1,omit0=False,mult=1):
  for s in range(int(omit0),d+1):
   ans[shift+s]+=mult*gaussian(d,s,p)*scale**s
 addG(m,0)
 addG(2*m,m,omit0=True)
 addG(3*m,3*m,omit0=True)
 for r in range(m):
  for s in range(1,m+1):
   ans[2*m+r+s]+=2*gaussian(m,r,p)*gaussian(m,s,p)*p**((m-r)*s)
 return [ans.get(j,0) for j in range(6*m+1)]

assert formula(2,2)==[1,3,1,15,35,39,69,87,651,1395,651,63,1]
assert formula(2,1)==[1,1,3,5,7,7,1]
assert formula(3,1)==[1,1,4,7,13,13,1]
assert sum(formula(3,2))==57250
print('CHECKER_OK')
