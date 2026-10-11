import sympy as sp
x,y,z,T,R=sp.symbols('x y z T R', nonzero=True)
f1=y
f2=z
f3=-z-(T-R+R*x**2)*y-T*x
# Prior exact balance generators used in proof.
F=x*z+x*y-sp.Rational(1,2)*y**2+sp.Rational(1,2)*(T-R)*x**2+sp.Rational(1,4)*R*x**4
G=y*z+sp.Rational(1,2)*y**2+sp.Rational(1,2)*T*x**2
L=lambda h: sp.expand(sp.diff(h,x)*f1+sp.diff(h,y)*f2+sp.diff(h,z)*f3)
assert sp.simplify(L(F)-(y**2-T*x**2))==0
assert sp.simplify(L(G)-(z**2+(R-T)*y**2-R*x**2*y**2))==0
assert sp.simplify(L(x*y)-(y**2+x*z))==0
q=z+T*x
assert sp.simplify(L(q).subs(z,-T*x)-R*(1-x**2)*y)==0
print('VERIFY_OK')
