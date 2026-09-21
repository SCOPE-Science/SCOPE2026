import sympy as sp

x, y, z, a, b, c, m = sp.symbols("x y z a b c m", positive=True)
fx = -y - z
fy = x + a*y
fz = b + z*(x-c)

H = (x**2 + y**2)/2
LH = sp.expand(sp.diff(H, x)*fx + sp.diff(H, y)*fy + sp.diff(H, z)*fz)
print("L_H_residual =", sp.expand(LH - (a*y**2 - x*z)))

Delta = c**2 - 4*a*b
zminus = (c - sp.sqrt(Delta))/(2*a)
zplus = (c + sp.sqrt(Delta))/(2*a)
parabola = sp.simplify((m-zminus)*(zplus-m) - (c*m-b-a*m**2)/a)
print("parabola_residual =", parabola)

cap = sp.simplify((zplus-zminus)**2/4 - Delta/(4*a**2))
print("variance_cap_residual =", cap)

Y2 = sp.symbols("Y2")
cov_xz = sp.expand((a*Y2-a*m**2) - a*(Y2-m**2))
print("covariance_residual =", cov_xz)

q = a*z**2 - c*z + b
print("equilibrium_polynomial =", q)
print("sympy_version =", sp.__version__)
