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

The proof reduces feasibility to an exact packing problem for edge covers of complete graphs. The packing number is proved to be \(s-1\) for even \(s\) and \(s-2\) for odd \(s\), with explicit constructions.

The accompanying `verify.py` does not use that criterion to decide feasibility. For each candidate subset it lists every allowed shortest path between selected endpoint pairs and performs an exact backtracking search for a one-path-per-pair assignment covering every graph edge.

Recorded output:

```text
VERIFY_OK
direct isomorphism types: 32
direct vertex subsets: 17008
published-value comparisons: 5574
```

Thus every one of the \(17008\) candidate subsets in the \(32\) admissible complete multipartite isomorphism types through order \(10\) agrees with the theorem. The same script checks the minimum-value corollary against the published 2024 formula on \(5574\) multipartite types through order \(30\).

The finite checks corroborate the proof but do not replace the all-orders edge-cover construction.
