"""Independent symbolic checks for the balanced delayed Euler moment barrier.
Requires Python 3 and sympy; execute with python verify.py.
"""
import sympy as s
u=s.symbols('u', real=True)
x,y=s.symbols('x y')
p=q=s.Rational(1,3)
g={0:1,2:u,4:3*u*u}
K=s.zeros(5)
for i in range(5):
    pol=s.expand(sum(s.binomial(i,j)*(p*x+q*y)**(i-j)*y**j*x**(4-i)*g[j]
                     for j in range(0,i+1,2)))
    for k in range(5):
        K[i,k]=pol.coeff(x,k).coeff(y,4-k)
assert all(s.Poly(e,u).all_coeffs() == [0] or all(c>=0 for c in s.Poly(e,u).all_coeffs()) for e in K)
Q=14008-45261*u-10935*u**2+78003*u**3-19683*u**4
R=7004-4212*u-7209*u**2+2187*u**3
assert s.factor((s.eye(5)-K).det()) == s.factor(Q/19683)
S=1/(s.Rational(2,3)-u)
f=s.Matrix([0,0,S,3*S/2,6*S-3])
vec=(s.eye(5)-K).inv()*f
assert s.simplify(vec[4]-27*R/((2-3*u)*Q))==0
assert s.simplify(27*R.subs(u,0)/((2-3*u).subs(u,0)*Q.subs(u,0))-s.Rational(27,4))==0
# Exact one-positive-root argument: substitution u=(2/3)t/(1+t)
t=s.symbols('t', positive=True)
trans=s.Poly(s.cancel((1+t)**4*Q.subs(u,s.Rational(2,3)*t/(1+t))),t)
assert trans == s.Poly(-2*(901*t**4+10549*t**3+5667*t**2-12929*t-7004),t)
# Descartes: exactly one sign change in descending coefficient sequence.
sgns=[s.sign(c) for c in trans.all_coeffs()]
assert sum(sgns[i]!=sgns[i+1] for i in range(len(sgns)-1)) == 1
assert Q.subs(u,s.Rational(1,3))>0 and Q.subs(u,s.Rational(7,20))<0
root=s.nroots(Q,maxsteps=300)
rstar=[float(s.re(r)) for r in root if abs(float(s.im(r)))<1e-12 and 0<float(s.re(r))<2/3]
assert len(rstar)==1 and abs(rstar[0]-0.345556005763941)<1e-12
# Second-moment recurrence criterion at p=q=1/3.
L=s.Matrix([[p*p,2*p*q,q*q+u],[p,q,0],[1,0,0]])
assert s.simplify((s.eye(3)-L).det()-s.Rational(2,3)*(s.Rational(2,3)-u)) == 0
# Numerically check Perron radii on either side, not used to certify uniqueness.
import numpy as np
for z,expected in [(0.1,True),(0.3,True),(0.4,False),(0.6,False)]:
    rho=max(abs(v) for v in np.linalg.eigvals(np.array(K.subs(u,z),dtype=float)))
    assert (rho<1)==expected
print('PASS: exact fourth-moment matrix, determinant, rational stationary fourth moment, uniqueness, L2 comparison, sampled spectral checks')
print('u4=',rstar[0], 'u2=', 2/3)
