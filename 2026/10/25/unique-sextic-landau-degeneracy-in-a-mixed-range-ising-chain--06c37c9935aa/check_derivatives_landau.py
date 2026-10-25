"""Symbolic algebra verification for the exact Landau derivatives.
Requires SymPy. The mathematical proof does not rely only on this code.
"""
import sympy as s
A,Y,T=s.symbols('a y t', real=True)
D=lambda f:s.diff(f,Y)/(2*Y)+A*(1-T**2)*s.diff(f,T)/(2*Y)
F={1:A*T/(2*Y)}
for j in range(2,7): F[j]=s.cancel(D(F[j-1]))

def d_avg(order):
    n=order//2
    return s.factorial(order)*sum(s.binomial(k,2*(k-n))*s.binomial(2*(k-n),k-n)*F[k].subs(Y,1)/s.factorial(k) for k in range(n,2*n+1))
q2=s.factor(-d_avg(2)/A)
q4=s.factor(-d_avg(4)/A)
q6=s.factor(-d_avg(6)/A)
q2_expected=-(T+A*(1-T**2))/2
q4_expected=s.Rational(3,8)*(6*A**3*T**4-8*A**3*T**2+2*A**3-4*A**2*T**3+4*A**2*T-A*T**2+A-T)
q6_expected=s.Rational(5,16)*(120*A**5*T**6-240*A**5*T**4+136*A**5*T**2-16*A**5 -72*A**4*T**5+120*A**4*T**3-48*A**4*T -18*A**3*T**4+24*A**3*T**2-6*A**3 -12*A**2*T**3+12*A**2*T-9*A*T**2+9*A-9*T)
assert s.simplify(q2-q2_expected)==0
assert s.simplify(q4-q4_expected)==0
assert s.simplify(q6-q6_expected)==0
print('q2',q2)
print('q4',q4)
print('q6',q6)
print('quadratic, quartic and sextic identities: PASS')
