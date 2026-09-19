import sympy as sp

x, y = sp.symbols('x y', positive=True)
a, b, c, ap, bp, cp = sp.symbols('a b c ap bp cp')
alpha, delta = sp.symbols('alpha delta')

# Holling type-II model.
fx = alpha*x*(1-x**4) - a*x*y/(b+x)
fy = c*x*y/(b+x) - delta*y
alpha_p = alpha + y/(1-x**4) * (ap/(bp+x) - a/(b+x))
delta_p = delta + cp*x/(bp+x) - c*x/(b+x)
fx_p = alpha_p*x*(1-x**4) - ap*x*y/(bp+x)
fy_p = cp*x*y/(bp+x) - delta_p*y

# Ratio-dependent model.
fx_r = alpha*x*(1-x**4) - a*x*y/(b*y+x)
fy_r = c*x*y/(b*y+x) - delta*y
alpha_pr = alpha + y/(1-x**4) * (ap/(bp*y+x) - a/(b*y+x))
delta_pr = delta + cp*x/(bp*y+x) - c*x/(b*y+x)
fx_pr = alpha_pr*x*(1-x**4) - ap*x*y/(bp*y+x)
fy_pr = cp*x*y/(bp*y+x) - delta_pr*y

checks = {
    'typeII_prey_gauge_residual': sp.factor(sp.simplify(fx_p-fx)),
    'typeII_predator_gauge_residual': sp.factor(sp.simplify(fy_p-fy)),
    'ratio_prey_gauge_residual': sp.factor(sp.simplify(fx_pr-fx_r)),
    'ratio_predator_gauge_residual': sp.factor(sp.simplify(fy_pr-fy_r)),
}

# Exact reconstruction formulas from a fully observed trajectory.
xd, yd = sp.symbols('xd yd')
alpha_rec = (xd + a*x*y/(b+x))/(x*(1-x**4))
delta_rec = c*x/(b+x) - yd/y
alpha_rec_r = (xd + a*x*y/(b*y+x))/(x*(1-x**4))
delta_rec_r = c*x/(b*y+x) - yd/y
checks.update({
    'typeII_reconstructed_prey_residual': sp.factor(sp.simplify(alpha_rec*x*(1-x**4)-a*x*y/(b+x)-xd)),
    'typeII_reconstructed_predator_residual': sp.factor(sp.simplify(c*x*y/(b+x)-delta_rec*y-yd)),
    'ratio_reconstructed_prey_residual': sp.factor(sp.simplify(alpha_rec_r*x*(1-x**4)-a*x*y/(b*y+x)-xd)),
    'ratio_reconstructed_predator_residual': sp.factor(sp.simplify(c*x*y/(b*y+x)-delta_rec_r*y-yd)),
})

for name, value in checks.items():
    print(f'{name}: {value}')
assert all(v == 0 for v in checks.values())
print('all_symbolic_checks_passed: True')
