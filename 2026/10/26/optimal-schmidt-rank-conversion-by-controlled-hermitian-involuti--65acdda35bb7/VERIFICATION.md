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

The constructive proof gives the all-dimensional result. Its central checks are: (i) rank-product inequality for an operator written as a sum of simple tensor operators; (ii) its use in both directions for an involution; (iii) disjoint-support orthogonality of grouped vectors in the rank-decreasing construction; (iv) existence of a first-factor orthonormal frame with prescribed normalized group sums in the rank-increasing construction, obtained by extending an isometry; and (v) disjoint transpositions and mutually orthogonal control projections to ensure the resulting operator is both self-adjoint and square-one.

`check_involutions.py` is an executable finite consistency checker (Python 3 with NumPy). Running it produces:

```
PASS 254 dimensions/ranks; reflection, Schmidt rank, and exact OSR each.
```

The test covers square factor dimensions 1 through 8 and four rectangular pairs, checking all source and target Schmidt ranks in those dimensions. Numerical rank uses a fixed singular-value tolerance; its passing results are neither an exact-algebraic certificate nor a proof for all dimensions. The proof above remains required for the general claim. Source comparisons establish no exhaustive historical-priority guarantee.
