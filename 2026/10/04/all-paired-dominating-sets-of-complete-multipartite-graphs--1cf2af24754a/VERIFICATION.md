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

The proof uses an exact perfect-matching criterion for complete multipartite graphs: an even-order complete multipartite graph has a perfect matching exactly when no part contains more than half of its vertices. Sufficiency is proved inductively by matching vertices from two largest parts.

The included checker does not use that criterion when deciding test cases. It tests domination directly and recursively searches for a perfect matching in each induced selected subgraph. It then compares the observed size distribution with the closed formula and independently tests inclusion-minimality.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 87
vertex_subsets_checked = 22932
orders = 2..9
all polynomial coefficients matched
all minimal paired-dominating sets were exactly cross-part pairs
```

The finite computation is corroborative only; the all-orders statement follows from the proof.
