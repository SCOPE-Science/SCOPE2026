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

# Reproducibility and limits

Running `python verify_bouquet_pheat_lipschitz.py` with the Python standard library produces:

```
EXACT_WITNESS_SHARPNESS_OK 108
EXACT_GRID_DINI_UPPER_BOUND_OK 2536
NONLINEAR_PHASE_DIAGRAM_OK 384 strict_failure_cases= 378
BALANCED_TWO_BLADE_THRESHOLD_OK p*=3
ALL_CLIQUE_BOUQUET_PHEAT_CHECKS_OK
```

The checker assembles graph edges explicitly and computes the flow by summing oriented edge fluxes. Its first block uses exact rational arithmetic at integer exponents, including the half-height active-edge configurations. A second block exhausts a specified finite rational grid for small two-blade graphs. The remaining blocks compare the evaluated coefficient to explicit configurations, including the balanced critical case. No code run proves the asserted theorem for infinitely many clique sizes or every real exponent; the exact scalar minimization, orientation-by-orientation inequalities, and explicit attaining signal in the proof do that.

Independent audit has not been performed. The reproducibility check does not certify literature priority, infinite exhaustiveness or finite-positive-time instability bounds.
