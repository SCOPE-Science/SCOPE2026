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

Run `python verify.py` from this package with Python 3 and `mpmath` installed. The program produces `PASS: 125 independent finite/analytic formula checks` on execution and tests the canonical integral expressions against independent finite mixtures, confirms the finite exact formula, and checks selected numerical single-crossing inequalities. The universal and all-parameter results are proved in `RESULT.md`; no finite computation is treated as an infinite proof. Independent audit has not been performed.
