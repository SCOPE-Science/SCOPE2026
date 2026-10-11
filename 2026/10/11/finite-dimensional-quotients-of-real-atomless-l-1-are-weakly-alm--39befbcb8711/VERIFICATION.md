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

# Verification: exact finite-dimensional quotient law

1. **Existence of signs.** Rodríguez--Rueda Zoca, arXiv:2301.07943v1, Lemma 2.1, proves that finite atomless measure spaces admit measurable Rademacher-type signs with \(r_nf\rightharpoonup0\) for each \(f\in L^1\). These real signs are \(\pm1\).
2. **Fixed-kernel-vector identity.** Because \(r_n\in\{-1,1\}\),
\[
 \|r_nf-z\|_1=\tfrac12(\|f-z\|_1+\|f+z\|_1)
 +\tfrac12\int r_n(|f-z|-|f+z|)\,d\mu.
\]
The last term vanishes since the integrand without \(r_n\) is in \(L^1\), and the even average equals \(\int\max(|f|,|z|)\) for real scalars.
3. **Correct interchange with infimum.** Suppose a subsequence of infimum distances were smaller than \(\|f\|_1-\varepsilon\). Approximate minimizing \(z_n\in Z\) satisfy \(\|z_n\|_1\leq\|f\|_1+\|r_nf-z_n\|_1\); bounded sequences in finite-dimensional \(Z\) have convergent subsequences. Continuity in \(z\) contradicts Step 2. The candidate \(z=0\) gives the upper limit.
4. **Minimal coset representative.** For each unit coset, the distance to finite-dimensional \(Z\) is attained by coercivity of \(z\mapsto\|f_0-z\|_1\). Choose its norm-one representative \(f\).
5. **WASQ witnesses.** Put \(y_n=q(r_nf)\). Quotient bounded linear maps preserve weak nullness. By the distance law \(\|y_n\|\to1\); since \(1\pm r_n\ge0\), \(\|q(f)\pm y_n\|\leq\int|f|(1\pm r_n)\to1\). Weak lower semicontinuity supplies the lower limits.
6. **Prior implication check.** arXiv:2210.09158v1 Theorem 3.1 claimed full geodesic WASQ, which is why the metric-graph consequence is not being presented as a new theorem. The subsequent arXiv v2 restricts to finitely supported points; neither version claims arbitrary finite-dimensional quotients of atomless real \(L^1\) or the sharp Rademacher distance limit.

No numerical computation or automated independent certificate is asserted. The full analytic argument is contained in RESULT.md; independent audit has not been performed.
