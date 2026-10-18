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

## Reproducibility
Run `python3 certify.py` (Python 3.10+; standard library only). The program exhaustively generates the unrooted trees of orders 3 through 10, adds every nonedge, and tests every subset by a direct bitmask implementation of the defining condition. It asserts the graph counts, all extremal values, uniqueness of each cycle extremizer, and the eleven-vertex counterexample. Successful execution prints `VERIFIED`.

## Mathematical verification boundary
The finite generator is complete because every rooted tree is a multiset of smaller rooted trees, center-canonical codes identify unrooted tree isomorphism classes, and every unicyclic graph is a tree plus one edge. The symbolic cycle recurrence follows from the displayed four-state transfer matrix. The explicit pendant-star count follows by conditioning on the attachment hub. The strict all-order inequality is proved by induction in the main proof, not inferred from finite output.

## Limits
No complete extremal classification for orders at least eleven is asserted. This is self-reviewed only; no independent audit has been performed.
