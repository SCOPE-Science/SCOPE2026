"""Standalone exact arithmetic checks for rectangular rook diffusion RK4."""
from fractions import Fraction
from math import factorial
import sympy as S
p,q,h,N = S.symbols('p q h N', real=True)
R = lambda v: sum((-v*h)**k/S.factorial(k) for k in range(5))
A = S.factor((1+(q-1)*R(q)-R(p)-(q-1)*R(p+q))/(p*q))
B = S.factor((1+(p-1)*R(p)-R(q)-(p-1)*R(p+q))/(p*q))
C = S.factor((1-R(p)-R(q)+R(p+q))/(p*q))
D = S.factor((1+(p-1)*R(p)+(q-1)*R(q)+(p-1)*(q-1)*R(p+q))/(p*q))
a = p/2+q-1
b = p**2/6+(p+q)*(q-1)/2
c = p**3/24+p**2*(q-1)/6+p*q*(q-1)/4+q**2*(q-1)/6
f = 1-a*h+b*h**2-c*h**3
assert S.simplify(A-h*f)==0
assert S.simplify(C-h*h*(1-(p+q)*h/2+(2*p*p+3*p*q+2*q*q)*h*h/12))==0
order = 12-8*(p+q)*h+(3*p*p+5*p*q+3*q*q)*h*h
assert S.simplify(A-B-h*h*(p-q)*order/24)==0
assert S.simplify(S.discriminant(order,h)+16*(5*p*p+7*p*q+5*q*q))==0
cert = 5*p**4+30*p**3*(q-1)+6*p*p*(q-1)*(11*q-6)+36*p*q*(q-1)*(2*q-1)+36*q*q*(q-1)**2
assert S.simplify(144*(3*a*c-b*b)-cert)==0
Z = 12+(-12*N+8*p)*h+(6*N*N-8*N*p-2*N+3*p*p+4*p)*h*h
f_fixed = S.factor(f.subs(q,N-p))
assert S.simplify(Z-24*S.diff(f_fixed,p)/h)==0
assert S.simplify(S.discriminant(Z,h)+16*(9*N*N-12*N*p-6*N+5*p*p+12*p))==0
assert S.simplify(S.factor(R(0)))==1
# Row-stochastic FE decomposition, scalar symbolic validation.
y=S.symbols('y')
assert S.expand(sum((y-1)**k/S.factorial(k) for k in range(5))-(S.Rational(3,8)+y/S.Integer(3)+y*y/4+y**4/24))==0
symbolic_checks=9
matrix_checks=0
vertex_entries=0
for pp in range(2,6):
 for qq in range(pp+1,pp+4):
  n=pp*qq
  edges=S.zeros(n)
  idx=lambda i,j:i*qq+j
  for i in range(pp):
   for j in range(qq):
    u=idx(i,j)
    for k in range(pp):
     if k!=i:edges[u,idx(k,j)]=1
    for k in range(qq):
     if k!=j:edges[u,idx(i,k)]=1
  lap=(pp+qq-2)*S.eye(n)-edges
  for hv in [S.Rational(1,17),S.Rational(2,7),S.Rational(3,4)]:
   step=S.zeros(n)
   power=S.eye(n)
   for k in range(5):
    step+=(-hv)**k/S.factorial(k)*power
    power=power*lap
   vals={'A':A.subs({p:pp,q:qq,h:hv}), 'B':B.subs({p:pp,q:qq,h:hv}),
         'C':C.subs({p:pp,q:qq,h:hv}), 'D':D.subs({p:pp,q:qq,h:hv})}
   # All vertex-pair entries, not merely one representative.
   for i in range(pp):
    for j in range(qq):
     for k in range(pp):
      for ell in range(qq):
       typ='D' if (i==k and j==ell) else 'A' if j==ell else 'B' if i==k else 'C'
       assert step[idx(i,j),idx(k,ell)] == vals[typ],(pp,qq,hv,typ)
       vertex_entries+=1
   matrix_checks+=1
# Confirm threshold root order on exact rationals via signs and uniqueness certificates.
for pp in range(2,10):
 for qq in range(pp+1,11):
  fv=f.subs({p:pp,q:qq})
  assert S.factor(fv.subs(h,S.Rational(1,pp+qq-2)))>0
  assert S.factor(fv.subs(h,S.Integer(5)))<0
print(f'VERIFY_OK {symbolic_checks} symbolic identities, {matrix_checks} exact full RK4 matrices, {vertex_entries} exact vertex-pair entries; all finite endpoint tests')
