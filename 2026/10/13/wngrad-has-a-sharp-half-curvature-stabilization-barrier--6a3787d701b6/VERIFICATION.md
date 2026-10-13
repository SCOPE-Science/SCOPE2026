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
The package verifies the WNGrad half-curvature transient law on isotropic quadratics for both accumulator indexing conventions displayed in the source.

`verify.py` checks the exact objective ratio, the if-and-only-if half-curvature boundary, the finite escape bound from the unstable region, persistence of monotonicity after escape, bounded learned scales, and convergence from deterministic grids and randomized aggressive initializations.

The finite computations are transcription guards. The global convergence and finite-prefix theorem are proved analytically in `RESULT.md`.
