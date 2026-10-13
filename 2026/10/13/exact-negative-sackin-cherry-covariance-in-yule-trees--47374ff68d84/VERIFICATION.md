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

Run `python3 verify.py` with Python 3 and no third-party packages. This exact-rational program starts from the two-leaf rooted binary tree and computes all distinct unlabeled tree shapes reachable by successive uniform leaf splits, accumulating shape probability weights and the Sackin, cherry, and cherry-tip-depth statistics. It matches the claimed covariance and marginal formulas for every size from two through ten leaves, without floating point. The outputs include nine size checks and the final `ALL EXACT ENUMERATION CHECKS PASS` line.

The analytic proof, including the mixed conditional recurrence and telescoping covariance recurrence, applies to all sizes. The finite program checks small instances but is not a certificate for infinitely many sizes. No independent audit has been performed.
