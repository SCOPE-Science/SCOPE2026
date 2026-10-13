# Sharp one-step score loss from right-preconditioned polar updates

## Finding

For every real full-column-rank matrix \(G\in\mathbb R^{m\times n}\) with \(m\ge n\ge2\) and every real symmetric positive-definite \(B\in\mathbb R^{n\times n}\) with spectral condition number \(\kappa\ge1\), define the standard matrix-polar direction \(P_0=\operatorname{polar}(G)\) and the right-preconditioned direction \(P_1=\operatorname{polar}(GB^{-1})\). For the one-step, exact-line-search quadratic score
\[
S_B(P)=\frac{\langle G,P\rangle_F^2}{\operatorname{tr}(PBP^{\mathsf T})},
\]
we have the **sharp universal comparison**
\[
\boxed{\frac{4\kappa}{(\kappa+1)^2}\ \le\ \frac{S_B(P_1)}{S_B(P_0)}\ \le\ 1.}
\]
For fixed \(\kappa>1\), the lower constant is the exact infimum over already \(2\times2\) full-rank inputs. Equality in the upper inequality occurs precisely when \(B\) commutes with \((G^{\mathsf T}G)^{1/2}\). In particular, with output-isotropic curvature, right-preconditioning before polar normalization can make the optimally line-searched objective decrease asymptotically as little as \(4/\kappa\) of the standard polar update's decrease.

## Assumptions and scope

All matrices are real and all operations exact. \(B\succ0\) has least and greatest eigenvalues \(\mu>0\) and \(L\ge\mu\), with \(\kappa=L/\mu\). For each full-column-rank \(M\), its thin orthogonal polar factor is the unique matrix \(\operatorname{polar}(M)=M(M^{\mathsf T}M)^{-1/2}\) with orthonormal columns maximizing \(\langle M,P\rangle_F\) over \(P^{\mathsf T}P=I_n\). The ratio is strictly positive since \(G\) is full rank.

The score is exactly twice the largest decrease, under unrestricted exact line search along \(P\), of the output-isotropic strictly convex quadratic
\[
f(W)=\tfrac12\operatorname{tr}(WBW^{\mathsf T}),\qquad W=GB^{-1},\quad \nabla f(W)=G.
\]
Indeed \(f(W-\eta P)-f(W)=-\eta\langle G,P\rangle_F+\eta^2\operatorname{tr}(PBP^{\mathsf T})/2\), and the maximizer of the decrease is \(\eta=\langle G,P\rangle_F/\operatorname{tr}(PBP^{\mathsf T})\). This is a deterministic specialization of the quadratic score considered for matrix-polar optimizers in the motivating article [1], not a claim about all loss curvatures or all schedules.

## Proof

**Common denominator and upper bound.** Both \(P_i^{\mathsf T}P_i=I_n\), hence \(\operatorname{tr}(P_iBP_i^{\mathsf T})=\operatorname{tr}B\). The polar variational principle gives \(\langle G,P_0\rangle_F=\|G\|_*\ge\langle G,P_1\rangle_F>0\), establishing the upper inequality. Since \(G\) has full column rank, the maximizer of the polar variational principle is unique. Thus equality holds exactly when \(P_0=P_1\). Writing \(G=P_0H\) for \(H=(G^{\mathsf T}G)^{1/2}\succ0\), we have \(GB^{-1}=P_0HB^{-1}\), whose polar factor is \(P_0\) exactly when \(HB^{-1}\) is symmetric positive definite, equivalently when \(H\) commutes with \(B\).

**Scalar spectral inequality.** For each real unit vector \(v\), set \(a=v^{\mathsf T}Bv\), \(b=v^{\mathsf T}B^2v\). The positive semidefinite matrix \((B-\mu I)(LI-B)\) gives \(b\le(L+\mu)a-L\mu\). Minimizing \(a^2/((L+\mu)a-L\mu)\) over \(a\in[\mu,L]\) yields \(4L\mu/(L+\mu)^2\), with the critical point \(a=2L\mu/(L+\mu)\). Consequently
\[
\frac{v^{\mathsf T}Bv}{\|Bv\|_2}\ge\frac{2\sqrt{L\mu}}{L+\mu}=:c_\kappa.
\]
This is the familiar scalar Kantorovich angular inequality; only its application to the polar-direction comparison is asserted here.

**Nuclear-norm lift.** Let \(X=GB^{-1}=U\Sigma V^{\mathsf T}\) be any thin SVD, and write the columns of \(U,V\) as \(u_j,v_j\) and the positive singular values as \(\sigma_j\). Then \(P_1=UV^{\mathsf T}\), \(G=\sum_{j=1}^{n}\sigma_j u_j(Bv_j)^{\mathsf T}\), and
\[
\langle G,P_1\rangle_F=\sum_j\sigma_j v_j^{\mathsf T}Bv_j
\ge c_\kappa\sum_j\sigma_j\|Bv_j\|_2
\ge c_\kappa\|G\|_*.
\]
The last inequality is the nuclear-norm triangle inequality because each summand of \(G\) is rank one and its nuclear norm equals \(\sigma_j\|Bv_j\|_2\). Both score denominators coincide, so squaring proves the claimed lower bound.

**Sharpness under full rank.** Fix \(\kappa>1\), take \(m=n=2\), \(B=\operatorname{diag}(1,\kappa)\), and let \(V=[v_1,v_2]\) be orthogonal with
\[
v_1=\frac{(\sqrt\kappa,1)^{\mathsf T}}{\sqrt{\kappa+1}},\qquad
v_2=\frac{(-1,\sqrt\kappa)^{\mathsf T}}{\sqrt{\kappa+1}}.
\]
For every \(\varepsilon>0\), take \(X_\varepsilon=\operatorname{diag}(1,\varepsilon)V^{\mathsf T}\) and \(G_\varepsilon=X_\varepsilon B\). Both \(X_\varepsilon\) and \(G_\varepsilon\) are invertible. We have \(\operatorname{polar}(X_\varepsilon)=V^{\mathsf T}\), and, as \(\varepsilon\downarrow0\),
\[
\langle G_\varepsilon,\operatorname{polar}(X_\varepsilon)\rangle_F\longrightarrow v_1^{\mathsf T}Bv_1=\frac{2\kappa}{1+\kappa},\qquad
\|G_\varepsilon\|_*\longrightarrow\|Bv_1\|_2=\sqrt\kappa.
\]
Thus the score ratio tends to \(4\kappa/(\kappa+1)^2\), proving optimality of the constant without including any singular matrix in the theorem's domain. For \(\kappa=1\), \(B\) is scalar and \(P_0=P_1\), so the ratio is identically one.

## Verification

The standalone `verify.py` (NumPy required) independently reconstructs full-rank polar factors and both exact-line-search scores. It checks 70 exact rational sharpness identities, 2,160 randomized full-rank rectangular or square instances across six matrix widths, 2,160 explicit quadratic line-search decreases, five nearly rank-one sharpness sequences, and commuting equality tests. It reports:

`VERIFY_OK rational_sharpness=70 random_full_rank_cases=2160 sharp_sequences=5 line_search_cases=2160`

These finite checks are supporting diagnostics. The inequalities, equality characterization, and infimum for all admissible real matrices follow from the argument above.

## Relationship to prior work

Du and Su [1, Proposition 2] prove nonnegative gradient alignment for their right-preconditioned polar direction; [1, Section 4 and Appendix E] define its quadratic score and state that its theoretical score is not otherwise analyzed in that appendix. The present result gives a sharp, sign-definite ratio to the standard polar update specifically when the output-side curvature is isotropic and both directions are orthonormal. It does not contradict [1]'s numerical improvements in models with anisotropic output curvature. Lau, Long, and Su [2] explain matrix-polar optimization and preconditioning, but their inspected treatment does not state this conditioned comparison. The scalar Kantorovich inequality and the polar variational characterization are classical; the source-specific application, global bound, commutation boundary, and full-rank sharpness family constitute the claim.

## Limitations

The result requires full column rank, an SPD right curvature, a Euclidean output-side curvature, exact polar decompositions, and exact one-dimensional line searches. The lower endpoint is an infimum approached by increasingly ill-conditioned but invertible gradient matrices, not attained at a full-rank \(2\times2\) example. The bound is not a finite-precision guarantee, a multi-step convergence theorem, a guarantee about learning-rate rules, or a prediction for anisotropic output curvature, where different direction norms can change the ranking. An equivalent general matrix-alignment inequality could have appeared in older operator-inequality literature under different terminology; no exhaustive absence claim is made.

## References

[1] L. Du and W. Su, *The Newton–Muon Optimizer*, arXiv:2604.01472v1, publicly posted 2026-04-01; Sections 2.3 and 4, Appendix E. https://arxiv.org/abs/2604.01472

[2] T. T.-K. Lau, Q. Long, and W. Su, *PolarGrad: A Class of Matrix-Gradient Optimizers from a Unifying Preconditioning Perspective*, arXiv:2505.21799, 2025; Sections 3–4 and Appendix. https://arxiv.org/abs/2505.21799
