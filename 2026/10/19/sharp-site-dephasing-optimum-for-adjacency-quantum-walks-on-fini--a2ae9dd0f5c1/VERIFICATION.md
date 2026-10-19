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

The check code `verify_star_lindblad.py` was executed from the accompanying files and completed with `PASS`. It used exact symbolic characteristic-polynomial comparisons for three small star sizes, and direct numerical diagonalization of the full complex Liouvillian for additional sizes and noise values. It compared 5,880 eigenvalues with their independently constructed factor roots and evaluated all predicted optimizing gaps. The maximum eigenvalue matching discrepancy was approximately \(1.315\times10^{-13}\), and the largest optimum-gap discrepancy was approximately \(3.095\times10^{-8}\) (including the nonnormal exceptional-point case).

The argument valid for every degree is in `RESULT.md`: a complete symmetry-sector decomposition, the exact standard-cubic sign identity, and shifted Routh–Hurwitz bounds on competing sectors. The code alone is not claimed to prove arbitrary-degree assertions. No experimental measurements, finite-time mixing theorem, or independently conducted review is claimed.
