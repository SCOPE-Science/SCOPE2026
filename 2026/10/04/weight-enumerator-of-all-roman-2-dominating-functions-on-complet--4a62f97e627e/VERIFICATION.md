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

`verify.py` constructs every complete multipartite profile given by an integer partition of each order \(2\le N\le10\). For each graph it enumerates every labeling in \(\{0,1,2\}^N\), checks the Roman \(\{2\}\)-domination condition directly at every zero-labeled vertex, checks the equivalent part-count criterion, and compares the entire empirical weight enumerator with the theorem's closed formula.

A successful replay prints

`VERIFY_OK profiles=128 labelings=3169350 local_checks=3169350 max_order=10`

The replay is finite and is not used as proof for arbitrary order. Its role is to catch boundary errors in singleton parts, two-vertex parts, complete bipartite specializations, and the inclusion/exclusion between the three label-2 support regimes.
