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

# Exact reproducibility

From the package root, execute `python3 verification/check_cuboctahedral_ind2.py` using a standard Python 3 interpreter. No third-party Python packages, cached graph tables, prior files or network connections are required. Compare its output with `verification/check_output.txt`; a successful run begins with `CUBOCTAHEDRAL_IND2_EXACT_MORSE_CHARACTER_OK`.

The checker reconstructs the original binary cube and all twelve of its edges, forms the cuboctahedral adjacency matrix, evaluates the induced-degree condition on all \(4096\) subsets, and verifies the complete face vector \((1,12,66,164,177,36)\). It executes the stated twelve-pivot face matching and verifies the exactly \(212\) disjoint pairs and \(32\) critical three-cells. It then verifies acyclicity via a complete directed Hasse graph of \(456\) nodes and \(1524\) cover edges.

An independent mod-two simplicial boundary computation has ranks \(11\), \(55\), \(109\), \(36\) in degrees one through four. The checker enumerates all \(48\) signed-coordinate cube automorphisms, verifies that they preserve cuboctahedral adjacency, and evaluates the signed fixed-simplex Lefschetz sum for each. The computed values are checked against the ten signed-cycle conjugacy classes, their sizes and the full character table.

**Scientific limits:** A finite-field chain computation alone cannot prove the integral homotopy classification; the all-face acyclic Morse matching supplies that proof. The rational character table does not specify an integral lattice decomposition. All computations here are finite and complete for the single twelve-vertex graph. No claim about an infinite family or independently audited correctness is made.
