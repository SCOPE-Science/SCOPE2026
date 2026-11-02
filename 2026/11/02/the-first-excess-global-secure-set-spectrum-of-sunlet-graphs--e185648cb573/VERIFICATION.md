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

The standalone `verify.py` uses no external libraries. It reconstructs the sunlet's original adjacency and closed neighborhoods, enumerates every pair-state configuration of cardinality at most one above the domination lower bound, and checks **every nonempty selected attack set** directly for cycles of lengths three through eight. It tests 2,292 such configurations and confirms the complete classification, two minima and the exact cardinality-one-excess coefficient for every tested length.

It separately checks the reduced core-boundary security identity against the original test and checks the structural formula for cycle lengths nine through eleven. The returned output ends in `VERIFY_OK`.

The proof's all-length conclusion rests on the neighborhood-charge identity and exhaustive structural word classification in `RESULT.md`, not on finite enumeration. Checks do not independently audit the theorem or certify comprehensive historical priority. The published 2011 grid-like-graph article could not be read in full, leaving a limited historical-priority uncertainty.
