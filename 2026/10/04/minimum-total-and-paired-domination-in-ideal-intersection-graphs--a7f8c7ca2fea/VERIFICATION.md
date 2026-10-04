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

The standalone `verify.py` artifact was inspected at its packaged path before replay.

The first layer constructs the graph directly from local nilpotency lengths, using exponent vectors for ideals and active-support intersection for adjacency. It exhaustively checks every two-vertex subset against the literal total-domination definition, verifies that exactly the support-intersection/full-union pairs qualify, checks the three existence obstructions, and compares the number of qualifying pairs with the closed formula.

The second layer independently constructs ideal-intersection graphs of \(\mathbb Z/n\mathbb Z\) from divisors. Ideals are represented by divisors \(d\mid n\), and two nonzero proper ideals intersect nontrivially exactly when their least common multiple is less than \(n\). Every composite \(4\le n\le120\) is checked against the prime-exponent specialization.

Tail of the exact replay output:

```text
Z/108Z exponents=(2, 3) vertices=10 min_pairs=35
Z/110Z exponents=(1, 1, 1) vertices=6 min_pairs=3
Z/111Z exponents=(1, 1) vertices=2 min_pairs=0
Z/112Z exponents=(4, 1) vertices=8 min_pairs=18
Z/114Z exponents=(1, 1, 1) vertices=6 min_pairs=3
Z/115Z exponents=(1, 1) vertices=2 min_pairs=0
Z/116Z exponents=(2, 1) vertices=4 min_pairs=3
Z/117Z exponents=(2, 1) vertices=4 min_pairs=3
Z/118Z exponents=(1, 1) vertices=2 min_pairs=0
Z/119Z exponents=(1, 1) vertices=2 min_pairs=0
Z/120Z exponents=(3, 1, 1) vertices=14 min_pairs=40
VERIFY_OK
```

These finite tests are corroborative. The arbitrary-ring theorem follows from the chain-ring ideal decomposition, the singleton-support witness argument, and the exact ordered-pair count in `RESULT.md`.
