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

`verify_weighted_volume.py` reconstructs the published polynomial vector field symbolically and checks
\[
\nabla\!\cdot f=-az,
\qquad
\nabla\!\cdot f+a\dot x=0,
\qquad
\nabla\!\cdot(e^{ax}f)=0.
\]
The replay terminates with `VERIFY_WEIGHTED_VOLUME_OK`.

The remaining deductions are analytic: integrating the exact coboundary by Liouville's formula gives \(\det D\phi_t=e^{-a(x(t)-x(0))}\); a periodic orbit makes the endpoint term zero; and preservation of the positive locally finite weighted measure contradicts strict compact trapping of a bounded open set.

Limits: no numerical integration is used as proof; no claim of global completeness is made; no independent audit has been performed.
