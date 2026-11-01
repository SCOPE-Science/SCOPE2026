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
# Reproducible verification

Run `python3 verify_two_site_sunlet.py` in this directory after installing `requirements.txt`. The script constructs the weighted shortest-path distance matrix and the correctly centered zero-sum metric quadratic form, including the full vertex set. It compares eigenvalues with the proven Fourier formula, tests one- and two-site perturbations, checks the exact derivative formula, and verifies optimal angular separation.

Observed successful execution:

```text
EXACT_WEIGHTED_PENDANT_DECOMPOSITION_OK 32
ONE_VERSUS_TWO_STRONG_SITE_THRESHOLD_OK 1350
SHARP_TWO_SITE_PERTURBATION_AND_PLACEMENT_OK 168
ALL_CYCLIC_TWO_SITE_STIFFNESS_CHECKS_OK
```

The 32 identities use exact fractions; the spectral and perturbation checks are finite numerical diagnostics. The global support classification, all-parameter baseline, and sharp infinitesimal design are proved in `RESULT.md`; finite checks are not exhaustive proofs. No independent audit was undertaken.
