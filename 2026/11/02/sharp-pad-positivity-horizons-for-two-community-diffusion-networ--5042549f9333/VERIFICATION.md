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

Run `python verify.py` with Python 3 and the packages in `requirements.txt`. The verifier builds the weighted graph Laplacian from the three edge classes and computes the [2/2] Padé update by solving the dense matrix system. It separately evaluates the three spectral off-diagonal formulas.

Checks executed: 2,352 full-matrix cases (entry formulas, row sums, positive eigenvalues), 1,458 positive-root bracketing cases, two exact symbolic class formula identities, two exact critical-coefficient limits, 18 critical-horizon scaling tests and the exact four-vertex worked example. The run printed `VERIFY_OK`.

The analytic proof is uniform in graph sizes and nonnegative weights; finite numerical tests are only corroborative. The exact computation uses symbolic rational algebra; high-step floating computations use absolute tolerances to account for numerical conditioning. No independent external validation was performed.
