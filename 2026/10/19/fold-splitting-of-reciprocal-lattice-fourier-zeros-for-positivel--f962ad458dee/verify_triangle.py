"""Independent high-precision checks for weighted-triangle Fourier-zero folds.

Requires mpmath. Analytic all-index and lattice-asymptotic proofs are in RESULT.md.
"""
from math import pi
import mpmath as mp

mp.mp.dps = 55
I = 1j


def segment_integral(z):
    if z == 0:
        return mp.mpf(1)
    return -mp.expm1(-I*z)/(I*z)


def base_transform(xi, eta):
    if abs(eta) < mp.mpf("1e-25"):
        return mp.quad(lambda x: (1-x)*mp.exp(-I*xi*x), [0, 1])
    return (segment_integral(xi)
            - mp.exp(-I*eta)*segment_integral(xi-eta))/(I*eta)


def perturb_transform(xi, eta, polynomial):
    if polynomial == "x":
        return I*mp.diff(lambda z: base_transform(z, eta), xi)
    if polynomial == "x_squared":
        return -mp.diff(lambda z: base_transform(z, eta), xi, 2)
    raise ValueError("unknown polynomial")


def close(actual, expected, tolerance=mp.mpf("1e-30")):
    if abs(actual-expected) >= tolerance:
        raise AssertionError(f"expected {expected}, obtained {actual}")


nodes = [(2, 1), (1, 2), (-1, -2), (2, -1)]
for m, n in nodes:
    k, l = 2*mp.pi*m, 2*mp.pi*n
    d = k-l
    close(base_transform(k, l), 0)
    close(mp.diff(lambda z: base_transform(z, l), k), I/(k*d))
    close(mp.diff(lambda z: base_transform(k, z), l), -I/(l*d))
    close(mp.diff(lambda t: base_transform(k*(1+t), l*(1+t)), 0, 2), 1)
    close(perturb_transform(k, l, "x"), -1/(k*d))

    for poly in ["x", "x_squared"]:
        u = mp.re(perturb_transform(k, l, poly))
        eps = mp.mpf("0.002")
        if -eps*u <= 0:
            continue
        scale = mp.sqrt(-2*eps*u)
        for side in [-1, 1]:
            def residual(x, y):
                v = base_transform(x, y) + eps*perturb_transform(x, y, poly)
                return mp.re(v), mp.im(v)
            guess = (k*(1+side*scale), l*(1+side*scale))
            root = mp.findroot(residual, guess, tol=mp.mpf("1e-27"), maxsteps=50)
            if abs(complex(*[float(z) for z in residual(root[0], root[1])])) > 1e-24:
                raise AssertionError("root residual too large")
            if abs((root[0]-k)/k-side*scale) > mp.mpf("0.002"):
                raise AssertionError("root disagrees with square-root scale")

for radius in [20, 100, 250]:
    eligible = splitting = 0
    for m in range(-radius, radius+1):
        for n in range(-radius, radius+1):
            if m*n*(m-n) == 0 or m*m+n*n > radius*radius:
                continue
            eligible += 1
            splitting += (m*(m-n) > 0)
    print(f"radius={radius} lattice_nodes={eligible} positive_fold_nodes={splitting} fraction={splitting/eligible:.9f}")
print("Local derivative, root, and lattice-sector checks passed.")
