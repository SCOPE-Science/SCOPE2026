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

# Verification procedure and scope

Execute `python verification/minimax_verifier.py` with Python 3.11 or later. The program uses only the standard library and decimal arithmetic at 110-digit precision. It independently constructs the binary transition matrix, evaluates the joint conditional entropy from four probabilities, compares it with the entropy-identity expression, finds the unique stationary point using the analytic derivative, and examines the predicted small-time regimes.

The bundled verifier completed with `PASS: 76 high-precision analytical-formula checks`. The suite includes finite-time asymmetric channels, exact equal-rate optimizers, fixed-gap logarithmic asymptotics, and the near-balanced varying-rate limit. It checks a finite sample of parameter values at finite precision; it cannot prove strict concavity for all parameters or convergence as time approaches zero. Those claims are established in the proof in `RESULT.md`.

The underlying minimax equality is rederived analytically rather than taken solely from the motivating source. The novelty comparison is a best-knowledge literature assessment, not an independent publication-priority certification. No third-party full texts are bundled.
