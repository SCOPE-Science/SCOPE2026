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

## Exact computational verification

Execute `python3 verify_franklin_perfect_matching.py` with Python 3. No external packages, network access, or external data files are required. The verifier reconstructs the graph from its LCF chords and cyclic edges, checks 17 perfect matchings, builds the exact simplicial complex from all their subsets, and verifies all combinatorial counts.

The supplied Morse matching order is replayed, resulting in 377 disjoint pairs and seven critical simplices. Each of the 2,610 nonempty face incidences is explicitly oriented; a topological sort visits every one of the 761 vertices of this incidence graph. This certifies the matching's acyclicity. Standard discrete Morse theory then supplies the claimed homotopy equivalence, without relying solely on Betti numbers or finite-field calculations.

All \(2^{18}\) graph-edge subsets are independently examined to enumerate ordinary matchings. The face-vector comparison shows that all one- and two-edge matchings extend, while 72 three-edge matchings do not. The terminal `VERIFY_OK` is recorded in `verification_output.txt`.

## Scope and limits

The finite computation is exhaustive only for the fixed labeled twelve-vertex graph. No claim is made for a parameter family, an equivariant refinement, or a formal proof-assistant certificate. Scientific originality assessment cannot rule out every unpublished or unindexed equivalent result. Independent audit has not been performed.
