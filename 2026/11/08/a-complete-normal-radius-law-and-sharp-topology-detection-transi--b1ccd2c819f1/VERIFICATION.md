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

# Computation and proof checks

- The included `verify.py` directly enumerates deck displacements for nonzero exponents from -12 through 12; the proof establishes that the minimizing exponents are exactly ±1 or ±2 in the Möbius case and ±1 for the cylinder, so this finite enumeration is used only as a regression check.
- It compares both survival CDF branches with a deterministic 10,000-point midpoint quadrature for 72 cylinder/Möbius parameter configurations and representative radii.
- It independently checks the three analytic maximizer regimes against 30,001 center ordinates.
- The exact analytic proof is in `RESULT.md`. Finite checks do not certify an infinite theorem.
- No independent external mathematical audit has been conducted.
