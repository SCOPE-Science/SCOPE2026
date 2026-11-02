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

Run `python affine_certificate.py` and `python lcf_certificate.py` in the directory containing the provided files. Both use Python 3 standard-library modules only and raise assertion failures if any stated count or graph-structure check fails.

The affine certificate enumerates all 80,730 possible five-edge subsets of a 27-edge incidence graph, checks the induced-matching predicate, constructs all two-edge replacements, computes breadth-first distances from every optimum, identifies its 18 triangles, and verifies that their intersection graph is isomorphic to the original incidence graph. The optimality upper bound is separately established by the incidence inequality in the proof.

The LCF certificate constructs the host graph independently from a Hamiltonian cycle and chord sequence. Its pivoted maximal-clique search enumerates the complete edge-compatibility graph and yields maximal-clique counts 153 of size three and 27 of size five. It independently checks every optimal exchange and shortest-path distance, reconstructs the 18-triangle graph, and checks its isomorphism to the LCF host.

Expected success markers are `AFFINE_EXHAUSTIVE_MATCHING_LINE_GRAPH_PASS` and `LCF_MAXIMAL_CLIQUE_AND_METRIC_PASS`. These checks verify finite mathematical statements; they do not constitute an independent scholarly audit or establish literature novelty.
