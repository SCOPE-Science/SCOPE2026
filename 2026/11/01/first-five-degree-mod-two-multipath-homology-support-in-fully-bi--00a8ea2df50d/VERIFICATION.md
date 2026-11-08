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

PASS: The claimed finite domain is exactly simple wheels C_r*K_1 for 3≤r≤10 with both orientations of each undirected edge, no loops and F2 reduced simplicial homology. A face is exactly an indegree/outdegree ≤1 acyclic selected arc subset: directed paths cannot branch or cycle; conversely such a finite directed graph decomposes into disjoint directed paths. The source checker uses complete inclusion/exclusion through all 4r arc labels and an independent orientation of undirected degree≤2 acyclic path forests; both enumerate all faces. A freshly written independent third implementation used undirected path-forest union-find enumeration and consistent two-way orientations, then formed every simplicial boundary column and reduced by exact bitwise F2 Gaussian elimination for each r=3..10. All face counts, chain dimensions, ranks, connectedness and Euler–Poincaré identities matched the source log and claims; at r=10: 220395 faces including empty, chain dimensions (40,610,4660,19720,47964,67160,52900,22360,4620,360), positive boundary ranks (39,571,4089,15631,32333,34778,18082,4238,340). β_d=dim C_d−rank ∂_d−rank ∂_{d+1}, with β_0=1, yields reduced F2 ranks 49,40,40,42,20 at degrees 5..9 and zero elsewhere. Previous seven r have at most four nonzero reduced degrees. These are exhaustive finite computations within the declared domain, not extrapolations to r>10, integral torsion or homotopy.

## originality

PASS

Qualified best-of-knowledge PASS. Actual primary literature and published mathematical results were compared by definitions and theorem implications, not titles. Known bidirectional-polygon homology treats a rim lacking the hub; the all-parameter bidirected double-star theorem concerns trees; same-wheel discrete-Morse results compute a different complex; general cone/quiver statements do not give the F2 ranks. The known top-degree wheel rank 2r is not claimed as new. The exact eight-wheel F2 table and first five-support threshold have not been found already stated or implied. Unindexed equivalent computations remain a real risk, not an automatic failure.

## value

PASS

PASS: The wheel C_r*K_1 is the canonical first hub augmentation of a polygon, and the multipath complex measures topology of disjoint directed path selections. The exact eight-case homology census, including the first case with five separate nonzero degrees, supplies reproducible and potentially useful benchmark data for understanding spoke-induced homology; its four lower ranks at r=10 are not mechanically determined by the known top-rank theorem or the polygon result. The full 220395-face computation is substantial, not a tiny check. This is a motivated finite cutoff for a natural family, without falsely asserting an all-wheel classification, infinite monotonicity, integral torsion or a new top-rank result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
