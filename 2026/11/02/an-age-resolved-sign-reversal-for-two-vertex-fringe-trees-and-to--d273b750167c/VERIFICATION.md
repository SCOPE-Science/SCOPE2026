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

# Finite verification and analytic boundary

Execute `python VERIFY.py` with Python 3 from the same directory. It exhaustively enumerates 46,232 recursively labeled rooted trees of orders 3 through 9 and compares all eligible marked-event probabilities and covariances with exact `fractions.Fraction` arithmetic. It also compares full conditional path-length histograms across every valid child label and conditional means, and checks harmonic monotonicity and some asymptotic numerical diagnostics.

The finite diagnostic does not establish claims for all tree sizes or the limiting threshold. The exact deletion coupling, harmonic sum identity, strict monotonicity of the covariance bracket and the harmonic asymptotic in `RESULT.md` supply those proofs. No independent audit has been performed.
