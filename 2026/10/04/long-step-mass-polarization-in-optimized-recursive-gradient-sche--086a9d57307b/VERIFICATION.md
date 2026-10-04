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

The proof uses three exact inputs: the \(s\)-join formula, the sum-product identity for \(s\)-composable schedules, and the exact phase law for the optimized OBS-S scalar. From these, positivity, the persistent sub-\(2\) step, both mass-ratio bounds, and the maximum-step lower bound are elementary consequences.

`artifacts/verify_mass_polarization.py` constructs balanced recursive schedules for representative horizons using the published join formula, checks the sum-product identity, and verifies the finite-horizon inequalities.

The computation is not an exhaustive proof over all horizons. The all-horizon and asymptotic statements follow from the algebraic identities in the proof.
