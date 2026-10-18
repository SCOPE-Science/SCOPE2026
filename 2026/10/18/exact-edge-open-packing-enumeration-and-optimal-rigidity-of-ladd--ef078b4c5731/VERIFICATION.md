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

# Reproducibility checks

Place `verify.py` and `rational_certificate.json` in the same directory and execute `python3 verify.py` with a standard-library Python 3 installation. The certificate contains the complete common denominator and every state numerator for the 17-state transfer system; the verifier multiplies exact integer-coefficient bivariate polynomials to check the complete system, so these identities are not a truncated-series argument. It independently builds the ladder edge sets and excludes common-edge conflicts by direct endpoint inspection for all 74,898 subsets in orders 1 through 6, matching all coefficients. It verifies the 17-state potential inequality exhaustively and compares the proven optimal-size and multiplicity formulas with the transfer computation for orders 1 through 200; it checks the all-set recurrence through order 39. See `verification_output.txt` for actual output.

The infinite-family proof uses an exhaustive symbolic 17-state identity and an explicit potential argument. Brute-force small cases and bounded recurrences are regression checks only; they are not presented as proofs for all orders. Independent audit: not performed.
