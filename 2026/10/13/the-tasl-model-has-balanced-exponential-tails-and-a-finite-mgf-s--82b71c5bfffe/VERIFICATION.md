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
f_\alpha(x)
=
\frac{P_\alpha(x)}{C(\alpha)}
\frac{e^{-x}}{(1+e^{-x})^2},
\]
the leading polynomial term is
\[
\alpha^2x^6
\]
when \(\alpha\ne0\), and
\[
2x^4
\]
when \(\alpha=0\).

The logistic kernel satisfies
\[
\frac{e^{-x}}{(1+e^{-x})^2}\sim e^{-x}
\]
as \(x\to+\infty\) and is asymptotic to \(e^x\) as \(x\to-\infty\). Hence both extreme tails have the same exponential rate and leading constant.

The MGF integrand behaves like
\[
x^m e^{-(1-t)x}
\]
on the right and, after reflection, like
\[
x^m e^{-(1+t)x}
\]
on the left. Thus the MGF exists exactly for
\[
-1<t<1.
\]

The included checker evaluates the exact published density for positive, negative, and zero values of \(\alpha\), verifies density and survival tail ratios, confirms right-hazard and left reversed-hazard convergence, and checks finite MGF values strictly inside the strip.
