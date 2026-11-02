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

The supplementary standalone executable `verify.py` checks exact finite-period and covariance algebra, and finitely truncated mean-zero periodic kernel tails. It relies only on Python's standard library. Invoke `python3 verify.py` in a directory containing the extracted files.

The reported PASS count is a finite-consistency count only. No finite matrix, sample period or computation proves compactness, the Hardy essential norm, operator-algebra membership, or the exact infinite-dimensional distance. Those deductions are given analytically in `RESULT.md`.

Actual analytic checks reconstructed: periodic cancellation forces the Gram-sandwich error to be Hilbert–Schmidt; the Cesàro essential norm is two; the finite shift-orbit average is a positive contraction in the Calkin algebra; squared-distance averaging gives the lower bound; finite-row compact corrections to the scalar Cesàro element give the matching upper bound. The equality is an infimum; no attainment assertion is made beyond asymptotically attaining finite-rank corrections.

Research source limitations: Sang's theorem supplies Cesàro membership in the full Toeplitz algebra; the proof does not construct this factorization independently. Specialist priority checking and independent mathematical audit have not been performed.
