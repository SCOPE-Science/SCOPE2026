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

The seven embedded artifacts are self-contained. `checker.py` can be run with `python3 checker.py` and requires only the Python standard library. The test suite uses exact fractions to compare the beta-binomial formula to independently generated urn transition probabilities; checks exact finite-age means, variances, stationary regenerative equations and tail normalization; and verifies the conditional mean-decay identity by direct state enumeration. Result: 9,580 assertions passed when constructing this package and again from the embedded copy.

The proof of the infinite-population limit does not depend on finite enumeration. In particular, the conditional binomial central limit theorem and the martingale functional central limit theorem supply the respective infinite-dimensional steps; the stopping clocks are independent and converge as point processes. The path-level statement is limited to compact time intervals with Skorokhod \(J_1\) convergence. The displayed stationary Laplace law is previously known for Brownian motion with resetting, and the historical-priority assessment for the reinforced urn is not an independent audit.
