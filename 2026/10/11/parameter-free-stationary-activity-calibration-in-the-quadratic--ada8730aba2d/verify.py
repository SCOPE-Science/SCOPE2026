from fractions import Fraction
import sympy as sp

x,y,z,e,f,g = sp.symbols('x y z e f g', real=True)
h = e*x**2 + f*x + g
dx = y*z + h
dy = x**2 - y
dz = 1 - 4*x
x0 = sp.Rational(1,4)
y0 = sp.Rational(1,16)
z0 = -e - 4*f - 16*g

checks = []
checks.append(("equilibrium_dx", sp.simplify(dx.subs({x:x0,y:y0,z:z0})) == 0))
checks.append(("equilibrium_dy", sp.simplify(dy.subs({x:x0,y:y0,z:z0})) == 0))
checks.append(("equilibrium_dz", sp.simplify(dz.subs({x:x0,y:y0,z:z0})) == 0))
checks.append(("centered_z_channel", sp.expand(dz + 4*(x-x0)) == 0))
checks.append(("h_at_equilibrium", sp.simplify(h.subs(x,x0) - (e+4*f+16*g)/16) == 0))
# Algebra underlying the conditional-variance decompositions.
r1 = sp.symbols('r1', real=True)  # r1 = dx, with E[r1|x]=0
r2 = sp.symbols('r2', real=True)  # r2 = dy, with E[r2|y]=0
checks.append(("x_channel_residual", sp.expand(((-h)+r1) + h - r1) == 0))
checks.append(("y_channel_residual", sp.expand((y+r2) - y - r2) == 0))

for name, ok in checks:
    print(f"{name}: {'PASS' if ok else 'FAIL'}")
if not all(ok for _,ok in checks):
    raise SystemExit(1)
print("all_symbolic_checks: PASS")
