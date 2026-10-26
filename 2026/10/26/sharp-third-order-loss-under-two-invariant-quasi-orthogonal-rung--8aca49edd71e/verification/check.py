"""Reproduction of algebra and finite diagnostics for a two-frequency invariant projection example."""
from fractions import Fraction
from math import sqrt
import numpy as np
from scipy.optimize import root
import sympy as sp

# 1. Exact polynomial identity for two quadratic invariant constraints.
x,A,B,C=sp.symbols('x A B C',real=True)
g=(1-B*x)**2+x*(A-C*x)**2-1
assert sp.factor(g-x*((A*A-2*B)+(B*B-2*A*C)*x+C*C*x*x))==0
h,a,b,c=sp.symbols('h a b c',real=True)
q=sp.expand((g/x).subs({A:h+a*h**3,B:h**2/2+b*h**4,C:c*h**3})/h**4)
assert sp.simplify(q.subs(h,0)-(2*(a-b)+(sp.Rational(1,4)-2*c)*x))==0

# 2. Kutta RK3 stages span the three Krylov powers, with exact classical coefficients.
w1,w2,w3=sp.symbols('w1 w2 w3')
k1=w1;k2=w1+h*w2/2;k3=w1+h*w2+h*h*w3
assert sp.expand(h*(k1+4*k2+k3)/6-(h*w1+h*h*w2/2+h**3*w3/6))==0

# 3. Exact threshold/leading coefficient with mode frequencies 1 and 2, unit energies.
xi=(sp.Integer(1),sp.Integer(4))
a_star=-sum(z*z for z in xi)/(24*sum(xi))
assert a_star==sp.Rational(-17,120)
C2=sum(z*(a_star+z/sp.Integer(24))**2 for z in xi)
assert C2==sp.Rational(1,80)

# 4. Recompute frozen projected-gradients numerical root and compare exact energy and scaling.
J=np.array([[0.,-1.],[1.,0.]])
K=np.kron(np.diag([1.,2.]),J)
u=np.array([1.,0.,1.,0.]);W=np.column_stack((K@u,K@K@u,K@K@K@u))
G=W.T@W
assert min(np.linalg.eigvalsh(G))>0
expected=sqrt(float(C2))
ratios=[];global_ratios=[]
for N in (8,16,32,64,128):
 h=1/N
 start=np.array([h,h*h/2,h**3/6]);prediction=u+W@start
 P=[]
 for j in range(2):
  grad=np.zeros(4);grad[2*j:2*j+2]=prediction[2*j:2*j+2]
  P.append(W@np.linalg.solve(G,W.T@grad))
 P=np.column_stack(P)
 def F(t):
  v=prediction+P@t
  return [(sum(v[2*j:2*j+2]**2)-1) for j in range(2)]
 ans=root(F,[0.,0.],tol=1e-10)
 assert np.linalg.norm(F(ans.x))<1e-11
 projected=prediction+P@ans.x
 ratios.append(np.linalg.norm(projected-prediction)/h**3)
 outcome=np.array([complex(*projected[2*j:2*j+2])**N for j in range(2)])
 exact=np.exp(1j*np.array([1.,2.]))
 global_ratios.append(np.linalg.norm(outcome-exact)/h**2)
assert abs(ratios[-1]-expected)<2.5e-3,(ratios,expected)
assert abs(global_ratios[-1]-expected)<3e-5,(global_ratios,expected)
assert all(abs(global_ratios[i+1]-expected)<abs(global_ratios[i]-expected) for i in range(4))
print('VERIFY_OK exact-polynomial / RK3 / rational asymptotic / 5 nonlinear roots / 5 global phase tests')
print('a_star=',a_star,'C=',expected,'last local ratio=',ratios[-1],'last global ratio=',global_ratios[-1])
