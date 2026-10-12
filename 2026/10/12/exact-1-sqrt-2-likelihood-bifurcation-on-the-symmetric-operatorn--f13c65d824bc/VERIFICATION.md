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

The final claim was checked by direct symbolic algebra on the restricted likelihood.

With \(2a+b=1\), \(r=s\cos\theta\), and \(t=s\sin\theta\), all dependence on the projective scale \(s\) cancels. Setting \(v=\sin\theta+\cos\theta\) reduces the objective, up to a positive scale and additive constant, to
\[
g_b(v)=a\log(v-1)+(a-1)\log(v+1),\qquad 1<v\le\sqrt{2}.
\]
Differentiation gives
\[
g_b'(v)=\frac{1-bv}{v^2-1},
\]
so the transition can occur only when \(1/b=\sqrt{2}\), namely \(b=1/\sqrt{2}\). For \(b>1/\sqrt{2}\), solving \((1+q)/\sqrt{1+q^2}=1/b\) yields the two reciprocal positive maximizer ratios stated in the result.

At equality, \(v=\sqrt{2}\cos h\) and \(g_b''(\sqrt{2})=-1/\sqrt{2}\), producing the strict quartic loss \(-h^4/(4\sqrt{2})+O(h^6)\).

As a separate cross-check, specializing the degree-six sliced logarithmic discriminant printed in arXiv:2607.19593v2 to its reflection-symmetric data line gives \(2(4a^2+4ab-b^2)^3\); under \(2a+b=1\) this vanishes exactly when \(1-2b^2=0\).

No numerical experiment is used as proof. The result does not classify off-slice critical points of the full positive Grassmannian.
