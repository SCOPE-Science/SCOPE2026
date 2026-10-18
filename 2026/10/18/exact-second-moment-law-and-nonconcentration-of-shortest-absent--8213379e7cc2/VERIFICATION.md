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

# Reproduction checks
Run `python3 check_moments.py` using only the Python standard library. The program computes shortest absent target sets directly for every binary source word through length 14 and compares first and second moments with coefficients of both bivariate rational functions. It independently constructs the one-target and two-target arch-transition expansions through total degree 12 and checks the stated length-10 weight-5 variance and the positive root enclosures. The program prints three `PASS` lines on success.

The unrestricted claim depends on the exact arch-factorization bijection, the complete two-target transfer, rational matrix inversion, and dominant-pole argument in `RESULT.md`, not finite testing. Independent mathematical audit and independent validation have not been performed.
