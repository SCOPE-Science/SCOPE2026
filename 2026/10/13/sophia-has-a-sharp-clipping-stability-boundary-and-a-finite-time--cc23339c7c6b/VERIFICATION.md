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
The package verifies the sharp practical-Sophia dynamics on diagonal positive quadratics under the stated exact-curvature assumptions.

`verify.py` reconstructs the coordinatewise clipped map, checks curvature cancellation, exact clipping-core entry times, strict objective decrease in the stable regime, post-entry linear contraction, the explicit two-cycle at and above the boundary, and the finite-time soft-threshold formula at \(\eta=\gamma\).

The finite checks are transcription guards. The if-and-only-if stability boundary and finite-time resonance are proved analytically in `RESULT.md`.
