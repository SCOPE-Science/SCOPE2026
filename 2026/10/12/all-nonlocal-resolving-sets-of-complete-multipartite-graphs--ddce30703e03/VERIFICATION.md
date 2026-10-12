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

The checker enumerates every connected complete multipartite isomorphism type of orders \(2\) through \(10\). For each graph it computes all-pairs shortest-path distances by breadth-first search and checks every vertex subset directly against the nonlocal-resolving definition.

The direct result is independently compared with the partwise omission criterion, the full cardinality distribution
\[
z^{N-r}(1+z)^s\prod_{i:n_i\ge2}(n_i+z),
\]
the minimum size \(N-r\), and the minimum-basis count
\[
\prod_{i:n_i\ge2}n_i.
\]

Recorded output:

```text
VERIFY_OK
complete_multipartite_types_checked = 128
orders = 2..10
vertex_subsets_checked = 64916
minimum_bases_checked = 1371
all direct nonlocal-resolving tests matched the partwise omission classification
all cardinality enumerators matched the product formula
all dimensions matched N-r
all minimum-basis counts matched the product of non-singleton part sizes
```

The finite enumeration is corroborative only. The arbitrary-order theorem follows from the proof that a same-part nonadjacent pair can be distinguished only by one of its own endpoints.
