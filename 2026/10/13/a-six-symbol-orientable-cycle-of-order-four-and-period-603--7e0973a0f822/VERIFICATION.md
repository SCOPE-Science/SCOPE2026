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

The mathematical claim is a finite existence assertion. With `verify.py` and `witness.txt` in the same directory, run `python3 verify.py`. The script independently assembles every cyclic four-letter window, compares all 363609 ordered window-reversal pairs, checks that no window is palindromic, checks the reverse-direction windows and distinctness, and rules out shorter periods. Only the Python standard library is needed.

Expected exact output:

```
VERIFY_OK period=603 distinct_four_windows=603 distinct_reverse_windows=603 partitioned_words=1242 omitted_reversal_pairs=27
```

The checks establish only the existence of a 603-symbol orientable order-four cyclic word. They do not enumerate every possible sequence or prove optimality beyond the witness. The published universal bound 612 remains external to this certificate.
