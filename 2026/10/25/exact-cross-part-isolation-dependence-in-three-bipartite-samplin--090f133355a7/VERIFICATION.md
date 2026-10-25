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

Run `python verify.py` using only a standard Python installation. Successful execution prints exact general-parameter case counts, independent enumerated binary-matrix tests, and sparse-limit approximations. Checks include the full support, vanishing marginal cases, the strict-sign boundary, the ratio-product identity where defined, and the factorial-moment identity obtained by independent enumeration.

At construction, the checker passed 58,896 exact probability/sign/product cases and 1,318 enumerated moment comparisons over 74,384 binary matrices. The numerical sparse sequence at \(c=2\) approached \(-2e^{-4}\). The all-size identity and limiting value rest on explicit analytic arguments in `RESULT.md`; finite enumeration and floating-point consistency cannot prove those general statements. No independent external audit has been carried out.
