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

The proof reduces mutual visibility to a shortest-path condition inside a complete multipartite graph and then counts non-visible sets by their nonempty complements.

The included checker is definition-level for the scientific premise. For every complete multipartite isomorphism type of orders two through ten, it constructs the graph, computes all-pairs distances, and tests a candidate set by deleting all selected vertices except each tested endpoint pair. The pair remains visible exactly when the shortest distance is unchanged. These direct results are compared with the structural criterion and every coefficient of the closed formula.

The same checker then enumerates all integer part-size partitions for orders three through thirty and verifies the coefficientwise maximum class, the unique cubic minimizer, the small-order minima, and the crossing with \(K_{3,N-3}\) from order six onward.

Recorded output:

```text
VERIFY_OK
multipartite_types_definition_checked = 128
vertex_subsets_definition_checked = 64916
definition_orders = 2..10
extremal_partition_orders = 3..30
all-set criterion and polynomial matched
coefficientwise maxima classification matched
minimum-existence threshold N=6 matched
```

The finite computations are corroborative only. The coefficientwise extremal theorem for arbitrary order follows from the symbolic proof.
