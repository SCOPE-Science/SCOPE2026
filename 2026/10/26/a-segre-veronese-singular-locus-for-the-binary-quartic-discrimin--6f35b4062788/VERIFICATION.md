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

# Reproducibility and verification

Run `python quartic_verify.py` with SymPy installed. The script recomputes the homogeneous binary-quartic discriminant modulo three, verifies the symbolic formula and all five derivatives after substitution of the two component parametrizations, and checks the pullback of the scheme-theoretic intersection ideal. It also exhaustively enumerates the \(121\) points of \(\mathbb P^4(\mathbb F_3)\), finding \(25\) singular support points, equal to the union of \(16\) quadric and \(13\) square points with \(4\) points in their intersection.

The geometric completeness statement is proved separately by root partitions and local factorization. The script does not prove scheme reducedness, classify the intrinsic Jacobian scheme, or establish priority over unpublished literature. The source polynomial identities have also been examined in the written proof; successful execution is supporting reproducibility, not independent audit.
