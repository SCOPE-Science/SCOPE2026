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

# Verification and scope

The analytic argument in `RESULT.md` proves the full stated parameter range. Its critical ingredients are: exact path resistances on trees, normalization of the resistance diameter to one, existence and uniqueness for the strictly convex reciprocal-cost problem, invariant unique minimizers under spoke permutations, the three competing diameter path families, and the KKT sign check at either active spoke cap.

Run `python check.py` with NumPy and SciPy installed. The tested script ran successfully from its actual file before packaging, producing:

```text
Exact rational branch/boundary cases: 5
Independent grounded-Laplacian resistance comparisons: 225
Asymmetric feasible allocation inequalities: 14625
Independent full-dimensional numerical minimizations: 54
Regime sample counts: {'triangle': 80, 'left_cap': 76, 'right_cap': 69}
All implemented checks passed; infinite-domain proof is analytic.
```

The random generator is seeded and the script fails upon a violated assertion. Exact-rational checks cover a handful of radical-square cases; they do not exhaust rational parameters. Numerical optimization and finite examples are not proofs for all parameters. The independent external audit channel is unperformed. The potentially relevant older tree-edge-reduction source could not be inspected in full.
