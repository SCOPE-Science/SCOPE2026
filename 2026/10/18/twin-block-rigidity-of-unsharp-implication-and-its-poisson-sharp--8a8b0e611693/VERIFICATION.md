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

# Reproducibility and verification

Execute `python verify.py` using Python 3 without additional packages. The script uses explicit finite order relations and searches for the greatest pseudocomplements in each interval, rather than implementing the theorem's local complement formulas. It then independently computes every set-valued implication table entry. It checks 441 labelled incidence structures with nonempty blocks (256 satisfying the sectional condition), exhaustively lists all graphs with edge multiplicities zero through two on at most four vertices, and evaluates all admissible examples with five vertices. Exact rational formal-series coefficients are checked against the independently counted graphs for five orders, and the sharpness probability is computed through 35 vertices.

Observed successful run:

```
VERIFY_OK incidence_tested 441 incidence_good 256 incidence_ambiguous_pairs 80 graphs_all_n_le_4 760 admissible_implications_tested 419 ambiguous_inputs 264
EXACT_SHARPNESS_COUNTS {1: (1, 1), 2: (2, 3), 3: (8, 11), 4: (41, 56), 5: (253, 348), 6: (1858, 2578), 7: (15796, 22054), 8: (152219, 213798)}
COUNT_DISTRIBUTIONS {1: {0: 1}, 2: {0: 2, 1: 1}, 3: {0: 8, 1: 3}, 4: {0: 41, 1: 12, 2: 3}, 5: {0: 253, 1: 80, 2: 15}}
SHARP_RATIO_N35 0.6674220289336128 POISSON_LIMIT 0.6065306597126334
```

The brute-force incidence census is finite, and an empirical convergence check is not an infinite proof. The unrestricted sectional classification, implication rigidity, component enumeration, and Poisson convergence all have mathematical proofs in `RESULT.md`. Independent mathematical validation and independent originality review have not been carried out.
