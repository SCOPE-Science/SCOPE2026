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

# Reproducible verification

Execute `python3 verify_pappus_strong_matching.py` using Python 3.10 or later. The executable reconstructs the fixed cubic graph, forms the squared-line conflict relation on all 27 graph-edge labels, and exhaustively enumerates all simplicial faces in two independent ways. It also rules out six-edge induced matchings, constructs every Morse pair exactly as specified in the proof, and verifies acyclicity across all 2,214 nonempty face-poset incidences. This supplies the finite witness needed for the integral Forman sphere-wedge argument.

The program separately enumerates all 216 graph automorphisms by adjacency-compatible bijection backtracking, counts signed fixed oriented simplices, and derives the complete second-homology character. Its deterministic output is stored verbatim as `verification_output.txt`; successful execution ends with `VERIFY_OK` and verifies zero full-group invariant dimension. The exact calculation enumerates the entire finite domain, not a sample. The check does not establish a classification for a graph family, rule out unseen literature, or constitute an independent audit.
