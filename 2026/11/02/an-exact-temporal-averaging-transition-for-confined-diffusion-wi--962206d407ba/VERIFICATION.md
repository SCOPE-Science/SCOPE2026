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

The analytic two-moment closure is derived directly from the Brownian-plus-historical-reset jump generator, rather than assumed from one-time distributions. The Laplace transform is solved by an integrating factor and inverted exactly; its boundary case is obtained by a continuous limit. The three asymptotic regimes use the standard confluent-hypergeometric large-negative-argument expansion and an explicit logarithmic transform at criticality.

Run `python verification/check_memory_time_average.py` with Python 3, NumPy, SciPy, and mpmath. This program checks 84 independently generated parameter/time identities and comparisons, including an independently simulated position history. The simulation uses a finite mesh and random samples and does not prove exact identities. Numerical inversion and comparison do not replace the analytic proof. The run reproduced the three Monte Carlo second moments to within 1.4% relative error.

Scientific limitations: no pathwise or central-limit conclusion, no arbitrary-memory-kernel extension, no finite-sample identification claim. Publication priority and independent scientific audit remain unverified.
