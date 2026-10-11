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

The one-sided definitions of asymptotic and strong asymptotic expansivity were checked against arXiv:2610.01196v1. For a bounded normal operator \(N\), the proof was replayed directly from the spectral identity
\[
\|N^n x\|^2=\int |z|^{2n}\,d\mu_x(z).
\]
Positive spectral mass outside \(\overline{\mathbb D}\) was checked to force unbounded growth by passing to one annulus \(|z|\ge1+1/k\). Zero mass on \(\mathbb T\) then gives pointwise decay with a unit dominating function, so dominated convergence proves ordinary asymptotic expansivity on every bounded forward orbit.

For strong asymptotic expansivity, the restriction to \(E_N(\overline{\mathbb D})H\) is a normal contraction. Uniform decay on the fixed bounded-orbit ball scales to operator-norm decay of its powers, and normality gives \(\|T^n\|=\|T\|^n\), forcing \(\|T\|<1\). The converse follows from geometric decay.

The example was checked without numerical approximation. Coordinate multiplication on planar \(L^2(\mathbb D)\) has essential range \(\overline{\mathbb D}\), empty point spectrum, zero spectral projection on \(\mathbb T\), and norm one. Coordinate multiplication on arclength \(L^2(\mathbb T)\) has nonzero unit-circle spectral projection and empty point spectrum. Their direct sum therefore has the same point, approximate-point, and whole spectra as the planar operator but fails asymptotic expansivity.

The proof does not extend automatically to nonnormal operators, where spectral projections with these orthogonality and norm identities need not exist.
