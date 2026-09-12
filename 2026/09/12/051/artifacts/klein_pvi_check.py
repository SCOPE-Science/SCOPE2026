"""Recovery test 1: exact verification that Boalch's Klein parametrization
solves PVI with (alpha,beta,gamma,delta)=(9,-4,4,45)/98, as a rational identity in s.
Also checks Boalch's commented solution-curve polynomial F(t,y) (non-fatal)."""
import sympy as sp

s = sp.Symbol('s')
y = -(5*s**2 - 8*s + 5)*(7*s**2 - 7*s + 4) / (
    s*(s - 2)*(s + 1)*(2*s - 1)*(4*s**2 - 7*s + 7))
t = (7*s**2 - 7*s + 4)**2 / (s**3*(4*s**2 - 7*s + 7)**2)
al, be, ga, de = (sp.Rational(9, 98), sp.Rational(-4, 98),
                  sp.Rational(4, 98), sp.Rational(45, 98))

ts = sp.diff(t, s)
dydt = sp.diff(y, s)/ts
d2ydt2 = sp.diff(dydt, s)/ts
res = (d2ydt2
       - sp.Rational(1, 2)*(1/y + 1/(y - 1) + 1/(y - t))*dydt**2
       + (1/t + 1/(t - 1) + 1/(y - t))*dydt
       - y*(y - 1)*(y - t)/(t**2*(t - 1)**2)*(
           al + be*t/y**2 + ga*(t - 1)/(y - 1)**2
           + de*t*(t - 1)/(y - t)**2))
num, den = sp.together(res).as_numer_denom()
num = sp.expand(num)
print("PVI residual numerator is zero:", num == 0)
print("PVI residual numerator degree:", sp.Poly(num, s).degree() if num != 0 else 0)

# Boalch k2p.tex commented-out solution curve F(t,y)
F = ((162*t**3 - 243*t**2 - 243*t + 162)*y**7
     + (-567*t**3 + 2268*t**2 - 567*t)*y**6
     + (-1701*t**3 - 1701*t**2)*y**5
     + (1407*t**4 + 2856*t**3 + 1407*t**2)*y**4
     + (14*t**5 - 2849*t**4 - 2849*t**3 + 14*t**2)*y**3
     + (-21*t**5 + 3444*t**4 - 21*t**3)*y**2
     + (-567*t**5 - 567*t**4)*y
     + (125*t**6 - 88*t**5 + 125*t**4))
Fn, _ = sp.together(F).as_numer_denom()
Fn = sp.expand(Fn)
print("F(t(s),y(s)) identically zero:", Fn == 0)

# numeric spot check at generic point
s0 = 0.3 + 0.7j
yf = sp.lambdify(s, y, 'mpmath')
tf = sp.lambdify(s, t, 'mpmath')
print("sample t(s0)=", tf(s0), " y(s0)=", yf(s0))
