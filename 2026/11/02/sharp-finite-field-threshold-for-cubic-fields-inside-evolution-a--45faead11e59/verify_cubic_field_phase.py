"""Exact checks for the cubic finite-field evolution-envelope transition.

Uses GF(3^3) and GF(4^3) arithmetic implemented here from defining
irreducible cubics; no external computational algebra package is needed.
"""
from itertools import product

class CubicField:
    def __init__(self, q):
        assert q in (3,4)
        self.q=q
        self.zero=(0,0,0)
        self.one=(1,0,0)
        self.t=(0,1,0)
        self.elems=list(product(range(q),repeat=3))
    def addk(self,a,b):return (a+b)%3 if self.q==3 else a^b
    def negk(self,a):return (-a)%3 if self.q==3 else a
    def subk(self,a,b):return self.addk(a,self.negk(b))
    def mulk(self,a,b):
        if self.q==3:return a*b%3
        z=0
        if b&1:z^=a
        if b&2:z^=a<<1
        if z&4:z^=7  # x^2+x+1, as binary 0b111
        return z
    def invk(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mulk(a,b)==1)
    def add(self,x,y):return tuple(self.addk(a,b) for a,b in zip(x,y))
    def neg(self,x):return tuple(self.negk(a) for a in x)
    def sub(self,x,y):return self.add(x,self.neg(y))
    def scale(self,a,x):return tuple(self.mulk(a,c) for c in x)
    def mul(self,x,y):
        c=[0]*5
        for i in range(3):
            for j in range(3):
                c[i+j]=self.addk(c[i+j],self.mulk(x[i],y[j]))
        # t^3=t+1, irreducible over GF(3) and GF(4).
        for i in (4,3):
            a=c[i]
            c[i]=0
            c[i-2]=self.addk(c[i-2],a)
            c[i-3]=self.addk(c[i-3],a)
        return tuple(c[:3])
    def power(self,x,n):
        y=self.one
        while n:
            if n&1:y=self.mul(y,x)
            x=self.mul(x,x); n//=2
        return y
    def inv(self,x):
        assert x!=self.zero
        y=self.power(x,self.q**3-2)
        assert self.mul(x,y)==self.one
        return y
    def rank(self,vecs):
        a=[list(row) for row in vecs]
        r=0
        for col in range(len(a[0])):
            pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
            if pivot is None:continue
            a[r],a[pivot]=a[pivot],a[r]
            scale=self.invk(a[r][col])
            a[r]=[self.mulk(scale,z) for z in a[r]]
            for i in range(len(a)):
                if i!=r and a[i][col]:
                    coeff=a[i][col]
                    a[i]=[self.subk(u,self.mulk(coeff,v)) for u,v in zip(a[i],a[r])]
            r+=1
            if r==len(a):break
        return r

# Exhaust all 11,232 ordered bases of GF(27) over GF(3).
F=CubicField(3)
assert all(F.mul(x,y)!=F.zero for x in F.elems if x!=F.zero for y in F.elems if y!=F.zero)
assert F.power(F.t,3)==F.add(F.t,F.one)
counts={2:0,3:0}
basis_count=0
for x in F.elems:
 for y in F.elems:
  for z in F.elems:
   if F.rank((x,y,z))!=3:continue
   basis_count+=1
   c=(F.mul(x,y),F.mul(x,z),F.mul(y,z))
   rank=F.rank(c)
   assert rank in (2,3)
   counts[rank]+=1
   if rank==2:
    # Every dependence has three nonzero coefficients; no pair proportional.
    for a,b in product(range(3),repeat=2):
     for d in range(3):
      if (a,b,d)==(0,0,0):continue
      relation=F.add(F.add(F.scale(a,c[0]),F.scale(b,c[1])),F.scale(d,c[2]))
      if relation==F.zero:assert a and b and d
assert basis_count==11232
for r1,r2,r3 in product((1,2),repeat=3):
 nonzero_patterns=set()
 for a,b,c in product(range(3),repeat=3):
  p=(F.mulk(a,b),F.mulk(a,c),F.mulk(b,c))
  if p==(0,0,0):continue
  if F.addk(F.addk(F.mulk(r1,p[0]),F.mulk(r2,p[1])),F.mulk(r3,p[2])):continue
  normalized=tuple(F.mulk(F.invk(next(v for v in p if v)),v) for v in p)
  nonzero_patterns.add(normalized)
 assert len(nonzero_patterns)==1
print('GF27_ORDERED_BASES',basis_count,'RANK2',counts[2],'RANK3',counts[3])
print('GF3_CROSS_PATTERN_PROJECTIVE_POINTS_PER_NONZERO_NORMAL=1')

# Construct the five-dimensional evolution envelope of GF(64) over GF(4).
F=CubicField(4)
assert all(F.mul(x,y)!=F.zero for x in F.elems if x!=F.zero for y in F.elems if y!=F.zero)
base=F
z=F.mul(F.t,F.inv(F.sub(F.t,F.one)))
basis=(F.one,F.t,z)
coords={}
for a,b,c in product(range(4),repeat=3):
 x=F.add(F.add(F.scale(a,basis[0]),F.scale(b,basis[1])),F.scale(c,basis[2]))
 assert x not in coords
 coords[x]=(a,b,c)
assert len(coords)==64
u,v=2,3
cu=F.mulk(u,F.invk(F.subk(u,1)))
cv=F.mulk(v,F.invk(F.subk(v,1)))
beta_u=(1,u,cu)
beta_v=(1,v,cv)
det=F.subk(F.mulk(u,cv),F.mulk(v,cu))
assert det!=0
c12=F.mul(basis[0],basis[1]); c13=F.mul(basis[0],basis[2]); c23=F.mul(basis[1],basis[2])
vu=F.scale(F.invk(det),F.sub(F.scale(cv,c12),F.scale(v,c13)))
vv=F.scale(F.invk(det),F.sub(F.scale(u,c13),F.scale(cu,c12)))
assert F.add(F.scale(F.mulk(u,cu),vu),F.scale(F.mulk(v,cv),vv))==c23

def phi(x):
 a,b,c=coords[x]
 return (a,b,c,
         F.addk(F.addk(a,F.mulk(b,u)),F.mulk(c,cu)),
         F.addk(F.addk(a,F.mulk(b,v)),F.mulk(c,cv)))
assert len({phi(x) for x in F.elems})==64
squares=[]
for i in range(3):
 x=F.sub(F.sub(F.mul(basis[i],basis[i]),F.scale(F.mulk(beta_u[i],beta_u[i]),vu)),F.scale(F.mulk(beta_v[i],beta_v[i]),vv))
 squares.append(phi(x))
squares.extend((phi(vu),phi(vv)))

def emul(x,y):
 out=[0]*5
 for i in range(5):
  c=F.mulk(x[i],y[i])
  for j in range(5):out[j]=F.addk(out[j],F.mulk(c,squares[i][j]))
 return tuple(out)
image=set(phi(x) for x in F.elems)
for x,y in product(F.elems,repeat=2):assert emul(phi(x),phi(y))==phi(F.mul(x,y))
for e_i,x in product(range(5),F.elems):
 vec=tuple(1 if i==e_i else 0 for i in range(5))
 assert emul(vec,phi(x)) in image
assert F.rank((vu,vv))==2
print('GF64_FIELD_EXTENSION_OVER_GF4_OK')
print('GF4_FIVE_DIMENSIONAL_EVOLUTION_IDEAL_EMBEDDING=VERIFIED')
print('VERIFY_OK')
