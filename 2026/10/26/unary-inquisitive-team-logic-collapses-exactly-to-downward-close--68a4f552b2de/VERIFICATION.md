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

Run \(\texttt{python3\ proof_checker.py}\) using Python 3 (standard library). It directly enumerates teams over finite equality structures, compares a direct inquisitive team evaluator to a separate unary-subset/constant-parameter recursion, checks invariance under all permutations, and verifies the explicit fixed-cardinality and complement-cardinality schemes through domain size five. The checker returns:

```
UNARY_COMPRESSION_AND_COLOR_INVARIANCE_OK 1 48
UNARY_COMPRESSION_AND_COLOR_INVARIANCE_OK 2 240
UNARY_COMPRESSION_AND_COLOR_INVARIANCE_OK 3 1008
UNARY_COMPRESSION_AND_COLOR_INVARIANCE_OK 4 4080
UNARY_TEAM_FORMULA_SCHEMES_OK
INQUISITIVE_UNARY_CHECK_OK 4080
```

The exhaustive finite tests do not prove an infinite-model statement. That statement is supported by the all-domain monadic MSO translation and the finite-rank game argument in RESULT.md. Independent audit is not performed.
