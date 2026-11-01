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

# Reproducible exact-rational verification

Run the included file using standard Python 3:

```sh
python verify_weighted_wheel_spread.py
```

Actual output:

```text
EXACT_FOUR_LEVEL_EXTREME_CONFIGURATIONS_OK 45 218571 774
EXACT_ONE_SIGN_AND_EXTRA_INTERFACE_DOMINANCE_OK 243
EXACT_PARITY_AND_SHARP_CORNER_JUMPS_OK 97
ALL_WEIGHTED_WHEEL_SPREAD_CHECKS_OK
```

The first stage examines 218571 feasible labelled configurations for 45 rational parameter settings, including the two limiting spoke lengths, and verifies the exact optimal value and all enumerated equality cases. The second evaluates the one-extreme-sign and additional-bridge competitors for \(4\le n\le30\). The third tests the exact parity, limiting endpoint, and derivative-jump identities for \(4\le n\le100\).

The finite test does not prove that every feasible real assignment is among the enumerated levels; the tight-component lemma in `RESULT.md` supplies that reduction for \(1/2<t<1\). The proof's strict inequalities and endpoint logic, not the program, establish all real-parameter quantifiers. No external mathematical audit has been conducted.
