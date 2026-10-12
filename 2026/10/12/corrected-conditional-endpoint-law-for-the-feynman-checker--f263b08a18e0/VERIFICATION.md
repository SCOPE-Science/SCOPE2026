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

The analytic checks used in the proof are:

1. With \(\phi(u)=\arcsin(1/\sqrt{2(1-u^2)})-u\arcsin(u/\sqrt{1-u^2})\), differentiation gives \(\phi'(u)=-\arcsin(u/\sqrt{1-u^2})\).
2. The allowed-region conditional ratio reduces to a positive quadratic form whose determinant is \(q\cos^2\alpha>0\) on every compact interval below \(1/\sqrt2\).
3. The exact phase average is
\[
p_-(u)=\frac12\left(1+\frac{u}{1+\sqrt{1-2u^2}}\right).
\]
Differentiating the first closed branch of \(G\) returns exactly \(p_-\).
4. In the hidden region, differentiating the published rate function gives \(H'(u)=2\operatorname{arcosh}(u/\sqrt{1-u^2})\). The adjacent-site exponential ratio simplifies to \(r(u)=(u+\sqrt{2u^2-1})/(1-u)\), hence
\[
p_+(u)=\frac{r(u)^2}{1+r(u)^2}=\frac12+\frac{1+\sqrt{2u^2-1}}{4u}.
\]
Differentiating the second branch of \(G\) returns exactly \(p_+\).
5. Both branches give \((1+\sqrt2-\log2)/4\) at the wall and the same first derivative \((2+\sqrt2)/4\). Substitution \(v=1/\sqrt2\pm r^2\) gives the common nonanalytic term \(2^{1/4}r^3/3\), proving the stated \(|v-v_*|^{3/2}\) coefficient.
6. The supplied checker recurrence preserves total probability to floating-point accuracy and approaches the corrected allowed-region branch. It is a consistency check only, not evidence for the infinite proof.

The proof relies on published asymptotics only on compact subregions. The wall itself is handled by the bound \(0\le |a_2/a|^2\le1\), so no unproved uniform asymptotic through the transition is assumed.
