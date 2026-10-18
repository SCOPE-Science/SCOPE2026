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

# Verification and reproducibility

The all-separation theorem is proved in `RESULT.md`. The supporting `verify.py` uses only Python 3 standard-library modules (`math`, `random`) and can be run by invoking `python3 verify.py` from this directory.

The verification routine evaluates twelve distinct strict-overlap parameters, checks the analytic optimizer against an independent determinant calculation and the unsquared stationary equation, and checks positive second variation for the putative smooth candidate. It performs 60,000 seeded trials using boundary and interior points and compares their triangle areas with the asserted formula, and checks the previously published center-separation-equals-radius special case. The checked run returned `VERIFY_OK lens cases=12 numerical_diagnostics=60036 prior_special_case=matched`.

All finite trials are **diagnostic**. They neither exhaust the continuum of parameter values nor prove uniqueness or impossibility of other triangles. Those conclusions follow exclusively from the tangent/altitude and strict trigonometric inequalities in `RESULT.md`. The cited 2024 special case is acknowledged as prior coverage. Independent validation has not been performed.
