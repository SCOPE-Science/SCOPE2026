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

# Reproducibility

Run `python verify.py` from the extracted package directory. It uses only the Python standard library. It reconstructs Zorn multiplication and verifies its commutator ranks by modular elimination for all trace-zero octonions over prime fields of orders three and five. The output records the three rank strata and commuting-pair totals. It also counts pairwise commuting tuples in a three-dimensional Heisenberg algebra directly for specified small sizes and confirms the all-arity polynomial identity at five test values of q and arities zero through five. A successful run ends with `VERIFY_OK`.

The geometric component statement and universal finite-field enumerator rely on the given symbolic algebraic proof, not on exhaustive sampling. Finite extension fields and characteristic two are not exhaustively tested or claimed. The algebraic scheme's nonreduced structure was not assessed.
