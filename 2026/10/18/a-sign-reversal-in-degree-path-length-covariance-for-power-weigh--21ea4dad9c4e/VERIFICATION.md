---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

Run `python3 verify_limit.py` with standard-library Python 3. It tests the finite telescope in equation (3) exactly and compares the resulting finite covariance to direct parent-sequence enumeration for orders 2 through 6 and exponents −3, −2, −1, 0, 1, 2, for 90 exact comparisons. It also checks the rational constants of the explicit sign-reversal example at exponent −2. The original `verify.py` is unchanged; it covers the finite covariance identity and selected checks for the linearly weighted example, not the endpoint rearrangement.

The infinite-size and large-label conclusions use the analytic argument in `RESULT.md`. In particular, the finite telescoping term in (3) and the Cesàro term in (2) must be combined before reading off the boundary contribution when the total weight is finite.
