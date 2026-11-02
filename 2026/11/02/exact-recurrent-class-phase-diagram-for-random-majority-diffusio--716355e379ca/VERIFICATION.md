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

# Verification of finite-state assertions

The complete proof is in `RESULT.md`. Run `python3 verification/verify.py` using only Python 3's standard library. The program independently computes positive-probability transition supports from the neighbor-majority update definition; finds sink strongly connected components; compares them to the predicted classes for all 216 ordered triples of sizes 1 through 6 on the lumped count chain and all 27 ordered triples of sizes 1 through 3 on the full labeled-coloring chain; and verifies 104 examples of exact swapped phases, uniform next-state probabilities and bichromatic-edge counts in the tied-largest class.

Observed output:

```
VERIFIED macro triples: 216 micro triples: 27 tied-class support checks: 104 cut checks: 104
Sample absorbing-class state sizes: [((1, 1, 1), [1, 1]), ((1, 2, 2), [1, 1, 4]), ((2, 3, 3), [1, 1, 8]), ((2, 2, 3), [1, 1, 2]), ((3, 3, 3), [1, 1]), ((2, 4, 4), [1, 1, 8])]
```

Finite computation cannot prove a universal theorem; the general proof uses neighborhood equality, exhaustive corner categories, direct closed-class verification and finite-chain reachability. No external independent assessment is represented by these tests.
