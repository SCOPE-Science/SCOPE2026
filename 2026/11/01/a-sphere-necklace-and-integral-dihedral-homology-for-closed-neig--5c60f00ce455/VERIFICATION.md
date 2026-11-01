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

The all-parameter proof is the explicit sequence of two sets of \(2n\) elementary free-face pairs, followed by the three-edge-path attachment of each tetrahedral boundary to the graph \(F\). The proof determines the integral homotopy type for every \(n\ge4\), not merely its field homology. The signed permutation of the oriented missing-tetrahedron boundaries and the square-cycle identities give the integral dihedral modules.

Run `python3 verify.py` with Python 3 and its standard library. The checker reconstructs the entire simplicial face poset for \(4\le n\le100\), checks all actual free-face removals, compares the residual simplices to an independently built union of tetrahedral boundaries, checks incidence and action signs, and computes mod-two homology on the *original* complex for \(4\le n\le16\). The recorded execution finished with `ALL_VERIFY_OK`.

The finite computation does not prove the unrestricted theorem; the proof does. There is no claim about the exceptional six-vertex graph, equivariant collapses, or any unpublished global novelty certification. No independent validation has been performed.
