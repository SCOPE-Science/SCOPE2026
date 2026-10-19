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

The unrestricted theorem is proved in `RESULT.md`; computational checks provide independent finite corroboration only. The source file `verify.py` runs with the Python standard library and needs no external dependencies.

Command: `python verify.py`

Expected observed output:

```text
VERIFY_OK orders=1..8 full_palindromic_profiles_through_three_periods tested_length_levels=1506 independent_palindrome_methods=2 privileged_factor_equality_orders=1..7 distinct_circular_factors_checked=17827 periodic_complexity_formula=True circular_total_formula=True
```

Two palindrome detectors are used: direct comparison of every circular factor against its reversal and expansion around all periodic centers. They agree on complete sets across all specified lengths. The privileged-word detector independently checks the recursive complete-first-return definition. Checks of finite orders \(1\) through \(8\) are not a proof of universal quantification. The paper's two-adic center lemma, its exceptional-seam case, and the richness step supply that proof. No independent scientific audit was performed.
