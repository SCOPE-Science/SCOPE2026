"""Exact characteristic-two computations for the cubic tangent section of the Barth--Nieto quintic."""
from itertools import product, combinations
from collections import Counter
import sympy as sp

# GF(4)=F2[a]/(a^2+a+1); bit encoding 0,1,a,a+1.
def add(a,b):return a^b
def mul(a,b):
 z=0
 for i in range(2):
  if (b>>i)&1:z^=a<<i
 for i in (2,):
  if (z>>i)&1: z^=0b111<<(i-2)
 return z
assert [mul(2,a) for a in range(4)]==[0,2,3,1]
def inv(a):
 for b in range(1,4):
  if mul(a,b)==1:return b
 raise ValueError
def norm(v):
 c=next(a for a in v if a)
 r=inv(c)
 return tuple(mul(a,r) for a in v)
def f(v):
 z=0
 for i,j in combinations(range(4),2):
  z=add(z,mul(mul(v[i],v[j]),add(v[i],v[j])))
 return z

def plus(v,w):return tuple(add(a,b) for a,b in zip(v,w))
def times(v,a):return tuple(mul(a,b) for b in v)
ps=sorted({norm(v) for v in product(range(4),repeat=4) if any(v)})
assert len(ps)==85
Ps={p for p in ps if f(p)==0}
assert len(Ps)==45,len(Ps)
lines=set()
for a,b in combinations(ps,2):
 lin=tuple(sorted({norm(plus(times(a,c),times(b,d))) for c,d in product(range(4),repeat=2) if c or d}))
 assert len(lin)==5
 lines.add(lin)
assert len(lines)==357
lying=sorted(L for L in lines if set(L)<=Ps)
assert len(lying)==27,len(lying)
def pow2(v):return tuple(mul(x,x) for x in v)
def frobline(L):return tuple(sorted(norm(pow2(v)) for v in L))
seen=set();cycles=[]
for L in lying:
 if L in seen:continue
 c=[];u=L
 while u not in seen:
  seen.add(u);c.append(u);u=frobline(u)
 assert u==L
 cycles.append(len(c))
assert Counter(cycles)=={1:15,2:6},Counter(cycles)
Ps2={v for v in Ps if norm(pow2(v))==v}
assert len(Ps2)==15
print('GF4_POINTS_ON_CUBIC=45;GF2_POINTS=15')
print('GF4_LINES=27;FROBENIUS_CYCLES_OF_LINES=(1^15,2^6)')
# Exact local equation from Sigma5(1+z), z5=0, Sigma1(z)=0 in characteristic two.
x=sp.symbols('x0:4');z=list(x)+[sum(x)]
E3=sum(z[i]*z[j]*z[k] for i,j,k in combinations(range(5),3))
E5=sp.prod(z)
base=sum(sp.prod(Y[j] for j in range(6) if j!=i) for i in range(6) for Y in [[1+zz for zz in z]+[1]])
assert sp.Poly(base-(E3+E5),*x,modulus=2).is_zero
Q=sum(x[i]*x[j]*(x[i]+x[j]) for i,j in combinations(range(4),2))
assert sp.Poly(E3-Q,*x,modulus=2).is_zero
assert sp.Poly(sum(y**3 for y in z)-E3,*x,modulus=2).is_zero
print('SEGRE_CUBIC_BASE_EQUALS_QUINTIC_TANGENT_CUBIC_OK')
# partial derivatives of tangent form Q are (sum of the other 3 coordinates)^2.
for i in range(4):
 other=sum(x[j] for j in range(4) if j!=i)
 assert sp.Poly(sp.diff(Q,x[i])-other**2,*x,modulus=2).is_zero
print('LOCAL_EQUATION=Q3+PRODUCT(x0,x1,x2,x3,x0+x1+x2+x3)')
print('Q3_SMOOTH_OVER_ALGEBRAIC_CLOSURE=YES_BY_LINEAR_PARTIAL_SQUARES')
# F2 special fiber has all 31 points of P4; 16 are singular.
def sig5(y):
 return sum(__import__('math').prod(y[j] for j in range(6) if j!=i) for i in range(6))%2
def deriv(y,i):
 return sum(__import__('math').prod(y[j] for j in inds) for inds in combinations([j for j in range(6) if j!=i],4))%2
xs=[];sg=[]
for coords in product(range(2),repeat=5):
 y=tuple(coords)+(sum(coords)%2,)
 if not any(y):continue
 assert sig5(y)==0
 xs.append(y)
 if len({deriv(y,i) for i in range(6)})==1: sg.append(y)
assert len(xs)==31 and len(sg)==16
assert all((sum(1 for t in y if t==0)>=4 or all(t==1 for t in y)) for y in sg)
print('F2_QUINTIC_POINTS=31;F2_SINGULAR_POINTS=16;F2_SMOOTH_POINTS=15')
print('VERIFY_OK')
