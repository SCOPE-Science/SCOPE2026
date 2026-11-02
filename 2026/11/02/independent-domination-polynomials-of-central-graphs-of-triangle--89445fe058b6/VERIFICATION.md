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

Run `python verify.py` with Python 3.8 or newer. The program builds central graphs directly from their definitions and checks independent dominating sets using both independence and domination predicates. It exhausts every labelled graph with four, five or six vertices that is triangle-free and has minimum degree at least two (560 graphs), then verifies two explicit same-degree-sequence counterexamples. Expected output ends with `VERIFY_OK`. This finite check is independent of the symbolic cardinality proof and does not certify unbounded order.
