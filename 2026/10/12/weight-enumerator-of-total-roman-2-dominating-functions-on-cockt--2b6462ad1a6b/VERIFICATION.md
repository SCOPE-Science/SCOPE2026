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
CP_n=K_{2n}-nK_2
\]
by deleting \(n\) partner edges from the complete graph.

For every labeling
\[
f:V(CP_n)\to\{0,1,2\},
\]
it checks the definition directly: every zero vertex must have open-neighborhood label sum at least \(2\), and every positive vertex must have a positive neighbor.

For
\[
2\le n\le5,
\]
the checker exhausts all
\[
3^{2n}
\]
labelings, forms the complete weight distribution, and compares every coefficient against the closed formula. It also checks the minimum weight and the complete set of minimum functions.

Recorded output:

```text
VERIFY_OK
n=2: gamma_tI=3, minimum_functions=4, total_functions=52
n=3: gamma_tI=3, minimum_functions=20, total_functions=668
n=4: gamma_tI=3, minimum_functions=56, total_functions=6456
n=5: gamma_tI=3, minimum_functions=120, total_functions=58888
labelings_checked = 66420
all coefficients matched the closed weight enumerator
```

The computation checks \(66{,}420\) labelings in total. It is exhaustive for the tested orders but finite; the arbitrary-order result follows from the support classification and low-weight correction proof.
