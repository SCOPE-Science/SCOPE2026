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

Run `python verify_hopf.py` with SymPy installed. The checker is self-contained and symbolically verifies the Jacobian factorization, eigenvector conventions, first Lyapunov coefficient, the distinct harmonic-balance calculation, and the expansion coefficients for the branch and period-floor gap. A successful run prints `PASS` and exact formulas.

The existence, smoothness, and orbital stability of the local family are mathematical consequences of the nondegenerate Hopf bifurcation theorem using these algebraic hypotheses. This file does not claim independent proof certification or global phase-portrait completeness. The comparisons with earlier literature concern the analytical results actually inspected; unknown equivalent work remains possible.
