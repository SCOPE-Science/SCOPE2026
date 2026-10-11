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

# Reproducibility and scope

The proof covers every strictly positive summable real weight sequence and every interval of the coordinate filtration, including an infinite upper endpoint. The critical lemma is a two-source, two-sink transport computation: two permutation matchings give the exact norm by finite transport duality. The norm is maximized by molecules that change a single coordinate inside the interval and by molecules whose distinct prefixes differ at a coordinate of smallest preceding weight, with identical all-one interval blocks.

The accompanying `check_intervals.py` independently solves each finite-cube dual Lipschitz linear program with pinned base-point potential. It uses Python 3, NumPy, and SciPy. The recorded six suites include nonmonotone weights. Forty-eight interval comparisons all agree numerically with the stated formula to within \(9\cdot10^{-16}\). This finite check is a sanity test, not evidence that a finite enumeration proves the infinite theorem.

The metric approximation property of this invariant-metric compact group subclass was established in earlier literature. Only the exact specified interval-projection norms and ensuing structural threshold are proposed as new. No independent mathematical audit has been performed.
