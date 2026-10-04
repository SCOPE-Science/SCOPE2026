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

The proof was checked symbolically from the incidence-algebra definitions. For a rooted forest, direct Möbius inversion reduces to the root identity \(Df(r)=f(r)\) and the unique-parent identity \(Df(v)=f(v)-f(p(v))\). Applying the same formula twice supplies the sign condition used in the convex-order implication.

A direct matrix replay on several branching forests constructed the zeta and Möbius matrices and checked every indicator function. In each case the local derivative identity held and \(\lVert D^2\mathbf 1_A\rVert_\infty\le2\).

For the three-element chain \(r<a<b\) with \(\mu=\delta_a\) and \(\nu=(\delta_r+\delta_b)/2\), the replay gives hockey-stick expectation differences \((0,0,\tfrac12)\), first-moment difference \(0\), second-moment difference \(1\), \(d_{\mathrm{TV}}=1\), and \(d_\zeta=\tfrac12\). This verifies sharpness.

Finite replay is not used as an infinite proof. The general result rests on the unique-parent Möbius formula and the hockey-stick representation. The proof does not cover posets containing merge points.
