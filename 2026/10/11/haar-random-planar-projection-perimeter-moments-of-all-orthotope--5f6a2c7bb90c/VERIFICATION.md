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

The theorem is proved symbolically by an exact conditional-Haar and beta-integral argument. The standalone `verify.py` provides independent numerical regression tests, **not** a proof for every dimension.

Its principal equalities are
\[
\ell_i=\|\operatorname{proj}_S e_i\|,
\qquad
\mathbb E\ell_i^2=\frac2d,
\qquad
\mathbb E\ell_i\ell_j=\frac{\pi H_d}{2(d-1)}\quad(i\ne j).
\]
The code integrates the beta density and angular-elliptic factor using high precision rather than substituting the closed hypergeometric value into itself. It separately generates Haar planes by QR factorization and compares Monte Carlo perimeter means, squared moments, and pair correlations against the exact formula. Small projected-cube hull perimeters are computed directly from projected vertices, independently checking the zonotope-perimeter identity.

An exact proof of the asymptotic variance follows by bounding the hypergeometric remainder after its linear term with the second moment of a beta law and applying a standard Stirling gamma-ratio expansion. Numerical evaluations at increasing dimensions merely confirm the trend.

**Scope of verification:** all dimensions in the theorem are covered analytically; the code tests representative finite dimensions only. The high-dimensional limit is a variance statement and makes no distributional claim.
