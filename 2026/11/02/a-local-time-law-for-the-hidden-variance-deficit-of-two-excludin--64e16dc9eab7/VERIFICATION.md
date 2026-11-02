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

# Reproducibility and proof boundaries

Run `python verification_checker.py` with Python 3. The script uses `fractions.Fraction` to verify the exact generator, both diagonal predictable brackets and vanishing predictable cross bracket over a finite test domain. It separately checks the reflecting image formula against uniformised walk transitions and calculates selected Gaussian tail/mean consistency cases. If SciPy is installed, numerical heat-kernel quadrature checks first-order convergence of gap occupation expectations.

The recorded output is `verification_output.txt`. The mathematical argument is the exact reflection decomposition and joint martingale functional limit reconstructed in `RESULT.md`; neither numerical convergence nor finite enumeration proves that analytic limit. The proven scope is two exclusion walkers, on the infinite one-dimensional lattice, with deterministic initial gaps whose ratio to the spatial scaling tends to a finite nonnegative value. No independent audit has been performed.
