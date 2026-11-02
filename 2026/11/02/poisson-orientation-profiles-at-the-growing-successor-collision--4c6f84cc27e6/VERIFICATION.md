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

The supplied `checker.py` was run directly after extraction from the package. It independently counts witness profiles by direct enumeration of index subsets and by a separate orientation-frequency aggregation; all tested exact rational averages match the formula. It checks all uniform-order combinations for \((n,k,j)=(2,3,3),(3,3,3),(4,3,3),(3,4,4),(4,4,4)\), plus one- and two-edge adjacency counts for \(n\le7\) and orientation weights for \(3\le j\le11\). Execution finishes with `ALL_CHECKS_OK`.

The infinite joint Poisson law is established by the factorial-moment argument, not exhaustive finite checks. The explicit limits assume fixed \(j\), independent uniformly sampled orders, and critical scaling with finite positive \(c\). No independent audit has been performed.
