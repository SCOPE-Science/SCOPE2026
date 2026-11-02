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

# Reproducible finite checks

Run the standalone Python program with `python3 verify.py`, in a directory containing the two files `verify.py` and this document. No third-party packages, downloads, optional data or external services are required.

The program enumerates all binary indexed words of lengths \(1\) through \(18\), retains precisely the cyclic `010`-avoiders, reduces each to a canonical rotation, and groups necklaces by the literal cyclic ordered three-gram count vector. It matches every resulting fiber cardinality to the Burnside formula, including the constant-string profiles. It separately verifies the coefficients of both claimed rational generating functions against profile and singleton classifications through \(n=150\), and tests the singleton iff-condition for \(1\le t\le16\), all feasible long-gap counts and \(0\le A,B\le8\).

Actual execution from the assembled package produced:

```
VERIFY_OK literal_indexed_words=524286 literal_n=1..18 matched_profiles=522 generating_functions_n=1..150 singleton_cases_checked=12312
COUNTS [(8, 12, 10), (9, 16, 13), (10, 20, 13), (12, 32, 16), (18, 94, 23), (24, 212, 32), (36, 686, 48)]
```

These are independent finite tests of the specified formulas, not formal verification of the proof and not an exhaustive search over all possible lengths. The proof in `RESULT.md` establishes the all-integer theorems by explicit run decompositions, cyclic Burnside orbit enumeration, complete ambiguity witnesses and rational-function analysis.
