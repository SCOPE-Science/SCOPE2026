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

The proof uses only the definition of secure total domination and the adjacency rule for complete multipartite graphs. The key invariant is the number of represented parts before and after a defender swap.

The included checker does not use the theorem when testing a subset. It first tests total domination vertex by vertex. For every unselected vertex it then searches all adjacent selected defenders and retests total domination after each possible swap. The resulting valid subsets are compared with the stated part-count criterion, with every polynomial coefficient, and with every minimum-size/minimum-count case.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 128
vertex_subsets_checked = 64916
orders = 2..10
all-set criterion matched
all polynomial coefficients matched
minimum sizes and minimum-set counts matched
```

The exhaustive test is finite corroboration only; the theorem for arbitrary part sizes follows from the proof.
