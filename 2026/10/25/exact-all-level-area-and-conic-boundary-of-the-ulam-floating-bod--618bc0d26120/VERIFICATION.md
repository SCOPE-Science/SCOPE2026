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

# Verification of the triangle Ulam-body area formula

The general theorem is proved analytically in `RESULT.md`. The accompanying standard-library-only `verify.py` tests the independent construction of cap centroids by polygon clipping and bisection, area by the shoelace formula, and the resulting Ulam-body boundary area at 12 parameter/triangle choices. Three tests use an invertible affine image of the standard triangle. Further tests substitute into the two conic equations at 156 sample positions, compare the centroid-complement area identity at 99 values, and verify the exact half-cap formula numerically.

Run `python verify.py` from this directory. Expected successful output begins `VERIFY_OK triangle Ulam normalized area`; the program exits with an exception on a discrepancy. The numerical area tolerance is \(2.5\times10^{-5}\) in area-ratio units, and conic residual tolerance is \(10^{-13}\). The calculations do not assert that a finite mesh exhaustively verifies a continuum of cap directions. In particular, numeric agreement is not the proof of the closed formula; the exact cap parametrizations, Green integrals, and moment complement identity are the proof.

The supporting scientific references are the foundational Ulam-body theorem, the original metronoid treatment, and the average-quantile geometric formulation, listed in `RESULT.md`. The exact area claim has not been independently audited.
