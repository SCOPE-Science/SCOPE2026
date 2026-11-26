---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Global laminarity passes to restrictions; conversely a nonlaminar intersecting pair has a finite witness consisting of one point in its intersection and one in each difference. For a restricted fibre S of intermediate size, containing, properly contained and disjoint fibres cover the right side. The source calls these classes a partition, although an empty fibre belongs to both of the last two; the covering pigeonhole argument is sufficient, or the empty fibres can be assigned to just one class. A class of at least one third yields a complete rectangle on S or an empty one on S or its complement. If there is no intermediate fibre, the large fibres form a chain, so a third of the right side in large fibres gives a complete rectangle. Otherwise more than two thirds have small fibres. Their distinct maximal fibres are disjoint, with each small fibre contained in a maximal one. If the union of maximal fibres is smaller than one third of the left side, its complement avoids them all; otherwise take maximal fibres until their union first reaches one third, never reaching two thirds. The small fibres are either contained in this union or disjoint from it, so one group exceeds one third of the right side and gives an empty rectangle on a sufficiently large left side. Multiplicities are counted by right indices throughout. In the three-block construction, any right side exceeding one block must see two types; their intersection has at most one block and the complement of their union has at most one block. This rules out every fraction above one third, including for arbitrarily large sides.

## originality

PASS

The distinct claim is the sharp universal fraction 1/3 for all finite restrictions of laminar-fibre relations, not existence of a positive strong Erdős–Hajnal constant. The strongest inspected quantitative predecessor for the same class gives 1/6. The broader methods and structural descriptions inspected did not imply the improved lower bound and matching obstruction.

## value

PASS

This settles the first nontrivial endpoint of a studied hierarchy: it doubles the cited general guarantee specialized to k=2 and shows that even the pure laminar structure cannot force a larger common fraction. The result applies to all relative sizes of the two sides and handles repetitions, so the exact constant is useful both as a baseline for stronger hypotheses and as a limitation of arguments that use laminarity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
