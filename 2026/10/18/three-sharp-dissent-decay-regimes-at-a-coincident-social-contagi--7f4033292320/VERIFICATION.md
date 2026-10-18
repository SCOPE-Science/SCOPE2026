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

# Verification

The reproducibility script `verify.py` performs exact symbolic reduction of the full normalized equations and of the nonlinear-clock ratio identities, and integrates six independent positive trajectories. It reports exact-identity success, numerical convergence in the low and marginal regimes, and stabilization of the transformed high-conversion amplitude; the numerical diagnostics are neither a proof of a limiting law nor an exhaustive parameter search. Dependencies are specified in `requirements.txt`. Run `python -m pip install -r requirements.txt` and `python verify.py` in this directory.

The proof in `RESULT.md` establishes positivity, convergence of both non-susceptible compartments, divergence of the nonlinear clock, the scalar logistic trichotomy and the positive high-conversion asymptotic constant. Separate independent scientific validation has not been performed.
