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

# Finite exact verification and mathematical scope

Run `python3 verify.py` from the same directory (standard library only). Verified output ends in:

`CERTIFICATE_OK tail_primes 6 head_classes 32 components 19 gaps 18 overlaps 13 zeta_N 20000`

All finite comparisons are exact rational inequalities, not floating-point tolerances. The program's 32 rows represent the complete finite partition into four exponent classes for prime two, and two classes for each prime three, five, and seven. The prime-tail test verifies six base primes, then the mathematical argument based on Nagura's theorem and the monotonicity of the Euler-product expression covers all later primes. Those infinite deductions are supplied in `RESULT.md`, not falsely presented as exhausted by code. The listed exact interval endpoints follow from nineteen connected-block merges; 18 comparisons are strict gaps. Independent audit: not performed.
