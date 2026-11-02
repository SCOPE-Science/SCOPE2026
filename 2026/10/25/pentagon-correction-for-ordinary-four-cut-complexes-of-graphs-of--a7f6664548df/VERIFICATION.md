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

PASS. The Alexander dual face test is that each induced four-set is connected; full 2-skeleton, tree tetrahedra, pentagon 4-simplices and no larger simplices follow from forbidding C3 and C4. Private triangle rows for star/path tetrahedra, plus incidence C5 blocks for the five tetrahedra of each pentagon, yield a full-rank unimodular minor in d3 of rank c4-c5. Distinct pentagons have disjoint 4-path supports, d4 has primitive image of rank c5, and ker d3/im d4=0 integrally. H2 is free of rank choose(n-1,3)-c4+c5, D simply connected and Hurewicz-Whitehead gives wedge of S2; Alexander duality shifts the degree to n-5. Independently generated qualifying 4- and 5-faces, verified no qualifying 6-faces and checked mod-2 boundary rank for C8, C10, C5+three isolates and two disjoint C5 (rank examples (8,8,0,27), (10,10,0,74), (8,5,1,31), (10,10,2,76)); inspected repository script also supplies Petersen/dodecahedron cases. No claim on original complex homotopy type or girth<5.

## originality

PASS

PASS best-of-knowledge. A previously published high-girth theorem applies to girth >=6 for k=4, precisely excluding pentagons, whereas these graphs allow induced C5 and produce a new +c5 integral correction. Foundational Bayer et al cut-complex papers give definitions, general methods and other families; neither inspected full article states arbitrary girth-5 four-cut dual wedge classification. Petersen rank 26 is previously tabulated and explicitly not novelty. Search incompleteness remains a risk.

## value

PASS

PASS. The first excluded girth boundary of the known high-girth theorem is a natural structural gap. The contribution is an all-graph correction formula with unit-integral chain ranks and full dual homotopy classification, not merely a tiny finite-table calculation; c5 detects exactly the new potential d4 faces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
