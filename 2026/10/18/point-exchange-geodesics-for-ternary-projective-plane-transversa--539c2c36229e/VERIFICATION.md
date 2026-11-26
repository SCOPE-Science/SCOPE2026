---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A Johnson step can increase intersection with a fixed target by at most one. Therefore the all-pairs target-directed move test in the supplied proof is sufficient by induction. An independent exhaustive check constructs PG(2,3) using powers of a norm-one generator g of F_27 defined by g^3=g+1. The powers give one representative of every projective point, and the 13 translates of a two-dimensional subspace give all projective lines. The check enumerates complements that contain no line, constructs the exchange edges by pairwise symmetric difference, and runs BFS from every feasible vertex, rather than using the supplied targeted-exchange algorithm. All 3,995,862 distinct ordered pairs at k=6 through 13 have distance half the symmetric difference size. The full transversal census, radius–diameter pairs and k=6 degree and eccentricity classes agree; the 234 no-whole-line sets are exactly the nonvertex points on triangle sides. At k=5 the 13 components each have size nine and every vertex has degree eight; at k=4 the only vertices are the 13 lines and there are no edges; smaller levels are empty. The statement applies to transversals containing a line as well as those containing none.

## originality

PASS

The distinct claim is Johnson isometry for the full line-hitting families across every level k=6 through 13, together with the sharp threshold and exact metric census. The minimum and static classification of blocking sets are not new. The strongest available related exchange theorem treats only the induced class without whole lines, and the general graph-independent-set theorems do not model the hypergraph constraint.

## value

PASS

The thirteen-point plane is a natural symmetric hypergraph for exact constrained exchange. The result identifies a sharp jump from 13 disconnected cliques to a family with no shortest-path detours at any higher level. Exact degrees and eccentricities distinguish the two geometrically meaningful classes at the transition. This is an all-pairs metric fact not supplied by the static counts or implied by ordinary matroid exchange, and provides a benchmark for geometric hitting-set reconfiguration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
