"""Standalone exact verifier for a rank-three polynomial-preconditioned Arnoldi numerical-range boundary."""
import sympy as s
K,t=s.symbols('K t', real=True)
I=s.eye(3)
N=s.Matrix([[0,1,0],[0,0,1],[0,0,0]])
A=I+K*N
Q=I-t*K*N
B=s.expand(A*Q**2)
a=K*(1-2*t)
b=K**2*(t*t-2*t)
assert s.simplify(B-(I+a*N+b*N**2))==s.zeros(3)
S=s.simplify((B+B.T)/2)
v_antisym=s.Matrix([1,0,-1]);assert s.simplify(S*v_antisym-(1-b/2)*v_antisym)==s.zeros(3,1)
U=s.Matrix.hstack(s.Matrix([1,0,1])/s.sqrt(2),s.Matrix([0,1,0]))
T=s.simplify(U.T*S*U)
assert s.simplify(T-s.Matrix([[1+b/2,a/s.sqrt(2)],[a/s.sqrt(2),1]]))==s.zeros(2)
assert s.simplify(2*T.det()-(2-K**2*(1-2*t+3*t**2)))==0
assert s.simplify(1-2*t+3*t**2-s.Rational(2,3)-3*(t-s.Rational(1,3))**2)==0
K0=s.sqrt(3);t0=s.Rational(1,3)
w=s.Matrix([1,-1/s.sqrt(3),1]); assert s.simplify(S.subs({K:K0,t:t0})*w)==s.zeros(3,1)
assert s.simplify((w.T*B.subs({K:K0,t:t0})*w)[0])==0
q2=I-K*N/2+3*K*K*N**2/8
assert s.simplify(A*q2**2)==I
assert s.simplify(Q.subs(t,s.Rational(1,2))-I+K*N/2)==s.zeros(3)
assert s.simplify(B.subs(t,s.Rational(1,2))-(I-3*K*K*N**2/4))==s.zeros(3)
assert s.simplify((s.eye(3)+K*N).det())==1
for knum in (s.Rational(1,3),s.Rational(4,3),s.Rational(17,10)):
 for tnum in (s.Rational(-5,2),0,s.Rational(1,3),s.Rational(1,2),1,2):
  X=S.subs({K:knum,t:tnum})
  assert X == (B.subs({K:knum,t:tnum})+B.subs({K:knum,t:tnum}).T)/2
  if tnum==s.Rational(1,3) and knum* knum<3:
   assert all(x>0 for x in X.eigenvals())
print('PASS: symbolic recurrence, two invariant blocks, sharp quadratic minimizer, endpoint null vector, degree-two exactness, 18 numerical specializations')
