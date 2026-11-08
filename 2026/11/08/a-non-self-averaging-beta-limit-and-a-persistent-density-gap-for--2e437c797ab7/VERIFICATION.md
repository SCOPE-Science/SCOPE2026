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

Run `python verify.py` using Python 3 (standard library only). The actual packaged checker was run and returned:

```
PASS: exact finite labeled/lumped stationary comparisons = 9
PASS: total exact generator, covariance and beta-moment identities = 212
LIMIT: finite b enumeration is not used to prove the asymptotic convergence.
```

The checker independently assembles full labeled finite-state infinitesimal generators and the symmetry-lumped generators, solves both using rational Gaussian elimination, and checks the exact stationary covariance formula. It also substitutes exact rational Beta moments into the stationary moment recursions at 5 positive noise rates through degree 10. No floating-point tolerances are used for these checks.

What the computations do **not** establish: convergence of all stationary measures as the leaf number tends to infinity, uniqueness of the limit, absolute novelty, or generalizations beyond the stated star model. Those infinite assertions are established in the analytic proof using uniform generator convergence, zero-flux stationarity, and a determinate polynomial-moment recursion. Independent mathematical audit remains not performed.
