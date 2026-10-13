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
# Verification guide

Run `python3 verify_corner.py` with Python 3.8 or later. It uses only the standard library.

The checker independently enumerates all labeled binary two-state transition pairs, tests the \(f\)-corner definition by breadth-first search over input words whose first letter is \(a\), and checks all products of qualifying factors. It then verifies the two displayed factors' strong connectivity, the two positive-distance values of three, and the effect of the word \(\mathtt{aba}\) on every product state.

The expected output is:

```
VERIFY_OK individual_corners=5 two_by_two_products=25 minimal_total_states=5 strong_factor_sizes=2,3 forward_positive_distance=3 reverse_positive_distance=3 joint_reset=aba
```

The elementary proof and the two-state structural classification are in `RESULT.md`. This is a self-review supported by executable finite checks, not an independent audit; the breadth-first searches certify only the displayed finite objects and the finite two-state census.
