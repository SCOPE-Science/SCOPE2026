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

# Verification and limits

Run `python verify_poisson_threshold.py` with a Python 3 environment satisfying `requirements.txt`. Actual execution returned:

`VERIFY_OK: 3 exact rational identities; 21 split-integral checks; critical and transition tests; moment-optimality checks; one illustrative sample-path convergence check`

The rational identity checks compare independently written holding-interval multiplier formulas. The integral checks numerically integrate the same finite logarithmic potential in two different coordinate systems, including samples on both sides of the critical intensity and the critical closed form. Other tests check the asymptotic cotangent coefficients and the sample-index mean-square minimizer. A seeded finite sample path is a demonstration of the strong-law prediction, **not** its proof.

The theorem's uniform-in-parameters correctness instead relies on the analytical beta-integral, principal-value/digamma identity, endpoint asymptotic expansions and renewal strong law in `RESULT.md`. The computed examples cannot prove any infinite-time or universal statement. No independent audit or external certification was performed. A closely related 1972 article was inspected at abstract level only and remains an originality risk.
