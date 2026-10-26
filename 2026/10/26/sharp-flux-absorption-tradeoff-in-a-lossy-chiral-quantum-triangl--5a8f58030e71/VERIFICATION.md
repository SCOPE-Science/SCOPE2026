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

## Reproducible checks

The standalone `check.py` requires Python 3, NumPy, SciPy and SymPy. Run `python check.py` in a directory containing this file. It calculates the \(3\times3\) Lyapunov residual as symbolic polynomials, reduces each by the trigonometric relation \(c^2+s^2=1\), checks Hermiticity and the specified matrix element, then independently solves 81 complex Lyapunov systems and checks optimization formulas and sample inequalities.

Execution of the packaged code yielded `PASS: 11 symbolic matrix/identity checks; 139 independent numerical/optimization checks`. The symbolic calculation verifies the matrix algebra, not the spectral-stability theorem or global extremality; those require the separate analytic arguments in `RESULT.md`. The numerical checks are finite consistency tests, not proof of an infinite statement.

## Mathematical limits

The theorem requires a strictly positive single absorber and an equal-hopping three-site cycle, initialized next to the trap. Vanishing flux sine generates a dark state and infinite mean absorption time. The quoted optimum is the global minimum of the infinite-horizon mean time for this continuous-loss model only. No independent audit has been conducted.
