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

# Reproducibility and checks

Run `python verify.py` with Python 3 and `mpmath==1.3.0` (or compatible implementation). The script uses direct high-precision Fourier/cosine quadrature of the fractional phase difference, rather than subtracting two nearly equal position-space integrals. The verifier was executed on its packaged source and printed:

```
PASS: 38 direct numerical consistency assertions
```

The 38 checks include six Gaussian Fourier-integral evaluations and six evenness identities at two positive times; four fractional-order derivative comparisons; eight implicit-centering and crossover-envelope comparisons per-time block including decreasing-error and high-precision checks; four leading logarithmic-Fourier coefficient checks; and two far-tail coefficient comparisons. Numeric tolerances are shown in the source code and apply only at the explicitly tested parameter values.

The proof of the theorem, including its uniform remainder and all infinitely many oscillatory subsequences, is analytic. Quadrature cannot certify uniformity or infinite limits. No external independent audit or validation has been performed.
