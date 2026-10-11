import sympy as sp

delta, t = sp.symbols("delta t", real=True)
phi1 = (1 + 4*sp.cos(2*t))/(48*sp.pi)
rho = 1/sp.cos(sp.pi/3 - delta*phi1)

first = sp.simplify(sp.diff(rho, delta).subs(delta, 0))
target = -sp.sqrt(3)*(1 + 4*sp.cos(2*t))/(24*sp.pi)
assert sp.simplify(first-target) == 0

g_at_zero = sp.simplify(target.subs(t, 0))
g_at_halfpi = sp.simplify(target.subs(t, sp.pi/2))
assert g_at_zero == -5*sp.sqrt(3)/(24*sp.pi)
assert g_at_halfpi == sp.sqrt(3)/(8*sp.pi)

osc = sp.simplify(g_at_halfpi-g_at_zero)
assert osc == sp.sqrt(3)/(3*sp.pi)

decimal = sp.N(osc, 30)
assert abs(float(decimal)-0.1837762984739307) < 1e-15

# The first variation is affine in cos(2t), whose range is exactly [-1,1],
# so the two values checked above are the global extrema.
print("VERIFY_OK")
print("coefficient", decimal)
