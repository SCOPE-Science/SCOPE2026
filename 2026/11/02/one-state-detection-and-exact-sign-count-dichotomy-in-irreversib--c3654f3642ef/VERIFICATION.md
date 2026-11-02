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

The analytical proof is in `RESULT.md` and the complete executable numerical cross-check is in `check_threecycle.py`.

Run from the directory containing both files:

```sh
python3 check_threecycle.py
```

The script uses only the Python 3 standard library. It implements Poisson uniformization directly for the three-state transition generator, independently of the closed-form spectral solution. The observed run passed 13,747 comparisons/assertions; maximum absolute discrepancy was \(5.088\times10^{-15}\). It separately checks the two exact boundary examples and the identity of the unique negative-state indicator for positive-discriminant random cases.

The full infinite statements, including all positive rates, all lags and the double-root boundary, follow from the algebraic proof. Finite sampling, a numerical tolerance and a source search cannot establish mathematical universality or historical uniqueness. Independent mathematical validation and independent priority assessment have not been performed.
