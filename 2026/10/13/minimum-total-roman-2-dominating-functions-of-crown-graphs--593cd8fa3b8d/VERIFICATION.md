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

The checker constructs
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
for
\[
2\le n\le6.
\]
It exhausts every labeling
\[
f:V(\operatorname{Cr}_n)\to\{0,1,2\}.
\]
For each labeling it checks the zero-vertex condition
\[
\sum_{u\in N(v)}f(u)\ge2
\]
and verifies that every positive vertex has a positive neighbor.

The complete set of minimum functions is compared with the formula obtained by choosing two common deleted-matching indices and assigning label \(1\) to all four corresponding endpoints.

Recorded output:

```text
VERIFY_OK
n=2: gamma_tR2=4, minimum_functions=1
n=3: gamma_tR2=4, minimum_functions=3
n=4: gamma_tR2=4, minimum_functions=6
n=5: gamma_tR2=4, minimum_functions=10
n=6: gamma_tR2=4, minimum_functions=15
ternary_labelings_checked = 597861
all minima were identical two-index label-1 supports on the two sides
```

The checker exhausts \(597{,}861\) ternary labelings. The finite computation is corroborative only; the arbitrary-order theorem follows from the side-weight and matched-coordinate proof.
