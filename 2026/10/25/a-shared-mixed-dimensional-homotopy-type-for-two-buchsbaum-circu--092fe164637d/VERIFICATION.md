---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For each undirected 16-vertex circulant step set (1,2,3,8) and (1,4,7,8), exact face enumeration yields (f0,f1,f2)=(16,64,64). The inspected independent reproducer constructs 63 disjoint acyclic Hasse pairs (144 cells, 320 arrows), leaving critical cells (1,1,16). Its actual signed 49-by-64 triangle presentation has Smith invariant factors 1 repeated 48, so H1 is Z, and the sixteen Morse 2-cell attaching degrees into the one-cell circle all vanish. Thus the claimed integral homotopy wedge follows. Distinct edge-common-neighbor distributions prove graph nonisomorphism. No extrapolation beyond the two named graphs.

## originality

PASS

The exact S^1 wedge sixteen S^2 type and shared type of two nonisomorphic named Buchsbaum circulants is a concrete refinement of the established combinatorial/Buchsbaum classification. The two named graph objects and the chain-level homotopy computation were compared with the primary 2015 graph classification and semantic findings on other circulants and graph independence complexes. No inspected theorem implies these particular homotopy decompositions; the judgment is best of knowledge.

## value

PASS

The two graphs are canonical entries in an existing well-covered Buchsbaum-circulant classification. Their complete mixed-dimensional integral homotopy types, including elimination of possible attaching degrees/torsion and a shared type despite graph nonisomorphism, are genuine topological invariants not mechanically entailed by the known Buchsbaum labels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
