---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The king graph is P5 ⊠ P5 (adjacent in Chebyshev distance ≤1). Independently enumerated 6427 faces including empty, using compatible row masks; recovered f-vector in dimensions 0..6 (25,228,964,1987,1974,978,242). A fresh 25-pivot matching yields 3174 pairs, with all 79 remaining critical positive-dimensional faces maximal: counts 45 in dimension three, 32 in four, 2 in five. Global directed Hasse acyclicity was verified on 6426 nonempty faces and 28953 incidences, and actual Morse differentials d4 (45x32), d5 (32x2) independently calculated zero. Independent integral critical-cycle lifts and chain projections then computed the signed D4 actions in each degree. Traces for identity, quarter-turn, half-turn, horizontal axis and diagonal agree respectively with χ3=(45,-1,5,3,-3), χ4=(32,0,0,4,0), χ5=(2,0,-2,0,0). Signed simplicial Lefschetz checks for every symmetry corroborate the graded action; rational dihedral character inner products yield the exact irreducible decompositions. The complete integral groups are free in degrees 3,4,5 of ranks 45,32,2.

## originality

PASS

The specific surviving result is not covered by the inspected same-object antecedents or dominating theorem hypotheses; every comparison below identifies what previous results actually imply. This is best-of-knowledge, not proof of absolute novelty.

## value

PASS

The 5x5 king-board nonattacking-placement complex is a canonical small graph-product example. Its full graded representation under board symmetries is a natural, not previously implied, invariant refining the known nonequivariant wedge decomposition; the faithful two-dimensional top homology and differing reflection traces provide exact symmetry information useful for equivariant computations. This is a motivated complete finite classification, not a claim about all board sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
