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

# Reproduction and verification

Run `python3 CHECK.py` with Python 3.9 or later; the checker uses only the standard library. It verifies the sorted singular-value map on an exact rational mesh, the rank-two termination law with exact fractions, and the asymmetric three-mode similarity identity for 26 steps at 90-digit decimal precision. The checker is a finite consistency check, not an exhaustive or independently verified proof for infinitely many real inputs; the infinite claims follow from the algebra in RESULT.md.

Scientific scope is limited to the thin-polar exact nonnegative line-search iteration on the isotropic Frobenius quadratic. No claims about independent audit, certification, or general numerical precision are made.
