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

# Verification and reproducibility

The mathematical object, full claim and analytic proof appear in `RESULT.md`. Run the reproducibility diagnostics with `python3 check.py` from the directory containing the files. The checker uses only Python's standard library and, in its completed run, printed:

```
PASS: 53019 finite assertions; exact rational identities, continuum-grid design checks, independent Fourier quadrature, finite-horizon integration, and seeded path simulation
```

The checker uses independent implementations of the stationary variance, the frequency-spectrum Fourier integral and the finite-time average-variance integral, as well as a seeded simulation of diffusion with Poisson multiplier jumps. It also tests the exact rational denominator identities and inequality boundaries. Finite grids and Monte Carlo observations cannot prove global continuum optimization or the central limit theorem. Both of those are supplied by the factorized inequality/derivative argument and the jump-martingale argument in the proof. No independent third-party audit or formal proof certification has been performed.
