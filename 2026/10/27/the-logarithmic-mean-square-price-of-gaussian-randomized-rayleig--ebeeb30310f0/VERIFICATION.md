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

Run `python3 verify.py` using only the Python standard library. The checker samples independent standard circular complex Gaussian kernel coordinates, computes the two roots of the exact randomized Ritz polynomial with cancellation-resistant formulas, and checks the residual and sine-angle formulas. It also checks a stable-cutoff sequence of Monte Carlo moment estimates against the proven logarithmic asymptotic and verifies the exact Pareto limiting-tail formula by independent simulation. Random samples are reproducible by a fixed seed.

The proof in RESULT.md is analytical. Monte Carlo estimates and finitely many residual checks cannot certify an infinite-dimensional statement, asymptotic limit, or historical originality. The experiment has ordinary sampling fluctuations and does not claim independent validation.
