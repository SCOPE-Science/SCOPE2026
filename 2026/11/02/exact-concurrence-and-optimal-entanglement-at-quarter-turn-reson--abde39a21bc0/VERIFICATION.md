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

The exact analytical checks and independent floating-point comparisons are implemented by `verify.py`, which should be executed from the same directory with SymPy, NumPy and SciPy installed:

```sh
python verify.py
```

The executable verifies the source generator's spectral projectors, the exact \(4\)-cycle of the gate and its reset-state orbit at both nontrivial quarter turns, the separable half-turn, the stationary normalization, both spin-flip spectral coefficients, the characteristic polynomial, the positive square-root simplification, and the unique global concurrence maximum. It independently evaluates ten reset probabilities using a numerical matrix exponential and direct mixed-state Wootters eigenvalues, with geometric-series truncation at residual weighting below \(2\times10^{-14}\).

The finite numerical comparisons are diagnostic only; the complete continuum claim follows from the exact rational formulas and sign of a quadratic derivative. The formulas classify only the three specified quarter-turn gate angles, not arbitrary detunings. No independent scientific audit has been performed.
