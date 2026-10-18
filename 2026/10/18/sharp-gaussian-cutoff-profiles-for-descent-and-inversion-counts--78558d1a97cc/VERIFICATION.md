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

# Reproducibility and checks

Run `python verify.py` with a standard Python 3 installation. No external packages or network access are required.

The verifier constructs the complete transition probabilities for every state reached after \(0\) through \(10\) shuffles when \(n=3,4\), through \(8\) shuffles when \(n=5\), and through \(6\) shuffles when \(n=6\). It independently constructs the ordered-suffix mixture from occupancy Stirling numbers and all uniform permutations, then compares every state probability exactly as a rational number. It also checks exact inversion expectations, occupancy second moments and variance bounds, and all conditional Lehmer-tail means and variances for additional deck sizes. Separate finite-window checks corroborate the claimed occupancy scales.

Successful execution prints `PASS: exact chain/mixture distributions, inversion moments, occupancy and Lehmer-tail formulas; finite-window consistency` after finite-case summaries. The mathematical proof in `RESULT.md`, rather than the finite cases alone, establishes the limiting Gaussian laws, divergence, necessity, and Kolmogorov profiles. There is no external audit or validation claim.
