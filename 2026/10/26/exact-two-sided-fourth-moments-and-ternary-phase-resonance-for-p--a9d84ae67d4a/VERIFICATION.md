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
# Verification

The analytical proof determines, for all positive integers \(n\), the exact Haar moments \(\int|\chi_n|^2=1\), \(\int|\chi_n|^4=n+1\), and \(\int\chi_n^3\overline\chi_n=\int\chi_n^4=\mathbf 1_{3\mid n}\). These follow from Schur orthogonality, the two-factor Pieri decomposition, center symmetry and uniquely forced three-/four-factor horizontal-strip chains. They imply the complete fourth-moment identity and all sharp equality cases by finite-dimensional optimization.

Run `python CHECKER.py` with Python 3 (standard library only) to compute the Weyl-torus constant terms without floating-point arithmetic for every \(1\le n\le10\). It checks all four character moments against the exact formulas. The code does not attempt an infinite exhaustive computation; the all-degree argument is mathematical. External independent validation is not performed.
