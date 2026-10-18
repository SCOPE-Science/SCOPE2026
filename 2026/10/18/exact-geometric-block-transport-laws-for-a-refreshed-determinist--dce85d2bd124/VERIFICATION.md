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

# Reproducibility
Execute `python3 check.py` with Python 3 and SymPy installed. The checker establishes the Laurent generating function's normalization, first and second displacement moments, mixed time-displacement derivative identity, exact rational regenerative variance identity, velocity derivative, balanced-case derivative, and near-refresh boundary coefficients. It also enumerates all stationary arrow assignments on finite relevant intervals with exact rational probability weights for several biases, compares the results with Taylor coefficients of the proposed distribution, and independently controls geometric-clock truncation by its remaining tail probability. An observed successful execution reported 280 exact distribution assertions plus all symbolic identities.

The analytical derivation of each formula is in `RESULT.md`; finite enumeration is not used to establish the infinite all-parameter theorem. An independent human audit of correctness or priority has not occurred. The claimed central limit theorem is annealed, not quenched; a unique interior variance maximizer is not proved.
