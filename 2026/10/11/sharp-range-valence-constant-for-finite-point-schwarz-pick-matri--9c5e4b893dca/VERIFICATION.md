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

For the normalized Bergman kernel
\[
k_z(w)=\frac1{(1-\overline z w)^2},
\]
set \(g=f/\rho\) and \(v_k=(g'(z_i)g(z_i)^k)_{i=1}^n\). Then the exact finite-matrix identity
\[
\rho^2H_{g,Z}-H_{f,Z}
=\rho^2\sum_{k\ge0}(k+1)(1-\rho^{2k})v_kv_k^*
\]
proves \(H_{f,Z}\preceq\rho^2H_{g,Z}\) without approximation or numerical evidence.

For an \(m\)-valent holomorphic map \(g\), the area formula
\[
\int_{\mathbb D}|g'(z)|^2|h(g(z))|^2\,dA(z)
=\int_{\mathbb D}N_g(w)|h(w)|^2\,dA(w)
\]
with \(N_g\le m\) proves the \(m\)-contraction of the derivative-weighted Bergman operator. Its reproducing-kernel Gram matrix is precisely \(H_{g,Z}\), proving \(H_{g,Z}\preceq mG_Z\). The initiating theorem independently supplies \(H_{g,Z}\preceq nG_Z\). Hence the desired Loewner inequality follows.

For sharpness choose \(d=\min\{n,m\}\), \(f(z)=\rho z^d\), and the \(d\)-point orbit \(z_j=r e^{2\pi i(j-1)/d}\). The Fourier vector \(v_j=e^{2\pi i(d-1)(j-1)/d}\) has the exact eigenvalues
\[
\lambda_G=\frac{d^2r^{2d-2}}{(1-r^{2d})^2},\qquad
\lambda_H=\frac{d^3\rho^2r^{2d-2}}{(1-\rho^2r^{2d})^2}.
\]
For \(d=1\), the same formulas hold for the one-point Gram matrices. Thus \(\lambda_H/\lambda_G\to d\rho^2\) as \(r\downarrow0\); extra sample points cannot invalidate the principal-block obstruction.

These exact algebraic identities were checked by independent finite-matrix evaluation for several degrees and radii, solely as a consistency test. The proof covers all permitted parameters symbolically. No infinite conclusion is inferred from a finite experiment. Neither individual-map optimal constants nor general target domains are claimed.
