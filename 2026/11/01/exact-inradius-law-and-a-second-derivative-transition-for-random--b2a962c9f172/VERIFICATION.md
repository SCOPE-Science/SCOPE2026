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

# Verification

Run `python3 verify.py` using Python 3 with only the standard library. The program prints `PASS` after its diagnostic sequence. It has been executed successfully from its actual standalone path.

Its most independent test constructs a central section polygon by intersecting all 12 edges of \(\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}\) with each of 500 generic uniformly oriented planes. After circular sorting of the resulting four or six vertices it computes the smallest distance from the origin to a polygon side and compares it directly with the claimed polar expression to within \(5\cdot10^{-13}\). Further checks compare the positive-tail formula with independent Simpson quadrature on the spherical region, verify endpoint probability identities and support, and compare the analytic CDF with 150,000 seeded independent uniform spherical normals at eleven thresholds. The run passed 533 individually counted diagnostics.

The Taylor-law coefficient at the interior transition was separately compared at several high-precision offsets with the predicted \(9\sqrt3/8\) spherical-area constant, and the induced \(128\sqrt3/\pi\) radius-squared deficit coefficient was checked numerically. These finite checks are diagnostic and cannot certify the continuum claim: the analytic polarity, spherical-area integral, Gauss–Bonnet, and smooth scaling argument in RESULT.md constitute the proof.

Independent mathematical validation has not been performed. The checker is a standalone reproducibility artifact, not a formal proof assistant or a third-party certificate.
