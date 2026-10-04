---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

For a centered ellipsoid, linear invariance reduces the calculation to the Euclidean unit ball. With
\[
\rho=1-e^{-R},
\]
the Holmes--Thompson volume is
\[
V_E(R)
=
n\omega_n
\int_0^\rho
\frac{t^{n-1}}{(1-t^2)^{(n+1)/2}}\,dt.
\]

Set
\[
z=\operatorname{artanh}\rho
=
\frac12\log(2e^R-1).
\]
The substitution
\[
t=\tanh s
\]
gives
\[
V_E(R)
=
n\omega_n\int_0^z\sinh^{\,n-1}(s)\,ds.
\]

The published Hanner formula is
\[
V_H(R)
=
\frac{4^n}{n!\,\omega_n}z^n.
\]
Hence the quotient differs by a positive constant from
\[
G_n(z)
=
z^{-n}\int_0^z\sinh^{\,n-1}(s)\,ds
=
\int_0^1u^{n-1}
\left(\frac{\sinh(zu)}{zu}\right)^{n-1}du.
\]

For \(n\ge2\), the integrand is strictly increasing in \(z>0\) for every \(u>0\), because
\[
\frac{d}{dx}\frac{\sinh x}{x}
=
\frac{x\cosh x-\sinh x}{x^2}>0.
\]
Thus \(G_n\) is strictly increasing.

The embedded `verify.py` was replayed from its actual package path. It numerically evaluates the ellipsoid volume in both the original radial variable and the hyperbolic variable, verifies the exact quotient normalization, stress-tests monotonicity over dimensions \(2\) through \(12\), and checks the small-radius Mahler-product normalization.

The replay output was:

`VERIFY_OK Funk ellipsoid Hanner ratio`

The numerical checks are consistency tests only. The all-dimensional, all-radius result is established by the analytic monotonicity argument.
