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

The primary preprint was checked at its definitions, Proposition 3.5, and Corollary 3.9. The polynomial source field is exactly
\[
\dot x_1=-\varepsilon x_1^3+x_2,\qquad \dot x_2=-x_1^3-x_2^3,
\]
with \(\varepsilon>0\). The source gives a strict global Lyapunov function and proves by a Hessian argument that no Morse Lyapunov function exists.

For the new construction, the standard multiplier \(a(x)=\exp(-1/\|x\|^2)\) for \(x\ne0\), with \(a(0)=0\), is smooth and flat. Therefore both \(a f_\varepsilon\) and \(-a x\) have all derivatives equal to zero at the origin. For \(-a x\), direct differentiation of \(\|x\|^2\) gives a strictly negative orbital derivative away from the origin.

For \(a f_\varepsilon\), the positive factor on the punctured plane preserves oriented source orbits. The source-time parameter cannot remain bounded as physical time tends to infinity, because a finite nonzero orbit point has a neighborhood on which \(a\) is bounded below. It also cannot diverge at finite physical time because \(a\le1\). Thus global attraction and stability pass to the time change. A putative Morse Lyapunov function for the time-changed field would have strictly negative derivative along \(f_\varepsilon\) after division by \(a\), contradicting the inspected source proposition.

No numerical experiment, finite enumeration, or external certificate is used. The proof does not cover the real-analytic category, and it does not show that the full smooth local germ is insufficient.
