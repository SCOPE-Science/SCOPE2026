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

The proof's all-size steps are the explicit switch, colour-refinement induction, planar exterior-arc embedding (with the exceptional eight-vertex strip handled by Kuratowski's theorem), and a four-cycle count via three-edge paths. No finite program substitutes for these arguments.

`verify.py` checked all 152 witness parameter pairs with \(2\le m\le n\le18\) apart from \((2,2)\), using NetworkX 3.6.1. It verified connectivity, planarity, equality of every refinement colour at every vertex until stabilization, and the exact signed four-cycle-count change. It also checked the four-vertex regularity premise for \(C_4\). The run output is supplied in `verification_output.json`.

Reproduce via `python verify.py` with Python 3.11+ and NetworkX 3.6.1. Exhaustion stops at side length 18; arbitrary-side correctness rests on the proof.
