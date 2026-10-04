# A \(\sqrt{2}\) projective-instability law for three-mode rank-compressed LMSD

## Finding

Consider the exact-arithmetic rank-compressed weighted LMSD method of Yang--Yuan with nominal history length \(p=2\) on a strictly convex quadratic whose nonterminating active subspace has exactly three distinct eigenvalues \(0<\lambda_1<\lambda_2<\lambda_3\). Let the fixed positive spectral weight be \(W=\omega(H)\), write \(w_i=\omega(\lambda_i)>0\), and let \(u_k=g_{k,0}\) be the block-start gradients in the active eigenbasis. Then every \(u_k\) has all three active coordinates, and the extreme-mode ratio \(R_k=|u_k^{(1)}/u_k^{(3)}|\) satisfies the exact delayed recurrence \[R_{k+2}=C_W\frac{R_{k+1}}{R_k^2},\qquad C_W=\frac{(\lambda_3-\lambda_2)w_3}{(\lambda_2-\lambda_1)w_1}.\] With \(R_*=\sqrt{C_W}\) and \(z_k=\log(R_k/R_*)\), this becomes \(z_{k+2}=z_{k+1}-2z_k\). Hence either \(R_0=R_1=R_*\) and \(R_k\equiv R_*\), or \[\limsup_{k\to\infty}|z_k|^{1/k}=\sqrt{2},\qquad \limsup_{k\to\infty}R_k=\infty,\qquad \liminf_{k\to\infty}R_k=0.\] Thus, in the smallest nonterminating spectral dimension for \(p=2\), the normalized spectral composition is projectively unstable and repeatedly approaches finite-termination boundary strata even though the published theorem gives R-linear decay of the gradient norm.

## Assumptions and scope

Let \(H\succ0\) be the Hessian of a strictly convex quadratic after translating the minimizer to the origin. Restrict to a nonterminating active invariant subspace with exactly three distinct eigenvalues \(0<\lambda_1<\lambda_2<\lambda_3\), and use nominal history length \(p=2\). Let the fixed spectral weight be \(W=\omega(H)\succ0\), with \(w_i=\omega(\lambda_i)\). The statement concerns exact algebraic rank compression and exact arithmetic. The standard method is \(W=I\); harmonic-Ritz LMSD is \(W=H\); fixed power weights \(W=H^a\) are also included.

Yang--Yuan prove that a nonterminating rank-compressed run has more than \(p\) active modes at every block start. In the present three-mode case with \(p=2\), every block-start gradient therefore has all three coordinates nonzero, so every ratio below is well defined and every history has effective rank two.

## Proof

First take the standard weight \(W=I\). Yang--Yuan's complete-sweep formula for a regular \(p=2\) block starting from \(u=(u_1,u_2,u_3)^T\) is
\[
\psi_u(\lambda_r)=\frac{\sum_{{|I|=2}}\beta_I\phi_I^{(r)}}{\sum_{{|I|=2}}\beta_I},
\]
where
\[
\beta_{{ij}}=(\lambda_j-\lambda_i)^2\lambda_i\lambda_j u_i^2u_j^2,
\qquad
\phi_{{ij}}^{(r)}=\left(1-\frac{{\lambda_r}}{{\lambda_i}}\right)\left(1-\frac{{\lambda_r}}{{\lambda_j}}\right).
\]
At \(r=1\), every pair containing index \(1\) vanishes, so only \(I=\{{2,3\}}\) survives. At \(r=3\), only \(I=\{{1,2\}}\) survives. Cancelling the common denominator and simplifying gives
\[
\frac{{\psi_u(\lambda_1)}}{{\psi_u(\lambda_3)}}
=
\frac{{\lambda_3-\lambda_2}}{{\lambda_2-\lambda_1}}
\left(\frac{{u_3}}{{u_1}}\right)^2.
\]
The delayed endpoint recurrence is \(u_{{k+2}}=\psi_{{u_k}}(H)u_{{k+1}}\). Therefore, with \(R_k=|u_k^{(1)}/u_k^{(3)}|\),
\[
R_{{k+2}}
=
\frac{{\lambda_3-\lambda_2}}{{\lambda_2-\lambda_1}}
\frac{{R_{{k+1}}}}{{R_k^2}}.
\]

For a fixed positive spectral weight, Yang--Yuan's conjugacy uses \(S=W^{{1/2}}\) and \(\widetilde u_k=Su_k\), with exactly the same extracted stepsizes. Thus
\[
\widetilde R_k=\sqrt{{\frac{{w_1}}{{w_3}}}}R_k.
\]
Substitution into the standard recurrence yields
\[
R_{{k+2}}=\frac{{(\lambda_3-\lambda_2)w_3}}{{(\lambda_2-\lambda_1)w_1}}\frac{{R_{{k+1}}}}{{R_k^2}}=C_W\frac{{R_{{k+1}}}}{{R_k^2}}.
\]
Its positive fixed ratio is \(R_*=\sqrt{{C_W}}\). Taking \(z_k=\log(R_k/R_*)\) gives the exact linear recurrence
\[
z_{{k+2}}=z_{{k+1}}-2z_k.
\]
The characteristic roots are
\[
\rho_\pm=\frac{{1\pm i\sqrt7}}2,
\qquad |\rho_\pm|=\sqrt2.
\]
Hence every nonzero solution has \(\limsup |z_k|^{{1/k}}=\sqrt2\). The recurrence cannot be eventually one-signed: if two consecutive values are positive, then either the next value is nonpositive or, if it remains positive, the following value is negative; the same argument applies after multiplying by \(-1\). Because nonzero solutions have exponentially growing state norm while runs of one sign have uniformly bounded length, positive and negative subsequences are both unbounded. Consequently \(\limsup z_k=+\infty\) and \(\liminf z_k=-\infty\), which is equivalent to \(\limsup R_k=\infty\) and \(\liminf R_k=0\). The only zero log-state is \(z_0=z_1=0\), i.e. \(R_0=R_1=R_*\), and it remains fixed.

Finally, Yang--Yuan's global theorem still supplies R-linear decay of the block-start gradients. Thus decay in norm and instability of the projective extreme-mode ratio coexist. Since every subsequence of normalized block-start directions has a convergent subsubsequence, any subsequence with \(R_k\to\infty\) has a limit with the third extreme mode absent, and any subsequence with \(R_k\to0\) has a limit with the first extreme mode absent. These are boundary states with at most two active modes, exactly the finite-termination threshold for \(p=2\).

## Verification

The proof is algebraic and does not rely on numerical evidence. The bundled checker `verify_projective.py` independently evaluates the published determinant-ratio complete-sweep formula in high-precision decimal arithmetic for \(H=\operatorname{{diag}}(1,2,5)\), generates a compatible warm-up pair, and verifies the ratio recurrence over several delayed sweeps. The accepted package was replayed from the bundled path and returned `VERIFY_OK`.

## Relationship to prior work

Yang--Yuan establish finite termination when the active support has at most \(p\) eigenvalues, expose a three-dimensional \(p=2\) rank-changing limit, derive the determinant/Cauchy--Binet complete-sweep representation, and prove global R-linear convergence for standard and fixed-weight rank-compressed LMSD. Their paper does not state the three-mode extreme-ratio recurrence or the resulting \(\sqrt2\) log-projective instability.

Ferrandi--Hochstenbach review LMSD, its Ritz extraction, and numerical rank/conditioning issues. Curtis--Guo prove R-linear convergence for LMSD on strongly convex quadratics. The present statement is compatible with those norm-convergence results: it concerns projective spectral composition rather than failure of convergence. Targeted searches for three-mode, projective, ratio-recurrence, rank-loss, and weighted-LMSD formulations found no implication-equivalent statement in the inspected literature.

## Limitations

The result is exact-arithmetic and quadratic. It assumes a fixed positive spectral weight and exactly three active distinct eigenvalues with \(p=2\); it does not claim the same closed recurrence for larger supports, trajectory-dependent weights, nonquadratic objectives, or finite-precision rank truncation. The originality search was targeted rather than exhaustive, so an older equivalent result under different spectral-gradient notation remains a residual literature risk.

## References

1. S. Yang and Y.-x. Yuan, *Global and Unconditional R-Linear Convergence of Rank-Compressed Weighted LMSD Sweeps for Strictly Convex Quadratics*, arXiv:2609.12114v1, 2026.
2. G. Ferrandi and M. E. Hochstenbach, *Limited memory gradient methods for unconstrained optimization*, Numerical Algorithms 99 (2025), 735--764, DOI 10.1007/s11075-024-01895-9.
3. F. E. Curtis and W. Guo, *R-Linear Convergence of Limited Memory Steepest Descent*, IMA Journal of Numerical Analysis 38 (2018), 720--742, DOI 10.1093/imanum/drx016.
