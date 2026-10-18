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

The probability and algebraic statements are proved directly in `RESULT.md` from Dirichlet spacings and one-variable monotonicity. The executable `circle_coverage_verification.py` independently evaluates exact rational one-dimensional integrals for two gaps, exact rational derivative identities, deterministic uniform-simplex grid averages, and numerical root asymptotics. It uses only the Python standard library.

The deterministic simplex grids are approximations and do not certify all real arc lengths or all sample sizes. The finite root scans do not certify uniqueness; that conclusion comes from the proof using the single turning point of the auxiliary ratio. No independent audit has been performed. The incomplete availability of relevant older literature remains an originality risk.
