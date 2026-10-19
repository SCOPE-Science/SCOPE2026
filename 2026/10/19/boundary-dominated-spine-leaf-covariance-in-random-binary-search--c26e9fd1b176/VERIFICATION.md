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

Run `python verify.py` using Python 3; it requires no third-party modules. The implementation independently enumerates all permutations through eight keys and computes exact rational covariance and conditional-regression moments from the corresponding priority arrays. It compares these with the displayed finite-order formulas and separately checks the symbolic telescoping and conditional-mean identities at orders through 1000.

The reported checks passed: 2069 exact-rational comparisons and full enumeration of 46232 insertion orders. Computation does not establish the infinite statement; its proof is the finite local interaction calculation, boundary summation and coefficient recurrence in RESULT.md. The result assumes continuous priorities (so there are no ties) and internal, not external, leaves. Independent validation has not been performed.
