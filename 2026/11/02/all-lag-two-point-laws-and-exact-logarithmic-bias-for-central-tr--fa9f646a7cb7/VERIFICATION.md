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

# Reproducibility and limits

The included `verify_trinomial_5.py` is self-contained Python 3 code using only the standard library. Running `python3 verify_trinomial_5.py` checks 4,097 integer recurrence values against the base-five digit product; all sixteen adjacent-pair counts through \(k=12\) by a separate dynamic program; rational lag laws through \(h=72\); a complete block of 15,625 indices for each of 39 lags; and direct enumeration through \(k=6\). It prints:

`VERIFY_OK integer_terms=4097 exact_pair_levels=12 ratio_lags=39 ratio_block=15625 direct_pair_levels=6`

No proof relies on the checked finite bounds. Infinite assertions follow from the exact constant-term, digit-carry and character arguments in `RESULT.md`. The code is not an independent scientific audit.
