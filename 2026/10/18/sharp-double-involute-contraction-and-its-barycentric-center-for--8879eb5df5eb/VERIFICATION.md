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
# Verification details

`python3 verify.py` runs a standard-library, exact rational check of the first and dual involute half-sums, the three-by-three transition matrix, six admissible sample norms, and five successive full steps for a nonsymmetric starting polygon in each case.

The symbolic verification of the infinite-family theorem is in RESULT.md: derive the two interpolation lists, calculate the off-diagonal entries of their product, identify the rank-one barycentric update, prove the interval and equality case by arithmetic-geometric means, and establish attainable values using an explicit one-parameter family. The finite rational checks inspect indexing but do not prove the all-real-parameter assertion.

The reviewed mathematical claim assumes strict convexity, exactly three paired side directions, and the specified alternating Minkowski involutes. Independent audit has not been performed.
