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

Run with `python3 verify.py` (Python 3.9 or newer, standard library only). The script uses a fixed seed and directly constructs Gaussian sketch matrices, the compressed one-vector Ritz scalar and the exponential action for dimension-reducing sketches. It checks the Rayleigh residual decomposition and the exact eigenvector case on every draw.

The program separately checks explicit one-sided Student tails for two and three Gaussian sketch rows, their analytical tail constants, and deterministic rare-event witnesses for negative Ritz values despite a positive-definite source matrix. Its printed assertion count is 120028. The numerical tests illustrate the formula, but they cannot prove infinite moments or asymptotic limits. Those rely on the exact Student-density proof in RESULT.md.

The theorem concerns exact arithmetic and unconditioned iid real Gaussian sketches. No conclusion is made about the frequency of numerical overflow or any larger Krylov subspace. Independent auditing has not been performed.
