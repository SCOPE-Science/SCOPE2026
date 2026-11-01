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

# Reproduction

Execute `python3 verify_affine.py` with Python 3 and its standard library. The program prints 949 nonempty simplices and a mod-two Betti vector concentrated in dimensions zero, two and three, and checks the signed Lefschetz formula for each of 432 affine collineations of the order-three plane. Require `VERIFY_OK affine maps 432`.

The order-three check does not prove all-order statements, absence of integral torsion, or novelty. Those are addressed by the exact integral Mayer–Vietoris and join argument in `RESULT.md` and the literature comparison in `REVIEW.md`. No independent audit has been performed.
