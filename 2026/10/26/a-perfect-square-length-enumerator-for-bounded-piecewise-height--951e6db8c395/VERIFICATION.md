---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Used the published right/left insertion-distance recurrence (including singleton internal runs) to reconstruct the four-run exact height h=max{a+min(c,2)+1,b+2,c+2,d+min(b,2)+1}. Independently reimplemented the side-distance recurrence, not the packaged verifier, and exhaustively checked all 1296 tuples (a,b,c,d) with entries 1..6. The expression separates into max(g(a,c),g(d,b)), where g(x,y)=max(x+min(y,2)+1,y+2). For threshold H>=3 admissible pairs split disjointly as y=1,1<=x<=H-2 and 2<=y<=H-2,1<=x<=H-3, giving pair enumerator P_H=z S_(H-2)+S_(H-3) T_(H-2). Independence yields the complete four-run polynomial P_H^2, total (H^2-5H+7)^2; threshold H=3 has only 0101, and the exact height H>=4 enumerator is P_H^2-P_(H-1)^2. An independent combinatorial polynomial enumeration checked H=3..11. The full all-positive-run conclusion is from the analytic distance recurrence and disjoint pair parametrization, not the finite tests.

## originality

PASS

Best-of-knowledge originality of the precise final mathematical claim, not novelty of standard premises or algorithms: The four-run height formula is essentially a specialization of published run-block algorithms and is NOT claimed as original. The assessed assertion is the cumulative all-length polynomial and square-product count over all positive run lengths. Checked relevant primary statements and Resultary semantic results. Failed searches alone are not novelty proof; risks explicitly retained.

## value

PASS

The complete length-height distribution for a natural four-alternation word family is a precise combinatorial enumerator, rather than just an individual word decision procedure or maximal length. Its perfect-square factorization exposes an exact decoupling of opposite-run constraints and accommodates singleton interior runs. It is a relatively compact, non-landmark consequence of prior methods, but the exact all-length polynomial and cumulative cardinality can directly serve classification and word-combinatorics calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
