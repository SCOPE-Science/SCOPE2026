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

Run `python3 verify.py` with Python 3 and no external dependencies. The checker independently builds finite Alexander operation tables, enforces triple-associator pair relations, and in Latin cases constructs all three nucleus coefficient-equality graphs. Expected and observed output:

```
VERIFY_OK cyclic_parameters=58 latin_cyclic=33 modular_vector_cases=2
```

The cyclic tests cover all unit multipliers on groups of order at most 13, including non-Latin cases, and the noncyclic tests cover fixed-point-free maps on elementary 2-groups of ranks two and four. The conclusion about arbitrary coefficient rings in the Latin examples comes from integral permutation equalities, not division. Exhaustive checking of these finite examples is not a proof for arbitrary finite abelian groups; the general proof is given in `RESULT.md`. No independent external mathematical audit has been performed.
