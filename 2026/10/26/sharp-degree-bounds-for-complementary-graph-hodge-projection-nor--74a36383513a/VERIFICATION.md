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

# Reproducible checks
The attached standalone `verify_degree_projection.py` constructs reduced graph Laplacians, inverts them using Python's exact `fractions.Fraction`, forms full cut and cycle projectors, and checks their algebraic properties and the stated local/global inequalities.

Executed command: `python3 verify_degree_projection.py`.

Observed output:
```
PASS exact rational graphs= 74 columns= 635
PASS K4 equality and K5 sharp reversal, local twin resistance equality
```

Configurations include complete graphs, cycles, paths, stars, books, generalized Petersen graphs, and deterministic pseudorandom connected graphs. Exact integer/rational computations do not establish general graph assertions: the proof for every graph is the separate Dirichlet variational argument plus the complementary-column identity in `RESULT.md`. The checker makes no claims about independent audit, completeness of a literature search, or optimized nonorthogonal projections.
