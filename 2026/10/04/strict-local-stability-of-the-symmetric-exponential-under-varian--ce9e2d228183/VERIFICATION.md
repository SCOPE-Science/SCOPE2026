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

The theorem is analytic. The critical differentiation is reduced to
\[
M_p(t)=\frac12\int_0^\infty e^{-r}\int_{-r}^{r}\left|\frac d2+t(r-2)\right|^p\,dd\,dr,
\]
and the second derivative is dominated uniformly in the translation parameter by a constant multiple of \(r^{p-1}(r-2)^2e^{-r}\), which is integrable for every \(1<p<2\). This validates differentiation under the integral.

At \(t=0\), direct Gamma-integral evaluation gives
\[
M_p(0)=2^{-p}\Gamma(p+1),\qquad
M_p''(0)=2^{2-p}\Gamma(p+1)(p^2-3p+4).
\]
The denominator satisfies
\[
\|Z_{1/2+t}\|_2^2=\frac12+2t^2.
\]
These identities yield the claimed logarithmic Hessian \(4(2-p)^2/p\).

`verify_hessian.py` checks the algebraic reductions and performs direct deterministic quadrature of the defining moment integral at representative exponents. Its stored output is `VERIFY_OK` in `verification_output.txt`.

The quadrature is only a sanity check. It is not used to infer positivity for an interval, and no claim is made about the global optimizer or the conjectured transition location.
