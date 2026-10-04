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

The proof is symbolic: a zero-labeled vertex in part \(X_i\) sees exactly \(T-t_i\) vertices labeled \(2\), which yields the four exhaustive structural regimes.

The included checker does not use the structural classification when deciding a function. It constructs the complete multipartite graph from part labels, directly counts adjacent \(2\)-labels for every zero-labeled vertex, and records the weight of every valid ternary labeling. It then compares every coefficient with the closed formula and compares the smallest observed weight with the closed minimum formula.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 87
ternary_labelings_checked = 748341
orders = 2..9
all polynomial coefficients matched
minimum-weight formula matched
```

The exhaustive computation is finite corroboration only; the all-orders theorem follows from the proof.
