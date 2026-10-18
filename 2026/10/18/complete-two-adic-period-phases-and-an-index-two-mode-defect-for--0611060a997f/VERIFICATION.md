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

The package contains a standalone pure-Python script `verify.py`; run it with `python verify.py` in the directory containing this document. During preparation this program returned `VERIFY_OK; exact assertions: 16962`. It executes exhaustive residue checks modulo eight for the polynomial seed identities, exact modular power tests, proper-divisor exclusion, and independent scalar-mode comparisons. Exact integer congruences establish the universal seed cases, and the analytical valuation-lifting lemma then handles every modulus depth. The finite parameter regressions are not presented as an exhaustive proof over all integers. The main proof and all quantifiers are in RESULT.md. No external formal proof assistant and no independent audit were used.
