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

## Reproducibility

Run `python checker.py` with Python 3 and SymPy installed. The checker computes the grounded-Laplacian inverse on nine independently constructed finite graphs and verifies every cut and cycle projection column against the theorem's formulas, together with idempotence and the symbolic sign comparison identities. Its successful output is:

```
SYMBOLIC_IDENTITIES_OK
CLIQUE_STAR_CERTIFICATE_OK configurations=9 exact_columns=406
```

The nine tested parameter pairs are `(2,3)`, `(2,4)`, `(3,3)`, `(3,4)`, `(4,3)`, `(4,4)`, `(5,3)`, `(6,3)`, and `(6,5)`. The all-parameter result is established by explicit Green-matrix and sign identities in `RESULT.md`. Numerical or rational finite samples do not establish the infinite-family result by themselves. Neither independent peer review nor an independent mathematical audit has been performed.
