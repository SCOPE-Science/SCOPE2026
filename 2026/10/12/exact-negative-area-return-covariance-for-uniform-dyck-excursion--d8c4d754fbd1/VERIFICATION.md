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

Execute `python3 verify.py` in a directory containing the embedded standalone checker.

The checker independently enumerates all 82,499 Catalan excursions of semilength at most eleven. It compares exact rational raw moments \(\mathbb E[A_n]\), \(\mathbb E[R_n]\), \(\mathbb E[A_nR_n]\), \(\mathbb E[A_n^2]\) and \(\mathbb E[R_n^2]\) against the formulas in the proof. It separately checks exact coefficient-extraction identities through semilength 150 and evaluates the exact covariance and strict-sign inequality over the same finite range.

Analytic coverage beyond these finite tests follows from the formal power-series identities, the all-size Catalan ratio proof, and Stirling's asymptotic expansion in `RESULT.md`. Finite enumeration is neither an infinite proof nor an originality certificate. No external audit or independent validation has been performed.
