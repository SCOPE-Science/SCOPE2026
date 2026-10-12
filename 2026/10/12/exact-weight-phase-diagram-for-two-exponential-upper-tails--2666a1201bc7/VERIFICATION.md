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

The proof uses the exact survival function
\[
T_t(r)=e^{-t}\frac{r e^{-t/r}-e^{-tr}}{r-1}
\]
for \(r>1\), together with its continuous equal and sparse endpoints.

Differentiation reduces the sign of the weight derivative to \(h_t(r)\). After the substitutions \(x=t(r-1)\) and \(u=tx/(t+x)\), the nontrivial region \(u<1\) is equivalent to the sign of \(L_t(x)\), and
\[
L_t'(x)=
\frac{x^2\bigl((t-1)x^2+t(2t-3)x+t^2(2t-3)\bigr)}{(t+x)^2(1+x)\bigl(t-(t-1)x\bigr)}.
\]
Every denominator factor is positive on \(0<x<t/(t-1)\). This exact factorization yields the complete derivative sign pattern analytically.

For \(1<t<3/2\), the quadratic numerator has one negative and one positive root, so \(L_t\) decreases and then increases. Since \(L_t(0)=0\) and \(L_t(x)\to+\infty\) at the right boundary, there is exactly one positive zero and therefore exactly one interior tail minimizer. For \(t\ge3/2\), the derivative is strictly positive for every imbalanced pair.

The endpoint values are \(e^{-2t}(1+2t)\) and \(e^{-t}\); their unique crossover above the mean is the root of \(e^t=1+2t\). The numerical value \(1.2564312086261696769\ldots\) is supplementary only. No finite enumeration or numerical grid is used to establish any quantified statement.
