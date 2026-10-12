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

The analytic proof is primary. It derives every possible distance multiset from the two omission index sets and proves the classification for all \(n\ge3\).

The standalone script `verify.py` independently constructs the graph, computes all-pairs shortest-path distances by breadth-first search, and checks every subset directly from the definition. It compares this direct test with the theorem's structural criterion for every \(n\) from \(3\) through \(8\), verifies the exact size enumerator, and checks the minimum and basis count.

The expected replay summary is:

`ALL CHECKS PASSED; orders=3..8; subsets=87360; bases=332`

The finite range is a stress test only and is not an exhaustive proof for arbitrary \(n\). The recent toroidal-grid source's full text was unavailable during the literature check; this is an originality-access limitation, not a correctness dependency. No independent audit has been performed.
