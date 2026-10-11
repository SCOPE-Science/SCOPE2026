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

The theorem is proved by the affine cycle-kernel decomposition, free sums of two simplices, and the exact asymmetry rule for an affine join. The matching upper and lower bounds, including uniqueness, are symbolic and all-dimensional.

Running `python verify.py` in the directory containing this file gives:

```
VERIFY_OK cases= 270 reflection_identities= 3685
```

This standard-library script checks 270 deterministic, differently oriented semi-balanced cactus examples with interleaved cycles and bridges. Each check verifies the affine rank, cycle-circuit relation, positive center weights, and every sharp reflected-vertex decomposition by exact rational arithmetic. The code works directly from oriented edge lists that it constructs. Finite examples do not certify a universal theorem or publication priority.

The assertion \(s(Q_G)=H-1\) is proved by a general factor-join lower bound, not by numerical optimization. The reflection certificate alone would establish only an upper bound. No claims are made about non-semi-balanced orientations or graphs with overlapping cycles. Independent external audit and validation have not been performed.
