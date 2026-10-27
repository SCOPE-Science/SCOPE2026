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

# Verification protocol and scientific limits

Run `python3 verify.py` with any standard Python 3 interpreter in the same directory. No external packages or data files are required. The program explicitly forms and checks each candidate binary activity profile for every \(m\)-by-\(n\) rook network satisfying \(m,n\ge2\) and \(mn\le16\) (\(19\) boards, \(314{,}512\) profiles). It separately computes finite-field ranks by bitwise elimination for the \(81\) boards with \(2\le m,n\le10\), then compares the nullity-predicted number of solutions to the stated producer-count polynomial. It checks all claimed minimum-count multiplicities and the exact \(3\)-by-\(5\) distribution.

Observed stdout:

```
VERIFY_OK parameter_cases=81 fully_enumerated_boards=19 profiles_tested=314512
RECTANGLE_3x5 {3: 5, 5: 3, 7: 30, 9: 25, 15: 1}
```

These checks verify implementation consistency and finite instances only. The result for all \(m,n\ge2\) follows instead from the necessary-and-sufficient row/column parity parametrization in the proof. Literature comparison covers the named game-theoretic, graph-theoretic, and switching-matrix sources; it cannot eliminate every unindexed equivalent enumerator. Independent audit has not been performed.
