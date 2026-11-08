---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The complexes consist of *all subfaces of perfect matchings*, not ordinary matching complexes. Rebuilt P3×P_n and C3×P_n on 3n vertices for each even n∈{2,4,6,8}, distinguished transverse open edges from triangular periodic cross-sections, and independently enumerated all perfect matchings and all subfaces. Perfect matching counts open (3,11,41,153), periodic (4,19,91,436); all-face counts including empty open (20,495,12375,309480), periodic (26,817,25769,812758). Independently replayed lexicographic toggle pairings and an oriented full-Hasse topological sort in each case, not simply trusting output logs; every directed Hasse graph was acyclic, with 2,101,259 (open B8) and 5,600,955 (periodic T8) incidences. The remaining augmented Morse critical counts match none at n2, 1 vs 3 in dimension1 at n4, 1 vs 3 in dimension2 at n6, and 2 vs 12 in dimension3 at n8. The augmented empty face is paired, so the associated CW model has one baseline 0-cell and only those critical positive-dimensional cells; it is a point or the claimed wedges of spheres. Purity of facet dimension 3n/2−1 and lower-degree nonzero homology for n≥4 proves nonshellability.

## originality

PASS

PASS best-of-knowledge for a concrete first width-three boundary comparison at a motivated exact cutoff; prior 2-row formula/conjecture do not establish it.

## value

PASS

Boundary sensitivity is a natural topological question for domino/tiling complexes: the same three-row length yields wedge multiplicity 2 vs 12 at n8, and the finite n2,4,6,8 table maps the first nontrivial regimes. These are exact useful fixed-graph invariants supporting the proposed extension to P3 without pretending a uniform formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
