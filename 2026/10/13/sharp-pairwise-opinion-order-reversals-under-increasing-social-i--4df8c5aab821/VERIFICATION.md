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

# Reproducible verification

The proof establishes its unbounded-order claims analytically via a real-symmetric Laplacian spectral decomposition, a proper rational-function degree bound, simple eigenvalues and nonzero first-edge eigenmode differences on paths, and proper partial fractions. Strict global variance decrease follows directly from a termwise differentiated eigenmode expansion.

`verification.py` is self-contained given Python 3 and SymPy. Execute `python verification.py` in the directory containing it. The actual local exact-arithmetic verification returned:

```
VERIFY_OK exact_path_profiles=4 designed_crossings=1+2+3+4 explicit_five_path=1
```

The four path checks cover sizes three through six, which have one through four distinct prescribed crossing locations respectively. The five-path formula and its full denominator identity are checked exactly. The checks are not an exhaustive classification of arbitrary graphs and are not the basis for the infinite-size proof. Numerical trajectories, empirical validity, independence, and previously unknown theorem-equivalence checks are not claimed.
