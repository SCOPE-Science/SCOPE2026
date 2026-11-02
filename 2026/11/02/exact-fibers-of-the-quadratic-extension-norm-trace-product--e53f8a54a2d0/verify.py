from collections import Counter
from functools import lru_cache

class Field:
 def __init__(self,p,mod):
  self.p=p;self.mod=tuple(mod);self.d=len(mod)-1; self.sz=p**self.d
  self.powers=[p**i for i in range(self.d)]
  self.vec=[tuple((z//self.powers[i])%p for i in range(self.d)) for z in range(self.sz)]
 def add(self,a,b):
  return sum(((x+y)%self.p)*v for x,y,v in zip(self.vec[a],self.vec[b],self.powers))
 def neg(self,a):
  return sum((-x%self.p)*v for x,v in zip(self.vec[a],self.powers))
 @lru_cache(None)
 def mul(self,a,b):
  p=self.p;d=self.d; cs=[0]*(2*d-1)
  for i,x in enumerate(self.vec[a]):
   for j,y in enumerate(self.vec[b]):cs[i+j]=(cs[i+j]+x*y)%p
  for k in range(2*d-2,d-1,-1):
   c=cs[k]
   for j in range(d):cs[k-d+j]=(cs[k-d+j]-c*self.mod[j])%p
  return sum((cs[i]%p)*self.powers[i] for i in range(d))
 def pow(self,a,n):
  x=1
  while n:
   if n&1:x=self.mul(x,a)
   a=self.mul(a,a);n//=2
  return x

def run():
 # prime power q, extension polynomial over prime p of degree 2*m, low-to-high monic
 cases=[(2,[1,1,1]),(3,[1,0,1]),(4,[1,1,0,0,1]),(5,[2,0,1]),(7,[1,0,1]),(8,[1,1,0,0,0,0,1]),(9,[2,1,0,0,1]),(11,[1,0,1]),(13,[2,0,1]),(16,[1,0,1,1,1,0,0,0,1])]
 total=0
 for q,mod in cases:
  p=next(x for x in range(2,q+1) if q%x==0)
  f=Field(p,mod)
  total+=f.sz
  # test field no zero divisors by Fermat
  bad=[x for x in range(1,f.sz) if f.pow(x,f.sz-1)!=1]
  assert not bad,(q,mod,bad[:6])
  sub={x for x in range(f.sz) if f.pow(x,q)==x}
  assert len(sub)==q,(q,len(sub))
  hist=Counter()
  for x in range(f.sz):
   xq=f.pow(x,q)
   t=f.add(x,xq); n=f.mul(x,xq); y=f.mul(t,n)
   assert y in sub
   hist[y]+=1
  zeros=hist[0]
  counts=Counter(hist[y] for y in sub if y!=0)
  variance=sum((hist[y]-q)**2 for y in sub if y!=0)
  expected=0 if (q-1)%3 else 2*q*(q-1)
  assert zeros==q
  assert variance==expected,(q,variance,expected)
  if (q-1)%3:
   assert counts==Counter({q:q-1}),(q,counts)
  else:
   cubic_classes={}
   for y in sub-{0}:
    label=f.pow(y,(q-1)//3)
    cubic_classes.setdefault(label,set()).add(hist[y])
   assert len(cubic_classes)==3 and all(len(v)==1 for v in cubic_classes.values()),(q,cubic_classes)
  assert sum(hist[y]>0 for y in sub)==(3 if q==4 else q),q
  if q==4:
   assert sorted(counts.items())==[(0,1),(6,2)]
   assert hist[1]==0
  print('q',q,'nonzero fiber histogram',sorted(counts.items()),'variance',variance)

 print('VERIFY_OK cases=%d inputs=%d' % (len(cases),total))

if __name__=='__main__':run()
