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

The proof uses the source identity
\[
\phi_\lambda(t)
=
\frac{\cosh(\lambda(t-\pi))}{\cosh(\pi\lambda)}
\]
and checks the following exact consequences.

At \(t=2\pi/3\), with \(c=\cosh(\pi\lambda/3)\),
\[
\beta_3=\frac1{4c^2-3}.
\]
Because \(\cos(2\pi X/3)\) equals \(1\) on multiples of \(3\) and \(-1/2\) otherwise, the empirical transform is exactly \((3\widehat q_n-1)/2\). Its inverse is
\[
\lambda
=
\frac3\pi
\operatorname{arcosh}\!\left(
\frac12\sqrt{3+\beta_3^{-1}}
\right).
\]

The transform variance and derivative are
\[
\operatorname{Var}\{\cos(2\pi X/3)\}
=
\frac{1+\beta_3}{2}-\beta_3^2,
\]
and
\[
\beta_3'(\lambda)
=
-\frac{8\pi}{3}
\frac{c\sqrt{c^2-1}}{(4c^2-3)^2}.
\]
Their quotient gives
\[
V_3(\lambda)
=
\frac{9}{32\pi^2}
\frac{(4c^2-3)^2(4c^2-1)}{c^2}.
\]
The source parity variance simplifies via \(\cosh(3u)=c(4c^2-3)\), yielding
\[
\frac{V_3}{V_2}
=
\frac{9(4c^2-1)}{32c^4}.
\]
For \(z=c^2>1\), the derivative of \(9(4z-1)/(32z^2)\) is \(9(2-4z)/(32z^3)<0\).

The standalone script `verify.py` recomputes these identities on a deterministic grid and evaluates the source Fisher-information expression near the small-scale boundary. The finite checks are regression tests only; they do not replace the analytic proof.

Expected successful terminal line:
`VERIFY_OK max_identity_error<1e-12 ratio_sup<0.84375 efficiency_limits=(0.8888888889,0.75)`.
