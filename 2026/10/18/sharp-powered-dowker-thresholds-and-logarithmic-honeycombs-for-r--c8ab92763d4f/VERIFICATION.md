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

Run `python check.py` in the same directory as this document. It needs only the Python standard library. The checker computes certified rational intervals for trigonometric values, verifies every finite strict weak-log-Dowker inequality for regular even polygons of orders below 32 outside the three exceptional cases, and certifies the disk-comparison constant for all higher orders.

The analytic proof separately covers infinitely many polygon orders, ordinary Dowker convexity for powers at least one, exact equality in the three exceptional source-formula triples, the arithmetic--geometric mean passage from logarithm to positive powers, and the published normed-plane implication. The script is not a substitute for those arguments. External independent mathematical review has not been performed.
