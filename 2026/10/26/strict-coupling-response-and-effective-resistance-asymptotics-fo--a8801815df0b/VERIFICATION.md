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

# Reproducibility and checks

This package includes the standard-library Python 3 program `verify.py`. Invoke `python verify.py` from the directory containing the supplied files. It makes exact rational calculations on the two-vertex example and numerically solves stationary nonlinear equations on independently generated connected positive-weighted networks; 4,949 assertions passed in the recorded run. Exact mathematical content and one-sided parameter boundaries are proved in RESULT.md.

The identity tested is \(D'=-g^\mathsf T H^{-1}g\), with \(g=Lx\), along with the exact weak-coupling derivative and \(\lim_{\kappa\to\infty}\kappa^2D\). Rational checks are exact; finite precision and limited graph size are not evidence for infinitely many couplings or graphs. The proof rests on Hessian strict diagonal dominance and an exact Laplacian pseudoinverse identity, independently stated in RESULT.md. The program is not an independent audit, and publication priority is not independently certified.
