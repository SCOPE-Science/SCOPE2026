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

# Verification record

The standalone `verify.py` reconstructs the game from adjacency lists, computes exact rational utilities before and after each possible exchange, and checks the all-configuration Nash criterion and welfare maximization by brute force. It verifies 10,048 equal-part placements in 63 population classes. For two-vertex parts it checks 3,353 color placements, 23,520 profitable exchanges, 22 exact hitting-time distributions, the first two moments, and path-count decrement. A seven-vertex unequal-part witness is checked separately.

To reproduce, place `verify.py` in the same directory and run `python verify.py`. Python 3 standard library alone is required. Output ends with `ALL EXACT CHECKS PASSED` if every assertion succeeds. This finite test set does not certify the infinite theorem: the theorem is justified by the algebraic proof in RESULT.md. The computations do not establish publication priority or an independent external audit.
