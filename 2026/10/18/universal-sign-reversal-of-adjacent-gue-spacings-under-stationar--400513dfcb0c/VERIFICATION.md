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

Run `python3 check.py` from this directory. The checker uses only Python standard library operations: composite Simpson quadrature, exact closed-form constants, deterministic and two-point renewal laws, and exponential renewal age moments. It tests 234 assertions and prints moment values and signed covariance coefficients on success.

The analytical argument proves the all-distribution statements. The numerical checker samples finite parameter cases and cannot prove universal renewal assertions or exclude unseen prior literature. The proof specifies the Brownian variance convention and equality cases. No independent external mathematical audit has been performed.
