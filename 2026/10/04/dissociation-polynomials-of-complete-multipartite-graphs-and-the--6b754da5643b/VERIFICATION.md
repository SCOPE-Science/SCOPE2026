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

The proof classifies every dissociation set from induced degrees and then applies exact binomial transfer identities.

The included checker independently enumerates vertex subsets of complete multipartite graphs, computes induced degrees directly, and compares the observed coefficient vector with the formula. It also enumerates integer part partitions to test the coefficientwise extremizers.

Recorded output:

```text
VERIFY_OK
multipartite_types_bruteforced = 128
vertex_subsets_checked = 64916
coefficientwise_extremal_shapes_checked = 9270
```

The computation is finite corroboration only; the all-orders result follows from the proof.
