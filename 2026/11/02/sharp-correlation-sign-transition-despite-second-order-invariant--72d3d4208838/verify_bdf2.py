"""Exact stationary autocovariance checks for scalar BDF2--Maruyama.

Requires Python 3.10+ and SymPy 1.10+. The exact theorem is proved in
RESULT.md; this script independently checks covariance algebra and examples.
"""
from fractions import Fraction as F
import sympy as s

z = s.symbols('z', positive=True)
c = z + s.Rational(3, 2)
T = s.Matrix([[2/c, -s.Rational(1,2)/c, -s.Rational(1,2)/c],
              [1, 0, 0], [0, 0, 0]])
b = s.Matrix([s.Rational(3,2)/c, 0, 1])
u = s.symbols('u0:6')
S = s.Matrix([[u[0],u[1],u[2]], [u[1],u[3],u[4]], [u[2],u[4],u[5]]])
e = S-T*S*T.T-b*b.T
entries=[e[i,j] for i in range(3) for j in range(i,3)]
ans=s.solve(entries, list(u), dict=True)
assert len(ans)==1
S=s.simplify(S.subs(ans[0]))
assert all(s.cancel(v)==0 for v in S-T*S*T.T-b*b.T)
V=(5*z+4)/(2*z*(z+1)*(z+4))
q=(12+11*z-3*z**2)/((2*z+3)*(5*z+4))
assert s.cancel(S[0,0]-V)==0
assert s.cancel(S[0,1]-V*q)==0
assert s.cancel(S[0,2]-s.Rational(3,2)/c)==0
assert s.factor(2*z*V-1)== -z**2/((z+1)*(z+4))
assert s.factor(2*z*V - 2/(z+2))==z*(3*z+4)/((z+1)*(z+2)*(z+4))
assert s.cancel((c*q*q-2*q+s.Rational(1,2))-z**2*(z+4)*(9*z+8)/(2*(2*z+3)*(5*z+4)**2))==0
assert s.cancel((q - 2/(2*z+3))+(z+1)*(3*z-4)/((2*z+3)*(5*z+4)))==0
assert s.simplify(q.subs(z,s.Rational(1,2))-s.Rational(1,2))>0

nchecks=0
for num in range(1,21):
 for den in (1,2,4,7,10,25):
  zz=F(num,den)
  cc=zz+F(3,2)
  c0=F(5*zz+4,2*zz*(zz+1)*(zz+4))
  qq=F(12+11*zz-3*zz**2,(2*zz+3)*(5*zz+4))
  cv=[c0,qq*c0]
  for k in range(2,25):
   cv.append((2*cv[-1]-F(1,2)*cv[-2])/cc)
  for k in range(2,25):
   assert cc*cv[k]==2*cv[k-1]-F(1,2)*cv[k-2]
   nchecks+=1
  assert cv[0]>0
  assert 0< 2*zz*cv[0]<1
  assert 2*zz*cv[0]>F(2,2+zz)
  if zz<=F(1,2):
   assert all(v>0 for v in cv)
   nchecks+=len(cv)
  if zz==1:
   assert cv[0]==F(9,20)
   assert cv[1]==F(1,5)
   assert cv[2]==F(7,100)
   assert cv[3]==F(2,125)
   assert cv[4]==F(-3,2500)
print(f'VERIFY_OK Lyapunov symbolic identities, variance inequalities, 120 exact parameters, {nchecks} rational covariance checks')
