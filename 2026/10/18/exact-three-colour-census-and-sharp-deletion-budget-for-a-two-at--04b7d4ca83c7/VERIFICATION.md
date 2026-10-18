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

# Reproduction

Execute `python3 verify.py` in this package's directory. It requires only the Python standard library. The checker was executed with all assertions enabled and printed:

```
NINE_TEMPLATE_INCLUSION_EXCLUSION_OK 511
SEMANTIC_SPLITTING_OK n=0 colorings=1 satisfied=1 max_deletions=0
SEMANTIC_SPLITTING_OK n=1 colorings=9 satisfied=9 max_deletions=0
SEMANTIC_SPLITTING_OK n=2 colorings=81 satisfied=81 max_deletions=0
SEMANTIC_SPLITTING_OK n=3 colorings=729 satisfied=717 max_deletions=1
SEMANTIC_SPLITTING_OK n=4 colorings=6561 satisfied=6057 max_deletions=1
EXTENDED_COUNT_AND_SHARPNESS_OK n=5 n_up_to=19
THREE_COLOR_DEPENDENCE_QUANTITATIVE_THEOREM_OK
```

`semantic_satisfies` enumerates actual partitions of all assignments and validates each dependence atom directly, independently of the row--column normal form. `semantic_distance` enumerates deletion subsets and the split semantics for every colouring through three columns and every nonsatisfying colouring at four columns. Every colouring with up to four columns is checked against the normal form; the 59,049 five-column colourings provide a further numerical census. `verify_inclusion_exclusion` exhausts all 511 nonempty subfamilies of the nine templates. Since this latter finite calculation establishes the coefficients of a formal all-\(n\) identity, the exact sequence proof is not a finite-team extrapolation. The lower-bound construction is proved separately for every \(n\).

# Boundaries

The program does not provide independent verification or external certification of the general proof. Its computational scope is finite and its nine-template exhaustion only certifies the finite algebraic identity stated in the proof. No claim is made about larger consequent alphabets or arbitrary support graphs.
