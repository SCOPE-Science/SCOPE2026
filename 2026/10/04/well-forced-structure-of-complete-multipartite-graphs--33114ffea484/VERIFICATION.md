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

The proof uses the standard zero forcing color-change rule directly. Its critical observation is that with at least three white vertices, any possible first force leaves at least two white vertices in one part, after which no blue vertex has exactly one white neighbor.

The included checker independently constructs each complete multipartite graph and repeatedly searches for a blue vertex with exactly one white neighbor. It enumerates every initial blue subset and then tests inclusion-minimality by deletion.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 128
vertex_subsets_checked = 64916
orders = 2..10
all minimal-zero-forcing-set classifications matched
all well-forced decisions matched
all count formulas and irrelevant-vertex classifications matched
```

The computation is finite corroboration only; the theorem for arbitrary part sizes follows from the proof.
