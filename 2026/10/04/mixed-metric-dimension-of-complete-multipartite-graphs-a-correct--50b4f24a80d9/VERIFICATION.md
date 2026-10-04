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

The proof uses exact mixed distance codes: a landmark has edge distance zero exactly at an incident edge and one at every other edge, while same-part nonidentical vertices have distance two. These code forms yield the complement classification without finite-case assumptions.

The included checker decides mixed resolution directly. It constructs every vertex and edge, computes its complete distance vector to each tested landmark set, and requires all element vectors to be distinct. It then compares those definition-level decisions with the classification and enumerator.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 128
vertex_subsets_checked = 64916
orders = 2..10
definition-level mixed codes matched the complement classification
all enumerator coefficients matched
K_{3,3,5} direct mixed metric dimension = 10
2022 Theorem 5 claimed value for K_{3,3,5} = 8
```

The explicit K_{3,3,5} replay is included because it directly distinguishes the corrected value from the 2022 published formula. The bounded computation is corroborative only; the proof establishes the theorem for arbitrary part sizes.
