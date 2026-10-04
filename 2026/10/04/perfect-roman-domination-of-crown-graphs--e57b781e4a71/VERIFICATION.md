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

The checker constructs \(\operatorname{Cr}_n\) from two size-\(n\) independent sets with all cross edges except the matched pairs. It then evaluates the perfect Roman condition directly for every labeling by counting value-\(2\) neighbors of every zero vertex.

For every \(3\le n\le7\), it enumerates the full labeling space, independently determines the minimum weight, and compares every minimum function with the deleted-matching-pair classification.

Recorded output:

```text
VERIFY_OK
crown_graphs_checked = 5
labelings_checked = 5380749
minimum_functions_checked = 25
parameters n = 3..7
all perfect Roman domination numbers equal 4
all minimum functions are exactly matched pairs of label-2 vertices
all minimum-function counts equal n
```

The finite computation is corroborative only. The theorem for every \(n\ge3\) follows from the proof.
