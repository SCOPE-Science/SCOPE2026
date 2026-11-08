---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Pointed one-move profiles are classified: empty matching has only equal/up; maximal matching has equal/down/incomparable for n>=3; nonempty nonmaximal matchings for n>=4 have all four relation categories. Every non-maximal X has at least two unmatched vertices, with exactly binomial(n-2|X|,2) strict single-edge extensions; but the number of ALL strict upper matchings is one precisely when exactly two vertices are unmatched, since with >=3 vertices at least three distinct upper edge extensions exist. n-2|X|=2 can occur only for even n, realized by matching of size (n-2)/2. Independent combinatorial checks across n=2..11 corroborate boundary. The EF rank-two type recurrence establishes optimality for parity, though the theorem does not claim complete rank-three theories.

## originality

PASS

Shareshian–Wachs define matching complexes and prove topology/homology results (including torsion); their inspected abstract/introduction contain no finite-model-theoretic parity expressibility theorem. General EF-game methods do not immediately count unique matching extensions. Resultary matches concerned topology and discrete Morse facts, not this precise logical parity threshold. The short witness may occur implicitly in older finite-poset logic examples.

## value

PASS

A sharp definability jump for a canonical family of matching face posets is a meaningful structural logic/combinatorics fact; it pinpoints parity as visible with three nested quantifiers despite two-round collapse for all n>=4, without claiming full rank-three equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
