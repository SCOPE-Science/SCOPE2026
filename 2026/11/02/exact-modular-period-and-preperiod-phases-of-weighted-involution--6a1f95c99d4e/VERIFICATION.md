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

# Verification record

Run the standalone `verify.py` with Python 3 and no external dependencies. It constructs the recurrence modulo every tested modulus without calling the proof's shift representation, checks the proposed preperiod and least period, tests exact dyadic valuations at many translated indices, and tests deeper dyadic layers.

Recorded checks:

```
GENERAL_GRID_OK 12691 c -24..24 moduli 2..260
SHIFT_PHASE_OK 28800 checks, exceptions handled
DYADIC_LAYERS_OK 252 cases up to 4096
```

The checks are finite. The theorem's infinite correctness depends on the explicit prime-power binomial valuation estimates, the independent recurrence-minimality argument, the two-term dyadic cancellation, and the odd-weight induction in RESULT.md. Historical priority cannot be proved by finite checks; uninspected specialized sources remain possible. No independent mathematical audit has been performed.
