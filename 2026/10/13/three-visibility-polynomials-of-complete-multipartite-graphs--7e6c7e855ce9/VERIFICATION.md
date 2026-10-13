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

The checker constructs every connected complete multipartite isomorphism type of orders \(2\) through \(9\). For each graph and every vertex subset \(X\), it computes ordinary graph distances and tests \(X\)-visibility by deleting all possible internal blockers \(X\setminus\{u,v\}\) and checking whether the original distance is preserved.

It independently evaluates the required pairs for ordinary, outer, and dual mutual visibility. Each result is compared with the structural classification and with every coefficient of the three closed polynomials.

Recorded output:

```text
VERIFY_OK
complete_multipartite_types_checked = 87
orders = 2..9
vertex_subsets_checked = 22932
variant_set_tests = 68796
all mutual/outer/dual classifications matched direct geodesic visibility
all three cardinality enumerators matched the closed formulas
```

The finite enumeration is corroborative only. The theorem for arbitrary part sizes follows from the same-part distance-two criterion.
