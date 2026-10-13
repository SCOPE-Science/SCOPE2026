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

The checker uses the 2023 perfect double Italian interval definition directly.

For each tested square rook graph, a labeling is stored as an \(n\times n\) array. The verifier computes each row sum and column sum and checks, for every entry labeled \(0\) or \(1\),
\[
3\le r_i+c_j-x_{ij}\le4.
\]

It exhausts every labeling of total weight at most
\[
2n
\]
for
\[
n=2,3,4.
\]
The recorded output is:

```text
VERIFY_OK
n=2: gamma_pDI=4, minimum_functions=3
n=3: gamma_pDI=6, minimum_functions=21
n=4: gamma_pDI=8, minimum_functions=282
minimum_count_formula_n1_to_n10 = [1, 3, 21, 282, 6210, 202410, 9135630, 545007960, 41514583320, 3930730108200]
bounded_labelings_checked = 662647
all brute-force minima matched row-sum=column-sum=2
```

Thus direct exhaustive search verifies the lower bound and full minimum-function classification through \(n=4\). The coefficient formula is evaluated exactly with rational arithmetic through \(n=10\).

The exhaustive computation is finite corroboration only. The arbitrary-\(n\) value, equality classification, and counting formula are established by the symbolic proof in `RESULT.md`.
