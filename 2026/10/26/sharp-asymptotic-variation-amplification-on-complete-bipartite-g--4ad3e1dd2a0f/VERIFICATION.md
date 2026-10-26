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

# Verification of sharp joint asymptotics

The analytical argument in `RESULT.md` proves the universal inequality and uses an explicit point-mass function to give the matching asymptotic lower estimate. All quantities use unoriented-edge total variation and uniform graph-ball averages.

The attached standard-library `check.py` independently calculates every candidate ball average with exact rational arithmetic. Its run completed 126102 exact-rational assertions and checked configurations, including exhaustive ternary functions on small graphs, many deterministic rational samples, the point-mass formula, exact gap identity, and explicit variation expansion on \(K_{4,4}\). Re-run with `python3 check.py`.

These numerical checks are not a substitute for the analytical proof, and this verification does not determine the exact optimal constants at fixed finite sizes. The comparison with published literature was limited by the unavailable full text of one relevant 2021 graph-variation paper. Independent audit has not been performed.
