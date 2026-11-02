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

# Reproducibility and limits

Run `python verification/check.py` with dependencies in `verification/requirements.txt`. The script constructs exact finite-dimensional linear moment equations independently of the theorem's block asymptotic expansion and confirms 485 assertions. Its cases include the exact two-node rational baseline, random weighted connected graphs, a jointly reset four-node path with a full-rank leading coefficient, a exactly silent two-reset star, and a four-node graph whose cubic coefficient cancels although its finite-rate variance is strictly positive.

The numerical checks confirm finite cases and conditioning-aware asymptotic comparisons. They do not prove ergodicity, universal covariance scaling, all-rate silence, or arbitrary-graph rank assertions. Those facts follow analytically in `RESULT.md`, using the generator, grounded-Laplacian coercivity, block estimates, pathwise reset sections and a controllability Gramian. The physical approximation limit is also explicit: the checked process has unwrapped linear phase coupling, not nonlinear sine dynamics. Independence and external validation have not been performed.
