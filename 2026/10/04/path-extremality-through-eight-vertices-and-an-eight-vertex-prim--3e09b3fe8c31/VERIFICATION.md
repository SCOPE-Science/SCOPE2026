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

Run `python3 artifacts/verify.py` beside the embedded census. The verifier uses only the Python standard library. It decodes each graph6 record, enumerates every subset, computes zero-forcing closure by the defining unique-white-neighbor rule, and compares every coefficient to the stored exact path vector.

Expected replay summary:

```
orders: 1:1 2:2 3:4 4:11 5:34 6:156 7:1044 8:12346
graphs_checked: 13598
subsets_checked: 3305498
path_vector_n8: [0, 2, 18, 52, 70, 56, 28, 8, 1]
full_vector_equality_counts: 1:1 2:1 3:1 4:1 5:1 6:1 7:1 8:1
ALL CHECKS PASSED
```

The order-eight generation method is included separately and requires NetworkX. It starts from all 1,044 unlabeled seven-vertex atlas graphs, adds a new vertex with each of 128 neighborhoods, and quotients by exact graph isomorphism. The logical completeness of this augmentation follows by deleting one vertex from an arbitrary eight-vertex graph. The resulting 12,346 classes agree with the standard independent census count.

The replay proves only the finite coefficient inequalities. The passage to graphs with one prime bag is deductive and uses German's Corollary 4; it is not experimentally rechecked on an infinite family. No claim is made for arbitrary order-nine graphs or for graphs with multiple prime bags.
