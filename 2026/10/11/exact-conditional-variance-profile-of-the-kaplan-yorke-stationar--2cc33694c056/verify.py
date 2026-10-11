import sympy as s
u=s.symbols("u", real=True)
A=1/(2*(1-u**2))
assert s.simplify(A-(s.Rational(1,2)+u**2*A))==0
Vconst=s.simplify(A-s.Rational(1,2))
assert s.simplify(Vconst-u**2/(2*(1-u**2)))==0
Vmin=s.simplify(u**2/s.Integer(2)*(1/(1-u**2)-1))
assert s.simplify(Vmin-u**4/(2*(1-u**2)))==0
print("VERIFY_OK")
