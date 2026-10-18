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

# Reproducibility and validation

The source file `verify.c` is complete, portable C11. Run `cc -O3 -std=c11 -Wall -Wextra verify.c -o verify && ./verify` in the directory containing the extracted file. It performs independent coefficient-ring multiplication and brute-force testing of the original matrix-square equation over \(\mathbb F_2\) and \(\mathbb F_3\), not a replay of the intermediate fiber formulas. It also independently enumerates the anticommuting-pair base problem over prime fields of orders two, three, five and seven.

Actual execution output:

```
FULL q=2: observed=1600 expected=1600
FULL q=3: observed=39609 expected=39609
ANTI q=2: observed=88 expected=88
ANTI q=3: observed=417 expected=417
ANTI q=5: observed=4705 expected=4705
ANTI q=7: observed=23233 expected=23233
VERIFY_OK
```

This checks the formulas only for the listed prime fields. Generality over arbitrary fields and finite extensions comes from the displayed proof by locally trivial strata and constant-rank kernels. The source contains no external dependencies. Independent review has not been performed.
