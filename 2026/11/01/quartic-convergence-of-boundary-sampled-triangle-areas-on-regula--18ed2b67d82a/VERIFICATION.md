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

# Verification and reproduction

Run `python3 check.py` using the Python standard library. The checker independently adds up all distinct-edge midpoint-triangle areas and all repeated-edge expected triangles for integer side counts, compares their sum to the closed mean formula, and compares the exact second-moment identity to Monte Carlo draws. It also tests the strict ordering and leading quartic correction. The analytic proof in `RESULT.md` verifies the universal claims. Numerical and finite tests do **not** certify infinitely many side counts, historical novelty, or independent mathematical validation.
