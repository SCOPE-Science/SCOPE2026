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

# Verification record

`python check_tricylinder.py` (NumPy dependency) independently reconstructs radial section areas from two-dimensional integration and planar radial polygons, then compares them against the finite arctangent law. The repeatable random directions use seed `81233`.

In the recorded execution:

- 240 generic normal directions: largest arctangent-versus-radial-quadrature error \\(7.10\\times 10^{-10}\\).
- 24 of those directions: largest arctangent-versus-independent-polygon error \\(8.52\\times 10^{-9}\\).
- Three coordinate-, face-diagonal- and body-diagonal-normal benchmark formulas passed.
- Four tangent azimuths, including a coordinate tangent and a balanced tangent, passed shrinking-angle cubic-coefficient tests at \\(\\delta=0.04,0.02,0.01\\).

The computer tests use finite discretization and floating-point arithmetic and cannot prove statements for all normals or a uniform asymptotic remainder. The accompanying mathematical argument gives the required exact projection-sector decomposition, global lower bound and cubic-layer expansion. No independent review has been performed.
