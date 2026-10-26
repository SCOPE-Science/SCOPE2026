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

# Reproducibility

The proof in `RESULT.md` is analytic and applies to every integer degree and nonnegative real time. The `check.py` script independently constructs the vertex/edge incidence matrices, forms both Laplacians, compares their heat intertwining, and computes every absolute row sum of the edge heat matrix. Run with Python 3, NumPy and SciPy by executing `python check.py` in the extracted directory. In one actual execution, the script printed `CHECK_OK cases= 63 max_abs_error= 4.619e-14` and values of the peak for degrees 2, 3, 10, 100 and 1000.

The finite matrix experiment does not establish positivity or optimality for arbitrary degrees and times; those require the spectral and positive-convolution arguments in the proof. The source comparisons do not establish historical uniqueness. Independent audit has not been performed.
