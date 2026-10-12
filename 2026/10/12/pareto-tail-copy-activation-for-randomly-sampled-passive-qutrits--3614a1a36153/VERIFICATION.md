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

The claim is proved analytically in RESULT.md. The standalone verifier checks exact population ordering for 384 small finite cases, evaluates two exact probability integrals numerically, and compares a large finite-copy scaled integral to the derived asymptotic constant.

Run `python verify.py` with `scipy` installed. Successful original replay:

`VERIFY_OK finite_tensor_cases=384 tail_at_3=0.3474185942900126 tail_at_5=0.20885085501991435 constant=0.5226368151659937 10000_scaled=0.5226106846009265`

The theorem for unbounded copy numbers follows from the explicit adjacent-shell inequality and dominated convergence, not finite enumeration. Independent audit and validation have not been performed.
