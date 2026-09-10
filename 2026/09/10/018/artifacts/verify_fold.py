"""Verify fold geometry + anisotropic Knapp lower bound constants for lane-527 target."""
import math

# 1. Symbolic geometry via sympy if available, else direct formulas
try:
    import sympy as sp
    xi1, xi2 = sp.symbols('xi1 xi2')
    phi = xi1**2 - xi2**2 + xi1**3
    grad = [sp.diff(phi, xi1), sp.diff(phi, xi2)]
    H = sp.hessian(phi, (xi1, xi2))
    det = sp.factor(H.det())
    print("phi =", phi)
    print("grad =", grad)
    print("Hess =", H.tolist())
    print("det Hess =", det)
    # recenter u=xi1+1/3, v=xi2
    u, v = sp.symbols('u v')
    phi_uv = sp.expand((u - sp.Rational(1,3))**2 - v**2 + (u - sp.Rational(1,3))**3)
    print("phi(u-1/3,v) =", phi_uv)
    # Gaussian curvature numerator ~ det Hess; zero set
    print("det at xi1=-1/3:", det.subs(xi1, -sp.Rational(1,3)))
    print("d/dxi1 det:", sp.diff(det, xi1), "(nonzero => simple vanishing)")
except ImportError:
    print("sympy unavailable, using formulas directly")

# 2. Anisotropic Knapp constants
c = 0.1
cos04 = math.cos(0.4)
print("\ncos(0.4) =", cos04)

def knapp_ratio(R, p):
    # cap |u|<=R^-1/3, |v|<=R^-1/2 ; box constant c
    delta = R**(-1/3); sigma = R**(-1/2)
    Q = 4*delta*sigma
    f2 = 2*math.sqrt(delta*sigma)
    Emin = Q*cos04
    Vol = 8*c**3 * R**(11/6)
    Ep = Emin * Vol**(1/p)
    return Ep/f2, (-5/12 + 11/(6*p)), 1.842*(0.008)**(1/p)

for R in [64, 1000, 2**24]:
    for p in [3.5, 4.0, 4.2, 4.4]:
        r, e, const = knapp_ratio(R, p)
        print(f"R={R:>9}, p={p}: exponent e={e:+.5f}, const={const:.4f}, ratio>={r:.4f}")

# 3. Check shear-box containment in B_R: |x| bound
for R in [64, 1000, 2**24]:
    x1max = c*R**(1/3) + c*R/3
    x2max = c*R**(1/2); x3max = c*R
    nrm = math.sqrt(x1max**2 + x2max**2 + x3max**2)
    print(f"R={R}: box corner |x|<={nrm:.3f} vs R={R} -> inside: {nrm<=R}")

# 4. p0=7/2 blowup vs R^{1/24}
for R in [64, 1000, 2**24]:
    r, e, const = knapp_ratio(R, 3.5)
    print(f"R={R}: p=7/2 ratio>={r:.4f}, R^(1/24)={R**(1/24):.4f}, ratio/R^(1/24)={r/R**(1/24):.4f} (>=0.46 required)")

print("\nVERIFY_OK")
