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

# Reproducible checks
Run `python3 verify_balanced_nilpotent.py` with Python 3 standard library only. The actual unpacked verifier was executed and returned `VERIFY_OK_BALANCED_NILPOTENT_LAYERS`.

It constructs every partial bijection on up to six labeled points and directly tests the upward-layer arrow restriction for every ordered composition with at most four positive parts. Independent polynomial recursion counts transversal-colored partitions by rank, and all coefficients agree. A separate exhaustive comparison of all ordered compositions with sizes through twelve and at most five parts finds exactly balanced compositions as coefficientwise maximal.

No finite computation proves the universally quantified theorem; its proof is the path-partition bijection, the marked-recoloring double count, and the previously published classification of maximal bounded-nilpotency-class subsemigroups. No independent audit was performed.
