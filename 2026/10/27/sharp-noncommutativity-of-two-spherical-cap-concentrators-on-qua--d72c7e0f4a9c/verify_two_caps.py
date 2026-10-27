"""Exact rational certificate for the sharp degree-two spherical-cap commutator bound.
Run: python verify_two_caps.py   (requires SymPy)
"""
from fractions import Fraction as Q
from math import comb
import sympy as S

c,d,t=S.symbols('c d t')

def gap0(x): return S.Rational(5,16)*x*(1-x*x)*(3*x*x+1)
def gap1(x): return S.Rational(15,16)*x*(1-x*x)**2
A,B,C,D=gap0(c),gap1(c),gap0(d),gap1(d)

# Directly verify all three zonal eigenvalue differences by normalized integration.
u=S.symbols('u',real=True)
densities=[S.Rational(5,8)*(3*u*u-1)**2,
           S.Rational(15,4)*u*u*(1-u*u),
           S.Rational(15,16)*(1-u*u)**2]
levels=[S.integrate(f,(u,c,1)) for f in densities]
assert all(S.simplify(S.integrate(f,(u,-1,1))-1)==0 for f in densities)
assert S.simplify(levels[0]-levels[2]-gap0(c))==0
assert S.simplify(levels[1]-levels[2]-gap1(c))==0

# Symbolic rotation on the space of real trace-free symmetric 3x3 matrices.
x,z=S.symbols('x z',real=True)
rot=S.Matrix([
 [(3*x*x-1)/2, -S.sqrt(3)*x*z, 0, S.sqrt(3)*z*z/2, 0],
 [S.sqrt(3)*x*z, x*x-z*z, 0, -x*z, 0],
 [0, 0, x, 0, -z],
 [S.sqrt(3)*z*z/2, x*z, 0, (1+x*x)/2, 0],
 [0, 0, z, 0, x]])
relation=S.Poly(z*z-(1-x*x),z,domain='EX')
def reduce_circle(expression):
 return S.simplify(S.rem(S.Poly(S.expand(expression),z,domain='EX'),relation).as_expr())
assert all(reduce_circle(q)==0 for q in (rot.T*rot-S.eye(5)))
rotated=rot*S.diag(gap0(d),gap1(d),gap1(d),0,0)*rot.T
skew=S.diag(gap0(c),gap1(c),gap1(c),0,0)*rotated-rotated*S.diag(gap0(c),gap1(c),gap1(c),0,0)
assert all(reduce_circle(skew[i,j])==0 for i in (0,1,3) for j in (2,4))
# The two parity blocks of the real skew commutator have strengths L and R.
X01sq=3*t*(1-t)*(A-B)**2*(C*(3*t-1)/2-D*(2*t-1))**2
X03sq=3*(1-t)**2*A**2*(C*(3*t-1)/4-D*t)**2
X13sq=t*(1-t)*B**2*(S.Rational(3,2)*C*(1-t)+D*(2*t-1))**2
Lsq=S.expand(X01sq+X03sq+X13sq)
R2=S.expand(B**2*D**2*t*(1-t))
# Verify every squared commutator entry against its derived polynomial.
for (i,j),f in [((0,1),X01sq),((0,3),X03sq),
                ((1,3),X13sq),((2,4),R2)]:
 assert reduce_circle(skew[i,j]**2-f.subs(t,x*x))==0
K=S.Rational(9,250)
F=S.Poly(K*K-Lsq,c,d,t)
assert F.degree_list()==(10,10,4)

shape=tuple(i+1 for i in F.degree_list())
coef={}
for powers,value in F.terms():
 v=Q(int(value.p),int(value.q))
 for i in range(powers[0],shape[0]):
  fi=Q(comb(i,powers[0]),comb(shape[0]-1,powers[0]))
  for j in range(powers[1],shape[1]):
   fj=Q(comb(j,powers[1]),comb(shape[1]-1,powers[1]))
   for k in range(powers[2],shape[2]):
    fk=Q(comb(k,powers[2]),comb(shape[2]-1,powers[2]))
    key=(i,j,k)
    coef[key]=coef.get(key,Q(0))+v*fi*fj*fk
assert len(coef)==shape[0]*shape[1]*shape[2]

def bisect_bernstein(B, axis):
 """Exact de Casteljau bisection; returns Bernstein nets for two half-boxes."""
 out=[]
 dims=list(shape)
 for side in (0,1): out.append({})
 # Slice along axis, keeping the other two indices fixed.
 for i in range(dims[(axis+1)%3]):
  for j in range(dims[(axis+2)%3]):
   seq=[]
   for k in range(dims[axis]):
    key=[0,0,0]; key[axis]=k;key[(axis+1)%3]=i;key[(axis+2)%3]=j
    seq.append(B[tuple(key)])
   triangle=[seq]
   while len(triangle[-1])>1:
    row=triangle[-1]
    triangle.append([(row[m]+row[m+1])/2 for m in range(len(row)-1)])
   first=[row[0] for row in triangle]
   last=[triangle[len(seq)-1-k][k] for k in range(len(seq))]
   for k in range(dims[axis]):
    key=[0,0,0];key[axis]=k;key[(axis+1)%3]=i;key[(axis+2)%3]=j
    out[0][tuple(key)]=first[k]
    out[1][tuple(key)]=last[k]
 return out

# Adaptive bisection is purely a way of finding a finite exact certificate.
# A node is accepted ONLY when each exact Bernstein coefficient is positive.
stack=[(coef,0,())]; nodes=0; leaves=[]; deepest=0
while stack:
 net,depth,path=stack.pop()
 nodes+=1
 m=min(net.values())
 if m>0:
  leaves.append((path,m))
  deepest=max(deepest,depth)
  continue
 assert depth<24, 'No finite certificate found before the safety depth'
 axis=(0,1,2)[depth%3]
 left,right=bisect_bernstein(net,axis)
 stack.append((right,depth+1,path+((axis,1),)))
 stack.append((left,depth+1,path+((axis,0),)))
assert len(leaves)>0
assert min(v for _,v in leaves)>Q(1,40000)
print('COVERING BOXES',[[list(z) for z in path] for path,v in leaves])
print('EXACT BERNSTEIN PASS', 'nodes',nodes,'leaves',len(leaves),'depth',deepest,
      'minimum_leaf_coefficient',float(min(v for _,v in leaves)))
# Independently identify the exact optimizer of the other, two-dimensional skew block.
y=S.symbols('y',real=True)
g=gap1(y)
assert S.simplify(S.diff(g,y)-S.Rational(15,16)*(1-y*y)*(1-5*y*y)) == 0
assert S.simplify(g.subs(y,S.sqrt(5)/5)**2 / 2 - K)==0
assert S.simplify(t*(1-t)-S.Rational(1,4)+(t-S.Rational(1,2))**2)==0
print('TWO-BLOCK SHARP NORM',str(K),'attained_at_cap_cosine', '1/sqrt(5)', 'axes_dot','1/sqrt(2)')
