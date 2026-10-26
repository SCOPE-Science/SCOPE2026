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

# Verification summary

The included `check.py` operates using Python's exact `fractions.Fraction`. It inverts the affine least-squares Gram matrix and constructs the entire finite projection kernel independently of the claimed probability formula. It then tests induced endpoint norms, rare-vertex rows, sign extremizers, weighted kernel symmetry and idempotence, three four-coordinate rational values and both strict mean-preserving spread directions and the componentwise monotonic inequality across sampled rational biases.

Run `python check.py` with standard Python (no external libraries required). The completed local run returned:

```
PASS {'assertions': 4863, 'matrix_instances': 38, 'bias_comparisons': 500}
```

These are only finite consistency checks. The proof of arbitrary-dimensional norm equality, localization, unique minimization, and limiting supremum appears in `RESULT.md`; no program run or finite enumeration substitutes for those universal arguments. Historical priority beyond the inspected literature is not independently settled.
