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

The verifier builds the rook graph directly from row and column adjacency and tests the perfect Italian rule without using the structural proof:
for every label-\(0\) vertex, the sum of labels on its open neighborhood must equal \(2\).

For
\[
(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),
\]
the program enumerates every ternary labeling of weight at most the claimed optimum. It finds no feasible lower-weight labeling and verifies that the entire minimum layer equals the stated structural family.

It then generates all claimed minimum functions throughout
\[
2\le m\le8,
\qquad
m\le n\le9,
\]
and checks feasibility, weight, and the closed count formulas.

Recorded output:

```text
VERIFY_OK
m=2, n=2: gamma_pI=2, minimum_functions=2
m=2, n=3: gamma_pI=4, minimum_functions=12
m=2, n=4: gamma_pI=4, minimum_functions=10
m=2, n=5: gamma_pI=4, minimum_functions=15
m=3, n=3: gamma_pI=3, minimum_functions=6
m=3, n=4: gamma_pI=6, minimum_functions=22
m=3, n=5: gamma_pI=6, minimum_functions=15
bounded_weight_labelings_checked = 57007
constructed_minimum_functions_checked = 47296
direct_classification_cases = [(2, 2), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
construction_range = 2<=m<=8, m<=n<=9
all tested minimum families matched exactly
```

The bounded computation is corroborative only. The theorem for arbitrary \(m,n\) follows from the row-sum and column-sum proof in `RESULT.md`.
