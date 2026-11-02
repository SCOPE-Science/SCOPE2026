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

Run `python3 verify.py` from this package with Python's standard library. The checker enumerates every permutation on \(4\le n\le8\), exactly \(46{,}224\) permutations across the five sizes, and evaluates Ewens weights at \(\theta\in\{\tfrac12,1,2,3\}\) with rational arithmetic. It checks the four shape probabilities at every consecutive start and the four fixedpoint-shape covariances for every outside location, passing \(1{,}720\) exact assertions.

Separately checked by exact finite injection counting: the coefficient tables for increasing and peak patterns for every \(4\le n\le10\) and every triple start. Symbolic cancellation of the displayed probabilities into covariance numerators was checked algebraically. The unrestricted statement relies on the proved partial-cycle contraction and cycle-table enumeration, not on finite enumeration. No independent external audit has been performed.
