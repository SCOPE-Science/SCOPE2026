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

# Verification record

Mathematical verification uses the exact radial Laguerre decomposition and a separate Hermite-degree argument for the lower bound. The variable-dimension upper bound follows from a normalized sine-profile trial polynomial in the radial Jacobi basis. These steps are supplied in `RESULT.md` and do not rely on floating-point output.

`verify.py` independently builds the full multivariate compressed multiplication matrix and tests its smallest eigenvalue against the radial Jacobi eigenvalue at 24 finite parameter combinations. `verify_output.txt` contains the actual run output and finite critical-scale examples. Execute `OPENBLAS_NUM_THREADS=1 python verify.py` (Python 3 with NumPy and SciPy).

The numerical samples are illustrative; 24 finite comparisons and finite-degree asymptotic tables do not exhaust all dimensions, polynomial degrees, or asymptotic sequences. No independent audit has been performed.
