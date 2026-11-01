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

# Reproducible exact verification

Run `python3 verify.py` in the directory containing the seven-file result. Only the Python standard library is needed. Successful output has three lines beginning `VERIFY_OK`.

The verifier constructs the nine undirected edges of the unfilled triangular prism, indexes the 18 primitive vertex-edge pairs by directed arcs, and calculates the strong gradient of every one of the 720 vertex orders using the unique-earlier-neighbor criterion. It compares the 36 inclusion-maximal simplices with the **independently generated** three prism-automorphism orbits, and checks every simplex, the full face vector, and preservation under all twelve automorphisms.

For each triangle, it identifies an edge contained in that triangle and no other triangle; it verifies free-face status at every removal, resulting in a connected graph of 18 vertices and 42 edges. Thus the integral homotopy reduction and rank-25 graph cycle lattice are checked using exact arithmetic. Finally, it computes the signed chain character in dimensions zero, one and two and verifies the equality with two copies of the group regular character plus the triangle-permutation sign character.

The program completes a finite exhaustive computation; it does not certify any claim about graphs outside this exact input. The review is a self-review only, not independent auditing.
