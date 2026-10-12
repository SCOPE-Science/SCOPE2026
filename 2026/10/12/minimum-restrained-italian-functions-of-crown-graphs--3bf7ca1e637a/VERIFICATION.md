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

The checker constructs \(\operatorname{Cr}_n\) for
\[
3\le n\le6.
\]

It exhausts every labeling
\[
f:V(\operatorname{Cr}_n)\to\{0,1,2\}.
\]
For each labeling it tests the exact Italian condition on every zero vertex and checks that every zero vertex has a zero neighbor.

For \(n=4,5,6\), the complete minimum family is compared with
\[
f(a_i)=f(b_i)=z_i,
\qquad
z\in\{0,1,2\}^n,
\qquad
\sum_i z_i=2.
\]

Recorded output:

```text
VERIFY_OK
n=3: gamma_rI=4, minimum_functions=3
n=4: gamma_rI=4, minimum_functions=10
n=5: gamma_rI=4, minimum_functions=15
n=6: gamma_rI=4, minimum_functions=21
ternary_labelings_checked = 597780
for n=4,5,6 every minimum function was an identical-side vector of side weight 2
```

The checker exhausts \(597{,}780\) ternary labelings. The finite computation is corroborative only; the arbitrary-order theorem follows from the side-weight and matched-zero arguments in the proof.
