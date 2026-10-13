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
The bundled symbolic checker verifies the exact \((H_1)\) witness at
\[
\sigma=1,\qquad a_0=4,\qquad d_1=10,\qquad d_2=\frac15.
\]
It obtains
\[
r_1=2,
\qquad
T_1=-\frac{51}{5},
\qquad
D_1=-\frac{12}{5}.
\]
Thus a nonconstant mode is already transversely unstable at the homogeneous Hopf point.

The checker then translates the planar restriction to the equilibrium \((1/2,1/4)\), constructs the exact quadratic and cubic multilinear forms, and evaluates the standard Hopf coefficient. It returns
\[
l_1=-5\sqrt2<0.
\]
The crossing speed is
\[
\frac1{16}>0.
\]
Hence the homogeneous branch is supercritical and lies on \(a>4\).

The invariant-subspace step is exact: spatially constant functions have zero Laplacian, so the PDE vector field on that subspace equals the planar vector field independently of diffusion.
