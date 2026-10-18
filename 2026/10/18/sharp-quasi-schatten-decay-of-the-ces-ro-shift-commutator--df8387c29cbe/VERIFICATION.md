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
# Reproduction and limits

Run `python3 verify_commutator.py` using Python's standard library from the same directory as this file. The checked output is `CESARO_SHIFT_QUASI_SCHATTEN_FINITE_IDENTITIES_OK dimensions=28`.

The checker constructs the finite-dimensional Cesàro and unilateral-shift matrices over exact rational numbers; compares their commutator to the predicted strict-lower-triangular coefficient formula for all dimensions 2 through 29; reconstructs the strict lower-triangle reduction to an ordinary summation matrix; verifies exact first-difference inverses and tridiagonal Gram identities; and checks the finite closed-form sine spectrum against the squared Frobenius norm.

These tests do not certify the spectrum at infinite dimension. The analytical proof in RESULT.md supplies the global dyadic counting estimates, the exponentially low-rank off-block approximation, the two-sided Ky Fan transfer, and the critical ideal endpoint. The trace is the sum of diagonal entries only after trace-class membership is established analytically. No independent audit has been performed.
