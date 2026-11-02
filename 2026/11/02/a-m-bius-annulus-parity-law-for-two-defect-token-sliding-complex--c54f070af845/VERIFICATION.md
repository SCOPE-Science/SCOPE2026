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

Run `python verify_direct.py` and `python verify_gaps.py`. The first directly reconstructs labelled maximum independent sets of the actual cycle-power graph, checks every allowed slide, graph cycle of lengths three and four, all vertex links and every boundary component, and tests connectivity. The second builds configurations from cyclic gap compositions and independently constructs legal slides as gap transfers, checking the same cardinalities and local incidence table. Both programs finish with explicit `_ALL_PASS` markers.

The all-parameter argument is in RESULT.md. These finite enumerations are supporting checks only; they do not constitute an exhaustive search over infinite parameter ranges.
