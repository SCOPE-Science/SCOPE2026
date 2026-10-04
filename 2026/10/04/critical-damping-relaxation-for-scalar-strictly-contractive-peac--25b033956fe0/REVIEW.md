# Same-model review

## Correctness
**PASS.** The four scalar updates follow directly from the first-order conditions of the two quadratic subproblems and the two relaxed multiplier updates. Eliminating \(x^{k+1}\) and \(\lambda^{k+1/2}\) gives a two-dimensional linear recurrence. Its determinant and trace are
\[
\det M_\alpha=u^2(1-\alpha)^2,
\qquad
\operatorname{tr}M_\alpha=u^2\alpha^2-2w\alpha+(1+u^2).
\]
Under \(\min\{a,b\}<\beta<\max\{a,b\}\), the endpoint trace is negative. The function setting the negative repeated-root condition is strictly decreasing on \([0,1]\), so the stated root exists uniquely. The determinant lower bound proves all smaller relaxations are slower, and the trace lower bound proves all larger relaxations are slower. The accompanying checker independently reconstructs the recurrence and confirms the identities on rational cases.

## Originality
**PASS.** The 2014 source introduces the common underrelaxation, proves convergence, and reports empirical values near one; it does not state this scalar quadratic exact minimizer. A 2016 symmetric-ADMM paper studies admissible larger step-size regions, and general Douglas–Rachford rate papers study related reflected-resolvent contractions, but the inspected statements do not imply the exact common-relaxation critical-damping formula here. Targeted searches for scalar quadratic, spectral-radius, optimal-relaxation, and critical-damping formulations did not locate an implication-equivalent statement.

The closest limitation is access/comparison rather than a mathematical gap: only the abstract and metadata of the 2016 symmetric-ADMM paper were available for detailed comparison in this review, so an equivalent scalar calculation hidden in later full text or a thesis remains a residual risk.

## Value
**PASS.** The source paper leaves practical selection of its underrelaxation empirical. The smallest strongly convex equality-coupled quadratic is therefore a natural calibration problem rather than an arbitrary slice. The result gives a closed-form parameter rule, explains it structurally as critical damping, and shows that underrelaxation can improve asymptotic speed even where the \(\alpha=1\) endpoint converges. This is useful for interpreting parameter heuristics and for testing broader symmetric-ADMM or Peaceman–Rachford tuning rules.

Same-model review: passed. Independent audit: not yet performed.
