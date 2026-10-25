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

The result is proved analytically in `RESULT.md`; numerical checks in `verify.py` complement, and do not establish, the continuum assertions. Run `python3 verify.py` in the directory containing this file and the script. A successful run prints `PASS 48 numerical comparisons and transition checks` and the three thresholds. All local assertions exclude the two zero-Hessian boundary values. No claim about all global minimizers is verified or made.
