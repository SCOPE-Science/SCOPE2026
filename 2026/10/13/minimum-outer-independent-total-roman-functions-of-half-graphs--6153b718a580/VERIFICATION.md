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

The verifier constructs \(H_n\) directly for
\[
2\le n\le7.
\]

For every labeling
\[
f:V(H_n)\to\{0,1,2\},
\]
it checks:

- the zero-labeled set is independent;
- every zero-labeled vertex has a neighbor labeled \(2\); and
- every positive-labeled vertex has a positive-labeled neighbor.

It computes the minimum weight and compares the entire minimum-function set with the staircase family \(F_0,\ldots,F_n\), including the extra all-one minimum at \(n=2\).

Recorded output:

```text
VERIFY_OK
n=2: gamma_oitR=4, minimum_functions=4
n=3: gamma_oitR=5, minimum_functions=4
n=4: gamma_oitR=6, minimum_functions=5
n=5: gamma_oitR=7, minimum_functions=6
n=6: gamma_oitR=8, minimum_functions=7
n=7: gamma_oitR=9, minimum_functions=8
ternary_labelings_checked = 5380830
all minimum functions matched the staircase classification
```

The checker examines \(5{,}380{,}830\) ternary labelings. The finite computation is corroborative only; the theorem for arbitrary \(n\) follows from the vertex-cover classification and leaf-forcing proof.
