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

Execute `python3 verify_windmill.py` from this package with a Python 3 interpreter and NumPy installed. The standalone script constructs its own adjacency matrices for the path windmill graphs (not read from stored spectra or logs), groups adjacent eigenvalues numerically to form projector Schur squares, and tests the predicted rank and all proposed kernel vectors.

Observed replay output:

`VERIFY_OK graph_cases=40 max_order=67 path_span_tests=10 even_mode_resolvents=30 m3_b3_rank=7/10 max_kernel_residual=1.67e-15 min_positive_mode=2.778e-02`

The 40 graph cases cover all `2 <= m <= 11` and `3 <= b <= 6`. Independently, the script checks the finite sine-square profile span for each `m` and the trigonometric even-mode resolvent identity for 30 mode instances. These experiments check arithmetic consistency only. All unbounded claims rely on the proof in `RESULT.md`, including exact spectral separation, the Gram compression criterion, Fourier inversion, and the converse kernel argument. A floating-point tolerance is not an exact certificate.
