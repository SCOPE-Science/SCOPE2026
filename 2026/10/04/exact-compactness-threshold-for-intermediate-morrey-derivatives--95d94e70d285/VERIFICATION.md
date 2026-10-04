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

The proof was checked symbolically against the exact finite-interval definitions and source statements.

For \(0\le\alpha<1-j/m\), an exponent \(\alpha_0\) can always be chosen with
\[
\max\{\alpha,1-(j+1)/m\}<\alpha_0<1-j/m.
\]
Then \(1-\alpha_0\) lies in the strict compactness interval of the focal theorem, and compact resolvent gives the required compact embedding \(D(B)\hookrightarrow H\).

At the critical exponent, the focal Hilbert-scale estimate gives boundedness. For a compact-resolvent eigenpair \(Be_n=\beta_n e_n\), the test family
\[
\nu_n(t)=\beta_n^{-1}e^{i\beta_n^{1/m}t}e_n
\]
has both source terms of constant pointwise norm one. Its target size is exactly proportional to
\[
\beta_n^{\alpha-(1-j/m)}.
\]
Thus the supercritical target norms diverge. At equality, distinct target functions remain separated by the constant Morrey distance \(\sqrt2\,T^{(1-\lambda)/p}\), so no subsequence can converge.

No numerical computation, finite enumeration, or external certificate is used. The proof does not assert anything beyond \(0\le\alpha\le1\), finite time intervals, or the positive self-adjoint compact-resolvent Hilbert setting.
