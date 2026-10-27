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

# Verification record
The `verify_curvature.py` program is standalone Python, uses only Python standard-library rational arithmetic for the critical inequalities, and optionally mpmath to check sample gamma values. The actual replay passed:

`PASS: exact genus-three and all-genus-four-plus bounds; polynomial-series coefficients; optional gamma diagnostics`

Exact tests include the coefficient identity \(b_3=48\), the exact lower bound \(865827184/1977326743>5/12\), the exact upper bound \(1148/6075<2/5\), and positive series coefficients through degree 31. The mathematical proof independently shows the general coefficient sign and the bound for the infinite tail; testing finitely many coefficients does not establish it. Numeric sample curvature signs for genera \(3,4,5,6,8,16\) agree with the proof but cannot verify all genera. The complex beta integral is analytically reduced to Gaussian integrals and an Euler beta integral in RESULT.md; no quadrature-based certification is claimed. Source dates come from the primary arXiv submission history.

Independent audit has not been performed.
