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

Run `python verify.py` with Python 3.9 or later and the standard library only. The program checks the signed monomial derivative formula against direct integer matrix multiplication, the finite-state Poisson/martingale variance identities with exact fractions, and finite-horizon visit-count distributions by two methods.

The executed output was:

```
CHECK_OK derivative_words=2550 poisson_vectors=984 exact_moment_distributions=45
```

The code is a finite consistency check. It does not independently establish the all-dimensional central limit theorem, whose proof uses the explicit Poisson identity and the standard finite-state martingale central limit theorem. The key external premise is the originating paper's full Bernoulli symbolic coding under normalized invariant Lebesgue measure. The strict limits are for fixed dimension; no dimension-uniform limit is tested or asserted.
