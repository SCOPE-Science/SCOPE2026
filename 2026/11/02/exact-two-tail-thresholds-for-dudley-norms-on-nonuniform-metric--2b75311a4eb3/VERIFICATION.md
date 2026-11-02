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

# Reproducibility and scope

Run `python verify_star.py` in an environment with Python 3, NumPy and SciPy. The code uses exact `fractions.Fraction` calculations for the proposed tail formula and direct maximizing-function construction; it independently formulates the original bounded-Lipschitz finite-dimensional optimization using `scipy.optimize.linprog(method="highs")`.

The executed checks produced:

```
OK: 916 independent LP comparisons
example radii: ['1', '2', '4', '7'] charges: ['2', '-3', '1', '-1'] norm: 22/5 decimal 4.4
OK: 1370 exact rational optimizing witnesses
```

The witness routine checks the full Lipschitz constraints, sup-norm plus Lipschitz budget, and exact objective equality using rational arithmetic. Random fixed-seed examples cover zero coefficients, repeated arm lengths, unequal radii, and one- or two-sided signs. Numerical LP comparisons use a tolerance of at most \(10^{-8}\) due to floating-point optimization. These tests do not establish the theorem for all inputs; that guarantee comes from the analytical two-cap reduction and piecewise-linear root argument in RESULT.md.

The literature comparison has residual historical-priority risk, and no independent audit has been performed.
