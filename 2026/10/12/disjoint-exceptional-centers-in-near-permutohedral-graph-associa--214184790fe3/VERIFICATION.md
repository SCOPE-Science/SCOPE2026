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
# Verification summary

This package contains a self-contained standard-library program `near_permutohedral_checker.py`. Run it with `python3 near_permutohedral_checker.py` on Python 3.8 or later; no third-party modules or network access are needed. Its actual completed checks were:

- All 770 connected labeled simple graphs on \(3\), \(4\), or \(5\) vertices satisfy the exceptional-index antichain criterion exactly when their complement is a matching.
- All 16 graphs on \(3\le n\le7\) vertices obtained by deleting \(0\le r\le\lfloor n/2\rfloor\) disjoint edges have disconnected proper induced subsets precisely equal to those missing edges.
- Exhaustive tubing face enumeration, independent of the blowup formula, gives the \(h\)-vector \(A_n(t)-rtA_{n-2}(t)\), and maximal-tubing counts match its specialization at \(t=1\), in all 16 cases.

For \(n=7\), \(r=3\) the vector is \((1,117,1113,2218,1113,117,1)\), summing to \(4680\). All regressions terminate with `ALL_CHECKS_PASSED`. These are **finite regression checks only**. The all-parameter theorem is justified by the ray-comparability lemma, the explicit quotient star fan, and the integral cohomological blowup formula in `RESULT.md`; no claim of external certification or exhaustive proof-by-enumeration is made.
