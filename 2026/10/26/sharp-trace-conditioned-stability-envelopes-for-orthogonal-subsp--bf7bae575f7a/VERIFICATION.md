---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The centered difference is exact. In the Hessian basis, squared coordinates close under B = D + b eta^2 1 (lambda_i^2)^T. The coefficients follow from the beta diagonal moment and projector idempotence; a-1 = (d-2)(d-k)/(k(d-1)(d+2)) is nonnegative. Similarity by diag(lambda_i) gives M = D + b eta^2 lambda lambda^T, symmetric positive semidefinite. Strict stability requires I-M positive definite, hence each D_i<1, and after diagonal congruence the remaining rank-one condition is exactly the claimed scalar inequality. The scalar increases from zero to infinity below the common pole. For eta above the pole even a largest-eigenvalue diagonal entry excludes stability. For eta=0 the iterate is fixed; for eta<0 the mean iterate grows for every nonzero start. For k<d and eta>0 strict positivity makes the Perron mode visible from every nonzero squared-coordinate initialization, including at the boundary. The column sums establish the isotropic bound and strict non-scalar improvement. Strict convexity gives the balanced and saturated spectra with exact equality conditions, including coinciding degenerate trace endpoints. The k=d bound is a uniform threshold, not a per-start assertion for initializations missing the top eigenspace. Independently recovered both secular polynomials and checked 28 spectra using symmetric eigenvalues (python /workspace/independent_checks.py 4).

## originality

PASS

Credit the prior covariance formulation, the spherical k=1 stability criterion, the Haar moments and the known isotropic/sufficient baseline. The supported distinct contribution is the explicit all-spectrum rank-k orthogonal specialization and sharp conditioned spectral envelopes, not the general covariance method or the rank-one threshold in spectral-radius form.

## value

PASS

The fixed-curvature-statistics question is natural for step selection: the extrema and trace do not identify the edge, but they determine exact attainable best and worst limits. The strict envelope, equality cases and explicit separation quantify what information is lost beyond a simple safe-step bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
