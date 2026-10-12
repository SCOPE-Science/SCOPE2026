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

The checker constructs the half graph
\[
H_n
\]
for
\[
2\le n\le7.
\]

For every map
\[
f:V(H_n)\to\{0,1,2\},
\]
it tests the Italian condition
\[
\sum_{u\in N(v)}f(u)\ge2
\]
at every zero-labeled vertex and the quasi-total condition that every label-\(2\) vertex has a positive-labeled neighbor.

It then computes the minimum weight and compares the complete minimum-function list with the theorem.

Recorded output:

```text
VERIFY_OK
n=2: gamma_qtI=3, minimum_functions=2
n=3: gamma_qtI=4, minimum_functions=4
n=4: gamma_qtI=4, minimum_functions=1
n=5: gamma_qtI=4, minimum_functions=1
n=6: gamma_qtI=4, minimum_functions=1
n=7: gamma_qtI=4, minimum_functions=1
ternary_labelings_checked = 5380830
all minimum functions matched the piecewise classification
```

The checker examines \(5{,}380{,}830\) ternary labelings. The finite computation is corroborative only; the arbitrary-\(n\) uniqueness result follows from the leaf and nested-neighborhood proof.
