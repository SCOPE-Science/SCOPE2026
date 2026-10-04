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

For \(X=\mathrm{ces}_2^{(2)}\),
\[
\|(x,y)\|^2=\frac{5x^2+2|xy|+y^2}{4}.
\]
Against \(|(x,y)|_*^2=5x^2+y^2\), homogeneity and absoluteness reduce the ratio to
\[
\frac{\|(x,y)\|^2}{|(x,y)|_*^2}
=\frac{5+2t+t^2}{4(5+t^2)},\qquad t\ge0.
\]
The derivative numerator of \((5+2t+t^2)/(5+t^2)\) is exactly \(2(5-t^2)\). Hence the quotient is minimized at the two axis limits and maximized at \(t=\sqrt5\). The exact ratio of maximum to minimum is \(1+1/\sqrt5\).

A symbolic replay also checks
\[
\left(1+\frac1{\sqrt5}\right)(5+t^2)-(5+2t+t^2)
=\frac1{\sqrt5}(t-\sqrt5)^2.
\]
The primary article was checked at Lemma 2.5 and Example 2.10 for, respectively, the equivalent-norm Ptolemy comparison and the exact value \(C_P(\mathrm{ces}_2^{(2)})=1+1/\sqrt5\).

Limits: no higher-dimensional or \(p\ne2\) statement is asserted. Literature search cannot exclude every obscure prior source.
