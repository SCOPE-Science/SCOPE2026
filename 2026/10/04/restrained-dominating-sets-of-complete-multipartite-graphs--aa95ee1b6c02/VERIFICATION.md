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

The symbolic proof derives the criterion directly from adjacency between partite classes and then counts the corresponding support patterns.

The included checker does not use the criterion when deciding test cases. It constructs each complete multipartite graph from part labels and directly checks, for every candidate subset, that each outside vertex has both a selected neighbor and an outside neighbor. It compares the accepted subsets with the structural criterion, the full coefficient vector with the formulas, and the minimum value and minimum-set count with the case distinction.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 128
vertex_subsets_checked = 64916
orders = 2..10
all-set criterion matched direct restrained-domination test
all polynomial coefficients matched
all minimum values and minimum-set counts matched
```

The finite computation is corroborative only; the all-orders theorem follows from the proof.
