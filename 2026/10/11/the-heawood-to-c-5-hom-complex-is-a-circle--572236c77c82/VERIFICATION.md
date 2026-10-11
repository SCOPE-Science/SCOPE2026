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
# Verification

Run `python3 verify_heawood_c5_hom.py` beside `verification_data.json`.

The replay reconstructs the Fano-plane incidence graph from its modular incidence rule; checks \(14\) vertices, \(21\) edges, cubic degrees, and the unique common-line property for each point pair; exhaustively enumerates all \(3300\) graph homomorphisms to \(C_5\); regenerates the entire \(11340\)-edge recoloring graph; verifies that it is connected; and performs breadth-first search from every recoloring vertex to verify diameter and radius \(35\).

For the representative mapping every point to \(0\) and every line to \(1\), the replay constructs the orientation used in Theorem 5.1 of arXiv:2408.04802 and verifies an explicit topological ordering of all \(14\) source vertices. This proves that the orientation has no directed cycle. The external theorem then identifies the unique Hom-complex component as a circle.

The finite certificate is exhaustive for the stated labeled graph and target. It does not reprove the published universal-cover theorem and does not establish a family statement for other incidence graphs, cages, or cycle targets.
