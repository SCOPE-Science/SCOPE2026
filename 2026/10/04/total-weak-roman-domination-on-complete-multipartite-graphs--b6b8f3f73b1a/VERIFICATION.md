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

The proof reduces total weak Roman feasibility to support changes after a one-unit donor transfer. The polynomial then follows by exact inclusion-exclusion over invalid two-part supports.

The included checker does not use the theorem when deciding a labeling. It reconstructs the graph, tests total domination vertex by vertex, and for each zero-labeled vertex tries every adjacent positive donor and retests total domination after the transfer. It then compares the accepted labelings with the structural criterion, every weight coefficient, and the minimum formulas.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 87
ternary_labelings_checked = 748341
orders = 2..9
all-function criterion matched
all weight-enumerator coefficients matched
minimum weights and minimum-function counts matched
```

The finite computation is corroborative only; the all-orders theorem follows from the proof.
