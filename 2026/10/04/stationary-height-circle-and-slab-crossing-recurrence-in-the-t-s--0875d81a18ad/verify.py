from sympy import symbols, expand, simplify

x,y,z,m,n = symbols('x y z m n', real=True)
fx = y-x
fy = m*x-x*z
fz = -n*z+x*y
F = y**2 + z**2 - 2*m*z
LF = expand(F.diff(x)*fx + F.diff(y)*fy + F.diff(z)*fz)
expected = expand(-2*n*z*(z-m))
assert expand(LF-expected) == 0

Lx2 = expand((x**2).diff(x)*fx)
assert expand(Lx2 - 2*x*(y-x)) == 0

Lz = expand(fz)
assert expand(Lz - (x*y-n*z)) == 0

# Equilibria in the m>0,n>0 regime: O and P_±.
s = symbols('s', real=True)
peq = {x:s, y:s, z:m}
assert simplify(fx.subs(peq)) == 0
assert simplify(fy.subs(peq)) == 0
assert simplify(fz.subs(peq).subs(s**2,m*n)) == 0

# Endpoint-support tangency checks used in the rigidity argument.
# At z=0 and xy=0, either x=0 or y=0; invariance forces the other to vanish.
assert simplify(fx.subs({x:0,z:0}) - y) == 0
assert simplify(fy.subs({y:0,z:0}) - m*x) == 0
# At z=m and xy=mn, y'=0 and preservation of xy requires y(y-x)=0.
prod_dot = expand(fx*y + x*fy)
prod_dot_zm = expand(prod_dot.subs(z,m))
assert expand(prod_dot_zm - y*(y-x)) == 0

print('VERIFY_OK')
print('Lie_F =', LF)
print('Lie_x2 =', Lx2)
print('Lie_z =', Lz)
print('prod_dot_at_z=m =', prod_dot_zm)
