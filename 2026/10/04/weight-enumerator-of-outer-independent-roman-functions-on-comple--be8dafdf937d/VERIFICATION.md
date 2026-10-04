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

The checker tests the outer-independent Roman conditions directly for every ternary labeling; it does not use the structural theorem to decide validity. It independently expands the claimed polynomial with integer arithmetic.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 87
ternary_labelings_checked = 748341
valid_functions_checked = 183936
orders = 2..9
all enumerator coefficients matched
all total-function counts matched
published minimum-value formula recovered
```

The finite computation is corroborative only; the arbitrary-order theorem follows from the proof.
