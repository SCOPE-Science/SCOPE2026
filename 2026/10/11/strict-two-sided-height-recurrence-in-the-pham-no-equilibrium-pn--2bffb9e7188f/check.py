import sympy as sp
x,y,z,a,b,c,t,R,phi = sp.symbols('x y z a b c t R phi', real=True)
xd = y
yd = -x + y*z
zd = -x - a*x*y - b*x*z + c
E = (x**2+y**2)/2
Edot = sp.diff(E,x)*xd + sp.diff(E,y)*yd + sp.diff(E,z)*zd
assert sp.expand(Edot - y**2*z) == 0
th = t + phi
xh = R*sp.cos(th)
yh = -R*sp.sin(th)
expr = sp.expand_trig(xh*(1+a*yh)-c)
# Integrate against the constant and first cosine mode over one full period.
const_coeff = sp.simplify(sp.integrate(expr, (t, 0, 2*sp.pi))/(2*sp.pi))
cos1_coeff = sp.simplify(sp.integrate(expr*sp.cos(th), (t, 0, 2*sp.pi))/sp.pi)
assert const_coeff == -c
assert cos1_coeff == R
print('energy_derivative:', sp.simplify(Edot))
print('z0_constraint_constant_coefficient:', const_coeff)
print('z0_constraint_first_cosine_coefficient:', cos1_coeff)
print('Conclusion: an identically constant z=0 harmonic orbit with c != 0 is impossible.')
print('VERIFY_OK')
