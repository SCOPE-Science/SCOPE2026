"""Exact arithmetic checks for the sharp third symmetric Toeplitz bound.

Run with Python 3 and SymPy. The mathematical inequalities are proved in
RESULT.md; this script verifies the polynomial identities they use.
"""
import sympy as S
s, r, t, x, y, z = S.symbols('s r t x y z', real=True)
Q = S.Rational

def zero(expr):
    assert S.expand(expr) == 0, S.factor(expr)

# Coefficient identities from the logarithmic-derivative equation.
w = S.symbols('w')
omega = x*w + y*w**2 + z*w**3
p = S.series(1 + 2*s*omega/(1-omega), w, 0, 4).removeO()
a2 = 2*s*x
a3 = s*(y + (1+2*s)*x**2)
a4 = s*(Q(2,3)*z + (Q(4,3)+2*s)*x*y +
        (Q(2,3)+2*s+Q(4,3)*s**2)*x**3)
h = w + a2*w**2+a3*w**3+a4*w**4
zero(S.series(w*S.diff(h,w)/h-p,w,0,4).removeO())

U = 2*x - Q(2,3)*z - (Q(4,3)+2*s)*x*y - (Q(2,3)+2*s+Q(4,3)*s*s)*x**3
V = 4*x**2 + Q(4,3)*x*z - 2*y**2 - (Q(4,3)+4*s)*x*x*y - (Q(2,3)+4*s+Q(16,3)*s*s)*x**4
zero((a2-a4)-s*U)
zero(a2*a2+a2*a4-2*a3*a3-s*s*V)

M1 = Q(2,3)*(4+3*s+2*s*s)
R1 = 2*r + Q(2,3)*(1-r*r) + (Q(4,3)+2*s)*r*(1-r*r) + (Q(2,3)+2*s+Q(4,3)*s*s)*r**3
zero(M1-R1-Q(2,3)*(1-r)*((1-r)*(r+3)+3*s+2*s*s*(r*r+r+1)))

Q2=4*r*r + Q(2,3)*(1+6*s+8*s*s)*r**4 + Q(4,3)*(1+3*s)*r*r*(1-r*r)*t + 2*(1-r*r)**2*t*t + Q(4,3)*r*(1-r*r)*(1-(1-r)*t*t)
Q0 = S.expand(Q2.subs(s,0))
zero(S.diff(Q0,t,2)/2-Q(2,3)*(1-r)**2*(r+1)*(r+3))
zero(Q0.subs(t,1)-2-Q(8,3)*r*r)
zero(Q0.subs(t,1)-Q0.subs(t,0)-Q(2,3)*(1-r*r)*(r*r-2*r+3))
zero(S.diff(Q2,s).subs(s,0) - 4*(r**4+r*r*(1-r*r)*t))
zero(S.diff(Q2,s,2)/2 - Q(16,3)*r**4)

M2 = Q(2,3)*(7+6*s+8*s*s)
zero(U.subs({x:S.I,y:0,z:0}) - S.I*M1)
zero(V.subs({x:S.I,y:0,z:0}) + M2)
zero(S.expand((U*V).subs({x:S.I,y:0,z:0})+S.I*M1*M2))

# Schur parametrization constraint: c2=(1-r²)b,
# c3=(1-r²)(d-conj(c1)b²), |b|=t, |d|<=1-t².
# Its triangle majorant of |c3| is (1-r²)[1-(1-r)t²].
# Positivity of the factored polynomials gives the proof for all 0<=s, r,t<=1.
print('PASS: coefficient, factor, positivity-factor, and extremal identities')
