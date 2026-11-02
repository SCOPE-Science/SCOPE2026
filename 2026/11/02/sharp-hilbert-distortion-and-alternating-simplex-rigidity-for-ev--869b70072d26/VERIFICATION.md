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

# Reproducibility and limits

Execute `python3 check_wheel.py` with standard Python 3 and no third-party packages. The actual run returned:

```text
CHECK_OK exact_rational_PSD_and_pair_bounds=12 rim_orders=14..36 edges=600 nonedges=3586
```

For each integer \(7\le m\le18\), the checker constructs the rational Gram matrix, verifies positive semidefiniteness by exact rational Schur-complement elimination, performs a fresh graph breadth-first search, and checks every graph metric pair against the exact rational squared-distortion bounds. The source file was executed from the same package directory before embedding. The all-\(m\) conclusion relies on the written Fourier argument, including the explicit separate estimate at \(m=7\); no finite test is presented as exhaustive proof. The checker does not verify historical novelty or independent mathematical validation.
