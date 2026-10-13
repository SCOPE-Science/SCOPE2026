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

The checker constructs the half graph \\(H_n\\) with edges \\(a_i b_j\\) exactly when \\(i\\le j\\). It tests the perfect Italian condition directly: every vertex labeled \\(0\\) must see total neighbor label exactly \\(2\\).

For each \\(2\\le n\\le14\\), the checker exhausts all labelings in increasing total weight until the first feasible weight. Thus for every tested \\(n\\ge4\\) it exhaustively rules out weights below \\(4\\) and checks every weight-
\\(4\\) candidate.

Recorded output:

```text
VERIFY_OK
n=2: gamma_p_I=3, minimum_functions=2
n=3: gamma_p_I=4, minimum_functions=2
n=4: gamma_p_I=4, minimum_functions=1
n=5: gamma_p_I=4, minimum_functions=1
n=6: gamma_p_I=4, minimum_functions=1
n=7: gamma_p_I=4, minimum_functions=1
n=8: gamma_p_I=4, minimum_functions=1
n=9: gamma_p_I=4, minimum_functions=1
n=10: gamma_p_I=4, minimum_functions=1
n=11: gamma_p_I=4, minimum_functions=1
n=12: gamma_p_I=4, minimum_functions=1
n=13: gamma_p_I=4, minimum_functions=1
n=14: gamma_p_I=4, minimum_functions=1
bounded_labelings_checked = 123949
for every n>=4 the unique minimum labels a_1 and b_n by 2
```

The checker examines \\(123{,}949\\) bounded-weight labelings. It confirms the two small boundary cases and the unique optimum for every tested \\(n\\ge4\\). The computation is corroborative; the theorem for arbitrary \\(n\\) follows from the symbolic prefix-suffix proof.
