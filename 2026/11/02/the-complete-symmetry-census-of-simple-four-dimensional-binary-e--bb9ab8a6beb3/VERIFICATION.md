---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An isomorphism between perfect algebras has disjoint column supports because products of images of distinct basis elements vanish and the target squares are independent. Since there are four nonempty columns and four coordinates, each support is a singleton; over F2 each nonzero entry is 1. Respect for squares is precisely simultaneous index relabeling. For a singular algebra in this dimension the square span is a proper ideal if nonzero, and zero multiplication has proper ideals. For nonsingular A, a terminal strong component gives a proper ideal if the graph is not strongly connected; otherwise multiplying a nonzero ideal element by a basis vector supplies a square, and multiplying squares propagates along arrows to all four independent squares. For exhaustive replay I generated the ordered bases of F2^4 by extending the row span, not by testing every binary matrix, then tested Boolean transitive closure and removed complete relabeling orbits. This recovers 20,160 invertible matrices, 11,658 qualifying labelled matrices, 516 simple orbits and 392 other perfect orbits. Both group-by-group count vectors and the eight decimal representatives agree. The five fixed counts 11,658,72,62,9,6 give 516 by Burnside. Group order determines the S4 subgroup type here except at order four, where an element of order four distinguishes C4 from V4. The two-transitive action of A4 on ordered pairs has the same diagonal and off-diagonal orbits as S4, so exact A4 cannot occur. In fact the only qualifying S4-invariant matrix is I+J, with all off-diagonal entries 1 and all diagonal entries 0.

## originality

PASS

Pass the joint simplicity and abstract full automorphism-group census in dimension four over F2, not the monomial change-of-basis theorem, the simplicity criterion, the known unrestricted total 908 or the existence of an S4 example by itself. The strongest exact comparisons inspected have different restrictions or different invariants. The current survey presents the arbitrary-field dimension-four simple classification as an open question; this does not establish priority for its finite-field slice, but the inspected material does not cover the table. The earlier nonsimple classification does not include this characteristic or the simple family.

## value

PASS

The field and dimension are a natural bounded classification setting: four basis elements permit distinct commuting and cyclic stabilizers of order four, and the simple locus isolates algebras with no decomposition by a proper ideal. A classification or realization study in this family needs the actual cell counts, not just the maximum or an unrestricted number of orbits. The census supplies all labelled and unlabelled frequencies and explicit representatives, quantifies rigidity, and records a structural obstruction to exact A4. Its value is the previously unaccounted joint exact census, not the use of brute force or the known reductions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
