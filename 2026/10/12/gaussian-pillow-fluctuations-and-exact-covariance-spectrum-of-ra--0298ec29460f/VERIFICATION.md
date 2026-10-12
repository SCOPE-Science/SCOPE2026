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

# Reproducibility and proof limits

Run `python checker.py` with Python 3 and only the standard library. The source was actually executed, printing:

```
Exact permutation covariance checked for k=2..6: 245 pairs, max error= 3.469446951953614e-18
Discrete sine-eigenpair identities checked: 204
k= 4 n= 24 scaled variance=0.065141 exact=0.0625 kurtosis=3.2726
k= 5 n= 120 scaled variance=0.040275 exact=0.04 kurtosis=3.1542
k= 6 n= 720 scaled variance=0.060981 exact=0.0625 kurtosis=2.9809
All finite checks passed. Functional convergence requires the written proof.
```

The proof is analytic: the exact permutation covariance, Dirichlet covariance identity, uniform cell-kernel limit, exponential triangular-array Lyapunov bound, eighth-moment increment tightness, finite-grid tridiagonal spectral identity, and summable variance union bound appear in RESULT.md. The arithmetic checker verifies only finite instances and does not establish convergence in infinitely many mesh sizes. The Gaussian limit is weak convergence in continuous functions; an almost-sure coupling of the rescaled fields is not claimed. No external validation or independent audit has occurred.
