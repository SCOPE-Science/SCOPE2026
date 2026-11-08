---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For each selected rook vertex (i,j) the induced degree is d_i+e_j-2; equality/opposition of row and column parities therefore characterizes even/odd degrees. Each binary incidence matrix has unique parity-class sets, leaving two disjoint admissible rectangles with prescribed mod-two margins. The sign-character projection proves B_ab even for zero-sized sides. The two-row dichotomy between one full column and only single cells gives the displayed closed forms, including the empty set in both. I independently enumerated actual graph induced degrees for boards (1,1),(1,3),(2,1..5),(3,3),(3,4) and matched the polynomial/structural predictions; the general theorem is symbolic, not inferred from these tests.

## originality

PASS

The line-graph equivalence and roots-of-unity margin filter are standard. Belmonte–Sau treats largest odd induced subgraphs and complexity, not cardinality-generating polynomials for the rectangular rook family; the additional complete-prism support/residue classification is not a consequence of the cited optimizing bounds. No equivalent full family was found in Resultary or the searched published-record index; this is qualified priority, not a novelty certificate.

## value

PASS

Complete coefficientwise enumerators for a natural highly symmetric graph family determine exactly which induced even/odd-degree subgraph sizes are possible. Complete prisms exhibit unbounded missing even cardinalities above n and binomial exact multiplicities, a substantive distinction from merely determining maximum sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
