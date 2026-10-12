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

The checker constructs the crown graph and its complement and tests the Italian condition independently on both. It exhaustively tests every ternary labeling for \(n=4,5,6\), totaling \(597{,}051\) labelings.

Recorded output:

```text
VERIFY_OK
n=4: gamma_gI=4, minimum_functions=10
n=5: gamma_gI=4, minimum_functions=15
n=6: gamma_gI=4, minimum_functions=21
full_labelings_checked = 597051
constructed_parameter_range = 4..50
all exhaustive minima matched the aligned matched-pair classification
```

For the claimed sample orders \(n=5,6\), the complete minimum layer matches the theorem exactly. The checker also constructs every predicted minimum function and verifies both complementary conditions for \(4\le n\le50\). Finite checks are corroborative only; the arbitrary-order proof is in `RESULT.md`.
