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
# Reproducibility and checks

`python3 checker.py` uses the standard library and constructs degree-two, degree-three, and degree-seven Moore graphs. It verifies every ordered pair's common-neighbor count, every edge's signed norm support geometry, rational exact forms of the positive heat transport, all three signed potential branches with rational multipliers, and the exact Hoffman–Singleton peak. Output on the research artifact:

```
CHECK_OK exact_combinatorial_and_transport_checks= 3037 Hoffman_Singleton_peak=49/45 Petersen_profile=(5exp(-2t)-2exp(-5t))/3
SIGNED_OK exact_rational_potential_checks= 7020 degrees=2,3,7 phases=3
```

`python3 lp_check.py` (optional NumPy/SciPy) independently solves full vertex-Lipschitz linear programs rather than the derived reduced optimization. It checks 316 edge/filter cases, including 84 positive heat-time cases:

```
LP_CROSSCHECK_OK signed_and_heat_edge_cases= 316 heat_subset= 84
```

These finite experiments corroborate but do not establish the theorem for all graph orders or real coefficients. The general proof is the exact edge-neighbor distance argument, complete Lipschitz feasible-polytope reduction, signed piecewise-linear maximization, and interpolation in the mean-zero adjacency algebra. Historical originality has not been independently certified.
