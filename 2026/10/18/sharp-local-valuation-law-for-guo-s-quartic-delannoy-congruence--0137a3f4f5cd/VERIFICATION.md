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

# Verification protocol

Run `python3 verification.py` (only Python 3 standard library). The script checks degree-bounded finite-difference identities for the cubic coefficient polynomial and its lower-degree companions, verifies exceptional truncations for small odd primes, and performs exact modular comparisons at varied prime-adic depths. The finite-difference checks certify the displayed rational-polynomial summation identities because both sides have degree at most eight and ten exact values are compared; the proof in `RESULT.md` supplies the polynomial coefficientwise reflection and valuation arguments. Direct numerical checks are not treated as infinite proof. The remaining limitation is independent mathematical/priority review, not a missing computational certificate.
