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

# Executable verification

Run `python3 verify_buckyball_rips.py` with Python 3 standard library. No downloaded mathematical datasets are required. The checker reconstructs the graph by vertex truncation from its icosahedral dart description. It validates all \(802\) simplices at radius two and all \(6462\) simplices at radius three, determines the Morse pairs and checks all \(2100\) and \(25860\) directed incidences for cycles, and eliminates all fundamental-group generators using two-simplex relations.

For each radius \(2\) through \(6\), it enumerates all edges, triangles and tetrahedra, computes complete mod-two boundary ranks, confirms the Euler/betti identities, and tests the explicit \(116\)-triangle polyhedral surface cycle for being a nonboundary (radii two to five) or a boundary (radius six). The included `verification_output.txt` is an actual successful run. The terminating marker is `BUCKYBALL_RIPS_EARLY_TOPOLOGY_AND_PERSISTENCE_VERIFIED`.

The finite calculations prove exact properties of this specified graph. They are not evidence of a classification for other graphs or homotopy types beyond radius three. An independent audit has not been performed.
