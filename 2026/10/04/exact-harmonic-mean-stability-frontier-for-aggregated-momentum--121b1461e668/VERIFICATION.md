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
The proof derives the exact modal characteristic polynomial of equal-weight Aggregated Momentum on a positive quadratic.

`verify.py` checks the polynomial identity at \(z=-1\) exactly with rational arithmetic, tests the nonreal unit-circle exclusion identity, solves the characteristic polynomial with a standalone Durand–Kerner routine on both sides of the analytic boundary, and reproduces the default-vector constants.

The numerical root calculations are finite guards only. The necessary-and-sufficient stability theorem follows from the exact characteristic equation, continuity of roots, the unit-circle exclusion argument, and the sign condition at \(z=-1\).
