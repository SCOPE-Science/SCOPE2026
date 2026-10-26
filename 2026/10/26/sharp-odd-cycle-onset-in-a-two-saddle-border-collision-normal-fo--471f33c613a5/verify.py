"""Exact symbolic checks for the strict LLR three-cycle threshold."""
import sympy as S
L,d,u,B,t=S.symbols('L d u B t', real=True)
AL=S.Matrix([[L,1],[-d,0]])
AR=S.Matrix([[-B,1],[u,0]])
e=S.Matrix([1,0]); M=AR*AL**2
Jm=1+B*(L**2-d)-L*(u-d)-d*d*u
Jp=1-B*(L**2-d)+L*(u-d)-d*d*u
assert S.simplify(S.det(S.eye(2)-M)-Jm)==0
assert S.simplify(S.det(S.eye(2)+M)-Jp)==0
assert S.simplify(S.det(M)+d*d*u)==0
v=(S.eye(2)-M).inv()*(AR*(AL*e+e)+e)
p1=AL*v+e; p2=AL*p1+e
N0=B*(L+1)+u*(L+d)+d-1
N1=B*(L+d)-L-u*(1-d)-1
N2=L*L+L*d+L+d*d-d+1
assert S.factor(Jm*v[0]+N0)==0
assert S.factor(Jm*p1[0]+N1)==0
assert S.factor(Jm*p2[0]-N2)==0
Bmin=(L+u*(1-d)+1)/(L+d)
Bmax=(1+L*(u-d)-d*d*u)/(L*L-d)
H=S.factor((Bmax-Bmin)*(L+d)*(L*L-d))
Ht=-t**3+(d*(u-4)-4)*t*t+(d*d*(u-6)+3*d*(u-3)-4)*t+d*(-d*d+d+3)*u-(3*d**3+6*d*d+2*d+1)
assert S.expand(H.subs(L,1+d+t)-Ht)==0
U=(3*d**3+6*d*d+2*d+1)/(d*(-d*d+d+3))
q=9*d**4+22*d**3+19*d*d-2*d-3
assert S.factor(S.diff(U,d)-q/(d*d*(d*d-d-3)**2))==0
assert q.subs(d,S.Rational(363621,1000000))<0
assert q.subs(d,S.Rational(363622,1000000))>0
assert S.simplify(Jm.subs(B,Bmin).subs(L,1+d)+3*(d*d+d+1)*(d*u-d-1)/(2*d+1))==0
assert S.simplify(Jp.subs(B,u-1).subs(L,1+d)-2*(1-d*d*u))==0
assert S.factor(Jm.subs(B,u-1).subs(L,1+d))==0
assert S.simplify(N1.subs(B,u-1).subs(L,1+d)-3*(d*(u-1)-1))==0
param={L:S.Rational(7,5),d:S.Rational(1,3),B:S.Rational(8,3),u:S.Integer(3)}
assert (v[0].subs(param),p1[0].subs(param),p2[0].subs(param))==(S.Rational(-1230,143),S.Rational(-25,143),S.Rational(518,143))
assert Jm.subs(param)==S.Rational(286,225)
assert Jp.subs(param)==S.Rational(14,225)
assert param[L]>1+param[d] and param[B]>abs(1-param[u])
print('All 20 exact symbolic and rational identity checks passed.')
