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

# Reproducibility and limits

Run `python verify.py` after installing the packages listed in `requirements.txt`. The source file included here is the same implementation tested in the supporting check; the package extraction must be replayed independently before release. An observed successful run printed `VERIFY_OK graph_detector_cases=1079 prime_step_models=57 sitewise_capture=1348 loss_eigenspectrum=4`. The verifier independently evaluates Hermitian Fourier spectral ranks by eigendecomposition and SVD; it samples 1,079 sink placements across 57 graph models for eight primes, 1,348 single-sink vertex probabilities and four dissipative spectra.

Numerical spectral clustering in these finite tests is only corroboration. The complete infinite-dimensional-parameter proof is finite algebra: cyclotomic polynomial minimality, prime Fourier full-spark minors, spectral decay in finite matrices and an exact character-orthogonality sum. Only the non-Hermitian no-jump model and infinite-time claims are established. There has been no independent audit.
