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

# Mathematical verification

The independently executable Python 3 checker `check_rank1_unary.py` uses only the standard library. Run `python3 check_rank1_unary.py`. Its observed terminal lines are:

```
UPPER_TEAM_SEMANTICS_OK 150
SUPPORT_FIBER_SYNTHESIS_OK 24
QUANTIFIER_FREE_CAPACITY_OK 305 1830
RANK_ONE_SUPPORT_THINNING_OK 2400
RANK_ONE_MONADIC_CHECK_OK
```

The first test directly evaluates splitting a full one-variable team into a colour-exclusion disjunct plus repeated constancy disjuncts. The second compares finite forbidden-basis synthesis with its intended multiplicity constraints. The third checks the exact capacity rules for a family of syntactic formulas. The fourth checks preservation of universal and existential rank-one semantics under support-preserving restriction. No external packages are needed.

The proof in `RESULT.md` is general: it uses the downward-closure principle, singleton reduction for rank-one existential matrices, Dickson's finite-basis lemma, and a structural capacity induction for pure equality. Executed finite tests do not prove completeness for arbitrary multiplicities, signatures, or formula sizes, nor do they validate any historical priority claim.
