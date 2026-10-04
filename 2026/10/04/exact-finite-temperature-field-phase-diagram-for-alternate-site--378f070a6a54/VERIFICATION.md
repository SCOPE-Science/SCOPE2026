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

`verify_xx4_field_phase.py` evaluates the published \(u,v,y,Z\) expressions and checks their exact phase reduction numerically over deterministic grids.

It checks
\[
y^2-uv
=
L(x)c^2-Q(x)c-R(x)
\]
at 96 parameter points and separately checks the predicted concurrence sign at those points.

It computes the unique solution of
\[
\sinh^2x=\cosh(\sqrt2\,x)
\]
by bisection, verifies the quoted universal temperature ratio, checks convergence of the low-temperature activation-field asymptotic, and checks the high-field concurrence tail in three parameter regimes.

The checker also evaluates explicit positive-concurrence points inside regions that finite-resolution source plots visually suggest are zero.

The numerical replay is supplementary. The all-parameter phase theorem is proved analytically in `RESULT.md`.

No independent audit has been performed.
