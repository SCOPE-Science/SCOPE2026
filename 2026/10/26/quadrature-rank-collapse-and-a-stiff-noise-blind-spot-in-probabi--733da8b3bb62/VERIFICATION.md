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

# Reproduction

Run `python verify.py` using Python 3's standard library. The program creates Gauss–Legendre rules, verifies their polynomial moments, builds the impulse-response covariance and its scalar noiseless Gaussian correction, checks the full two-node closed form, compares exact and quadrature formulas, and tests the forced-ODE error. At the recorded run it passed 2,886 deterministic assertions.

A hand-checkable example takes \(a=h=\kappa=1\): the midpoint-filtered mean is approximately \(0.3934693402873666\), while the exact forced solution is approximately \(0.36787944117144233\). The one-node posterior position variance is exactly zero by its rank-one conditional covariance formula. The exact-covariance filter instead has one-step variance approximately \(0.032755957487965615\), and two-node Gauss quadrature gives approximately \(0.0315177113279678\).

Analytical verification is in `RESULT.md`: \(Hv(s)=1\), weighted-variance covariance identity, monotonicity and one-/two-node rank, smallest-node Laplace asymptotics, induction on the filtered mesh covariance, and \(2\sinh(z/2)>z\). Numeric test loops alone do not prove the universal statements or the asymptotic equivalences. No independent audit has been performed.
