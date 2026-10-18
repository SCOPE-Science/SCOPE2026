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
# Verification and limitations

Execute the two standalone Python 3 programs `verify_faces.py` and `verify_chains.py` using only the standard library. The former independently generates rooted-spanning-path facets, enumerates all faces for \(n=5,\ldots,11\), and checks every dihedral element's signed reduced Lefschetz number and the exact reflection-fixed-face binomial count. It also tests the two alternating formal top-cycle boundaries. The latter uses a separate opposite-bipartition missing-vertex construction of facets, calculates augmented simplicial boundary ranks over \(\mathbb F_2\) and \(\mathbb F_{101}\) for \(n=5,\ldots,9\), and checks cancellation of both top cycles. Both programs passed their assertions when run from the included source files.

The universal integral theorem relies on the written combinatorial proof and the prior Chari–Joswig homotopy classification. Finite fields do not certify arbitrary integral torsion for all \(n\), and finite enumeration is not an infinite proof. The exact integral top-lattice identification is proved by primitive coefficients of disjoint integral cycles, not inferred from finite-field experiments. No independent scientific audit has been performed.
