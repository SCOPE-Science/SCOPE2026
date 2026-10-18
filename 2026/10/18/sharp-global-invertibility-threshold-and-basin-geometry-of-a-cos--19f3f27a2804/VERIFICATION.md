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

# Verification record

The standalone `verify.py` was executed with Python 3 using only standard-library dependencies, and completed with 18,228 passed assertions. Its exact-rational checks cover the key factorization and slope bounds at a finite parameter grid; additional float checks compare the closed derivative to an independently evaluated central difference, establish geometry at sampled angles, and test sample orbits.

The infinite claims do not depend on the finite checks. They follow from the explicit geometric lift, the exact derivative identity, the uniform algebraic minorant, the equality characterization, and one-dimensional monotonicity. The self-review is passed; no independent audit or external certificate has been performed.
