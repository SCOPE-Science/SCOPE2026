"""Check the boundary-zero/equilibrium identification for the parameter example in arXiv:2609.17336v1.

Uses only the Python standard library. The calculations reproduce exact equilibria
of the perturbed Rössler system and the blown-up coordinates of the numerical
initial data printed in Eq. (30) of the source.
"""
from math import atan2, hypot, pi, sqrt

eps = 1.0 / 500.0
a = 1.0
b1 = 1.0
c1 = 2.0
b = a + eps**2 * b1
c = 2.0 * a + eps**2 * c1
omega = sqrt(2.0 - a*a)

disc = c*c - 4.0*a*b
z_lo = (c - sqrt(disc)) / (2.0*a)
z_hi = (c + sqrt(disc)) / (2.0*a)

# For a=omega=1, the source's linear map is
# X=u+v-w, Y=-u+w, Z=v-w, hence
# u=X-Z, w=Y+u, v=Z+w.
def blown_coordinates(x, y, z):
    X, Y, Z = x-a, y+1.0, z-1.0
    u = X-Z
    w = Y+u
    v = Z+w
    r = hypot(u, v)
    R = r/eps
    W = w/eps
    theta = None if r == 0.0 else atan2(v, u)
    return R, W, theta

equilibria = [
    (a*z_lo, -z_lo, z_lo),
    (a*z_hi, -z_hi, z_hi),
]
leading_boundary_points = [
    (1.0-eps, -1.0+eps, 1.0-eps),
    (1.0+eps, -1.0-eps, 1.0+eps),
]
source_eq30_guesses = [
    (1.0-2.0*eps, -1.0+eps, 1.0-2.0*eps),
    (1.0+2.0*eps, -1.0-eps, 1.0+2.0*eps),
]

print(f"epsilon = {eps:.12g}")
print(f"discriminant = {disc:.16g}")
for name, point in zip(("E_low", "E_high"), equilibria):
    print(name, tuple(f"{q:.15f}" for q in point), blown_coordinates(*point))

for name, lead, eq in zip(("P_plus leading", "P_minus leading"),
                          leading_boundary_points, equilibria):
    err = max(abs(x-y) for x, y in zip(lead, eq))
    print(name, "max error to matching exact equilibrium =", f"{err:.12g}")

for name, point in zip(("Eq30 P_plus guess", "Eq30 P_minus guess"),
                       source_eq30_guesses):
    R, W, theta = blown_coordinates(*point)
    print(name, f"R={R:.12g}", f"W={W:.12g}",
          f"theta/pi={theta/pi:.12g}")
