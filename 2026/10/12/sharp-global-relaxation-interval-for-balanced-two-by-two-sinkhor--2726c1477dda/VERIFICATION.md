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
The main theorem is a symbolic statement about every strictly positive \(2\times2\) kernel and all strictly positive starts. Its correctness rests on exact log-ratio identities, a strictly convex coercive potential, a compact descent argument, and convergence of a scalar driven affine recursion. No finite test can replace those steps.

The standalone checker replays the log-ratio algorithm for the positive kernel
\[
K=\begin{pmatrix}100&1\\1&100\end{pmatrix}.
\]
This kernel has the exact balanced coupling
\[
P_*=K/202.
\]
Its Birkhoff factor equals \(99/101\), so the general Hilbert-contractivity guarantee ends at the exact upper endpoint
\[
\frac{101}{100}.
\]
The checker confirms potential descent and projective convergence at \(\omega=19/10\), far beyond that general bound; it also checks the exact reflection identity at \(\omega=2\) numerically from several nonoptimal states.

The analytic nonconvergence witness starts from the projective ratios
\[
x_0=\log2,\qquad y_0=0.
\]
The initial potential gap is exactly
\[
\Phi(x_0,y_0)-\Phi(0,0)
=\log\left(\frac{3}{2\sqrt2}\right)>0.
\]
At \(\omega=2\) this positive gap is preserved forever, so the coupling cannot tend to \(P_*\). At \(\omega>2\) it cannot decrease, giving the corresponding exclusion without numeric approximation.

The checker additionally tests a positive non-symmetric kernel and verifies that the normalized row and column marginal residuals approach zero. It is corroborative rather than a complete numerical certificate of the infinite theorem.
