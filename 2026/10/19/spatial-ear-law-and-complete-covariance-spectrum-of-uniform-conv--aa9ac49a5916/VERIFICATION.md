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

The analytical arguments in `RESULT.md` establish the all-size result. For finite corroboration, run `python verify_ears.py` under Python 3 (standard library only). This script creates triangulations recursively from the base edge, builds ear masks from incident diagonals, and uses superset-zeta accumulation of observed ear masks to check *all* possible joint inclusion events independently of the Catalan formula. It reconstructs rational covariance matrices, checks exact ranks, and evaluates analytic Fourier-mode eigenvector equations with numerical tolerance. It also enumerates the independent fair-bit \(01\) pattern on eight positions and verifies each of its \(256\) joint moments.

Observed output from the standalone script:

```
PASS exact triangulations 6916
PASS all joint ear-event sets 4080
PASS covariance entries, Fourier eigenvectors and exact ranks 8
PASS independent fair-bit local-moment model 256
PASS Catalan-ratio convergence samples 7
```

The finite checks cover convex polygon sizes four through eleven; this is **not** an exhaustive verification for arbitrary size. In particular, finite checking cannot prove positivity for all \(n\ge8\) or finite-dimensional convergence; explicit proof steps in `RESULT.md` establish these claims. The Fourier eigenvector check is numerical, while rational covariance rank and mixed-moment enumerations are exact. No external independent validation has been performed.
