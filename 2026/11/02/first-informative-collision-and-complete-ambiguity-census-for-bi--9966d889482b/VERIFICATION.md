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

Run `python3 verify.py` from the directory containing `COLLISIONS.csv`, using standard Python 3 only. The program computes the complete prefix-tree census for every binary length from seven to seventeen using fourteen exact integer counts. It checks all sixteen length-seventeen doubletons, no higher multiplicities, matching collision CSV, four size-four reversal/complement orbits and every smaller informative length's injectivity.

An independent literal index-combination implementation recomputes each deck for all 1920 binary words of lengths seven to ten and each of the thirty-two words in the sixteen collision pairs. In the performed run, the output begins:

```
VERIFY_OK length_range=7..17 words_at_17=131072 distinct_decks_at_17=131056 doubleton_decks_at_17=16 singleton_decks_at_17=131040 symmetry_orbits=4 independent_short_words=1920
```

It prints eleven additional census lines and four representatives. Numeric vector comparison is exact; no hash-equality or randomized test is used. The recurrence's mathematical validity is proved in `RESULT.md`. These checks establish only the stated finite range and do not constitute independent scientific audit.
