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

The analytic proof is the primary evidence. It establishes the exact outside distance multiset for each part, the pairwise-distinct active-occupancy criterion, the bounded distinct-occupancy lower bound, the feasibility criterion, and the reduction to the largest parts.

The included `verify.py` independently stress-tests the statement from the original distance definition. It generates every connected complete multipartite isomorphism type through order \(11\), computes all-pairs shortest-path distances, enumerates every subset, compares the direct local-outer multiset condition with the structural criterion, and checks the resulting minimum against the closed formula.

Expected output:

`ALL CHECKS PASSED; multipartite_types=183; subsets=177556; max_order=11`

The exhaustive test is finite and does not constitute a proof for unbounded order. No independent audit has been performed.
