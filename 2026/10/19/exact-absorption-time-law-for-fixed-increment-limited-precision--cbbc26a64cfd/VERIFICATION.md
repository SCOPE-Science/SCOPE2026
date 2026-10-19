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

Execute `python3 verify.py` in the directory containing this file. This self-contained standard-library Python script uses exact `fractions.Fraction` calculations and recomputes guard truncation directly from binary significand geometry. The present run returned:

```
EXACT_CHECKS_PASSED 62496
EXAMPLE: E=0, p=5, r=3, a=1/128, absorbing_power=1, expected_steps=128, variance=896
```

It tests 62,496 statewise transitions across positive and negative exponent shifts, several precisions and random-bit budgets; confirms the terminal state is absorbing; and verifies backward first- and second-moment recurrences. This is finite numerical/combinatorial stress testing in exact arithmetic. The proof in RESULT.md establishes universal claims, including almost-sure absorption and ideal-rounding divergence.

**Unproved extensions:** varying increments, other few-bit SR operators, finite exponent-range overflow/subnormal behavior, and correlated random bits. No independent review is claimed.
