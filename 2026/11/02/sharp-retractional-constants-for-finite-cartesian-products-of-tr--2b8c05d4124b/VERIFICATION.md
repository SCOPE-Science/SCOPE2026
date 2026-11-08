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

For d>=1 nontrivial finite unit-edge trees, product shortest-path metric, arbitrary roots, commuting prefix retractions have exact optimum 1 for one or two factors and 2 for three or more. For one factor parent folds are nonexpansive. For two factors, lex parent-before-descendant order and simultaneous coordinate-parent predecessor make each one-point fold nonexpansive on prior prefix: when earlier first coordinate differs it is outside current descendant subtree so first coordinate distance drops by one, compensating second coordinate; within same first row the second-coordinate parent distance drops. For d>=3 recursive row-prefix maps use ancestral projections π_Q in the first factor, change by at most one in that coordinate when second-factor membership changes, making graph-edge output distance<=2. Nested one-point fold compositions commute. For lower bound, any last vertex v has three neighbors in distinct factors whose closed radius-one balls intersect only at v; penultimate retraction must move v but fix its neighbors, so integer Lipschitz <2 is impossible. The result is about retractional free-space projections, not arbitrary Banach bases.

## originality

PASS

General free-space retractional bases of Hájek–Medina, finite-graph obstruction results of Novotný, and median metric graph retractions are relevant, but no inspected theorem yields the exact d<=2 versus d>=3 threshold for arbitrary unit-edge tree products. The previously studied binary-Hamming cube is a special case and does not imply the arbitrary branching path/tree extension. Older median graph folding literature could encode equivalent 1-Lipschitz filtrations.

## value

PASS

An exact classification of the minimal commutative retractional basis constant on a natural fundamental family of graph metrics, identifying a sharp two-to-three-factor obstruction with explicit construction for arbitrary branching finite trees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
