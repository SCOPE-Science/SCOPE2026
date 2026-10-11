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

# Verification of the analytic theorem

The theorem does not depend on a finite computation, or a solver log. It is verified by the following directly checkable analytic steps.

1. For each coordinate \(n\), the norm of the corresponding \(\ell_1\)-row is exactly \(A+t-2\min(a_n,t)\); because \(a_n\to0\), the supremal row norm is \(A+t\). No coordinate is assumed to maximize the operator norm.
2. For \(x\in c_0\), the output coordinates converge to \(\varphi_a(x)\). This yields \(t\|x\|_\infty\le2\|T_{a,t}x\|_\infty\), making norm-convergent maximizing sequences of outputs correspond to norm-convergent inputs.
3. If the operator attains its norm, one **fixed finite coordinate** must attain it because the limiting coordinate magnitude is at most \(A<A+t\). The equality case of the absolutely convergent weighted triangle inequality then forces all coordinates with positive weight to have one common unit phase; membership in \(c_0\) makes that support finite. Conversely finite support provides an explicit finite-support extremizer.
4. For arbitrary \(b\in\ell_1\), the pullback of \(b\) under the extended map has coefficients \(\bigl((\sum_n b_n)a_k-tb_k\bigr)\in\ell_1\); thus the extension is weak-star continuous. Finite truncations and Banach--Alaoglu identify the full weak-star closure, not just some cluster points.
5. A zero weight permits an exact weak-star maximizer at that coordinate. If every weight is positive, no single coordinate can reach \(A+t\); a hypothetical supremum of \(A+t\) requires \(|\varphi_a(z)|=A\), which forces a constant unit-phase sequence. Its output norm is then \(|A-t|<A+t\), an exact contradiction.
6. The three density constructions preserve nonnegative coefficients and the fixed total mass \(A\). Each set \(\{a:a_n>0\}\) is relatively open dense, so full support is a dense \(G_\delta\), while the union of the nowhere dense closed zero-coordinate sets is a dense meager \(F_\sigma\). The operator-distance equality \(\|T_{a,t}-T_{b,t}\|=\|a-b\|_1\) transfers the density statements without any unproved continuity assumption.

The complex case uses the real-part equality argument with a unit scalar phase; no ordering of complex coefficients is used. The classification excludes \(t=0\) and \(A=0\), where different endpoint behavior would invalidate the stated strict inequalities. Scientific verification here is a same-model mathematical review, not independent auditing.
