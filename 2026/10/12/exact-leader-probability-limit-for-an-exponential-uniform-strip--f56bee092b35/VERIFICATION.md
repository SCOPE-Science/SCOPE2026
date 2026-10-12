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

The proof uses the published strip CDF
\[
F(x,y)=1-e^{-x}-(x+1-y)\left(e^{-(y-1)_+}-e^{-x}\right).
\]
With \(y=x+v\), \(w=1-v\), and \(x\ge1\), this becomes
\[
F(x,x+v)=1-e^{-x}\left[1+w(e^w-1)\right].
\]
Writing
\[
A(w)=1+w(e^w-1),
\]
direct integration gives
\[
n\int_1^\infty e^{-x}(1-A(w)e^{-x})^{n-1}\,dx
=
\frac{1-(1-A(w)e^{-1})^n}{A(w)}.
\]
The contribution from \(0<x<1\) is at most \(n(1-e^{-1})^{n-1}\), hence vanishes. Since \(1\le A(w)\le e\), dominated convergence yields
\[
\lim_{n\to\infty}a_n
=
\int_0^1\frac{dw}{1+w(e^w-1)}.
\]
Finally, \(e^w-1>w\) for \(w>0\), so this integral is strictly below
\[
\int_0^1\frac{dw}{1+w^2}=\frac{\pi}{4}<0.8.
\]

The standalone script `verify.py` evaluates the limiting integral by composite Simpson quadrature, checks the range of \(A\), and compares the exact finite-\(n\) upper-strip expression with direct numerical integration at deterministic test values. These finite-precision computations are reproducibility checks only.

Expected successful terminal line:
`VERIFY_OK limit=0.732359299692 pi_over_4=0.785398163397`.
