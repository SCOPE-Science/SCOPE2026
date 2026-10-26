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

# Reproducibility checks

Run `python3 rrt_subtree_checker.py` in any Python 3 installation using only its standard library. The checker enumerates all recursive trees on up to nine labeled vertices and compares exact rational ancestry probabilities, first moments, signed conditional covariances, vanishing unconditional covariance, and the strict conditional expectation witnessing nonindependence. A completed local run returned **1,022 exact assertions PASS**.

The universal proof uses explicit Pólya-urn factorial moments and Dirichlet-multinomial covariance identities, as reconstructed in `RESULT.md`. Exhaustive tests cover only the stated finite sizes and cannot establish the unrestricted theorem by themselves. Publication priority and independent scientific validation remain unassessed externally.
