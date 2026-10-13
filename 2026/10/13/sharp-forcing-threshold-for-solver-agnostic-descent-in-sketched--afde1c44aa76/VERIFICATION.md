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

The theorem is proved analytically in `RESULT.md`.

`artifacts/verify_forcing_frontier.py` checks the two-eigenvalue equality construction, the zero directional derivative at the frontier, positive directional derivative above it, and source-compatible least-squares realizations using exact symbolic algebra and high-precision numerical checks.

The script is supporting evidence only. The universal quantifier over all admissible residuals follows from the explicit maximization over the Euclidean residual ball and the spectral inequality in the proof.
