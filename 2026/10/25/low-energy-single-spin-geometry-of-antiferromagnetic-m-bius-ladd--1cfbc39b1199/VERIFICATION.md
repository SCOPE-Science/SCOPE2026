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

# Verification evidence

`verify.py` uses Python's standard library. It constructs the exact unweighted graph on \(2n\) labeled vertices, evaluates all \(2^{2n}\) spin configurations, and forms all legal one-vertex-flip transitions. Run `python3 verify.py` alongside this file; the final status is `ALL_VERIFY_OK`.

Exhaustive checks were performed for every \(3\le n\le10\). At odd widths \(n=3,5,7,9\), the program verifies two zero-defect states, level-three size \(4n\), level-four size \(n(n+3)\), precisely two \(5n+1\)-vertex components plus \(n(n-3)\) isolated states through four defects, and the existence of a five-defect spin-flip path between ground states. At even widths \(n=4,6,8,10\), it checks ground size \(2n\), level-three size \(4n\), full sublevel connectivity, degree four for every ground state and degree two for every excited state, and exactly two excited intermediates for each of the \(2n\) edges of a connected cycle of ground states.

The finite computations corroborate, but do not prove, the infinite-family results. The proof in `RESULT.md` classifies arbitrary column strings and provides the sharp communication path. No assumption about randomness or a numerical optimizer is needed. Independent mathematical audit has not been performed.
