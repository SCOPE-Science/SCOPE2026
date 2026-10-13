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

# Reproduction and limits

Execute `python3 verifier.py` using Python 3 with no third-party packages. The checker uses exact rational arithmetic for the one-step witness, the derived mortality identity, the stepwise feasibility inequality, and an explicit conservative replacement. Successful execution prints `VERIFY_OK`.

The general assertions do not depend on a numeric survey: the analytic proof in `RESULT.md` sums the model's source equations, solves the recovered update, takes a controlled strictly positive limiting family and matches flows in the alternative map. The checker is a reproducibility supplement, not an exhaustive state-space exploration or an independent audit. No claim about any continuous-time trajectory, latent learning algorithm, external validation, or empirical epidemic follows from the finite arithmetic example.
