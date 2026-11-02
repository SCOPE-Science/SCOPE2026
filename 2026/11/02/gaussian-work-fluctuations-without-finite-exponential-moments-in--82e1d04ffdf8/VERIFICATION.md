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

# Verification and reproducibility

The proof is contained in `RESULT.md`. Run `python verify.py` with Python 3 and NumPy to reproduce exact rational stationary-moment and Poisson-corrector identities, eighteen coupled-transform generator identities, and three numerical exact-transition tests of the long-time work variance. The checker uses seeded random sampling and explicitly states finite-sample tolerances. Its successful output is numerical corroboration and is not substituted for the analytical generator/martingale proof or the single-switch exponential-moment obstruction.

The joint process starts at stationarity. The simulated initial state is sampled by a centered normal variable plus the difference of two independent gamma variables of the parameter indicated in `RESULT.md`; between switching times, updates are exact Gaussian free-diffusion or Ornstein–Uhlenbeck transitions. Every jump contributes the signed change in harmonic potential. All scientific assumptions, normalization, limiting ranges and unproved generalizations are specified in `RESULT.md`.

Independent external audit: not performed. Publication priority is not independently certified.
