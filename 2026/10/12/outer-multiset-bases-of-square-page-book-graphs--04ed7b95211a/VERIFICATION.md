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

The checker constructs each square-page book graph from its common spine and page vertices, computes all-pairs shortest-path distances, and forms each outside vertex's distance multiset directly.

For every \(3\le r\le9\), it exhaustively tests every landmark set smaller than the claimed optimum and verifies that none resolves. It then enumerates every set of size \(2r-3\), compares the resulting complete basis family with the two complement types in the theorem, and checks the closed basis-count formula.

Recorded output:

```text
VERIFY_OK
book_parameters_checked = 7
vertex_subsets_checked = 1382441
minimum_outer_multiset_bases_checked = 2984
parameters r = 3..9
all smaller landmark sets failed directly
all bases matched the complement classification
all basis counts matched the closed formula
```

The finite computation is corroborative only. The theorem for all \(r\ge3\) follows from the exact signature proof.
