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

Execute `python3 check_cycle_convexity.py` in a standard Python 3 interpreter; no nonstandard dependencies or external data are required.

The program computes convexity directly from **all** shortest paths, checks the purported arc classification exhaustively through 13 vertices, enumerates every one- through four-vertex support on 3–17-vertex cycles, checks the precise cyclic-gap criterion for each triple, evaluates the complete adversarial online version-space recurrence through 15 vertices, and verifies complete constructive lower-bound decision trees through order 100. It prints `ALL_CYCLE_CONVEXITY_CHECKS_PASS` on success.

These computational checks are finite. Universal statements follow from the exact interval classification, cyclic-gap argument, counting, and explicit online threshold-tree construction in `RESULT.md`. No independent external audit has been performed.
