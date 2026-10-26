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

Run `python verify.py` with Python 3 in the directory of this document. The standalone checker explicitly builds all \(384\) identity-fixing maps for the quandle \((\mathbb Z/4\mathbb Z)^2\), checks their bijectivity, checks the defining identity for every ordered pair of domain elements for each map, and verifies stabilizer orbit sizes \(1,3,12\). It also checks the full automorphism count \(6144\), the affine index \(4\), and a quandle automorphism which is not affine.

The local replay completed and printed `PAIR_ORBIT_SIZES_OK 1 3 12`, `POINT_STABILIZER_OK 384`, `AUTOMORPHISM_ORDER_OK 6144`, `AFFINE_INDEX_OK 4`, `NONAFFINE_EXAMPLE_OK`, and `VERIFY_OK`. These checks are finite only; the infinite-family theorem is proved in `RESULT.md`. No independent audit was performed.
