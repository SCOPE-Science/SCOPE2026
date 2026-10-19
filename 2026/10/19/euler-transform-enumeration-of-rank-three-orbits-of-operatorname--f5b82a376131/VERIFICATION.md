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

# Verification record

## Actual executable checks
From a directory containing `CHECKER.py`, run `python3 CHECKER.py`. The script independently enumerates every map \(t\) and idempotent \(e\), filters the equations \(t^3=t\) and \(te=et=e^2=e\), enumerates permutation-conjugacy classes directly, and compares the results with the formal Euler products. Exhaustive agreement was obtained for \(1\le n\le5\); the checker computes the infinite-formula coefficients through degree thirteen.

Observed exhaustive triples of (labeled pairs, conjugacy orbits, rank-three orbits) are `(1,1,0)`, `(5,3,0)`, `(34,8,1)`, `(297,21,4)`, `(3106,52,15)` in increasing order of \(n\). The rank-three coefficient list starting at degree zero is `0,0,0,1,4,15,46,133,362,951,2419,6002,14591,34833`.

## Logical verification and limits
The standalone argument in RESULT.md proves the bijection between compatible pairs and nested unlabeled multisets and proves the Euler-transform identity coefficientwise for all finite sizes; the checker tests the bijection's enumerative consequences only for its stated finite range. The classification of compatible pairs as rank-three endomorphisms and of rank-three orbits as essential for \(n\ge5\) is established in Gould–Grau–Johnson, Theorem 2.1 and Proposition 4.2, not independently rederived here. No assertion about the complete minimum generator number or its asymptotic is made. No independent audit has been performed.
