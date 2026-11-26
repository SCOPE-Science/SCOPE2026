---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Computational checks and limits

The retained `artifacts/verify.py` contains numerical comparisons of the exact finite-field probability at radical dimensions 80 and 81 against the limiting constant for field orders 2 and 4, with relative tolerance \(10^{-8}\). It can be run from the package root using Python 3; success ends with `FULL_VERIFY_OK`. This script includes additional bounded map and orbit checks for the structural inputs, not separate novelty claims for those inputs. The proof of the sharp asymptotic is in `RESULT.md`, which also gives a direct series calculation and tail bound for the displayed constants.
