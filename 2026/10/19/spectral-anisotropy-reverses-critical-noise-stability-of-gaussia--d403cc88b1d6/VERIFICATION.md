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

# Verification protocol

The standalone `verify.py` checks exact finite-step log-energy algebra for dimensions one through nine, exponents on both sides of the critical value, the two-dimensional logarithmic angular integral, the strict anisotropy comparison at fixed trace, the critical mean trace identity, selected stationary Mellin cumulants, and expanding-log recurrence identities. It uses a fixed-seed generator and deterministic midpoint quadrature to make the numerical checks reproducible.

Command: `python verify.py`.

Observed output:

```
PASS: 1927 finite exact-identity and numerical checks
critical examples (mu): 0.11593151565841253 -0.3054725200172801
```

**What is actually proved:** The text in `RESULT.md` derives all infinite-time and zero-drift claims analytically from exact reductions, standard laws of large numbers and random-walk recurrence, stationary-process ergodicity, and a strict Hessian inequality. The independent Gaussian draws, positive-definite domain and positive initial energy are essential.

**What is not checked by this program:** Almost-sure convergence over infinitely many iterations, mathematically exhaustive originality, extensions to nonlinear nonconvex objectives, approximate Hessians, or toroidal projection. No external or independent mathematical audit is represented by this file.
