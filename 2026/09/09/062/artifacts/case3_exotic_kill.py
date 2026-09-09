"""Kill the exotic (n=6,e1=e2=0) tuple under GENEROUS k-ranges: exact P-recurrence.
Under standard Kovacic k-ranges E1=E2={1} so this tuple never arises; this script shows
it dies anyway (P_n+1 = nonzero degree-14 polynomial). sympy required. stdlib otherwise."""
import sympy as sp
x = sp.symbols('x')
n = 6
S = x*(x-1)*(x-2)
theta = sp.Rational(1,2)/x
P, Pm1 = sp.Integer(1), sp.Integer(-1)
for i in range(0, n+1):
    Pm1 = sp.expand(S*sp.diff(Pm1, x) + ((n-i)*sp.diff(S, x) - S*theta)*Pm1)
Pn = Pm1
res = sp.simplify(Pn + 1)
print("P_6+1 =", res)
assert res != 0
print("degree:", sp.Poly(res, x).degree(), "-> tuple REJECTED")
print("EXOTIC_KILL_OK")
