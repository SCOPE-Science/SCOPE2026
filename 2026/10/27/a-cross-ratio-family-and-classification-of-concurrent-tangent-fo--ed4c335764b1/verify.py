"""Exact symbolic checks for a four-conic family; requires sympy >= 1.12.

This program checks the all-parameter syzygy and algebraic factors used in
the geometric proof. It does not substitute finite examples for the proof.
"""
import sympy as s

x,y,z,t=s.symbols('x y z t')
B=[(t-1)*x*(x-t*z), -t*(t-1)*x*z,
   -t*(t-1)*z*(x-z), t*(x-z)*(x-t*z)]
F=[y*y+b for b in B]
f=s.prod(F)
A=(-t*(t-1)*x**3+2*t*(t-1)*(t+1)*x*x*z
   -2*t*x*y*y-3*t*t*(t-1)*x*z*z+2*t*y*y*z)
C=(3*t*(t-1)*x*x*z-2*x*y*y
   -2*t*(t-1)*(t+1)*x*z*z+2*t*y*y*z+t*t*(t-1)*z**3)
assert s.factor(A*s.diff(f,x)+C*s.diff(f,z))==0
assert s.factor(B[0]-B[1]-(t-1)*x*x)==0
assert s.factor(B[1]-B[2]+t*(t-1)*z*z)==0
assert s.factor(B[2]-B[3]+t*(x-z)**2)==0
assert s.factor(B[3]-B[0]-(x-t*z)**2)==0
assert s.factor(B[0]-B[2]-(t-1)*(x*x-t*z*z))==0
assert s.factor(B[1]-B[3]+t*(x*x-2*x*z+t*z*z))==0
# For each opposite pair, the base conic is nonzero at every zero of
# the difference. These nonzero resultants also exclude a triple point.
for i,j in [(0,2),(1,3)]:
 h=s.expand((B[i]-B[j]).subs(z,1))
 for k in (i,j):
  result=s.factor(s.resultant(B[k].subs(z,1),h,x))
  assert result!=0
  assert s.factor(result.subs(t,0))==0
  assert s.factor(result.subs(t,1))==0
# Four contact-point incidence columns, with complementary nonzero entries.
P=[(0,1),(1,0),(1,1),(t,1)]
for p,(i,j) in zip(P,[(0,1),(1,2),(2,3),(3,0)]):
 vals=[s.factor(b.subs({x:p[0],z:p[1]})) for b in B]
 assert vals[i]==vals[j]==0
 assert all(vals[k]!=0 for k in range(4) if k not in (i,j))
print('VERIFY_OK: polynomial syzygy, four A7 contacts, opposite pairs, no triples')
