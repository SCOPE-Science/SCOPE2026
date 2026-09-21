import sympy as sp

th = sp.symbols('th', real=True)
r, beta = sp.symbols('r beta', real=True, nonzero=True)
A = sp.symbols('A')
phi = sp.sin(th)


def proj(expr, n):
    return sp.simplify(
        sp.integrate(sp.expand_trig(expr) * sp.sin(n * th), (th, 0, sp.pi))
        / (sp.pi / 2)
    )


def L(expr, nmax=8):
    ans = 0
    for n in range(1, nmax + 1):
        c = proj(expr, n)
        ans += c * beta * (1 - n**2) * sp.sin(n * th)
    return sp.trigsimp(ans)


def B(u, v):
    # Dimensionless critical relation: alpha*k = r*beta.
    return -r * beta * (u * sp.diff(v, th) + v * sp.diff(u, th)) / 2


def C(u, v, w):
    return -beta * u * v * w


H2 = -r * sp.sin(2 * th) / 6
R3 = 2 * B(phi, H2) + C(phi, phi, phi)
a3 = sp.factor(proj(R3, 1))
H3 = (r**2 + 1) * sp.sin(3 * th) / 32

R4 = 2 * B(phi, H3) + B(H2, H2) + 3 * C(phi, phi, H2)
H4 = (
    r * (r**2 + 9) * sp.sin(2 * th) / 864
    - r * (13 * r**2 + 27) * sp.sin(4 * th) / 2160
)

R5 = (
    2 * B(phi, H4)
    + 2 * B(H2, H3)
    + 3 * C(phi, phi, H3)
    + 3 * C(phi, H2, H2)
)
a5 = sp.factor(proj(R5, 1))

u = A * phi + A**2 * H2 + A**3 * H3 + A**4 * H4
Aprime = a3 * A**3 + a5 * A**5
residual = sp.expand(sp.diff(u, A) * Aprime - (L(u) + B(u, u) + C(u, u, u)))

print('a3 =', a3)
print('a5 =', a5)
print('log_coefficient =', sp.factor(-a5 / (-a3)))
for order in range(1, 6):
    center = sp.factor(proj(residual.coeff(A, order), 1))
    print(f'center_residual_A^{order} =', center)
for order in range(1, 5):
    vals = [sp.factor(proj(residual.coeff(A, order), n)) for n in range(1, 7)]
    print(f'all_modes_residual_A^{order} =', vals)
