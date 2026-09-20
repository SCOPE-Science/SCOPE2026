# Review — sharp row-coherence obstruction in PDNQP diagonal steps

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The central identity is exact: the PDNQP dual mass makes every row of \(K=M_y^{-1/2}BM_w^{-1/2}\) have norm one, so \(\|K\|_F^2=m\) and \(\|K\|_2\le\sqrt m\). The source step matrices give \(S^{1/2}BT^{1/2}=0.99K\), with the primal/dual balancing parameter canceling.

For the family \(B=[\mathbf1_{m\times p},I_m,-I_m]\), \(H=I\), and unit residual penalties, the source mass formulas give shared primal mass \(m+1\), private and residual masses \(2\), and dual mass \(p/(m+1)+1\). The resulting Gram matrix
\[
KK^T=\frac{a}{a+1}\mathbf1\mathbf1^T+\frac1{a+1}I_m,
\qquad a=\frac{p}{m+1},
\]
has largest eigenvalue \((ma+1)/(a+1)\), proving asymptotic sharpness. The original equality matrix \([\mathbf1,I_m]\) is full row rank, and its entries are already infinity-norm equilibrated.

The explicit rejected-direction certificate uses a top singular pair of \(K\). On this signed block family, the componentwise absolute coupling term has no cancellation and equals \(0.99\|K\|_2\), while the metric left-hand side is one and the Hessian contribution is nonnegative. Hence \(0.99\|K\|_2>1\) forces failure of the cited acceptance inequality. Numerical verification agrees with all closed forms to floating-point precision.

The row-\(\ell_1\) comparison bound follows from a direct weighted AM--GM/Schur estimate. It is explicitly restricted to control of the coupling operator and is not presented as a complete replacement for the source acceptance mechanism.

## Originality

**PASS, to the best of our knowledge.** The motivating PDNQP preprint is very recent. Searches were made for the paper title/acronym, its diagonal preconditioning formulas, row-normalized primal--dual step rules, coherent-row counterexamples, and equivalent operator-normalization formulations. The SCOPE archive was also checked for PDNQP and synonymous row-coherence/diagonal-step claims. No overlapping record or public source-specific correction was located.

The originality claim is deliberately narrow. The following are prior knowledge and are not claimed new: PDHG operator-norm step conditions; diagonal primal--dual preconditioning; Schur-test bounds; Ruiz equilibration; and the elementary fact that unit row norms do not in general bound spectral norm by a constant. Pock--Chambolle (2011) already gives diagonal preconditioners with convergence guarantees in a general convex primal--dual setting.

The claimed contribution is the exact identification of the 2026 PDNQP dual mass as row normalization of its residual-form coupling, the sharp \(\sqrt m\) obstruction under the source primal masses, a full-row-rank infinity-equilibrated family attaining the obstruction asymptotically, and a top-singular-direction certificate that directly violates the source acceptance inequality.

Residual originality risk remains because the source is new and contemporaneous follow-up notes may not yet be indexed. Older diagonal-preconditioning literature may contain related generic coherence examples, but no inspected source was found to specialize them to this PDNQP formula and acceptance test. This review therefore makes only a to-the-best-of-our-knowledge claim.

## Value

**PASS.** The result identifies a concrete global quantity omitted by the initialization: normalized row coherence. It shows that the gap can be as large as \(\sqrt m\) even when the original constraints are linearly independent and standard infinity-norm equilibration has nothing left to change. The explicit failure direction explains why the adaptive acceptance safeguard can be genuinely active rather than merely conservative, and the comparison with row-\(\ell_1\) scaling separates rowwise normalization from operator control.

## Limitations

The family is adversarial and structured, and no claim is made that benchmark distributions approach the worst case. The result does not establish divergence, an end-to-end complexity lower bound, or a superiority theorem for an alternative preconditioner. It concerns the source initialization and its acceptance inequality. Any later revision of the recent PDNQP preprint may alter the relevant formulas or discussion and should be checked against this record.
