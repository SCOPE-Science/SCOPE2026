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

Run `python verify_rigidity.py` with Python 3 and SymPy available. Its complete successful output is:

```
PURE_LINE_TRIPLE_INCIDENCE_CLASSIFICATION_OK 120 30
PROJECTIVE_NORMAL_FORM_AND_RECIPROCAL_ROOTS_OK
NEAR_FREE_NUMERICAL_CONSTRAINTS_OK
RIGIDITY_REPLAY_OK
```

The script checks every allowable labeled collection of three or four line-only triple points on six lines, the one-cycle structure of the residual double-point graph, the exact line-and-conic incidence equations, elimination to the quadratic equation, the determinant and tangency squares, and reciprocal-projective equivalence. The case exclusions and normal form are proved in `RESULT.md`, so the enumeration is a cross-check rather than a substitute for geometry. The new proof needs the previously published degree-four syzygy-rank calculation for existence, and does not claim to have generated a new Jacobian certificate. Neither independent external audit nor independent mathematical validation has been performed.
