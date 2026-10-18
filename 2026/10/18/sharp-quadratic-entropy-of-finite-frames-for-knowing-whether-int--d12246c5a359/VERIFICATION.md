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

Run `python3 checker.py` with Python 3.8 or later. The checker enumerates all 2, 16, 512, and 65,536 labelled relations on one through four vertices respectively and evaluates both the row-type criterion and every Boolean valuation of the actual modal formula. Observed accepted-frame counts: 2, 10, 128, 3070. Every comparison agreed. It also checks all members of the fixed-part lower-bound family through eleven vertices, and for constructions through six vertices checks all valuations as well.

The inequalities for arbitrary n require the symbolic partition and bipartite-construction proof in RESULT.md; these computations are not substitutes for an infinite proof.
