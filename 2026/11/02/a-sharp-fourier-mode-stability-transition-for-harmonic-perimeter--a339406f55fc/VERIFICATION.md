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

# Reproduction and limits

From the directory containing `RESULT.md` and `verify.py`, run:

```
python verify.py
```

Expected terminal marker on successful execution: `HARMONIC_PERIMETER_CHECK_OK 762`. The checker uses only Python's standard library. It compares exact rational Fourier multiplier values and the claimed mode ordering at six rational radii for frequencies three through sixty-four; it also computes twelve direct finite-Fourier-quadrature perimeter deficits for genuine perturbed circle boundary data, using the Poisson multiplier at the selected radii. The direct quadrature is independent of the second-variation formula.

The proof in `RESULT.md`, not these finite checks, establishes the infinite-frequency inequalities, strict-convexity scope, all radii in the open unit interval, and the sharp spectral transition. The remainder is at fixed smooth perturbation and fixed radius. An independent mathematical audit has not been performed.
