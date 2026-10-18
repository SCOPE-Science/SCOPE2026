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

# Verification and limits

The stationary covariance was independently recomputed by solving the continuous Lyapunov equation, and lagged covariance by a matrix exponential, for 105 finite combinations covering seven chain lengths, three parameter sets, and five lags. The exact formula, source-to-end variance normalization, reverse lag, and stationary endpoint covariance all matched numerical linear algebra within prescribed tolerances. The optimizer was checked for \(m\in\{1,2,3,5,10,20,50,100,250\}\), with three subcritical, critical, and supercritical asymptotic profiles and three scaled critical-window tests. Actual console output is in `checks.txt`; executable script is `verify.py`.

The proof for all finite \(n\) and the depth asymptotics are analytical, using covariance equations, a strictly decreasing optimizer equation, controlled factorial expansions, and central-binomial coefficient asymptotics. The finite numerical checks do not establish the infinite limit on their own.

The closest available original PDFs were read to compare objects and statements. The recent motivating preprint was available in abstract form only; full-document noncoverage has not been inferred from the abstract. No independent expert review or external validation has been completed.
