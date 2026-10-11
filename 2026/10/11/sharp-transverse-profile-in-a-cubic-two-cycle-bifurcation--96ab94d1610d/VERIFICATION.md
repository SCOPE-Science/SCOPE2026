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
# Reproducibility and verification

Run `python3 check_branch.py` from the directory containing this file and `check_branch.py`. Only the Python standard library is required. The script integrates the exact scalar angular equation and variational equations and prints `CHECK_OK` when its prescribed finite-precision consistency tests succeed. Checked approximations are \(C=26.8029305380\) and \(32\pi/C=3.7507452692\); the rounding is not part of the analytic claim.

The analytic proof independently establishes the exact polar identities, the denominator's strict sign, \(\partial_a\log P_a'(0)|_{a=-1/4}=-32\pi\), the positive second return coefficient, and the application of the implicit-function theorem. A finite numerical integration cannot establish uniqueness or the asymptotic remainder bound. No external certification or independent audit has been carried out.
