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

# Reproducibility and verification

The exact Fourier-series calculation and the stationary-point Hessian in `RESULT.md` establish the theorem analytically. The following numerical programs test the formula in finite precision but do not certify universal quantifiers.

Run with Python 3 plus SciPy and mpmath installed:

```
python annular_opt_check.py
python high_precision_bias.py
```

The first program passed 270 test assertions over annular thicknesses, radii, reflection symmetry, convex derivatives, and the two asymptotic limits. It numerically differentiates the paired Laurent series analytically term-by-term and solves the unique derivative zero by Brent's method. Truncation uses an exponential mode cutoff.

The second program uses high-precision mpmath and an independent differentiation/root scheme. At \(\alpha=0.2\), \(h=0.45\), the actual optimum displacement was approximately \(3.11472300957\times 10^{-9}\) against predicted \(3.11472352296\times10^{-9}\). At \(\alpha=0.35\), \(h=0.45\), the actual displacement was approximately \(-4.83396288989\times10^{-9}\) against predicted \(-4.83396372635\times10^{-9}\). Additional cases checked signs down to \(10^{-13}\).

**Limits of computation.** Finite-precision tests are not an infinite proof; near-zero phases produce tiny signed differences and need arbitrary precision. The formal error term in the thin-annulus formula is absolute, so near zeros of the cosine the leading term is not claimed as a relative approximation. No independent audit or validation has been performed.
