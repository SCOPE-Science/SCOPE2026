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

Execute `python3 verify_arch.py`. The program requires no nonstandard dependencies. It checks exact morphism relations by direct finite-word substitution, compares five successive substitution iterates, tests every Tribonacci prefix of length up to 10,000, and independently tests each distinct short factor using explicit ternary-subsequence enumeration through factor length 14. It also verifies the letter-count factor bounds through length 150 and dyadic-style iterates through substitution level 18. Expected output starts with `TRIBONACCI_ARCH_RETURN_MORPHISM_PASS`.

All three free-word identities are precise finite checks. The general substitution conjugacy is proved by induction in RESULT.md. The all-factor inequality follows by a symbolic argument about consecutive rare-letter positions, and the numerical density bound uses a published factor-frequency discrepancy theorem. No finite enumeration is treated as a proof of an infinite assertion. Independent external audit was not performed.
