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
# Reproducibility and verification

Run `python3 verify.py` using Python's standard library. This checks the exact backward-equation solution, the proposed closed-form optimizer against a self-contained golden-section minimizer, and the algebraic endpoint/gradient sign conditions over deterministic parameter grids.

The core argument is the monotonicity of the derivative numerator \(P(h)\), not a finite computation. A separate exploratory event-driven Monte Carlo check used three independent physical parameter sets and 35,000 trajectories each, with relative errors below \(0.12\%\). Monte Carlo does not establish infinite-parameter correctness. No independent audit has been performed.
