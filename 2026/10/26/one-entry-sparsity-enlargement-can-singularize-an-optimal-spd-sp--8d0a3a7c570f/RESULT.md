# One-entry sparsity enlargement can singularize an optimal SPD sparse approximate inverse

## Finding
For each positive-definite real matrix \(A\), let \(M_{\mathcal J}\) denote the unique **fixed-pattern**, Frobenius-optimal right sparse approximate inverse, minimizing \(\|I-AM\|_F^2\) over matrices supported in the permitted pattern \(\mathcal J\). Inclusion of sparsity patterns decreases this objective but need not preserve the nonsingularity of \(M_{\mathcal J}\), even when \(A\) is symmetric positive definite (SPD) and the original pattern contains all diagonal positions.

**Exact three-dimensional obstruction.** Put
\[
A_0=\begin{pmatrix}1&1&1\\1&3&5\\1&5&10\end{pmatrix},\qquad
\mathcal J_0=\{(1,1),(2,2),(3,3)\},\qquad
\mathcal J_1=\mathcal J_0\cup\{(1,2)\}.
\]
The two unique minimizers are
\[
M_0=\operatorname{diag}(1/3,3/35,5/63),\qquad
M_1=\begin{pmatrix}1/3&1/3&0\\0&0&0\\0&0&5/63\end{pmatrix}.
\]
Then \(M_0\) is invertible but \(M_1\) has rank two, despite the strict residual improvement
\[
\|I-A_0M_0\|_F^2=509/315,
\qquad\|I-A_0M_1\|_F^2=97/63,
\qquad \Delta=8/105>0.
\]
Dimension three is the smallest dimension in which enlarging the full diagonal pattern by **one** position can produce a singular Frobenius-optimal approximate inverse for SPD input.

**Robust spectral deterioration.** For \(0<\varepsilon<\sqrt{18}-4\), set
\[
A_\varepsilon=\begin{pmatrix}1&1&1\\1&3&5+\varepsilon\\1&5+\varepsilon&10\end{pmatrix}.
\]
Each \(A_\varepsilon\) is SPD. Both fixed-pattern minimizers are nonsingular for \(\varepsilon>0\); the enriched one satisfies
\[
\det M_1(\varepsilon)=
-\frac{5\varepsilon}{3(\varepsilon^2+6\varepsilon+12)(\varepsilon^2+10\varepsilon+126)},
\]
while its squared objective is strictly smaller, with exact gap
\[
\|I-A_\varepsilon M_0(\varepsilon)\|_F^2-
\|I-A_\varepsilon M_1(\varepsilon)\|_F^2
=\frac{(\varepsilon^2+7\varepsilon+8)^2}{2(\varepsilon^2+6\varepsilon+12)(\varepsilon^2+10\varepsilon+35)}>0.
\]
Nevertheless, as \(\varepsilon\downarrow0\),
\[
\kappa_2(A_\varepsilon M_1(\varepsilon))=\Theta(\varepsilon^{-1}),
\quad \kappa_2(A_\varepsilon M_0(\varepsilon))=O(1),
\quad \kappa_2(A_\varepsilon)=O(1).
\]
Thus arbitrarily severe conditioning deterioration is possible under a **strictly improving** one-entry Frobenius pattern enlargement, even in a SPD family with uniformly bounded input condition number.

## Assumptions and scope
All matrices are real, calculations are in exact arithmetic, and the Frobenius minimization uses a prescribed **permitted** support (coefficients at permitted positions may be zero). Matrix \(A\) is SPD. Coordinates in the displayed patterns are one-based. Define the right-preconditioned matrix as \(AM\); since transposing a nonsingular SPD matrix exchanges left and right approximate-inverse constructions, the corresponding left preconditioner is equally affected by rank collapse. No claim is made that a specified adaptive implementation must select the indicated entry.

For a general \(n\times n\) nonsingular \(A\) and pattern \(\mathcal J\), the minimizer is unique when each selected submatrix of columns of \(A\) has full column rank; this holds for SPD \(A\) and any pattern of distinct column positions. The admissible matrix \(M\) may have fewer *actual* nonzeros than positions in the support allowance.

## Proof
**(1) Unique columnwise optimizers.** Frobenius separability gives
\[
\min_{\operatorname{supp}(M)\subseteq\mathcal J}\|I-AM\|_F^2
=\sum_{j=1}^n \min_{\operatorname{supp}(m_j)\subseteq\mathcal J_j}\|e_j-Am_j\|_2^2.
\]
For a diagonal-only pattern, the unique coefficient at \((j,j)\) equals \(a_{jj}/\|Ae_j\|_2^2>0\) for SPD \(A\). In the example the leading principal minors of \(A_0\) are \(1,2,2\), so \(A_0\succ0\). Its column norms squared are \(3,35,126\), yielding \(M_0\) as displayed.

**(2) Exact rank collapse.** Only the second fitted column changes upon allowing position \((1,2)\). With \(u=A_0e_1=(1,1,1)^\mathsf T\) and \(v=A_0e_2=(1,3,5)^\mathsf T\), the normal equations are
\[
\begin{pmatrix}3&9\\9&35\end{pmatrix}
\begin{pmatrix}c_1\\c_2\end{pmatrix}
=\begin{pmatrix}1\\3\end{pmatrix}.
\]
Their unique solution is \((c_1,c_2)=(1/3,0)\). Therefore the enriched matrix has a zero second row and rank two, whereas the original diagonal matrix is invertible. The squared residual for the second column changes from \(1-9/35=26/35\) to \(1-1/3=2/3\), a strict improvement \(8/105\); every other fitted column is unchanged. Summing their squared residuals gives the stated total objectives.

**(3) Minimal dimension.** Dimension one has no additional off-diagonal position. In dimension two, after adding exactly one off-diagonal position to the full diagonal pattern, the resulting optimal matrix is triangular. Its untouched diagonal coefficient is positive by the diagonal formula; its other diagonal coefficient is \((A^{-1})_{jj}>0\), since the enriched column uses both columns of \(A\) and is exactly \(A^{-1}e_j\). Hence its determinant is nonzero. This exhausts both possible single-position additions and proves minimality. Direct sums with identity extend the obstruction to all \(n\ge3\).

**(4) Perturbation and the gap.** The leading principal minors of \(A_\varepsilon\) are \(1,2,2-8\varepsilon-\varepsilon^2\), all positive on the stated interval. The only changed coefficient pair solves
\[
\begin{pmatrix}3&9+\varepsilon\\9+\varepsilon&35+10\varepsilon+\varepsilon^2\end{pmatrix}
\begin{pmatrix}c_1\\c_2\end{pmatrix}=
\begin{pmatrix}1\\3\end{pmatrix},
\]
so
\[
c_1=\frac{\varepsilon^2+7\varepsilon+8}{2(\varepsilon^2+6\varepsilon+12)},\qquad
c_2=-\frac{\varepsilon}{2(\varepsilon^2+6\varepsilon+12)}.
\]
The untouched diagonal coefficients are \(1/3\) and \(10/(\varepsilon^2+10\varepsilon+126)\). Consequently \(M_1(\varepsilon)\) is upper triangular, and multiplication of its diagonal entries gives the displayed determinant. The baseline diagonal coefficient for column two is \(3/(\varepsilon^2+10\varepsilon+35)\). Orthogonal least-squares projection yields the exact objective improvement as written (or substitute these coefficients into the squared norms), which is positive throughout the stated interval.

**(5) Diverging conditioning.** As \(\varepsilon\downarrow0\), the matrices \(A_\varepsilon M_1(\varepsilon)\) converge to \(A_0M_1\), which has rank exactly two. Both its nonzero singular values therefore remain bounded above and bounded away from zero for small positive \(\varepsilon\) by singular-value continuity. Their product, multiplied by the smallest singular value, equals \(|\det(A_\varepsilon M_1(\varepsilon))|=\Theta(\varepsilon)\). Thus the smallest singular value is \(\Theta(\varepsilon)\), giving the asserted \(\Theta(\varepsilon^{-1})\) condition number. The diagonal baseline preconditioner and \(A_\varepsilon\) converge to invertible limits, hence their condition numbers remain bounded.

## Verification
The accompanying `verify_spai.py` independently forms each least-squares normal equation using exact rational arithmetic, checks both optimal matrices and exact objective values, checks determinants and positive leading principal minors, then tests nine rational perturbations and a grid of two-dimensional SPD cases. It uses only the Python standard library; run `python verify_spai.py`. Its finite test set is a reproducibility check, not a substitute for Steps (1)–(5) of the proof.

## Relationship to prior work
The fixed-pattern Frobenius SPAI objective and its columnwise least-squares construction are classical; they are prominently used in Carson and Khan's 2022 SPAI-GMRES iterative-refinement framework [1] and in earlier Huckle and Ferronato treatments [2,3,4]. The 2012 review already states the qualitative fact that unfactored SPAI on SPD input need not itself be SPD [3], which is **not** claimed as novel. The present finding isolates a stronger and more specific behavior: one strictly beneficial support enlargement can destroy invertibility, dimension three is minimal for the specified operation, and nearby SPD matrices give unbounded *relative conditioning deterioration* with strictly decreasing Frobenius objective. Positive-definite or invertibility-preserving factored methods are not addressed.

## Limitations
This is a small explicit obstruction, not an instability-frequency statement. In particular, the example's residual is not so small that a norm-\(<1\) Neumann argument would guarantee invertibility, so it does not contradict such convergence bounds. The prescribed enlargement is admissible but is not shown to be chosen by any particular adaptive rule. Exact arithmetic is essential to the rank-collapse statement; finite-precision rounding, regularization, threshold stopping, factorized approximate inverses, and Krylov iteration counts are not analyzed. The original 1997 SPAI paper could not be read in full through available authorized access; priority relative to possible special examples or equivalent constructions therein remains a genuine risk.

## References
[1] E. Carson and N. Khan, *Mixed Precision Iterative Refinement with Sparse Approximate Inverse Preconditioning*, arXiv:2202.10204v1 (2022-02-21). https://arxiv.org/abs/2202.10204

[2] T. Huckle and M. Sedlacek, *Smoothing and Regularization with Modified Sparse Approximate Inverses* (2010). https://doi.org/10.1155/2010/930218

[3] M. Ferronato, *Preconditioning for Sparse Linear Systems at the Dawn of the 21st Century* (2012). https://doi.org/10.5402/2012/127647

[4] M. Grote and T. Huckle, *Parallel Preconditioning with Sparse Approximate Inverses* (1997). https://doi.org/10.1137/S1064827594276552
