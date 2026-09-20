import sympy as sp

x, y, z, a, mu = sp.symbols('x y z a mu', positive=True, real=True)
D = sp.sqrt(a**2 + 4*mu**2)
z_star = (a + D)/2
z_minus = (a - D)/2
r = mu/z_star

fx = -mu*x + y*z
fy = -mu*y + x*(z-a)
fz = 1 - x*y

def lie(f):
    return sp.expand(sp.diff(f, x)*fx + sp.diff(f, y)*fy + sp.diff(f, z)*fz)

checks = {
    'L_z': sp.simplify(lie(z) - (1-x*y)),
    'L_half_x2_minus_y2': sp.simplify(lie((x**2-y**2)/2) - (a*x*y-mu*(x**2-y**2))),
    'L_half_z2': sp.simplify(lie(z**2/2) - (z-x*y*z)),
    'L_half_x2_plus_y2': sp.simplify(lie((x**2+y**2)/2) - (-mu*(x**2+y**2)-a*x*y+2*x*y*z)),
    'equilibrium_quadratic': sp.simplify(z_star*(z_star-a)-mu**2),
    'r_equilibrium_relation': sp.simplify(mu*(1-r**2)-a*r),
    'zstar_times_r': sp.simplify(z_star*r-mu),
    'moment_gap_factorization': sp.simplify((sp.Symbol('m')*(sp.Symbol('m')-a)-mu**2) - (sp.Symbol('m')-z_star)*(sp.Symbol('m')-z_minus)),
}

for name, residual in checks.items():
    print(f'{name}: {sp.simplify(residual)}')

# Equality-set tangency for h=y-r*x on h=0.
h = y-r*x
on_h = sp.simplify(lie(h).subs(y, r*x))
expected = sp.simplify((a*r/mu)*x*(z-z_star))
print('equality_set_tangency_residual:', sp.simplify(on_h-expected))
print('sympy_version:', sp.__version__)
