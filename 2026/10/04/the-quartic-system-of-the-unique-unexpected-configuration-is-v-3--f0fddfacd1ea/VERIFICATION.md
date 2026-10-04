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

The exact verifier is `artifacts/verify.py`. It uses only the Python standard library. It recomputes the degree-four evaluation rank, the rich-line incidence fingerprint, all signed-permutation symmetries, the induced projective action on the four three-rich lines, the conjugacy-class census, and the degree-four character decomposition. The proof that the incidence action is faithful is mathematical: fixing the four three-rich lines fixes their six pairwise intersections, hence a projective frame.

The computation proves only the stated degree-four representation for the displayed nine-point configuration over characteristic zero. It does not certify any higher-degree or positive-characteristic analogue.
