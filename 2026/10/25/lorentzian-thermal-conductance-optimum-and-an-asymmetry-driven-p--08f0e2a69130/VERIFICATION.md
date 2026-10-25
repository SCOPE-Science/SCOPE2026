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

# Reproducibility of the exact heat-current formula

Run `python checker.py` with Python 3, SymPy, NumPy and SciPy installed. The program first assembles the six-dimensional Ornstein–Uhlenbeck drift and the 21 independent covariance equations, symbolically verifies the two determinant identities used by Cramer's rule, and checks the analytic derivative, Lorentzian simplification and endpoint-asymmetry identity. It then draws seeded admissible positive substrate constants, nonnegative middle constants, and unequal positive bath temperatures, solves the continuous Lyapunov equation independently, and compares currents obtained from each bath and each spring bond. A second seeded batch directly tests the constrained optimum against five representative alternatives. The last complete execution printed:

```
Symbolic exact determinant, current, derivative and detuning identities: PASS
Independent Lyapunov / energy-balance / optimization checks: 9100 PASS
```

All numerical comparisons use finite tolerance, and those results alone cannot prove parameter-uniform correctness. The universal conclusions rely on the symbolic covariance elimination and positivity/strict convexity of the denominator. This verification has not been independently audited.
