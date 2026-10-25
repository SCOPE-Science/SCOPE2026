"""Exact centralizer-subalgebra lower-central signatures over prime fields and F4."""
from collections import Counter
from itertools import product
BASIS = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

class Field:
 def __init__(self,q): self.q=q
 def add(self,a,b): return (a^b) if self.q==4 else (a+b)%self.q
 def neg(self,a): return a if self.q==4 else (-a)%self.q
 def mul(self,a,b):
  if self.q!=4: return a*b%self.q
  x=0
  for i in range(2):
   for j in range(2):
    if a&(1<<i) and b&(1<<j): x^=1<<(i+j)
  if x&8:x^=12
  if x&4:x^=7
  return x
 def inv(self,a):
  return next(b for b in range(1,self.q) if self.mul(a,b)==1)

def rref(rows,F):
 if not rows:return [],[]
 A=[r[:] for r in rows]; k=0; piv=[]
 for c in range(len(A[0])):
  i=next((i for i in range(k,len(A)) if A[i][c]),None)
  if i is None:continue
  A[k],A[i]=A[i],A[k]
  t=F.inv(A[k][c]); A[k]=[F.mul(t,v) for v in A[k]]
  for i in range(len(A)):
   if i!=k and A[i][c]:
    t=A[i][c]
    A[i]=[F.add(v,F.neg(F.mul(t,w))) for v,w in zip(A[i],A[k])]
  piv.append(c);k+=1
  if k==len(A):break
 return A[:k],piv

def nullspace(A,F):
 if not A:return [[int(i==j) for i in range(6)] for j in range(6)]
 R,p=rref(A,F);free=[j for j in range(6) if j not in p]
 out=[]
 for c in free:
  v=[0]*6;v[c]=1
  for i,j in enumerate(p):v[j]=F.neg(R[i][c])
  out.append(v)
 return out

def bracket(x,y,F):
 a,b,_,d,e,f=x; A,B,_,D,E,G=y
 return [0,F.add(F.mul(a,D),F.neg(F.mul(d,A))), F.add(F.add(F.add(F.mul(a,E),F.mul(b,G)),F.neg(F.mul(e,A))),F.neg(F.mul(f,B))),0,F.add(F.mul(d,G),F.neg(F.mul(f,D))),0]

def centralizer_basis(x,F):
 e=[]
 for i in range(6):
  unit=[int(k==i) for k in range(6)]
  e.append(bracket(x,unit,F))
 A=[[e[j][i] for j in range(6)] for i in range(6)]
 return nullspace(A,F)

def span_brackets(U,V,F):
 vals=[bracket(u,v,F) for u in U for v in V]
 return rref(vals,F)[0]

def classify(x,F):
 C=centralizer_basis(x,F)
 D=span_brackets(C,C,F)
 T=span_brackets(C,D,F)
 typ=(len(C),len(D),len(T))
 tags={(6,3,1):'n4',(5,2,0):'s5',(5,2,1):'f4_plus_k',(4,1,0):'h3_plus_k',(4,0,0):'abelian4',(3,0,0):'abelian3'}
 assert typ in tags,(F.q,x,typ)
 return tags[typ]

def predicted(q):
 return {'n4':q,'s5':q*(q*q-1) if q%2==0 else 2*q*(q-1),'f4_plus_k':0 if q%2==0 else q*(q-1)**2,'h3_plus_k':q**3*(q*q-1),'abelian4':q**3*(q-1),'abelian3':q**3*(q-1)*(q*q-1)}

def main():
 for q in (2,3,4,5):
  F=Field(q);c=Counter()
  for x in product(range(q),repeat=6):c[classify(x,F)]+=1
  expected=predicted(q)
  assert all(c[t]==n for t,n in expected.items()),(q,c,expected)
  assert sum(c.values())==q**6
  print(f'q={q}: {dict(sorted(c.items()))}; PASS')
 print('CENTRALIZER_TYPES_OK')
if __name__=='__main__':main()
