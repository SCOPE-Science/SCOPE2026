"""Exact direct enumeration of all natural bases and their graph outdegrees."""
from itertools import product

class Field:
 def __init__(self,p,m=1):
  self.p,self.m,self.q=p,m,p**m
  self.irred={2:{1:0b11,2:0b111,3:0b1011,4:0b10011}}
  self.add=lambda a,b: (a^b if p==2 else (a+b)%p) if m==1 or p==2 else ((a%3+b%3)%3+3*((a//3+b//3)%3))
  if m==1:self.mul=lambda a,b:(a*b)%p
  elif p==2:
   pol=self.irred[2][m];mask=self.q-1
   def mul(a,b):
    z=0
    while b:
     if b&1:z ^=a
     b >>=1
     a <<=1
     if a&self.q:a ^=pol
    return z&mask
   self.mul=mul
  elif (p,m)==(3,2):
   self.mul=lambda a,b: (((a%3)*(b%3)- (a//3)*(b//3))%3)+3*(((a%3)*(b//3)+(a//3)*(b%3))%3)
  else:raise ValueError((p,m))
  self.inv={a:next(b for b in range(1,self.q) if self.mul(a,b)==1) for a in range(1,self.q)}
 def neg(self,a):
  return next(x for x in range(self.q) if self.add(a,x)==0)
 def sub(self,a,b):return self.add(a,self.neg(b))

# Some characteristics in every residue type and extension degrees.
for p,m,exhaust in [(2,1,True),(2,2,True),(2,3,False),(2,4,False),(3,1,True),(3,2,False),(5,1,True),(7,1,False)]:
 F=Field(p,m);q=F.q
 vectors=[(x,y) for x in range(q) for y in range(q) if (x,y)!=(0,0)]
 lines=set()
 for x,y in vectors:
  if x:
   inv=F.inv[x];lines.add((1,F.mul(y,inv)))
  else:lines.add((0,1))
 forms=[(a,b,c) for a,b,c in product(range(q),repeat=3) if F.sub(F.mul(a,c),F.mul(b,b))!=0 and (p!=2 or (a,c)!=(0,0))]
 if not exhaust:
  # Deterministic spread, including diagonal and non-diagonal Gram matrices.
  forms=forms[::max(1,len(forms)//(2 if q==16 else 5))][:(2 if q==16 else 5)]
 checked=0
 for a,b,c in forms:
  def form(v,w):
   z=F.mul(a,F.mul(v[0],w[0]))
   z=F.add(z,F.mul(b,F.add(F.mul(v[0],w[1]),F.mul(v[1],w[0]))))
   z=F.add(z,F.mul(c,F.mul(v[1],w[1])))
   return z
  eps=sum(form(x,x)==0 for x in lines)
  assert eps in ((1,) if p==2 else (0,2)),(q,(a,b,c),eps)
  basis=[(v,w) for v,w in product(vectors,repeat=2) if form(v,w)==0 and F.sub(F.mul(v[0],w[1]),F.mul(v[1],w[0]))!=0]
  assert len(basis)==(q-1)**2*(q+1-eps),(q,(a,b,c),len(basis),eps)
  for u in vectors:
   cnt=[0,0,0]
   for v,w in basis:
    det=F.sub(F.mul(v[0],w[1]),F.mul(v[1],w[0]));d=F.inv[det]
    x=F.mul(F.sub(F.mul(u[0],w[1]),F.mul(u[1],w[0])),d)
    y=F.mul(F.sub(F.mul(v[0],u[1]),F.mul(v[1],u[0])),d)
    cnt[(x!=0)+(y!=0)]+=1
   k1=2*(q-1)**2 if form(u,u)!=0 else 0
   assert cnt==[0,k1,len(basis)-k1],(q,(a,b,c),u,cnt,k1)
   checked+=1
 print('field=',(p,m),'q=',q,'Gram_forms=',len(forms),'(B,u)_cases=',checked,'VERIFY_OK')
print('VERIFY_OK')
