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

The checker constructs every connected complete multipartite isomorphism type of orders \(2\) through \(10\).

It generates maximal geodesics directly. Every length-two shortest path is maximal because the diameter is at most two. An edge is included as a maximal geodesic exactly when it is not a subpath of any length-two geodesic.

Every vertex subset is then tested literally for whether it intersects every maximal geodesic. The direct result is compared with the theorem's complement classification. The checker also independently compares the full complement-size distribution, the formula
\[
\operatorname{gt}(G)=N-\max\{M,q+\mathbf 1_{\{s>0\}}\},
\]
and the minimum-basis count.

Recorded output:

```text
VERIFY_OK
complete_multipartite_types_checked = 128
orders = 2..10
vertex_subsets_checked = 64916
maximal_geodesic_instances_across_types = 4833
minimum_bases_checked = 1085
all direct maximal-geodesic hitting tests matched the complement classification
all cardinality enumerators matched the closed complement polynomial
all geodesic-transversal numbers and basis counts matched the formulas
```

The finite computation is corroborative only. The theorem for arbitrary part sizes follows from the explicit classification of maximal geodesics.
