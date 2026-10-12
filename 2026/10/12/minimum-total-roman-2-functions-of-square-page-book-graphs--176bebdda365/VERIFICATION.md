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

The checker constructs \(B_m\) directly and tests the defining zero-neighborhood inequality and the no-isolated-positive condition.

For every
\[
1\le m\le12,
\]
it exhausts every labeling whose total weight is at most the relevant minimum candidate.

Recorded output:

```text
VERIFY_OK
m=1: gamma_tR2=3, minimum_functions=4
m=2: gamma_tR2=4, minimum_functions=6
m=3: gamma_tR2=4, minimum_functions=1
m=4: gamma_tR2=4, minimum_functions=1
m=5: gamma_tR2=4, minimum_functions=1
m=6: gamma_tR2=4, minimum_functions=1
m=7: gamma_tR2=4, minimum_functions=1
m=8: gamma_tR2=4, minimum_functions=1
m=9: gamma_tR2=4, minimum_functions=1
m=10: gamma_tR2=4, minimum_functions=1
m=11: gamma_tR2=4, minimum_functions=1
m=12: gamma_tR2=4, minimum_functions=1
bounded_labelings_checked = 88801
all minimum functions matched the classification
```

The \(m=1\) computation is a boundary check only. The finite computation is exhaustive for all labelings relevant to the minimum-value and minimum-function claims in the tested range; the arbitrary-\(m\) theorem is proved symbolically in `RESULT.md`.
