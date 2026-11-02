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

The analytic proof is in RESULT.md. The standalone pure-Python program `verify.py` was executed on the supplied file and produced:

`PASS 594 independent finite checks; all three parameter families and singular limits. No infinite proof claimed.`

Coverage: stationary gas/liquid flux ODEs; interface flux continuity; nonnegative orientation components; gas mass by numerical quadrature; normalization and central point-source condition; homogeneous-rate recovery; strict monotonicity over sampled parameters; and singular-layer coefficients and profiles. The code evaluates a finite collection of parameters and cannot establish the existence/uniqueness claim, all-parameter inequalities, the weak measure limit, or literature novelty. These require the explicit mathematical proof and comparisons.

The full stationary PDE is the stated phase-dependent mean-field model; this package does not provide a particle-based simulation, independent scientific review, or a finite-time stability certificate.
