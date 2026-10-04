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

The proof separates global domination from monophonic coverage and derives both from the complete multipartite structure.

The included `verify.py` independently constructs adjacency, enumerates induced paths incrementally, forms monophonic intervals, tests domination in the graph and complement, and checks every vertex subset. It also compares the observed minimum size and number of minimum sets with the closed formulas.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 87
vertex_subsets_checked = 22932
orders = 2..9
```

Finite verification is corroborative only; the all-orders theorem follows from the proof.
