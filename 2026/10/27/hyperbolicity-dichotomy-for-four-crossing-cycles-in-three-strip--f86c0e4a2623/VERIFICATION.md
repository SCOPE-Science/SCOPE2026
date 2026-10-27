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

The standalone `checker.py` uses exact rational arithmetic for 588 algebraic crossing-geometry test fixtures spanning both signs of the central horizontal-velocity coefficient, multiple velocity offsets and both stability regimes. Its assertions cover two independent center-energy matching equations, the return multiplier, the strict normal-velocity crossing inequalities, the identity linking multiplier sign with the signed central mismatch, and the neutral case. It additionally evaluates the published example's multiplier numerically and confirms that time reversal produces the reciprocal.

The fixtures are algebraic checks, not a census of globally realized periodic trajectories; the theorem for actual transverse periodic trajectories is proved analytically in `RESULT.md`. The period-annulus assertion uses smooth local flight maps, conservation of energy and the implicit-function theorem; no numerical enumeration can replace that step. No independent mathematical audit has been performed.
