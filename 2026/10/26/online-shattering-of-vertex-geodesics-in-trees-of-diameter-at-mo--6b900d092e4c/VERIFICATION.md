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

# Reproducible verification and limits

Run `python3 verify_tree_geodesic_rank.py`. It uses only Python's standard library and enumerates exactly the unique paths of the specified finite trees. For any candidate version-space bit mask, the routine evaluates the maximum, over all vertices splitting the mask, of one plus the minimum of its two conditional ranks. Its caching terminates because both nonempty conditional masks have fewer hypotheses than the original mask.

The provided `tree_geodesic_certificates.json` records minimum representatives and complete binary query trees. Each leaf contains an explicit endpoint pair, and the verifier checks its path at every queried vertex along that leaf. It checks eight paths for the five-vertex diameter-four path, sixteen paths for the six-vertex branching obstruction, and two/four/eight paths for the lower-diameter representatives.

The finite classification loop checks 128 distinct centered diameter-four branch-multiset shapes with 5–12 vertices, all 36 bounded double-star parameter pairs, and selected further samples. The log is supplied as `tree_geodesic_verification.txt`. These computations certify their finite instances only; the unconditional theorem for trees of arbitrary finite order follows from the structural argument in RESULT.md.

The published-source comparison did not establish global historical priority, and no independent audit has been performed.
