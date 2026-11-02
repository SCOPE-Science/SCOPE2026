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

The proof is an all-parameter argument, not an extrapolation from finite tests. The sole extra program `verify_frontiers.py` enumerates original frontiers recursively, calculates exact online depth by a version-space recurrence, and calculates exact VC dimension on small instances by all coordinate-subset projections. Its test set includes arbitrary positive unary branches and mixed branching profiles. Larger cases test online dimension and an explicitly shattered support; the universal VC upper bound is supplied by the block-injection proof rather than by partial enumeration. Execute `python3 verify_frontiers.py` under Python 3 with no additional dependencies. No independent audit has been performed.
