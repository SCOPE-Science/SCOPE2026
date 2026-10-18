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

# Reproducibility and verification

The included Python programs and finite certificate reconstruct the complex directly from its graph edges and the 720 vertex orders. No outside software beyond the Python standard library is required. Execute `python verify_topology.py` and `python verify_representation.py` in the directory containing the certificate.

`verify_topology.py` checks the precise 36 facet bit masks, every one of the 108 nonempty faces, the 41 certified Hasse-pair matches, all 204 covering relations, and exhausts an acyclic topological ordering of the reoriented Hasse diagram. The critical face multiset is one vertex and 25 edges, hence Forman's theorem proves the asserted integral homotopy type.

`verify_representation.py` regenerates the entire complex independently, obtains binary boundary ranks 17 and 24, and computes signed Lefschetz traces of all twelve automorphisms. Their character is 25 at identity, 1 at identity with layer swap and at every three-cycle with/without swap, and -1 at every transposition with/without swap. This is the character of two regular rational modules plus the inflated sign.

`topology_output.txt` and `representation_output.txt` contain the exact observed outputs of these two programs. Neither finite homology over a field nor a log alone substitutes for the separate acyclic-matching proof of integral homotopy type. The research does not establish an infinite-family generalization or an integral equivariant decomposition. Independent scientific audit is not performed.
