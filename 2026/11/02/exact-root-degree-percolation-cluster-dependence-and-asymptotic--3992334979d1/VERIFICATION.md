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

Exact-rational verification: run `python verify.py` from the directory containing this file and the source code. The script compares 345 assertions across independently enumerated recursive trees, a Markov recursion, a formal-power-series expansion of the full bivariate transform, and the closed covariance formula. It uses no third-party libraries or downloaded dependencies. The exhaustive parent/retention enumeration is through tree size 6 only. The all-size and infinite-limit claims are justified analytically in RESULT.md, not by the finite checks.

The probabilistic limit uses an explicit L2-bounded martingale plus an early/late decomposition of independent original root-attachment indicators; the established marginal Mittag–Leffler identification is attributed in RESULT.md. The proof does not establish rates of joint convergence or results for varying retention parameters.
