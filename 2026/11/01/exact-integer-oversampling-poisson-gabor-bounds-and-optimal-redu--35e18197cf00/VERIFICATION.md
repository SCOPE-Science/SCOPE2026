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

# Verification notes

The mathematical argument in `RESULT.md` is a complete analytic calculation for all integer \(q\ge2\) and real \(w>0\). Independently reproducible supplementary checks are provided by `checks/check_poisson_bounds.py` and can be invoked using the Python 3 standard library only:

```
python3 checks/check_poisson_bounds.py
```

The checker printed `POISSON_FRAME_CHECKS_OK 951` and reported optimal width `0.551291516054163` and condition number `5.62088237421534`. Its 951 deterministic assertions test sharp fiber values for 12 parameter combinations, 900 pseudorandom fiber inequalities, nine truncated series comparisons with the exact Zak transform, and the width optimizer at six neighboring points. Numerical sampling does **not** prove any universal inequality or rule out hidden roots; the sign of the derivative, finite hyperbolic sum, and quartic uniqueness are proved symbolically in `RESULT.md`.

The normalization can also be checked without approximation on an indicator window: the Zak symbol for integer oversampling equals the oversampling factor, confirming the multiplicity in the scalar diagonalization. The Poisson formulas use a raw window \(g_w(t)=1/(t^2+w^2)\), not a unit-norm version. The spectral extrema are Zak-torus symbol extrema and need not be achieved by a nonzero \(L^2\) eigenvector.

Scientific limitations: only integer-oversampled rectangular lattices and this real even Poisson profile are covered. Historical literature may contain equivalent statements not identified in the inspected sources. Independent validation has not been performed.
