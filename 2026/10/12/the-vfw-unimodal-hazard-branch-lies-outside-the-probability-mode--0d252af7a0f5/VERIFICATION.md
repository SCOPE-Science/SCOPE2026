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
Set
\[
A(x)=\exp(\theta x^\vartheta-x^{-1})
\]
and
\[
G(x)=1-e^{-A(x)}.
\]

For \(\theta>0\), \(A(x)\) increases from zero to infinity and \(G(x)\) increases from zero to one.

For \(\theta=0\),
\[
G(x)\to1-e^{-1}.
\]

For \(\theta<0\),
\[
G(x)\to0
\]
at infinity, and
\[
G'(x)
=
x^{-2}
\left(1+\vartheta\theta x^{\vartheta+1}\right)
A(x)e^{-A(x)}
\]
changes sign at
\[
x_c=(-1/(\vartheta\theta))^{1/(\vartheta+1)}.
\]

The bundled checker evaluates these formulas directly and verifies the numerical counterexample \((\vartheta,\theta)=(1,-1)\).

For admissible positive scale it also verifies representative endpoint hazard behavior for the two simulation parameter pairs used by the source.
