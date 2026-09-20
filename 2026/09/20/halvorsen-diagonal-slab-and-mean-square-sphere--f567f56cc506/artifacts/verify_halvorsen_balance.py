from sympy import symbols, expand, simplify

x, y, z, a, b, c = symbols("x y z a b c")
d = symbols("d", nonzero=True)
sigma = a + b + c

f1 = -a*x - b*y - c*z - d*y**2
f2 = -a*y - b*z - c*x - d*z**2
f3 = -a*z - b*x - c*y - d*x**2
S = x + y + z
Q = x**2 + y**2 + z**2
R2 = (x + sigma/(2*d))**2 + (y + sigma/(2*d))**2 + (z + sigma/(2*d))**2

sum_residual = simplify(expand(f1 + f2 + f3 + sigma*S + d*Q))
sphere_residual = simplify(expand(f1 + f2 + f3 - (3*sigma**2/(4*d) - d*R2)))
E = {x: -sigma/d, y: -sigma/d, z: -sigma/d}
equilibrium_residuals = [simplify(fi.subs(E)) for fi in (f1, f2, f3)]

print("sum_balance_residual =", sum_residual)
print("sphere_balance_residual =", sphere_residual)
print("diagonal_equilibrium_residuals =", equilibrium_residuals)
