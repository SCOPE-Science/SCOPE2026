"""Exact symbolic checks for a Markov skew tent map's covariances.
Run with python CHECK.py (requires SymPy). Algebraic identities complement,
but do not replace, the infinite-dimensional mixing and CLT argument.
"""
import sympy as s

t,z,x=s.symbols('t z x',real=True)
C_A,D_A,C_B,D_B=s.symbols('C_A D_A C_B D_B')
# Inverse branches: left branch exists only on B; right branch everywhere.
right_pre=1-(1-t)*x
left_pre=t*(x-t)/(1-t)
f_A=C_A+D_A*x
f_B=C_B+D_B*x
L_A=s.expand((1-t)*f_B.subs(x,right_pre))
L_B=s.expand(t/(1-t)*f_A.subs(x,left_pre)+(1-t)*f_B.subs(x,right_pre))
basis=[C_A,D_A,C_B,D_B]

def lin_coeff(poly):
    return [s.diff(poly,q).subs({C_A:0,D_A:0,C_B:0,D_B:0}) for q in basis]

M=s.Matrix([lin_coeff(L_A.subs(x,0)),lin_coeff(s.diff(L_A,x)),
            lin_coeff(L_B.subs(x,0)),lin_coeff(s.diff(L_B,x))]);
M=s.simplify(M)
I=s.eye(4)
assert s.simplify(M-s.Matrix([
    [0,0,1-t,1-t],
    [0,0,0,-(1-t)**2],
    [t/(1-t),-t**3/(1-t)**2,1-t,1-t],
    [0,t**2/(1-t)**2,0,-(1-t)**2]
]))==s.zeros(4,4)

h_A=1/(1+t)
h_B=1/(1-t*t)
h=s.Matrix([h_A,0,h_B,0])
integ=s.Matrix([[t,t*t/2,1-t,(1-t*t)/2]])
assert s.simplify(integ*h)[0]==1
assert s.simplify(M*h-h)==s.zeros(4,1)
assert s.simplify(integ*M-integ)==s.zeros(1,4)
mu=s.factor((t*t*h_A+(1-t*t)*h_B)/2)
assert s.simplify(mu-(1+t+t*t)/(2*(1+t)))==0
f=s.Matrix([-mu*h_A,h_A,-mu*h_B,h_B])
J=s.Matrix([[s.integrate(x-mu,(x,0,t)),s.integrate(x*(x-mu),(x,0,t)),
             s.integrate(x-mu,(x,t,1)),s.integrate(x*(x-mu),(x,t,1))]])
assert s.simplify(integ*f)[0]==0
C0=s.factor((J*f)[0])
G=s.factor((J*(I-z*M).inv()*f)[0])
P=t*t+3*t+1+(t**4+2*t**3-2*t*t+t)*z+(t**5+t**4+t**3)*z*z
expected_G=(t*t-t+1)*P/(12*(1+t)**2*(1+t*z)*(1+(1-t)**2*z+t*t*z*z))
assert s.simplify(G-expected_G)==0
assert s.simplify(G.subs(z,0)-C0)==0
for n in range(11):
    c_n=s.factor((J*M**n*f)[0])
    assert s.simplify(s.diff(G,z,n).subs(z,0)/s.factorial(n)-c_n)==0

# Stable eigenvalues on zero mass; evaluate the Green--Kubo series algebraically.
lam=s.symbols('lambda')
character=s.factor(M.charpoly(lam).as_expr())
assert s.simplify(character-(lam-1)*(lam+t)*(lam*lam+(1-t)**2*lam+t*t))==0
projector=h*integ
K=s.factor((J*(I-M+projector).inv()*f)[0])
variance=s.factor(2*K-C0)
expected_variance=t*(1-t)*(t*t-t+1)/(12*(1+t)**3)
assert s.simplify(variance-expected_variance)==0
q=t**4+4*t**3-8*t*t+6*t-1
assert s.simplify(s.diff(variance,t)+q/(12*(1+t)**4))==0
# At the unique positive resonance 2-sqrt(3), the numerator does not cancel.
r=2-s.sqrt(3)
num,den=s.fraction(s.factor(G))
assert s.simplify(num.subs(z,-1/t)-6*t*(t*t-t+1))==0
leading=s.limit(((1+t*z)**3*G).subs(t,r),z,-1/r)
assert s.simplify(leading-r*(r*r-r+1)/(2*(1+r)**2))==0
K_res=s.factor(leading/2)
assert s.simplify(K_res-(s.Rational(1,4)-s.sqrt(3)/8))==0
assert s.simplify((1-r)**4-4*r*r)==0
assert s.simplify(q.subs(t,r)-(156-90*s.sqrt(3)))==0
for t0,s0 in [(s.Rational(1,4),s.Rational(13,2000)),
              (s.Rational(1,2),s.Rational(1,216)),
              (s.Rational(3,4),s.Rational(13,5488))]:
    assert variance.subs(t,t0)==s0
    assert s.simplify(M.subs(t,t0)*h.subs(t,t0)-h.subs(t,t0))==s.zeros(4,1)
print('PASS: invariant density, transfer operator, all 11 coefficient identities,')
print('      characteristic polynomial, Green--Kubo variance, derivative,')
print('      critical third-order pole and coefficient, three rational specializations')
