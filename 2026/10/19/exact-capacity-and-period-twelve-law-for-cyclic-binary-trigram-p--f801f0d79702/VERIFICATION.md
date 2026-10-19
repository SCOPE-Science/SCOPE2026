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

The accompanying `verify.py` is a standalone Python 3 checker with no external dependencies. Run `python3 verify.py` in the directory containing this file. The checker directly enumerates binary words for lengths 1 through 18, independently inspects all nonnegative eight-component cyclic count vectors for totals 1 through 11 by graph traversal, and compares direct parameter counting with rational-series coefficients for lengths 1 through 60.

Observed output:

```
CYCLIC_BINARY_TRIGRAM_PASS complete_word_lengths=1..18 structural_euler_lengths=1..11 parametric_gf_lengths=1..60 direct_words= 524286 first_ten= [2, 3, 4, 6, 8, 13, 18, 27, 38, 53]
```

These checks test finite consequences of the mathematical argument. The all-length claim, least period, and asymptotic leading term require and receive the symbolic Eulerian and generating-function proof in `RESULT.md`; exhaustive checks of finite lengths alone cannot prove them. No independent audit has been performed.
