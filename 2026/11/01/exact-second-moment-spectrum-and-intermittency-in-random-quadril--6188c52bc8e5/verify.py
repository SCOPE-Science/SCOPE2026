"""Exact symbolic and numerical checks for random quadrilateral subdivision.
Run with Python 3 and SymPy; all assertions are self-contained.
"""
import random
import sympy as S

s,t=S.symbols('s t',real=True)
u=S.symbols('u0:4',real=True)
V=[S.Matrix(v) for v in [(0,0),(1,0),(s,t),(0,1)]]
P=[V[i]+u[i]*(V[(i+1)%4]-V[i]) for i in range(4)]
def wedge(a,b):return S.det(S.Matrix.hstack(a,b))
def area(z):return S.expand(sum(wedge(z[i],z[(i+1)%4]) for i in range(4))/2)
def corners(z):return [S.expand(wedge(z[i]-z[(i-1)%4],z[(i+1)%4]-z[i])/2) for i in range(4)]
def imbalance(z):
 c=corners(z)
 return S.expand((c[0]-c[2])**2+(c[1]-c[3])**2)
def avg(expr):
 p=S.Poly(S.expand(expr),*u)
 out=S.Integer(0)
 for exponents, coefficient in p.terms():
  out+=coefficient*S.prod(S.Rational(1,k+1) for k in exponents)
 return S.factor(out)
A=area(V);D=imbalance(V)
assert S.simplify(A-(s+t)/2)==0
assert S.simplify(D-((2-s-t)**2+(t-s)**2)/4)==0
assert S.simplify(avg(area(P))-A/2)==0
A2=avg(area(P)**2)
D1=avg(imbalance(P))
assert S.factor(A2-S.Rational(37,144)*A*A-S.Rational(7,288)*D)==0
assert S.factor(D1-S.Rational(7,72)*A*A-S.Rational(1,16)*D)==0
print('Exact affine-normal-form integrations: PASS')

M=S.Matrix([[S.Rational(37,144),S.Rational(7,288)],[S.Rational(7,72),S.Rational(1,16)]])
x=S.symbols('x')
assert S.simplify(M.charpoly(x).as_expr() - (x-(23+7*S.sqrt(5))/144)*(x-(23-7*S.sqrt(5))/144))==0
lamplus=(23+7*S.sqrt(5))/144;lamminus=(23-7*S.sqrt(5))/144
cp=S.Rational(1,2)+1/S.sqrt(5);cm=S.Rational(1,2)-1/S.sqrt(5)
for n in range(0,10):
 assert S.simplify((M**n)[0,0]-cp*lamplus**n-cm*lamminus**n)==0
 assert S.simplify((M**n)[0,1])>=0 # positive cone, initial D>=0
delta=S.symbols('delta',nonnegative=True)
cp_delta=cp+delta/(4*S.sqrt(5)); cm_delta=cm-delta/(4*S.sqrt(5))
assert S.simplify(M.det()-S.Rational(71,5184))==0
for n in range(0,10):
 exact=(M**n*S.Matrix([1,delta]))[0]
 spectral=cp_delta*lamplus**n+cm_delta*lamminus**n
 assert S.simplify(exact-spectral)==0
 assert S.simplify((M**n)[0,1]-(lamplus**n-lamminus**n)/(4*S.sqrt(5)))==0
print('Matrix eigenvalues, all-shape moments, and strict shape-gap coefficient: PASS')

# Independent finite-trajectory simulation uses a square and computes moments.
rng=random.Random(10387)
for rounds in (1,3,5):
 moments=[0.,0.]
 N=28000
 for _ in range(N):
  z=[(1.,0.),(0.,1.),(-1.,0.),(0.,-1.)]
  for _ in range(rounds):
   f=[rng.random() for i in range(4)]
   z=[((1-f[i])*z[i][0]+f[i]*z[(i+1)%4][0],
       (1-f[i])*z[i][1]+f[i]*z[(i+1)%4][1]) for i in range(4)]
  ar=sum(z[i][0]*z[(i+1)%4][1]-z[(i+1)%4][0]*z[i][1] for i in range(4))/2
  moments[0]+=ar; moments[1]+=ar*ar
 target_mean=2**(1-rounds)
 target_s2=float(4*(cp*lamplus**rounds+cm*lamminus**rounds))
 assert abs(moments[0]/N-target_mean)<0.025
 assert abs(moments[1]/N-target_s2)<0.04
 print(f'Monte Carlo t={rounds}: mean={moments[0]/N:.8f} vs {target_mean:.8f}; second={moments[1]/N:.8f} vs {target_s2:.8f}')
print('ALL_QUADRILATERAL_MOMENT_CHECKS_PASSED')
