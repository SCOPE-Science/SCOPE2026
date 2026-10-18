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

Execute `python3 verify_unary.py` with Python 3 (no additional packages). Its independent concrete-team evaluator and monadic-set-translation evaluator use the source clauses separately and exhaustively compare each generated instance. The reproducible seed is fixed; 13,440 comparisons across domains of sizes 1, 2, and 3 completed successfully. Further test cases verify the nonempty-team translation of \(\exists y\,\neg R(y)\) via \(\exists^1y\,\neg(x=y)\), with special handling of the empty team.

The proof is not inferred from exhaustive finite sampling. The induction translating arbitrary formulas and the monadic quantifier-game proof establish the unrestricted finite/infinite result. Classical Lyndon preservation is used for the all-structures converse; it is not asserted in isolation over finite structures. The source's published two-free-variable counterexample supplies sharpness. No independent audit has been performed.
