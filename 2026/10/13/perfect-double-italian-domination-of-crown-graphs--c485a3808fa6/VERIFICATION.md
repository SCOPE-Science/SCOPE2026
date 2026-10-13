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

The checker uses the defining condition directly. For a labeling of
\[
\operatorname{Cr}_n
\]
it evaluates the closed-neighborhood weight at every vertex labeled \(0\) or \(1\) and requires that weight to lie in
\[
\{3,4\}.
\]

For every
\[
4\le n\le10,
\]
it exhausts every labeling of total weight below \(6\) and verifies that none is feasible. It then exhausts every labeling of weight exactly \(6\) and checks that the complete feasible family is precisely
\[
f(a_i)=f(b_i)=z_i,
\qquad
\sum_i z_i=3.
\]

Recorded output:

```text
VERIFY_OK
n=4: gamma_p_dI=6, minimum_functions=20
n=5: gamma_p_dI=6, minimum_functions=35
n=6: gamma_p_dI=6, minimum_functions=56
n=7: gamma_p_dI=6, minimum_functions=84
n=8: gamma_p_dI=6, minimum_functions=120
n=9: gamma_p_dI=6, minimum_functions=165
n=10: gamma_p_dI=6, minimum_functions=220
bounded_labelings_checked = 493494
minimum_functions_checked = 700
all minima matched identical side-vectors of side weight 3
```

The finite computation is exhaustive for all labelings relevant to the claimed minimum and minimum-function classification in the tested orders. It does not enumerate higher-weight feasible functions. The arbitrary-order theorem follows from the side-sum proof.
