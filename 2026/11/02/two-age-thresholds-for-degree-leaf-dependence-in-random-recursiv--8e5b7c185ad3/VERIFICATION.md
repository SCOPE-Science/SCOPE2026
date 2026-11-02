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

# Reproducibility

Run `python3 verify.py` from this directory with the standard Python library. The script enumerates all recursive-tree parent sequences with sizes three through nine, verifies every arrival-to-parent mixed covariance using rational arithmetic, verifies all vertex-degree/leaf covariances, and tests the sharp finite sign criterion through size 200. Numerical checks probe the interior asymptotic cutoff. It reports 374 exact/numerical grouped assertions passed.

The infinite theorem is proved analytically using independent parent choices, the telescoping leaf-survival probability, and convexity of a harmonic-sum sequence. The checker is additional finite evidence, not a substitute for proof. No independent audit has been performed.
