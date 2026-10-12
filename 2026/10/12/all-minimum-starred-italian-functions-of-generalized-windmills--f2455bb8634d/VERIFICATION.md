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
W_{m,r}=K_1\vee mK_r
\]
directly.

For each ternary labeling it verifies the exact Italian condition on every zero vertex and checks that the zero set is not dominating.

The exhaustive cases are
\[
(m,r)\in
\{(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(5,1),(5,2)\}.
\]

For every case the checker computes the minimum weight and the complete set of minimum functions, then compares them with the theorem's predicted family: center label \(2\), exactly one whole blade labeled \(1\), and every other outer vertex labeled \(0\).

Recorded output:

```text
VERIFY_OK
m=3, r=1: gamma_star_I=3, minimum_functions=3
m=3, r=2: gamma_star_I=4, minimum_functions=3
m=3, r=3: gamma_star_I=5, minimum_functions=3
m=3, r=4: gamma_star_I=6, minimum_functions=3
m=4, r=1: gamma_star_I=3, minimum_functions=4
m=4, r=2: gamma_star_I=4, minimum_functions=4
m=4, r=3: gamma_star_I=5, minimum_functions=4
m=5, r=1: gamma_star_I=3, minimum_functions=5
m=5, r=2: gamma_star_I=4, minimum_functions=5
ternary_labelings_checked = 3447765
parameter_cases_checked = 9
all minimum functions matched: center label 2 plus one whole blade labeled 1
```

The checker exhausts \(3{,}447{,}765\) ternary labelings across nine parameter pairs. The computation is exhaustive for those cases and corroborative only for the arbitrary-parameter theorem, whose proof is symbolic.
