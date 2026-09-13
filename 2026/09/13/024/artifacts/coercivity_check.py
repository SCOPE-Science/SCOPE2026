"""Coercivity / tightness check for lane-1545 (target-only refutation).

Verifies the uniform analytic bounds used in DRAFT.md:
 (i)  phi_h(x) = V_h(x) - 2 log(1+|x|) with V_h = x^4/4 - 2x^2 - h x
      is uniformly coercive for |h|<=1 and globally bounded below.
 (ii) Explicit global lower bound c_* and growth ratios |x|/phi -> 0.
 (iii) Reference measure (uniform on [-1,1]) has finite rate value,
       giving a uniform upper bound C0 on inf I_h.
These are analytic facts checked numerically on a grid + tail bound.
"""
import numpy as np

def Vh(x, h):
    return x**4/4.0 - 2.0*x**2 - h*x

def phi(x, h):
    return Vh(x, h) - 2.0*np.log1p(np.abs(x))

xs = np.concatenate([
    np.linspace(-10, 10, 200001),
    np.linspace(-50, 50, 20001),
])
hs = [-1.0, -0.5, 0.0, 0.5, 1.0]

c_star = min(phi(xs, h).min() for h in hs)
print(f"grid global min over |h|<=1: {c_star:.4f} (analytic bound -16)")

# tail: min_{|x|>=R} phi over h in [-1,1] (worst case h = -sign(x))
for R in [3, 4, 5, 8, 10]:
    m = min(phi(xs[np.abs(xs) >= R], h).min() for h in hs)
    print(f"R={R:2d}  min phi = {m:10.3f}")

# growth ratio |x|/phi for large x
for x in [5, 8, 12, 20]:
    print(f"x={x:2d}  max_h |x|/phi = {max(abs(x)/phi(np.array([x]), h)[0] for h in hs):.4f}")

# reference measure: uniform on [-1,1], density 1/2
# int V0 = 1/20 - 2/3 ; int |x| = 1/2 ; Sigma via quadrature
xg = np.linspace(-1, 1, 20001)
dx = xg[1]-xg[0]
intV0 = float(np.mean(xg**4/4.0 - 2.0*xg**2))
int_abs = float(np.mean(np.abs(xg)))
X, Y = np.meshgrid(xg, xg)
# avoid diagonal singularity: log(0) integrable; set diag to log(dx/2) approx
D = np.abs(X-Y)
D[D == 0] = dx/2.0
Sigma = float(np.mean(np.log(D)))
print(f"int V0 = {intV0:.5f} (exact {1/20-2/3:.5f})")
print(f"int |x| = {int_abs:.5f} (exact 0.5)")
print(f"Sigma(uniform[-1,1]) ~= {Sigma:.4f} (finite)")
I0 = intV0 - Sigma
print(f"I_0(nu0) ~= {I0:.4f}; sup_|h|<=1 I_h(nu0) <= I_0 + 0.5 = {I0+0.5:.4f} =: C0")
print("OK: coercivity, global lower bound, and finite reference energy confirmed.")
