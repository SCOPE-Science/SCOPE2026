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

# Reproducibility

The standalone Python program `hexagonal_prism_perfect_matching_character.py` requires Python 3.10+ and no third-party libraries. Run `python3 hexagonal_prism_perfect_matching_character.py`.

The program reconstructs the graph from the 12 labeled vertices and 18 edges; enumerates all twenty perfect matchings without external data; forms all 822 faces including the empty face; constructs the augmented integer simplicial boundary; verifies all initial boundary-square-zero identities; performs 408 integral unit-pivot cancellations with additional intermediate checks; and verifies that precisely six free degree-two generators remain with zero differential. These exact integer operations establish the reduced integral homology as \(\mathbb Z^6\) in degree two and zero otherwise.

The program then constructs the graph automorphisms representing all 24 elements of \(D_6\times C_2\), computes signed fixed-simplex traces on the augmented chain complex, and checks each trace against the asserted rational character formula. The printed four six-entry rows exhaust all group elements. The finite computation completely covers the graph and group stated in the claim; it does not extend to arbitrary prism lengths or establish unknown literature absence.
