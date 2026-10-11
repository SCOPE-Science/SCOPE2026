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

For
\[
x=2/m,
\]
the exact radius satisfies
\[
K(m)^2
=
\frac{\Gamma(2x)}{\Gamma(x)}
=
\frac{2^{2x-1}}{\sqrt\pi}
\Gamma\!\left(x+\frac12\right).
\]
Therefore
\[
\frac{d}{dx}\log K(2/x)^2
=
2\log2+
\psi\!\left(x+\frac12\right),
\]
and
\[
\frac{d^2}{dx^2}\log K(2/x)^2
=
\psi_1\!\left(x+\frac12\right)>0.
\]

The derivative starts at
\[
2\log2+\psi(1/2)=-\gamma<0
\]
and tends to infinity. Hence it has exactly one zero.

High-precision evaluation of that zero gives
\[
x_*=0.1450347431666722513354589782\ldots,
\]
so
\[
m_*=2/x_*=13.7897993014103048741\ldots,
\]
and direct evaluation of the exact gamma ratio gives
\[
K(m_*)=0.69348357463966042675\ldots.
\]
These numerical values only identify the exact analytically characterized point.

For \(x\downarrow0\),
\[
\log\Gamma(2x)-\log\Gamma(x)
=
-\log2-\gamma x+\frac{3\zeta(2)}2x^2+O(x^3).
\]
After dividing by two, substituting \(x=2/m\), and exponentiating, one gets
\[
K(m)
=
\frac1{\sqrt2}
\left(
1-\frac\gamma m+
\frac{\gamma^2+\pi^2}{2m^2}+O(m^{-3})
\right).
\]

Stirling's formula gives divergence of \(\Gamma(2x)/\Gamma(x)\) as \(x\to\infty\), hence \(K(m)\to\infty\) as \(m\downarrow0\).

The proof uses exact identities and asymptotic expansions with controlled limiting regimes; no finite grid search is used to infer uniqueness or global monotonicity.
