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

The complete proof is in `RESULT.md`. `checker.py` is a standalone Python 3 script using only the standard library. Run:

```
python checker.py
```

A successful run reported:

```
TETRAHEDRAL_VORONOI_MARGIN_OK deterministic=48 cdf_checks=89 sample=180000
integral=1 mean=0.529939502485 second_moment=0.398818759625 max_angle_error=0
empirical_mean=0.530696354461 empirical_second=0.399982340878 max_CDF_discrepancy=0.001059
```

It tests all 48 signed coordinate permutations of one generic triple, numerical density normalization, analytic CDF at 89 interior thresholds, two exact moments, uniform-sphere Monte Carlo at six thresholds, and distances to the three competing great-circle decision planes. Simulation is seeded for reproducibility. The finite tests cannot prove the continuous-distribution identities; the exact geometry and integrations supply the proof. No independent audit or formal mechanized certificate is asserted.
