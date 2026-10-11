import sympy as sp
A,x,a,zbar,f=sp.symbols('A x a zbar f', positive=True)
expr=1/(A+x)-(1/A-x/A**2+x**2/(A**2*(A+x)))
assert sp.simplify(expr)==0
aval=sp.Rational(1,2); b=sp.Rational(1,4); gamma=sp.Rational(3,40); g=sp.Rational(1,5)
assert sp.simplify(gamma/g-b)==sp.Rational(1,8)
bound=sp.simplify(aval*g*(b+f)/(gamma-g*(b+f)))
assert sp.simplify(bound-(1+4*f)/(1-8*f))==0
assert sp.simplify(g/gamma*(b+f)-(sp.Rational(2,3)+sp.Rational(8,3)*f))==0
print('VERIFY_OK')
