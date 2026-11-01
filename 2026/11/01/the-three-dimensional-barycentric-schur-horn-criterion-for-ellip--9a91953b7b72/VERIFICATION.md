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

# Reproduction and scope

Run `python3 verify.py` from the extracted package. Python's standard library suffices; no downloads, remote code, special datasets, or optional dependencies are required. The expected completed output is `PASS: 607 exact and numerical checks; analytic proof required for all dimensions/domain.`

The program checks the exact rational quartic for the positive-definite triaxial example with coordinate-square weights \((1/6,4/6,1/6)\), checks the three principal-axis obstructions, constructs the equal-diagonal barycentric frame numerically, and confirms the rotationally symmetric cases. It also performs 150 deterministic positive-definite matrix tests of the intrinsic quartic identity and 450 checks of the harmonic decomposition. All assertions must succeed.

Finite checking is not a proof that the quartic characterizes every pair; the proof comes from the full analytic frame parametrization and complex phase equation in `RESULT.md`. No external validation has occurred. The full-dimensional surface-area reduction and its equality statement are cited from Kania's published work, not independently rediscovered or independently audited here.
