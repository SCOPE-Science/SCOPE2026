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

# Reproducible checks

Run the standalone Python 3 file `verify.py` using the standard library: `python verify.py`. It requires no downloaded data. The program enumerates symmetric off-diagonal and diagonal edge patterns, constructs the corresponding bipartite graphs, checks the absence of independent triples for every union of involution-orbits, and compares complete fixed simplicial face sets to the explicit graph \(Q\cup K_L\). Independently, it constructs every connected labeled graph on at most five vertices, adds a single root bridge to its bipartite double cover, verifies the lift is connected, and checks that its geometric fixed-orbit simplices are precisely the original vertices and edges.

Actual result:

`VERIFY_OK symmetric_matrices=1098 connected_lifts=772 triangle_lift_fvector=[6, 15, 18, 9] reduced_mod2_betti=[0, 0, 0, 1]`

The independent-triple algorithm, graph connectivity check, and mod-two boundary calculation are executed on the definitions rather than on the theorem's edge formula. The finite checks are consistent with the statement, but they cannot establish the unrestricted fixed-space PL homeomorphism, universal realization, or integral homotopy conclusions; those follow from the explicit orbit-barycenter and perfect-matching proof. No independent external audit has been performed.
