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

The theorem is analytic for every \(m\ge2\) and \(a>0\).

`checker.py` directly integrates the Dirichlet density in dimensions one and two for selected noninteger and integer power exponents, independently checking the mixed covariance without using the differentiated-moment derivation.

It separately verifies the Greenwood specialization, both exact marginal variances, the finite correlation formula, and numerical convergence of the squared correlation to \(1/[4(\pi^2/6-1)]\) over thousands of finite values.

These computations are supplementary. The all-parameter result follows from the exact Dirichlet moment and log-moment identities in `RESULT.md`.
