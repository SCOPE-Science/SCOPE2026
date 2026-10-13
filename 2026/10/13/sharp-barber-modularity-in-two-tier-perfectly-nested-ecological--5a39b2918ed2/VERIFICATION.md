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

`python verify.py` uses only the Python standard library and performs exact arithmetic with `fractions.Fraction`.

For each of 156 positive-integer profiles with specialist count and generalist count at most four, total primary count at most six, core count at most three, and peripheral count at most four, it enumerates every partition of the primary species and optimizes every partner's placement. It compares the resulting global optimum with the proposed rational formula, sharp bound and equality criterion. On seven additional small profiles it independently enumerates every partition of *all* vertices (2,279 partitions in total) to confirm the formula and the unique optimal partition. Twenty-three additional family values check the sharp finite-count expression.

Expected terminal output:

`VERIFY_OK parametric_profiles=156 full_vertex_partitions=2279`

The correctness of the result for arbitrary parameters follows from the four-block sign table, the attainability argument and the elementary product inequality proved in RESULT.md. Finite tests alone are not infinite proof. No claim about arbitrary Ferrers graphs, modularity significance, real ecological outcomes or independent audit is made.
