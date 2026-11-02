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
# Computational verification and its limits

Run \(\texttt{python verify.py}\) with a standard Python 3 interpreter; no external packages are required. The code explicitly composes two polynomial substitutions modulo total degree \(N\), enumerating every coefficient of all involution-compatible \(2\times2\) linear parts for \(q=3,5\) at \(N=3\). The execution checks 510206 candidate substitutions and finds class-fiber counts \((1,729,27)\) per linear representative over \(\mathbb F_3\) and \((1,15625,125)\) per representative over \(\mathbb F_5\); multiplication by \(q(q+1)\) accounts for all mixed-sign matrices.

At \(N=4\), \(q=3\), the code independently enumerates 729 quadratic coefficient assignments for each representative, derives all eight cubic equations from direct composition, and uses modular Gaussian elimination to count their solution sets. The resulting three per-representative counts are \((1,729,2187)\). Further independent coefficient-sign counts verify the exponent formula for \(N=3,\ldots,11\).

These tests verify small cases and the code's arithmetic only. The general assertion for every odd prime power, truncation order and conjugacy class is proved symbolically in \(\texttt{RESULT.md}\), not by the finite census. Independent audit is not performed.
