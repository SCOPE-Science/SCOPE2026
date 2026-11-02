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

# Reproduction and limitations

With Python 3 and no third-party packages, run `python3 verify.py`. It computes the number of distinct nonnegative multiplicity vectors for every integer in a finite range via independent unbounded-coin dynamic programming and, for smaller inputs, by a top-down recursion with memoization. Counts are truncated at three because only their relations to zero and one are needed. Both algorithms use exact integer arithmetic.

The packaged test returned:

```
VERIFY_OK cases=299 residue_classes=45597 checked_integers=251679 independent_recursive_cases=19 exact_integer=yes
```

This checks plus-family parameters \(1\le a\le150\), minus-family parameters \(2\le a\le150\), all proposed first-double Apéry elements, both genus formulas, all positive uniquely represented integers in the tested ranges, and the maximal integer with at most one representation. Independent recursion agrees for the first 19 parameter/family cases. The tested integer range extends one generator \(b\) beyond the largest proposed first-double threshold in every case.

The exact proof for all parameters is in RESULT.md. The bounded tests alone would not certify the universal quantifier. The published \(p\)-Apéry-to-genus mechanism is separately credited; priority and independent mathematical validation have not been established.
