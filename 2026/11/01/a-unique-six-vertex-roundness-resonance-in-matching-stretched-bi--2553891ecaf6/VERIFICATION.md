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

# Verification performed

The companion script `verify_matching_stretch.py` independently calculates all-pairs weighted shortest paths for rational edge lengths, rather than assuming the proposed three-distance formula. It then tests exact zero-sum quadratic identities using fractions and computes the centered Gram rank for the two exact simultaneous singularities (six-point regular hexagon: powered distances \(1,3,4\); eight-point cube: \(1,2,3\)). It diagnoses the finite spectral phase diagram by numerical root finding and checks the uniform asymptotic Taylor approximation with high-precision arithmetic.

Run with `python3 verify_matching_stretch.py` (requires NumPy, SciPy and mpmath). Successful local replay returned:

```
EXACT_SHORTEST_PATH_METRIC_OK 528
EXACT_ZERO_SUM_DECOMPOSITION_OK 864
EXACT_POWERED_RESONANCE_RANK_OK 3 rank 2
EXACT_POWERED_RESONANCE_RANK_OK 4 rank 3
POWERED_DISTANCE_CRITICAL_PHASES_AND_RANKS_OK 153
HIGH_PRECISION_ASYMPTOTIC_DIAGNOSTICS_OK 16
ALL_MATCHING_STRETCH_CHECKS_OK
```

The general inequalities, root uniqueness, interval exclusion, rank changes and asymptotic expansion are proved analytically in `RESULT.md`. Finite checks cannot prove them for arbitrary parameter values, and independent mathematical audit remains unperformed.
