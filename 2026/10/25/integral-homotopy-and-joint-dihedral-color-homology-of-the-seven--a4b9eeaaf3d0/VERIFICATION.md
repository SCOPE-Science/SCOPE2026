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

Run `python3 c7k3_equivariant_checker.py` from the extracted package using Python 3 standard library. The executable reconstructs the categorical graph and every independent face; verifies its exact 5,282-face enumeration and 2,639 pairs and checks that the 25,242 directed incidence graph is acyclic by a full topological sort. Critical bitmasks are 132225 (dimension 3) and 166145, 590402, 592130 (dimension 4), plus the critical zero-cell after empty-face de-augmentation. The exact oriented integer Morse boundary rows for all critical four-faces are zero.

It constructs a primitive three-cycle (signed cross-polytope with 16 facets), checks its entire integral boundary vanishes and its projection is one, then evaluates every dihedral and color automorphism on it. Separate alternating signed fixed-simplex counts determine the fourth-homology traces. It asserts all 84 character identities and prints `C7_K3_EQUIVARIANT_HOMOTOPY_VERIFIED` only on full success. The fixed orbit count is exhaustive for this finite graph, not a claim about all cycle-product parameters. Interpretation of the Morse differential as attaching degree uses the standard discrete Morse theorem and \(\pi_3(S^3)\cong\mathbb Z\). No independent external audit has been performed.
