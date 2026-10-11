import sympy as sp
x,y,z,s1,s2,d,R,q=sp.symbols('x y z s1 s2 d R q', nonzero=True)
fx=-s1*x+s2*y
fy=R*x+d*y-x*z
fz=-q*z+x*y
zstar=R+s1*d/s2
H=x*y-(s1+d)*x**2/(2*s2)
LH=sp.diff(H,x)*fx+sp.diff(H,y)*fy+sp.diff(H,z)*fz
target=fx**2/s2-x**2*(z-zstar)
assert sp.simplify(LH-target)==0
A=sp.symbols('A')
# nonzero equilibria have y=(s1/s2)x, z=zstar, x^2=q*s2*zstar/s1
subs={y:s1*x/s2,z:zstar,x**2:q*s2*zstar/s1}
# Verify each vector-field component modulo x^2 relation.
assert sp.simplify(fx.subs({y:s1*x/s2}))==0
assert sp.simplify(fy.subs({y:s1*x/s2,z:zstar}))==0
assert sp.simplify(fz.subs({y:s1*x/s2,z:zstar}).subs(x**2,q*s2*zstar/s1))==0
# origin
assert all(sp.simplify(f.subs({x:0,y:0,z:0}))==0 for f in (fx,fy,fz))
print('VERIFY_OK')
