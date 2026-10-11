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

Run `python3 verify.py` in the package directory. The verifier uses only the Python standard library and reconstructs the result from the five graph6 strings.

It checks, without stored adjacency tables, that each graph has twelve vertices, eighteen edges, degree three at every vertex, is connected, has an explicit Hamiltonian cycle, and has exactly one automorphism. Pairwise graph-isomorphism searches verify that the five representatives are mutually nonisomorphic.

For every graph, breadth-first search supplies the exact shortest-path metric. The verifier then tests all \(4095\) nonempty vertex subsets at radii \(1,2,3\). For every threshold it checks the full face vector, rebuilds every Hasse cover, constructs the stated staged vertex-toggle matching, and verifies acyclicity by topologically sorting the entire oriented Hasse diagram. The critical-cell dimensions and multiplicities are checked against the claim.

The class-exhaustion statement additionally uses the published count in arXiv:1811.11655v1 that exactly five of the eighty cubic Hamiltonian graphs on twelve vertices are asymmetric. The code verifies that the five representatives give five distinct qualifying isomorphism classes; it does not independently regenerate the full eighty-graph census.

The supplied `verify_output.txt` is the output from replaying the verifier on the packaged `verify.py`; its final line is `VERIFY_OK`.
