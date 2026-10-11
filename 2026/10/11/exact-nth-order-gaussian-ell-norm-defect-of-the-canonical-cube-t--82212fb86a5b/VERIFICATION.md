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
The proof is analytic and valid for every fixed integer \(n\ge2\). The key exact identities are
\[
K_\varepsilon=\{x:\|x\|_\infty\le1,\ \|x\|_1\le n(1-\varepsilon)\}
\]
and
\[
\|x\|_{K_\varepsilon}=\max\left\{\|x\|_\infty,\frac{\|x\|_1}{n(1-\varepsilon)}\right\}.
\]
For \(0<\varepsilon<1/n\), the positive Gaussian excess is supported exactly where the deficits from the largest half-normal coordinate have total less than \(n\varepsilon M\). Scaling those \(n-1\) deficits by \(\varepsilon M\) produces a fixed simplex and the factor \(\varepsilon^n\). Dominated convergence then proves the limit.

The coefficient uses
\[
\int_{\substack{w_i\ge0\\\sum w_i<n}}\left(n-\sum w_i\right)dw=\frac{n^n}{n!}
\]
and
\[
\int_0^\infty m^n\left(\sqrt{2/\pi}e^{-m^2/2}\right)^n dm
=\left(\frac2\pi\right)^{n/2}\frac12\left(\frac2n\right)^{(n+1)/2}\Gamma\left(\frac{n+1}{2}\right).
\]
`verify.py` checks the second identity numerically in dimensions \(2\) through \(8\), and checks the final coefficient obtained by multiplication. This is a finite arithmetic replay only; it does not replace the proof of the all-dimensional limit.

The source was inspected at its definition of \(\ell\), Theorem 1.3, and the optimality paragraph defining \(K_\varepsilon\). It supplies the same family and an \(O(\varepsilon^n)\) upper estimate, but no asymptotic equality or leading coefficient. Independent validation has not been performed.
