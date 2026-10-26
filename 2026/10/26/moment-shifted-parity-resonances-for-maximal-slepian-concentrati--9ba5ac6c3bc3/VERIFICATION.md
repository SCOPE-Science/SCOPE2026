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

The analytic proof includes four checks: strict positivity and simplicity of the one-interval top mode, exact even/odd parity block reduction, cancellation of the even quadratic perturbation in the eigenvalue difference, and a uniform derivative bound establishing uniqueness and transversality at every sufficiently large resonance.

The standalone `numerical_check.py` reproduces the Gauss–Legendre/Nyström finite-matrix test for \(B=1\), \(\ell=0.8\), using 64 nodes. This is a nonrigorous numerical consistency check: it is not an infinite-dimensional eigenvalue certificate, and cannot prove existence of infinitely many crossings.

For \(n=6,10,20,40,80\), the computed half-distances are approximately \(3.009209103889,5.005516069504,10.002756056523,20.001377781126,40.000688859675\). They agree with the predicted \(n^{-1}\) shifts with decreasing errors. No external independent audit or validation has been performed.
