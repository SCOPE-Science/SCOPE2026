"""Symbolic identity checks for a monotone-control tumor-immune oscillator exclusion theorem.
Run: python3 CHECK.py (SymPy required)."""
import sympy as S
x,y,c,beta,r,alpha,eps,q,Tc,s=S.symbols('x y c beta r alpha eps q Tc s',positive=True)
h=S.Function('h')(y)
B=(1+eps*y)/(r*y)
P=c*y-(1+beta*y)*x+s*h
Q=r*y*(1-y-alpha*x/(1+eps*y))-q*y*h
D=S.factor(S.diff(B*P,x)+S.diff(B*Q,y))
a=eps*(beta+2*r)
b=beta+eps+r*(1-eps)
expected=-(a*y*y+b*y+1)/(r*y)-q*(eps*h+(1+eps*y)*S.diff(h,y))/r
assert S.simplify(D-expected)==0,(D,expected)
Qlow=r*y*(1-y-alpha*x/(1+eps*y))
Qhigh=Qlow-q*y
jump=S.factor(B*(Qlow-Qhigh)).subs(y,Tc)
assert S.simplify(jump-q*(1+eps*Tc)/r)==0
Dlo=S.factor(S.diff(B*(c*y-(1+beta*y)*x),x)+S.diff(B*Qlow,y))
Dhi=S.factor(S.diff(B*(c*y-(1+beta*y)*x+s),x)+S.diff(B*Qhigh,y))
assert S.simplify(Dlo+(a*y*y+b*y+1)/(r*y))==0
assert S.simplify(Dhi-Dlo+q*eps/r)==0
for be,rr,ee,expect in [(S.Rational(3,2),5,6,False),(1,5,2,True),(1,100,S.Rational(4,5),True)]:
    A=ee*(be+2*rr)
    C=be+ee+rr*(1-ee)
    holds=bool(C+2*S.sqrt(A)>=0)
    assert holds==expect,(be,rr,ee,C,A,holds)
print('CHECK_OK: exact bulk divergences, jump trace, and inside/outside parameter tests')
