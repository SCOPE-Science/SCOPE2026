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

The exact proof uses atom-cycle decomposition, a de Bruijn transfer matrix, disjoint-block independence, a terminating cutoff and a prime-valuation extremal argument. Execute `python3 code/verify.py` from this directory with Python 3 and no external packages. The standalone code performs independently implemented subset semantics and checks counts on finite cycles, noncyclic permutations, and even-power gap arithmetic.

Expected output:

```
VERIFY_OK equation_templates=10 independent_cycle_assignments=11588 full_transfer_matrix=YES
PERMUTATION_PRODUCT_OK models=918 size_at_most=5
ARITHMETIC_SHARP_GAP_OK even_iterates=2..80
```

Finite computations cannot establish the unbounded claims. In particular, the gap computation algorithm is proved to terminate but not benchmarked for arbitrary large term depth or arity. A separate external independent audit has not occurred.
