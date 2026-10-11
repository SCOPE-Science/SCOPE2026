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

The accompanying `verify.py` uses only the Python standard library. Invoke `python verify.py` after extracting the files in this item. The program reconstructs signed-edge intersections of the unit cross-polytope, checks that every candidate point lies in the hyperplane and on the unit \(\ell_1\) boundary, exhaustively computes intervertex distances, and compares with the closed form at sampled normals in dimensions 2, 3, 4 and 7.

The same program numerically integrates the all-dimensional distribution formula by Simpson quadrature over \([0,11]\), compares it with an independently seeded half-normal Monte Carlo estimator at four dimension/threshold combinations, and verifies endpoint probabilities. The analytic integration tail omitted beyond 11 is at most \(n\,\mathbb P\{|G|>11\}\) for the tested \(n\le8\), which is much less than the numerical tolerance. Successful execution ends with `CROSSPOLYTOPE_DIAMETER_FINITE_CHECKS_OK`.

Finite simulation, quadrature, and exhaustive checks of finitely many normals do **not** prove a continuous-parameter identity or an infinite-dimensional limit. Those conclusions are justified in RESULT.md by the deterministic extremal-edge formula, exact order-statistic conditioning, Gaussian tail bounds, and uniform moment estimates. No independent scientific audit has been performed.
