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

# Computational verification and limits

Run `python3 verify_12node_lines.py` with the standard Python interpreter; no external packages are needed. The program implements \(\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)\) and independently enumerates all \(85\) projective points and \(357\) projective lines in \(\mathbb P^3(\mathbb F_4)\). Each contained line is confirmed by evaluation of the quartic at all five of its rational points. The program also constructs the twenty explicitly predicted lines, compares both lists, enumerates the twelve singular points, checks all 190 line pairs and every smooth intersection's multiplicity and Frobenius action.

Expected successful terminal marker: `SYMMETRIC_12_NODE_QUARTIC_20_LINES_ALL_CHECKS_PASS`. Recorded independent enumeration statistics within this package: `contained_lines=20`, `singular_nodes=12`, `coordinate_lines=8`, `paired_lines=12`, `nodal_pairs=72`, `smooth_crossings=22`, `smooth_F2_crossings=4`, `line_closed_points_of_degree_2=10`, and `node_closed_points_of_degree_2=6`.

The finite-field enumeration alone does **not** prove completeness of geometric lines over the algebraic closure. That conclusion is proved separately by the product-is-square divisor argument and coefficient comparison in `RESULT.md`; it implies that all such lines descend to \(\mathbb F_4\). The computation does not establish the scheme structure of the unreduced Hilbert scheme, the Picard lattice, or geometric automorphisms. No independent mathematical audit or validation has been performed.
