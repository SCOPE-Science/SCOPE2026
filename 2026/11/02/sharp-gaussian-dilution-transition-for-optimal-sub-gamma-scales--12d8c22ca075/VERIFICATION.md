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

Run `python check_gamma_gaussian.py` (Python 3 standard library). The script performs exact Fraction-based algebra comparisons and dense independent floating-point comparisons; the actual recorded output appears in `verification_output.txt`. Every decoded package artifact was hashed from its actual UTF-8 bytes. The proof of all real-parameter statements is in `RESULT.md`, not in the finite checks. In particular, the asymptotic global-localization argument and the derivative sign analysis must be assessed as mathematical arguments. No independent audit or external certification has occurred.
