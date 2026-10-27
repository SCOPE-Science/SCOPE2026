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

The formula can be checked independently using `python3 verify.py`. This script enumerates the palindromic factors directly from every contiguous substring; it does not call the closed defect formula to generate palindromic factors.

Observed output:

`PASS: 16 Boolean levels; 6561 three-marker words; 1015 zero-to-two-marker words; exact maxima at lengths 3..22.`

Every one of the sixteen Boolean support patterns is also checked against the identity used in the infinite proof. The substantive mathematical proof is a complete four-case palindrome taxonomy, a layer-by-layer Boolean identity and a sharp integer-balancing argument; the finite tests cannot by themselves establish the theorem for unbounded gap lengths. No independent audit or external certification is asserted.
