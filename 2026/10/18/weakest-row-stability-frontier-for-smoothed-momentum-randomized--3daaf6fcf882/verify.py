"""Exact symbolic and rational checks for orthogonal-row momentum stability.
Run with python verify.py (requires sympy)."""
import sympy as S
p,b,M=S.symbols('p b M', real=True)
c=1-b;g=b+c*M
K0=S.Matrix([[1,M],[0,g]])
K1=S.Matrix([[0,M],[-c,g]])
# Symmetric covariance basis [x^2, xy, y^2]
def sym_square(K):
 a,d=K[0,0],K[0,1]
 e,f=K[1,0],K[1,1]
 return S.Matrix([[a*a,2*a*d,d*d],[a*e,a*f+d*e,d*f],[e*e,2*e*f,f*f]])
Q=S.simplify((1-p)*sym_square(K0)+p*sym_square(K1))
F=S.expand(-2*c*c*M*M + ((2*p-1)-2*b+(3-2*p)*b*b)*M+(1+b)*(1-b+b*p))
assert S.simplify((S.eye(3)-Q).det()-p*c*F)==0
assert S.simplify(F.subs(p,0)-c*(1-2*M)*(c*M+1+b))==0
assert S.simplify(S.diff(F,p)-(2*(1-b*b)*M+b*(1+b)))==0
assert S.simplify(F.subs(M,1)-(-p*b*b+(p+2)*b+2*p-2))==0
mean=(1-p)*K0+p*K1
assert S.simplify((S.eye(2)-mean).det()-p*c)==0
assert S.simplify(mean.det()-((1-p)*b+c*M))==0
# compare actual 2^t paths with the moment recursion at rational parameters
count=0
for pv in [S.Rational(1,8),S.Rational(1,3),S.Rational(1,2),S.Rational(3,4)]:
 for bv in [S.Rational(0),S.Rational(1,4),S.Rational(3,4)]:
  for mv in [S.Rational(0),S.Rational(1,3),S.Rational(2,3),S.Rational(1)]:
   mats=[k.subs({p:pv,b:bv,M:mv}) for k in [K0,K1]]
   qq=Q.subs({p:pv,b:bv,M:mv})
   vv=S.Matrix([1,0,0]); paths=[(S.Matrix([1,0]),S.Rational(1))]
   for t in range(1,6):
    paths=[(mats[i]*z,w*(pv if i else 1-pv)) for z,w in paths for i in (0,1)]
    vvt=S.Matrix([sum(w*z[0]**2 for z,w in paths),sum(w*z[0]*z[1] for z,w in paths),sum(w*z[1]**2 for z,w in paths)])
    vv=qq*vv
    assert vv==vvt,(pv,bv,mv,t)
    count+=1
print('PASS: symbolic determinant, first-moment stability identities, monotonicity and',count,'exact path-moment identities')
