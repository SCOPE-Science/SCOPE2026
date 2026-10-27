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

# Verification and limits

The embedded standalone `verify_winding.py` was executed directly with Python 3 using only the standard library. For every integer network size from two through sixteen, its rational calculations checked all nonzero residue classes, the second-difference integrality of each class representative, the candidate minimum norm, the exact threshold count (including saturated sine preimages), and the stable count immediately above threshold. Output ended in `ALL_EXACT_WINDING_CHECKS_PASS`.

The general theorem is proved in `RESULT.md` by an exact cyclic-residue argument and discreteness of the inverse lattice. Finite checks are not exhaustive evidence for all network sizes. No numerical continuation or independence certificate is claimed. Literature comparison has a residual historical-priority risk.
