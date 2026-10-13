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

# Checks and reproducibility

Run `python verify.py` with SymPy version at least 1.12 (specified in `requirements.txt`). The checker reconstructs the complex three-dimensional generator and claimed Hermitian survival Gramian, symbolically checks all nine Lyapunov entries, verifies the sharp ratio factorization and the optimum and equal-link comparison, and solves three independent unequal-rational-coupling full Lyapunov systems. The output `VERIFY_OK 17` records 17 implemented symbolic/exact checks. Analytical spectral stability and AM–GM with an exact polynomial factorization—not finite tests—supply the universal proof. The full claim assumes positive hopping amplitudes and positive sink rate; at zero links absorption can fail and is excluded. No independent external validation or certification has been performed.
