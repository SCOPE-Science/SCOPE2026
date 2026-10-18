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

# Reproduction and verification

Run `python3 verify_three_marker.py` using Python 3.10 or newer. The script uses only standard-library features and reads no input files or network resources.

The script enumerates each triple of distinct positions in length-\(n\) binary words for every \(3\leq n\leq30\), independently computes their complete scattered-subsequence profiles of lengths one through three by a dynamic program, and groups positions by the resulting tuple. It checks the maximum class size, all proposed explicit partners and the number of doubletons and equivalence classes. It separately verifies the rational-generating-function coefficient formula through length 1000.

Observed output ended in `VERIFY_OK`, including the checks:

```
N 7 WORDS 35 DOUBLETONS 1 CLASSES 34
N 8 WORDS 56 DOUBLETONS 2 CLASSES 54
N 12 WORDS 220 DOUBLETONS 14 CLASSES 206
N 20 WORDS 1140 DOUBLETONS 100 CLASSES 1040
N 30 WORDS 4060 DOUBLETONS 406 CLASSES 3654
VERIFY_OK
```

The finite experiment checks the implementation and detects small counterexamples; it does not prove the theorem for all lengths. The infinite classification, count and limiting density are derived in `RESULT.md` from exact algebraic identities and the resulting generating function.

Independent audit: not performed.
