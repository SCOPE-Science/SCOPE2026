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

# Verification of the circular-palindrome classification

Execute `python3 checker.py` with Python 3. No dependency other than the standard library is used. The program enumerates all distinct palindromic cyclic factors of each specified test word directly from the doubled string. It does not use the factor-family classification when generating these test values. Separate routines compute the theorem's closed-form predictions.

Observed check output:

```
PASS: direct distinct-palindrome comparisons: 1510
PASS: exact necklace and labeled-word distributions: 44
PASS: exact first/second moments: 44
PASS: all stated formulas and parity boundaries.
```

Coverage: every ordered nonnegative gap pair at length 2 through 55 (1,485 cases), 25 longer boundary samples at lengths 57, 88, 139, 200, and 301, and every labeled two-one word and unordered gap pair at lengths 2 through 45. Exact moments use `fractions.Fraction`.

Finite checks are corroboration only. The all-length result is proved by the explicit partition into zero-, one-, and two-marker palindromes, the equal-gap overlap correction, and rotation-orbit counting, as laid out in `RESULT.md`. No independent external proof check or certification has been performed. The primary 2014 article's full text was not accessible for a definitive historical-priority comparison.
