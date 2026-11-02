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

# Computational verification

Run `python verify_one_leaf_resonance.py` with packages in `requirements.txt` (NumPy). The program constructs the exact graph shortest-path metric, verifies the decomposition identity with rational inputs at integer powers \(p=1,2\), forms the full zero-sum powered-distance matrix and checks its inertia at and away from the candidate resonance, and evaluates both analytic asymptotic scales numerically.

Observed outputs:

```
EXACT_RATIONAL_ZERO_SUM_DECOMPOSITION_OK 1296
RESONANCE_AND_STRICT_DROP_FULL_MATRIX_OK 364
NEAR_BALANCED_LINEAR_RESONANCE_SCALE_OK
FIXED_SMALL_PART_SINGULAR_RESONANCE_SCALE_OK
ALL_ONE_LEAF_BICLIQUE_RESONANCE_CHECKS_OK
```

The tests have finite ranges and use floating point for noninteger powers; they do not prove the universal theorem or establish literature originality. All-parameter claims require the exact decomposition, scalar sign analysis, perturbation inequalities and asymptotic expansions in `RESULT.md`. Independent audit has not been performed.
