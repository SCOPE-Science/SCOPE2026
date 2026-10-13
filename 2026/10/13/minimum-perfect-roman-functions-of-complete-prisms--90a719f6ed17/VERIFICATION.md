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

The checker constructs the two clique layers of \(K_n\square K_2\) implicitly and tests the exact perfect Roman condition: every zero-labeled vertex must have exactly one neighbor labeled \(2\).

For every \(4\le n\le12\), it exhausts every ternary labeling whose total weight is at most \(4\). It verifies that no labeling below weight \(4\) is feasible and that every feasible weight-\(4\) labeling has label \(2\) on both endpoints of one matching edge and label \(0\) elsewhere.

Recorded output:

```text
VERIFY_OK
n=4: gamma_pR=4, minimum_functions=4
n=5: gamma_pR=4, minimum_functions=5
n=6: gamma_pR=4, minimum_functions=6
n=7: gamma_pR=4, minimum_functions=7
n=8: gamma_pR=4, minimum_functions=8
n=9: gamma_pR=4, minimum_functions=9
n=10: gamma_pR=4, minimum_functions=10
n=11: gamma_pR=4, minimum_functions=11
n=12: gamma_pR=4, minimum_functions=12
bounded_labelings_checked = 61899
all minima were matched pairs labelled 2, all other vertices 0
```

The computation checks \(61{,}899\) bounded-weight labelings. It is exhaustive for every labeling relevant to the minimum and minimum-function claims in the tested orders, but the arbitrary-order theorem follows from the symbolic proof.
