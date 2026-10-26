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

# Reproducibility

Run `python verify.py` using Python 3 and `mpmath` for optional high-precision asymptotic checks. The exact finite enumeration and ratio tests require only the Python standard library. A complete run reports `PASS 29784 exact or high-precision assertions` with `mpmath` installed.

The checker independently sums Dirichlet-multinomial probabilities over every weak composition in five small parameter systems, including heterogeneous rational concentrations. It tests the exact event probabilities, ratio and adjacent quotient, then tests the unit-concentration formula across a larger grid. The final high-precision checks compare the predicted second-order coefficient to Gamma evaluations for large category counts.

These finite computations provide consistency tests, not an infinite proof. The proof of the global one-crossing property uses Gamma convexity and decreasing trigamma, and the asymptotic needs a controlled expansion.
