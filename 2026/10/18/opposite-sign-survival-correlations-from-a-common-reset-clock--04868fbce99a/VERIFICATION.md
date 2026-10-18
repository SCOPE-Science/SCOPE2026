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

The proof uses exact Poisson point conditioning, the Brownian reflection formula, the convexity threshold \(d_2^2\ge6Dt\), and an exact beta integral. The displayed sufficient inequality on \(d_1\) guarantees a negative derivative at zero reset rate without numerical quadrature. Equal-distance strict positive covariance follows from a nonconstant conditional survival probability. The numerical standard-library checker separately evaluates a representative negative weak-rate integral and sample strict pointwise inequalities, but does not certify the analytic continuum result. No independent audit has been performed.
