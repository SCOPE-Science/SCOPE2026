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

# Verification of the mathematical finding

The package includes `CHECK.py`, a standalone Python-standard-library checker. To replay the supplementary numerical tests, execute `python3 CHECK.py` in the directory containing this file. The actual final checker run completed with:

`VERIFY_OK 2198 supplementary_assertions`

The checks independently evaluate the normalized path eigenvector equations and inner products for small path sizes, compare direct square-matrix elimination against the exact spectral Vandermonde product, bracket the predicted unique stationarity point for several finite path models, and approximate the continuum integral roots for three bandwidth fractions. They also check the limiting three-mode root relation, which is a consistency diagnostic rather than an additional claim of the theorem.

The exact determinant identity for all finite sizes follows from the explicitly displayed eigenbasis and the Vandermonde formula. Uniqueness follows from the analytically negative second logarithmic derivative. The continuum asymptotics follow from compact-uniform convergence of the normalized path spectral profiles and triangular Riemann sums. Numerical assertions are finite regression tests; they neither cover all sizes nor constitute proof of the asymptotic statements. The approximate displayed constants arise from the exact defining integral equation; no claim of interval-certified decimal rounding is made.

No independent audit has been performed.
