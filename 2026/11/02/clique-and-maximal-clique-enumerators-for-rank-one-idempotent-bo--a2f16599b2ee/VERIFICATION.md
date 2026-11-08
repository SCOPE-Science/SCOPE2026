---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Boolean rectangle multiplication X_AB X_CD is X_AD iff B intersects C, else zero; distinct idempotent rectangles commute exactly when both cross intersections vanish. Coordinate t lies in one of 1+(2^k-1)+(2^k-1)+k=2^(k+1)+k-1 allowed membership types; every label i needs a root coordinate A_i intersect B_i. Inclusion-exclusion over missing roots divided by k! gives c_nk, removing the empty coordinate type gives maximal enumerator. Any unused coordinate supplies a new singleton diagonal, and a commuting extension needs an unused coordinate, proving maximality iff the union covers [n]. Disjoint roots force k<=n and give unique full diagonal clique, omega=chi=n; all 1..n maximal sizes constructed. Independently computed commuting graph by literal Boolean matrices and enumerated all cliques n=1,2,3; counts (1,1),(1,7,1),(1,37,24,1) and maximal (1),(5,1),(19,21,1). n=4 source executable not run independently; all-n follows from coordinate proof.

## originality

PASS

Explicit whole-clique and maximal-clique coefficients and support criterion for nonzero rank-one idempotents are not the same as the previously known commuting graph clique number. General completely 0-simple Rees theorem 5.4 gives omega and a commuting criterion but not a full coefficient count in inspected primary sections. Resultary and mathematical alias searches did not return an exact enumerator. This is best-of-knowledge, not a global novelty proof.

## value

PASS

Natural family of nonzero Boolean rank-one idempotents and its commuting graph. Exact all-size clique generating coefficients and inclusion-maximal size distribution are independent graph invariants needed to study graph clique structure, not an arbitrary parameter slice or renaming. The colorful normal form and support criterion provide reusable combinatorial structure beyond the known clique number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
