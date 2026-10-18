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
# Verification of the weighted-line Lipschitz formula

The theorem is established analytically in `RESULT.md`. The independent audit channel has not been run and cannot be inferred from this record.

The standalone Python 3 program `check_weighted_line.py` uses a fixed random seed, generates strictly positive line weights and positive/negative residuals satisfying the exact zero-moment balance up to floating-point rounding, and checks 108,000 normalized gradient comparisons against the claimed upper bound for dimensions 2 through 5 and exponents 1.2, 1.5, 1.9, 2.1, 2.5, 3, 4, 7, and 15. Additional tests generate exact analytic two-support moment-balanced tangents for superquadratic exponents and limiting gradients with one nearly vanishing residual below the Hilbert exponent.

Run `python3 check_weighted_line.py` in the extracted directory. Expected output contains `PASS 108000 bounded residual-gradient comparisons` and `PASS prescribed two-support extremizers and endpoint gradients`. Numerical diagnostics do not prove universal statements. The delicate infinite-family steps are the dual sign-mass reduction and the subquadratic smoothing argument, which must be checked from the displayed proof rather than inferred from tests. No claim of independent validation or machine-certified proof is made.
