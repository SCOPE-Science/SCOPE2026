---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproduction

Run the exact embedded programs `python3 check_local.py` and `python3 check_direct.py` using any standard Python 3 installation. Both are dependency-free and have no input files. Their exact stdout outputs are embedded as `check_local.out` and `check_direct.out`.

The local method builds the original adjacency matrices from coordinates, computes all \(48\) edges and every edge-compatibility relation, explicitly verifies every local compatibility neighborhood, reconstructs all maximal induced-matching exchange graphs, and performs breadth-first searches from every rook maximum configuration. Its checks assert \(9\)-regular and triangle-free compatibility for the rook graph, \(8\)-regular compatibility and exactly \(32\) triangles for the Shrikhande graph, and no four-edge induced matching in either graph.

The independent method enumerates all original edge subsets of cardinality \(1,2,3,4\) and tests every endpoint-pair incidence directly, rather than counting compatibility-neighborhood triangles. It separately constructs token-jumping exchange graphs from set intersections.

**Limits:** Neither script examines other strongly regular graphs. All assertions here concern finite objects of size \(16\) and are exhaustively decidable; no random sampling or presumed extrapolation occurs. The scientific originality comparison remains subject to historical source coverage, and the self-review is not an external audit.
