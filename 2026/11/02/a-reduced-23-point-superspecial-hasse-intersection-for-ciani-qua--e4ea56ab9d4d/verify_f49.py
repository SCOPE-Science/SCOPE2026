"""Independent exact GF(49) enumerator and Hasse transversality checker."""
from collections import Counter
from itertools import permutations
P=7
# The integer u+7*v represents u+v*alpha, where alpha^2=-1.
def add(x,y):return ((x%P+y%P)%P)+P*((x//P+y//P)%P)
def neg(x):return (-(x%P))%P+P*((-(x//P))%P)
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x%P,x//P;c,d=y%P,y//P
 return (a*c-b*d)%P+P*((a*d+b*c)%P)
def powf(x,n):
 z=1
 while n:
  if n&1:z=mul(z,x)
  x=mul(x,x);n>>=1
 return z

def F(u,v,w):
 A=sub(mul(u,u),4);C=sub(mul(v,v),4)
 B=sub(mul(2,mul(u,v)),mul(4,w))
 return mul(B,sub(mul(B,B),mul(A,C)))
def discriminant(a,b,c):
 squares=[mul(x,x) for x in (a,b,c)]
 D=sub(sub(add(add(*squares[:2]),squares[2]),mul(mul(a,b),c)),4)
 for x in squares:D=mul(D,sub(x,4))
 return D

def det3(m):
 return add(sub(mul(m[0][0],sub(mul(m[1][1],m[2][2]),mul(m[1][2],m[2][1]))),mul(m[0][1],sub(mul(m[1][0],m[2][2]),mul(m[1][2],m[2][0])))),mul(m[0][2],sub(mul(m[1][0],m[2][1]),mul(m[1][1],m[2][0]))))

def differential(u,v,w):
 # F(u,v,w)=B(B^2-A*C), B=2uv-4w,
 # A=u^2-4,C=v^2-4, derivative dF=(3B^2-AC)dB-B(C dA+A dC)
 A=sub(mul(u,u),4);C=sub(mul(v,v),4);B=sub(mul(2,mul(u,v)),mul(4,w))
 T=sub(mul(3,mul(B,B)),mul(A,C))
 return [sub(mul(T,mul(2,v)),mul(B,mul(C,mul(2,u)))),sub(mul(T,mul(2,u)),mul(B,mul(A,mul(2,v)))),mul(T,3)] # -4 = 3 mod7

def jacobian(a,b,c):
 x=differential(a,b,c);y=differential(a,c,b);z=differential(b,c,a)
 return [x,[y[0],y[2],y[1]],[z[2],z[0],z[1]]]

sols=set();counts=Counter();jvals=[]
for a in range(49):
 for b in range(49):
  for c in range(49):
   if not discriminant(a,b,c):continue
   h=sum(1 for x in (F(a,b,c),F(a,c,b),F(b,c,a)) if x==0)
   counts[h]+=1
   if h==3:
    sols.add((a,b,c));jvals.append(det3(jacobian(a,b,c)))
assert len(sols)==23 and all(jvals),('number of points / Jacobian rank',len(sols),Counter(jvals))
assert len(sols)==counts[3]
assert counts==Counter({0:89912,1:11184,2:588,3:23}),counts
signs=[(1,1,1),(1,6,6),(6,1,6),(6,6,1)]
def orbit(q):
 return {tuple(mul(p[i],sg[i]) for i in range(3)) for p in set(permutations(q)) for sg in signs}
representatives=[(0,0,0),(0,0,1),(3,3,4),(3,7,7)]
expected=[1,6,4,12]
orbits=[orbit(q) for q in representatives]
assert list(map(len,orbits))==expected
assert all(o<=sols for o in orbits)
assert len(set.union(*orbits))==23
assert all(orbits[i].isdisjoint(orbits[j]) for i in range(4) for j in range(i+1,4))
print('VERIFY_F49_OK: 23 smooth solutions, orbit sizes 1/6/4/12, all 23 Jacobians nonsingular')
