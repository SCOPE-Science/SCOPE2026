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

# Verification of complete-bipartite three-color dynamics

The analytic all-size proof reduces every initial configuration to one of at most 49 potential pairs of nonempty color supports. The explicit excitation-triggered color transition is deterministic for each support pair, even for arbitrarily large graph parts. The 7-by-7 table in `RESULT.md` is an exhaustive finite logical certificate for this reduction; the recurrence from any pair is eventually one of three closed support classes. All actual configurations in those classes have microperiod 1, 3, or 4, respectively. Direct onto-color support weights then produce the ten displayed counts and sum to \(3^{a+b}\). No inference from finite graph-size experiments is needed.

The standalone `verify.py` independently implements the original vertex-level update rule and 49-case macro update, recomputes the macro orbit types, checks the ten closed-form counts by support-weight inclusion–exclusion, exhaustively enumerates all 72,720 labelled initial configurations for positive part sizes each at most five and combined size at most nine, and compares 3,000 seeded larger configurations. Replay by running `python3 verify.py` from the directory containing this file. The observed output was:

```
VERIFY_OK macro_pairs=49 exhaustive_states=72720 random_states=3000 support_table_and_all_formulas=verified
```

The finite computer checks are independent corroboration of the exact support certificate, not an all-size brute-force enumeration. All result limitations and historical-priority risks are specified in `RESULT.md` and `REVIEW.md`. No independent mathematical audit has been performed.
