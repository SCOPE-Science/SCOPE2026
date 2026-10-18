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

# Reproduction and limits

Run `python verify_joint.py` using Python 3 with only the standard library. The checker enumerates every labelled antisymmetric transitive order on one through five points (the cumulative counts are 1, 4, 23, 242, and 4,473). For every poset it independently enumerates all upsets, constructs the pseudocomplement by checking intersections with principal upsets, checks the weak-excluded-middle and double-negation counts and intersection against the closed formulas, and tests the necessary-and-sufficient structural characterization of zero neither-count.

Observed final output:

`VERIFY_OK all labelled posets <=5 4473`

This is bounded computational corroboration. The proof for arbitrary finite posets is contained in RESULT.md, including both directions of the frame classification. No outside oracle, formal proof assistant, or independent expert check is claimed.
