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
The sign correction is analytic and precedes interpolation.

For constant forcing, the exact Volterra integral is
\[
\int_0^t(t-s)^{h-1}\,ds=\frac{t^h}{h}.
\]
Hence the correct one-step increment is proportional to
\[
(v+1)^h-v^h,
\]
whereas the printed equation (4.5) is proportional to
\[
(v+1)^h+v^h.
\]

The bundled checker verifies the exact integer-order witness and evaluates representative fractional cases. It also computes the cumulative printed recurrence at a fixed terminal time for successively refined meshes and confirms the predicted \(1/\Delta\) growth.

The checker does not infer anything about unavailable simulation code and does not certify equations outside the accepted claim.
