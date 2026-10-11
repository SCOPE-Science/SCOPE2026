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
# Verification and reproducibility

The exact theorem depends on the Cauchy double-alternant Gram identity, the model-space decomposition for finite Blaschke products, global strong concavity of the pseudohyperbolic angular interaction, and a cyclic variance identity. The proof of each specialized step is included in `RESULT.md`. A finite test cannot establish the all-degree inequality.

Run `python verify_szego_ring.py` under Python 3 with no third-party dependencies. The script builds normalized Hardy-kernel matrices, computes determinants by complex Gaussian elimination, and verifies the regular-polygon Fourier eigenvectors/eigenvalues for 32 degree/radius pairs. It then checks 945 randomly perturbed circle configurations against the analytic determinant-stability bound and probes the exact sharpness asymptotic at three radii. The program was run on the included source and returned `PASS: 32 regular spectra, 945 jittered configurations, 3 sharpness sequences`.

The sharp constant is analytic: the angular potential curvature has minimum magnitude at separation \(\pi\), and a perturbed antipodal pair has determinant deficit \(c_r h^2+O_r(h^4)\). A zero or finite numerical tolerance is never interpreted as an exhaustive proof. The determinant refers only to the finite seed Gram matrix, not to an infinite Fredholm determinant. The theorem does not address repeated zeros, varying radii, or globally optimal condition numbers outside the regular-polygon family.
