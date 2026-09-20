import sympy as sp

x, y, z, T, R = sp.symbols("x y z T R")
f = (
    y,
    z,
    -z - (T - R + R*x**2)*y - T*x,
)

def lie(H):
    return sp.expand(
        sp.diff(H, x)*f[0]
        + sp.diff(H, y)*f[1]
        + sp.diff(H, z)*f[2]
    )

F = x*z + x*y - y**2/2 + (T-R)*x**2/2 + R*x**4/4
G = y*z + y**2/2 + T*x**2/2
K = z + y - R*(x - x**3/3)

checks = {
    "F_balance": sp.expand(lie(F) - (y**2 - T*x**2)),
    "G_balance": sp.expand(
        lie(G) - (z**2 + (R-T)*y**2 - R*x**2*y**2)
    ),
    "T0_first_integral": sp.expand(lie(K).subs(T, 0)),
}

for name, residual in checks.items():
    print(f"{name}: {sp.factor(residual)}")
    assert residual == 0
