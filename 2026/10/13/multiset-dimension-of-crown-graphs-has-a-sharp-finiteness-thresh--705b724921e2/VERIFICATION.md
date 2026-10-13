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

The checker constructs every crown graph
\[
\operatorname{Cr}_n
\]
with
\[
3\le n\le8.
\]
For each graph it computes all-pairs shortest-path distances by breadth-first search, enumerates every vertex subset, forms every sorted distance multiset, and tests pairwise distinctness directly.

The direct test is compared with the membership-pattern classification.

Recorded output:

```text
VERIFY_OK
crown_graphs_checked = 6
n_range = 3..8
vertex_subsets_checked = 87360
Cr_3_resolving_sets = 12, all of size 3
Cr_n_resolving_sets = 0 for n=4..8
all direct distance-multiset tests matched the classification
```

The computation confirms exactly twelve resolving sets for \(\operatorname{Cr}_3\), all of size \(3\), and no resolving set for every tested \(\operatorname{Cr}_n\) with \(4\le n\le8\).

The finite computation is corroborative only. The arbitrary-\(n\) impossibility follows from the four possible membership pairs and the exact \(n=4\) cross-part collision.
