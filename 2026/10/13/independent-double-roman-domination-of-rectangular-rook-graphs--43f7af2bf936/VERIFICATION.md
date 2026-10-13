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

The checker constructs \(R_{m,n}\) directly as the graph whose cells are adjacent when they share a row or a column. It tests the independent double Roman definition without using the proof:

1. the positive support is independent;
2. each label-\(0\) vertex has a label-\(3\) neighbor or at least two label-\(2\) neighbors;
3. each label-\(1\) vertex has a neighbor labeled at least \(2\).

It exhaustively checks every labeling on \(R_{2,2}\), \(R_{2,3}\), and \(R_{3,3}\), totaling \(266{,}496\) labelings. The complete minimum sets agree exactly with the theorem.

It then constructs all predicted minimum functions for every \(2\le m\le n\le8\), checks the defining conditions and weight directly, and verifies the permutation/injection counts.

Recorded output:

```text
VERIFY_OK
m=2, n=2: i_dR=4, minimum_functions=2
m=2, n=3: i_dR=6, minimum_functions=6
m=3, n=3: i_dR=6, minimum_functions=6
full_labelings_checked = 266496
constructed_parameter_range = 2<=m<=n<=8
all exhaustive minima matched the injection/permutation classification
```

The finite checks do not prove the arbitrary-size theorem. The proof for all \(m,n\) is the independent-matching and unoccupied-column argument in `RESULT.md`.
