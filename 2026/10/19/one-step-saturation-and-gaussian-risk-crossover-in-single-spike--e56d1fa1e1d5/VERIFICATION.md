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

Re-run `python3 CHECK.py` using Python 3 and NumPy. Actual checks from the standalone package path succeeded: 240 Gaussian projector/Schur complement identities, 960 direct-versus-reduced matrix-power vector identities, 960 spectral-residual inequalities, and 280 fixed-width trials across two dimensions. The two sample sizes exhibited decreasing empirical absolute deviations between first-step capture and the limiting ceiling.

The exact finite-dimensional distribution is proved by a Gaussian Schur-complement argument, not by sampling. The unrestricted supremum over all positive iteration counts is proved by the eigenvalue ratio upper bound in `RESULT.md`, not by testing finitely many powers. The independent chi-square comparison and beta-tail improvement probability follow analytically; simulations are merely a reproducibility check.

No independent audit or external validation is asserted.
