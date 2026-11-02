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

# Verification record

The characteristic-five hyperelliptic model, squarefree boundary, coefficient matrix, Frobenius-twisted stable-rank formula, first Cartier rank, polynomial intersections, non-fifth-power test, and Jacobian smoothness of the two rank-drop curves are proved in `RESULT.md`.

Running `python verify_symbolic.py` with SymPy produced `CHAR5_C6_SYMBOLIC_IDENTITIES_OK`. This checks exact universal polynomial identities over \(\mathbb F_5\) and the algebraic intersection factorization. It does not assume that finite experimentation proves the universal theorem.

Running `python verify_fields.py` (standard library only) produced `CHAR5_C6_INDEPENDENT_GF5_GF25_ITERATED_CARTIER_OK`. It independently constructs every relevant Cartier coefficient by polynomial convolution, forms the correct iterated Frobenius-twisted products and checks ranks for each smooth parameter over \(\mathbb F_5\) and \(\mathbb F_{25}\). Counts for ranks \(3,2,1,0\) were respectively \((12,2,2,1)\) and \((534,22,20,1)\), with \(8\) and \(48\) singular parameter choices excluded.

The finite-field census supports, but does not replace, the proof for every geometric parameter. This verification record contains no independent mathematical audit or external validation.
