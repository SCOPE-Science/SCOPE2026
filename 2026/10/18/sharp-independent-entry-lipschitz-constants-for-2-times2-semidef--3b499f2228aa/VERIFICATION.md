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

# Verification of the analytic claim

Run `python3 verify.py` in the same directory as the six scientific documents. The program uses Python 3 standard library only. A successful run prints `CHECKS_OK 15731` and the three expected sharp constants in order.

The checker uses exact rational test cases for normalization of the two coordinate rank-one maps and their quadratic norm identities, numeric comparisons between Lorentz and spectral formulas for positive-semidefinite projection, finite-difference Jacobian tests, exact endpoint interpolation tests within floating-point tolerance, induced-norm stress tests, random global input pairs, and explicit sharpness witnesses. It reads no external files and requires no data downloads.

## Mathematical verification versus numerical checks

The **continuum proof** rests on the explicit Jacobian, affine interpolation in the signed radial parameter, sharp absolute-row and -column inequalities, the complementary oblique-projection Euclidean norm identity, and generic-segment integration followed by continuity. The exact rational checks corroborate algebra; sampled floating-point experiments do **not** prove bounds for infinitely many inputs, certify historical originality, or establish independent validation. The claim concerns real symmetric two-by-two matrices and the three specified independent-entry norms.
