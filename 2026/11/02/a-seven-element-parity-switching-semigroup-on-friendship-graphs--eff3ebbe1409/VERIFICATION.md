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

# Verification details

Run `python artifacts/verify.py` with the Python standard library from the package root. The program performs complete state enumeration for each \(m\in\{1,2,3,4,5,6\}\) and matrix-rank calculations from basis vectors. For \(m\ge2\), it checks seven distinct transformations, their predicted ranks, the exact fixed-point populations, and collapse under all three minimal reset words. For \(m\in\{2,3\}\) the program also checks every switching word of length at most seven, across every initial state, against its canonical seven-map normal form.

The expected final line is `ALL CHECKS PASS`. The algebraic proof in RESULT.md establishes the claims for all integers \(m\ge2\); these finite tests only validate boundary handling and implementations. No independent human audit or external certification has been performed.
