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

# Verification of the cyclic character computation

The included standalone Python 3 source `verify_nauru_rotation.py` was executed from its package input before inclusion. The resulting exact output is included in `verify_nauru_rotation.txt`. It reconstructs the graph with 24 vertices and 36 edges, enumerates all 35,218 nonempty independent faces, checks each of the 205,656 signed codimension-one incidences, constructs 17,604 disjoint face–coface matching pairs, and verifies acyclicity by visiting all faces in a directed topological sort.

The integer Morse differential, its rank-two unimodular minor, and its kernel generator are explicitly checked. The lifted 696-term integral six-cycle is checked to have zero simplicial boundary. Its projected image after a one-step rotation is the negative of its projected original. For each of the twelve powers of rotation the full signed fixed-face Lefschetz sum is independently enumerated, and the resulting two rational characters are checked against their announced complete arrays. The final line of the recorded execution is `VERIFY_OK`.

The calculated characters concern rational homology of one 24-vertex graph only. The checks are finite and exact; they do not constitute independent validation, a proof of literature exhaustiveness, or an integral group-module classification.
