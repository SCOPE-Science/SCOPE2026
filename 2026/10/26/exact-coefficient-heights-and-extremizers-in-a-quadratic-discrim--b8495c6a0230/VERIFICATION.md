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

# Reproducibility and limits

Run `python3 verify.py` with Python 3.9 or later. It enumerates every positive-leading integer quadratic of coefficient height at most the proposed optimum for each squarefree parameter from 1 through 80, checks the complete predicted minimizer set (including symmetric exceptions), and enumerates several integer generators to cross-check the monic norm minimum. The expected final line is:

`CERTIFICATE_OK squarefree_parameter_checks= 75 symmetric_exceptional_cases= 5`

The exhaustive finite enumeration uses only the standard library, but does not prove the universal claims. The general proof requires the quadratic discriminant-index identity, the integral basis and norm formula, and the established theorem on squarefree values of quadratic polynomials. No claim about independent or external validation is made.
