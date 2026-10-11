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

Execute `python3 verify.py` using Python 3. The script requires no third-party modules, network access, external files or mutable input. It reconstructs the Clebsch adjacency graph from the five generators, checks all pairs of common-neighbor counts, builds the sixteen radius-one neighborhood facets, enumerates every face, creates a deterministic vertex-toggle matching, and verifies acyclicity by sorting the complete reversed Hasse graph.

Expected certificate: 16 vertices and 40 edges, 16 six-vertex facets, 808 nonempty faces with dimensions zero through five counts `16,120,320,240,96,16`; 376 augmented matched pairs including the empty face, equivalent to 375 ordinary matched pairs plus one critical vertex; 2,752 Hasse incidences, every directed incidence sorted, one critical edge and 56 critical triangles. The full exact signed integral Morse incidence row has 44 zero entries and six `+2` and six `-2` entries. The code calculates the row independently through gradient-path recursion and exact algebraic unit-pivot cancellations. A nonunit coefficient cannot silently pass.

The ordinary critical-cell CW structure has one vertex, one loop and 56 two-cells. A loop of degree two yields \(\mathbb{RP}^2\); all remaining attaching loops of degree zero or \(\pm2\) become null after that attachment, so the homotopy type is \(\mathbb{RP}^2\vee\bigvee^{55}S^2\). This final deduction is mathematical rather than an assertion by the code.

Direct simplicial boundary ranks over \(\mathbb F_2\) in dimensions one through five are `15,104,160,80,16`. Over \(\mathbb F_3\) they are `15,105,160,80,16`. The one-rank discrepancy in dimension two corroborates the \(\mathbb Z/2\) first-homology torsion. Standard cellular-homology and fundamental-group reasoning completes the result.

The script exhaustively verifies this explicitly defined finite graph and scale; it does not certify the construction for arbitrary graph families or provide an independent external audit.
