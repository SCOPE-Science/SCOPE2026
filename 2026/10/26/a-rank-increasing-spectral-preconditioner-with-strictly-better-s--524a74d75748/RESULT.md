# A rank-increasing spectral preconditioner with strictly better surrogate error and unbounded conditioning penalty

## Finding

For every real \(r>1\), there exist nested rank-one and rank-two right-orthogonal projection approximations to the same real symmetric positive-definite \(3\times3\) matrix such that the rank-two approximation has a strictly smaller spectral-norm (and Frobenius-norm) error, but a natural singular-value-flattening spectral right preconditioner has strictly worse Euclidean condition number. The ratio of the larger-rank condition number to the smaller-rank condition number is unbounded as \(r\to\infty\).

Specifically, let
\[
A_r=\operatorname{diag}(r^2,r,1),\quad
v=(e_2+e_3)/\sqrt2,\quad
W_1=e_1e_1^\top,\quad W_2=W_1+vv^\top,
\]
where the \(e_j\) are the canonical coordinate vectors. Let \(\widehat A_j=A_rW_j\) and \(\tau=\sqrt{(r^2+1)/2}\). Then
\[
\|A_r-\widehat A_1\|_2=r,
\qquad
\|A_r-\widehat A_2\|_2=\tau<r.
\]

For a rank-\(\ell\) surrogate with compact singular-value decomposition \(\widehat A_\ell=\widehat U_\ell\widehat\Sigma_\ell\widehat V_\ell^\top\), define the unregularized spectral right preconditioner at target level \(s_\ell>0\) by
\[
P_\ell=s_\ell^{-1}\widehat V_\ell\widehat\Sigma_\ell\widehat V_\ell^\top+(I-\widehat V_\ell\widehat V_\ell^\top).
\]
Choose the exact trailing singular-value targets \(s_1=\sigma_2(A_r)=r\) and \(s_2=\sigma_3(A_r)=1\). Then \(P_1=\operatorname{diag}(r,1,1)\) and
\[
P_2=\operatorname{diag}(r^2,1,1)+(\tau-1)vv^\top.
\]
They satisfy
\[
\kappa_2(A_rP_1^{-1})=r,
\qquad
\kappa_2(A_rP_2^{-1})
=\frac{T+\sqrt{T^2-4D}}{2\sqrt D}>r,
\]
where \(T=(r^2+3)/2\) and \(D=2r^2/(r^2+1)\). In particular,
\[
\lim_{r\to\infty}\frac{\kappa_2(A_rP_2^{-1})}{r^2}
=\frac1{2\sqrt2},\qquad
\frac{\kappa_2(A_rP_2^{-1})}{\kappa_2(A_rP_1^{-1})}
\sim\frac r{2\sqrt2}\to\infty.
\]
At \(r=3\), the approximation errors are \(3\) and \(\sqrt5\), whereas the preconditioned condition numbers are \(3\) and \(2+\sqrt5\), respectively.

## Assumptions and scope

All matrices are real, all calculations are in exact arithmetic, and \(r>1\). The normalizing levels \(s_\ell\) equal the respective exact next singular values of \(A_r\), rather than estimates inferred from the surrogate. The surrogates are nested right-orthogonal projections \(A_rW_j\); they are **not asserted to be row/column-sampling CUR outputs**. The preconditioner is the general low-rank spectral formula at regularization \(\mu=0\) from Huh, Cartis and Nakatsukasa [1, §3.1, equation (3.2)], applied algebraically to these surrogates. The claim concerns spectral condition numbers, not iteration counts or floating-point stability.

## Proof

The projectors are nested because \(e_1\perp v\) and each projector's columns are orthonormal. The rank-one discarded subspace is \(\operatorname{span}\{e_2,e_3\}\), so \(A_r(I-W_1)=\operatorname{diag}(0,r,1)\) has operator norm \(r\). On \(\operatorname{span}\{e_2,e_3\}\), \(I-W_2\) projects onto \(w=(e_2-e_3)/\sqrt2\); consequently
\[
A_r(I-W_2)=(A_rw)w^\top,
\quad \|A_rw\|_2=\sqrt{(r^2+1)/2}=\tau.
\]
This rank-one error has the same spectral and Frobenius norm \(\tau\), whereas the rank-one surrogate has Frobenius error \(\sqrt{r^2+1}\). Hence both errors strictly improve on increasing the rank.

The compact singular values of \(\widehat A_1\) and \(\widehat A_2\) are, respectively, \(r^2\) and \((r^2,\tau)\); the latter has right singular space spanned by \(e_1,v\). The displayed formulas for \(P_1,P_2\) follow immediately from the preconditioner definition. Their positive eigenvalues make both invertible. It follows that \(A_rP_1^{-1}=\operatorname{diag}(r,r,1)\).

Write \(B_r=\operatorname{diag}(r,1)[I_2+(\tau^{-1}-1)\widetilde v\widetilde v^\top]\), with \(\widetilde v=(1,1)^\top/\sqrt2\). The second preconditioned matrix is orthogonally block-diagonal with blocks \(1\) and \(B_r\). The eigenvalues \(\lambda_-\le\lambda_+\) of \(G_r=B_r^\top B_r\) have sum
\[
\operatorname{tr}G_r=(r^2+1)+\frac{r^2+1}{2}(\tau^{-2}-1)
=\frac{r^2+3}{2}=T
\]
and product
\[
\det G_r=(\det B_r)^2=r^2/\tau^2
=\frac{2r^2}{r^2+1}=D.
\]
Since \(\det(I_2-G_r)=1-T+D=-(r^2-1)^2/[2(r^2+1)]<0\), the two eigenvalues straddle \(1\). Thus the three squared singular values of \(A_rP_2^{-1}\) are ordered \(\lambda_-<1<\lambda_+\), and
\[
\kappa_2(A_rP_2^{-1})=\sqrt{\lambda_+/\lambda_-}
=\lambda_+/\sqrt{D}=(T+\sqrt{T^2-4D})/(2\sqrt D).
\]
To prove this condition number strictly exceeds \(r\), observe that for every \(k>1\), \(k\mapsto k+k^{-1}\) is strictly increasing. Here
\[
\kappa_2(A_rP_2^{-1})+\kappa_2(A_rP_2^{-1})^{-1}=T/\sqrt D,
\]
while the exact identity
\[
T^2-D(r+r^{-1})^2=(r^2-1)^2/4>0
\]
implies \(T/\sqrt D>r+r^{-1}\). Hence the desired strict inequality holds for every \(r>1\), not just asymptotically. Finally \(T\sim r^2/2\), \(D\to2\) and \(\lambda_+\sim T\) establish the limiting formula. Substituting \(r=3\) gives \(T=6\), \(D=9/5\), and the stated exact witness.

## Verification

The self-contained `check.py` evaluates the two preconditioned singular-value condition numbers and both approximation errors directly from the defined matrices for ten real parameter values. Symbolic identities for \(\operatorname{tr}G_r\), \(\det G_r\), the straddling test, and the strict-condition comparison are also checked using exact polynomial cancellation. The proof above, rather than the sampled numerical checks, establishes the quantified statements for all \(r>1\).

## Relationship to prior work

Huh, Cartis and Nakatsukasa [1] introduce the general spectral preconditioner formula used here, analyze conditional approximation-error bounds, and discuss the hazards of over-preconditioning and rank selection. Their paper does not, in the inspected statements of §3.1, §4.1, §7.2, and Appendix A, furnish this nested-projection family or the opposite trends in approximation error and condition number. The perturbation assumptions underlying their condition-number estimate do not apply here when \(\mu=0\). Kahl and Rittich [2] examine effective conditioning for deflated conjugate gradients with approximate invariant subspaces, a distinct singular projection-based construction; the relevant small-angle perturbation regimes do not imply the present finite-angle and growing-rank result.

## Limitations

These nested projection surrogates need not arise in an actual incremental CUR column/row-selection algorithm, and the result does not diagnose any specific sampling implementation. Targets are externally specified exact trailing singular values; alternative target choices or regularization may behave differently. Large preconditioned condition number does not by itself imply slow LSQR on any specified right-hand side, and no runtime/iteration complexity is asserted. Prior work in different spectral-preconditioning conventions could contain an equivalent construction; a full historical uniqueness claim is not made.

## References

[1] J. E. Huh, C. Cartis and Y. Nakatsukasa, *Adaptive LSQR Preconditioning from One Small Sketch*, arXiv:2604.05065v1 (2026-04-06), §§3.1, 4.1, 7.2, Appendix A. https://arxiv.org/html/2604.05065v1

[2] K. Kahl and H. Rittich, *Analysis of the Deflated Conjugate Gradient Method Based on Symmetric Multigrid Theory*, arXiv:1209.1963, especially the approximate-eigenspace condition-number discussion. https://arxiv.org/abs/1209.1963
