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

Run `python verification/check.py` using a standard Python 3 installation from the extracted record root.

The exact certificate represents coefficients in \(\mathbb Q(\sqrt2)\) and composes fifth-order Taylor polynomials, proving the coefficients through order five and checking the exact identities for \(K\), \(\alpha\) and \(A^4\). It independently computes three pairs of positive two-cycle points for \(\delta=10^{-7},10^{-9},10^{-11}\) using 70-digit decimal arithmetic, confirming the approaching quarter-power amplitude from either side.

The executable records `EXACT_TAYLOR_OK`, three `BRANCH_OK` checks and `ALL_CHECKS_PASS`. Its finite precision branch tests do not prove uniqueness or full asymptotic limits: those follow from the analytic four-root theorem, signed contraction and reciprocal fourth-power increment argument in `RESULT.md`. No independent audit was performed.
