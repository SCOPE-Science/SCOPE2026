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

The proof is symbolic and applies to arbitrary complete multipartite graphs.

A finite regression checker rebuilds every complete multipartite graph whose unordered part-size profile has total order at most \(9\). For each graph it enumerates every vertex subset, tests total domination and the locating condition directly from adjacency masks, and compares the coefficient table against the theorem's omission-choice formula.

Expected replay output:

`VERIFY_OK multipartite_types=87 max_order=9`

The exhaustive computation does not replace the infinite proof. It checks implementation-independent consequences of the characterization on all \(87\) isomorphism types in the stated finite range.
