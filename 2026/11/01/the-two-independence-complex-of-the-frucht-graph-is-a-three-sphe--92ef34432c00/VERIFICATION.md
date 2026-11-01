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

# Computational reproduction

Execute `python3 verify.py` with Python 3. It constructs the specified 12-vertex graph, verifies it has 18 edges and all degrees 3, tests all 4095 nonempty vertex masks through two independent characterizations, and enumerates exactly 824 simplices. It independently reconstructs the vertex-toggle matching and confirms 411 pairs with critical masks 512 (degree zero) and 338 (degree three). It explicitly constructs all 3244 oriented Hasse incidences, verifies the matched orientation is acyclic by topological sorting, and computes exact mod-two simplicial boundary ranks 11, 55, 135, 157, 52, 1 in degrees one through six. The resulting only nonzero reduced mod-two Betti number is one in dimension three. The attached recorded output is `verification_output.txt`.

The integral sphere claim follows not from the field calculation but from the fully verified acyclic matching and the discrete Morse theorem: one critical vertex and one critical three-cell form a three-sphere CW complex. No external audit or machine proof of the discrete Morse theorem is claimed.
