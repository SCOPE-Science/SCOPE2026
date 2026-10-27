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

The analytic proof establishes the bound for all n>=3 and all VT syndromes. Reproduce finite checks with `python3 verify.py` using Python 3 standard library only. The program verifies every received binary word of lengths n-2 for 3<=n<=13 and every explicit witness pair (n,a) for 3<=n<=80. Output `VERIFY_OK` is recorded in `verify_output.txt`. These checks are finite, not an independent certification or proof beyond verified ranges. The source literature was compared on quantified statements, not just titles. No independent audit has been performed.
