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

The accompanying standard-library Python program completely enumerates the graph, matching complexes, and automorphism group. It constructs explicit acyclic Morse reductions and computes every signed critical boundary matrix. Exact integer minors of determinants \(-3,1,-1\), and the independent reduction modulo three for the first matrix, establish the needed Smith invariant factors. Its own observed output is included, with no claim of external or independent verification.

The proof covers all thirty graph edges by exact automorphism enumeration. No claim is made about other planar graphs or multiple-edge deletions. The connection-map image saturation follows from the homology long exact sequence; a chain-level matrix for that particular map is not provided.
