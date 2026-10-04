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

The symbolic proof is exhaustive because every function has label \(2\) in zero, one, or at least two parts. The two quasi-total Roman conditions are checked exactly in each case.

The included checker does not use the structural classification to decide feasibility. It reconstructs each complete multipartite graph from its part labels and, for every ternary vertex labeling, directly tests that each zero has an adjacent \(2\) and each \(2\) has an adjacent positive vertex. It independently expands the displayed polynomial with integer polynomial arithmetic.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 87
ternary_labelings_checked = 748341
orders = 2..9
definition-level QTR condition matched every polynomial coefficient
total-function count matched
minimum-weight corollary matched
```

The finite computation is corroborative only; the theorem for arbitrary part sizes follows from the proof.
