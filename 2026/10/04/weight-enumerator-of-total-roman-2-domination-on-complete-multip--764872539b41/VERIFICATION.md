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

The symbolic proof uses only complete-multipartite neighborhoods. For a vertex in part \(X_i\), the open-neighborhood label sum is exactly total weight minus the weight inside \(X_i\). The totality condition is likewise exactly the requirement that positive labels occupy at least two parts.

The included checker independently iterates over every ternary labeling, evaluates both defining conditions directly from adjacency, evaluates the structural criterion separately, and expands the closed polynomial with integer arithmetic.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 87
ternary_assignments_checked = 748341
valid_functions_checked = 682457
orders = 2..9
structural criterion matched direct neighborhood tests
all weight-enumerator coefficients matched
minimum-weight corollary matched
```

The finite computation is corroborative only; the arbitrary-order theorem follows from the proof.
