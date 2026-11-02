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

# Reproducibility checks and limits

Execute `python3 verify_rk2.py` using Python 3 and only its standard library. The script verifies the exact moment polynomial against direct enumeration of independently sampled rational two-point curvature laws, checks its global tableau variance gap, tests sharp stability roots over a parameter grid, evaluates the identity on rationally rotated two-dimensional positive-definite matrices, and checks the analytical heavy-tail contraction coefficient.

Observed output:

```text
VERIFY_OK exact_laws=162, variance_identity=162, frontiers=63, matrix_cases=108, shared_vs_independent=1 normalized_horizon_last=3.999988000
```

The proof itself is in `RESULT.md`. Finite enumerations and floating-point bisections do not certify claims for arbitrary dimensions, continuous laws, infinite time or large noise. Those claims depend on the algebraic expansions, the spectral theorem, a strictly positive derivative, and the Pareto moment calculation explicitly presented there.

No independent scientific validation has been performed. The literature comparison remains subject to independent publication-priority checks.
