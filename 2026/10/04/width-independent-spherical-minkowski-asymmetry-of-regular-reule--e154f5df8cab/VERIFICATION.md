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

For a regular spherical odd-\(n\)-gon on a circle of radius \(\rho\), a farthest vertex pair has azimuth difference
\[
\pi-\frac{\pi}{n}.
\]
The spherical cosine law therefore gives
\[
\cos\omega
=
1-\left(1+\cos\frac{\pi}{n}\right)\sin^2\rho,
\]
hence
\[
\sin\rho
=
\frac{\sin(\omega/2)}{\cos(\pi/(2n))}.
\]

The complete curved Reuleaux body's circumradius is checked analytically by two opposite estimates. Since all generating vertices lie in the body, their vector average
\[
\frac1n\sum_jv_j=(\cos\rho)o
\]
forces every containing spherical ball to have radius at least \(\rho\). Conversely,
\[
B_{\omega-\rho}(o)\subset W_{n,\omega}
\]
by the triangle inequality. Hou–Jin's exact identity
\[
r(W)+R(W)=\omega
\]
then gives \(R(W)\le\rho\), so equality follows.

Substitution into the Hou–Jin definition produces
\[
\operatorname{as}_s(W_{n,\omega})
=
\frac{1}{2\cos(\pi/(2n))-1}.
\]

The embedded `verify.py` was replayed from its actual package path. It reconstructs regular vertex sets for odd \(3\le n\le63\) at several admissible widths, checks the farthest-distance relation, the vertex-average identity, sampled inner-ball inclusion, the asymmetry cancellation, strict monotonicity, the triangle endpoint, and the asymptotic coefficients.

The replay output was:

`VERIFY_OK spherical Reuleaux asymmetry profile`

The finite replay is a consistency check only. It is not used to establish the quantified theorem.
