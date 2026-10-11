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

The proof was reconstructed from the sharp spherical isominwidth theorem and checked independently at every transition-sensitive step.

For the acute branch, if \(s\) is the side length and \(w\) the width-realizing altitude of the regular minimizer, spherical Pythagoras gives
\[
\cos s=\cos w\cos\frac{s}{2}.
\]
Solving for \(q=\cos s\), applying the equilateral spherical cosine law, and then spherical excess yields the stated first branch. Exact symbolic differentiation gives
\[
\lim_{w\uparrow\pi/2}M'(w)=\frac{3}{\sqrt2}.
\]

For the obtuse branch, the source identifies the minimizer as \(U_{\pi-w}^{\circ}\) and gives the polar identity
\[
\operatorname{area}(L)=2\pi-\operatorname{per}(L^{\circ}).
\]
The three Reuleaux arcs each have length \(\sin t\,\beta(t)\), where
\[
\beta(t)=\arccos\!\left(\frac{\cos t}{1+\cos t}\right).
\]
This gives the stated second branch and the exact limit
\[
\lim_{w\downarrow\pi/2}M'(w)=3.
\]

The bundled symbolic checker verifies the algebraic side relation, continuity at the transition, both derivative limits, and the positivity of the slope jump. It is a consistency check rather than a substitute for the analytic proof.

The scientific boundary is explicit: no inference is made from finite experiments, and no claim is made about differentiability of the minimizing shapes themselves. A close stability paper was only available at abstract level in the checked public material; that access limitation is retained as an originality risk rather than treated as evidence of novelty.
