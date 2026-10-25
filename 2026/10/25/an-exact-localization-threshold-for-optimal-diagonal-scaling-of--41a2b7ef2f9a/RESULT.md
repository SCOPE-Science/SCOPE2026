# An exact localization threshold for optimal diagonal scaling of one-spike matrices

## Finding
For every integer \(n\ge3\), parameters \(t,a,b>0\), and \(k=n-1\), consider the positive-definite one-spike matrix
\[
 A=I_n+tuu^{\mathsf T},\qquad u=(a,b,\ldots,b)^{\mathsf T}.
\]
Let \(\kappa(B)=\lambda_{\max}(B)/\lambda_{\min}(B)\). Minimize \(\kappa(DAD)\) over **all** real positive diagonal matrices \(D\), modulo a common positive scalar. Define
\[
 P=1+ta^2,\quad Q=1+tkb^2,\quad
 r=\frac{tab\sqrt{k}}{\sqrt{PQ}}\in(0,1).
\]
There exists a global minimizing diagonal matrix of the form \(D_*={\rm diag}(x_*,1,\ldots,1)\), where
\[
 x_*=\begin{cases}1,&a^2\le kb^2,\\
 \sqrt{Q/P},&a^2>kb^2.
 \end{cases}
\]
The global optimal condition number is exactly
\[
 \kappa_*=\begin{cases}
 1+t(a^2+kb^2),&a^2\le kb^2,\\
 (1+r)/(1-r),&a^2>kb^2.
 \end{cases}
\]
Consequently, **no diagonal congruence scaling can improve the condition number of the unscaled matrix when the exceptional coordinate carries at most half the spike's squared mass**; strict improvement is possible precisely when \(a^2>kb^2\). This classification includes all nonsymmetric diagonal scalings of the \(k\) exchangeable coordinates, rather than assuming equal scaling a priori.

For example, take \(n=5,t=b=1,a=3\). Then the unscaled condition number is \(14\); the optimal scaling \(D_*={\rm diag}(1/\sqrt2,1,1,1,1)\) achieves
\[
 \kappa_*=(43+30\sqrt2)/7<14.
\]
In contrast, conventional Jacobi diagonal equilibration has condition number
\[
 \kappa_{\rm Jac}=
 \frac{7+\sqrt{189/5}}{7-\sqrt{189/5}}>14.
\]
Thus on this same natural spike family, Jacobi equilibration can make conditioning **worse than leaving the matrix unchanged**, even when a different diagonal scaling improves it.

## Assumptions and scope
The statement concerns the spectral condition number of the symmetrically preconditioned SPD matrix \(DAD\), not the generally different condition number of a one-sided matrix \(DA\). Parameters satisfy \(n\in\{3,4,\ldots\}\) and \(t,a,b>0\). The one-spike matrix is full rank. Diagonal factors may be arbitrary positive numbers, with no condition-number or proximity constraint on \(D\) itself. Relative signs of \(a,b\) are irrelevant by a diagonal orthogonal similarity; positivity fixes a convenient convention. The result makes no claim about numerical solver runtime or finite-precision effects.

## Proof
**1. Symmetrization does not restrict the global optimum.** Fix any positive diagonal \(D\) with \(K=\kappa(DAD)\), and let \(\lambda=\lambda_{\min}(DAD)>0\). The diagonal matrix \(Z=\lambda D^{-2}\) obeys the exact pair of Löwner inequalities \(Z\preceq A\preceq KZ\). For each permutation \(G\) of the last \(k\) coordinates, \(GAG^{\mathsf T}=A\), so \(GZG^{\mathsf T}\preceq A\preceq K GZG^{\mathsf T}\). Their arithmetic average is a positive diagonal matrix \(\bar Z={\rm diag}(z_1,z,\ldots,z)\) satisfying the same inequalities. Setting \(\bar D=\bar Z^{-1/2}\) yields \(I\preceq\bar D A\bar D\preceq K I\); hence \(\kappa(\bar D A\bar D)\le K\). Thus no asymmetric scaling can outperform the best two-level scaling. Multiplying \(\bar D\) by a common positive number permits the normalization \(D={\rm diag}(x,1,\ldots,1)\), \(x>0\).

**2. Exact two-dimensional block.** The \((n-2)\)-dimensional subspace of vectors with zero first coordinate and remaining coordinates summing to zero is an invariant eigenspace of \(DAD\) with eigenvalue \(1\). On the orthogonal complement spanned by the first coordinate and the normalized all-ones vector in the last \(k\) coordinates, the matrix is
\[
 B(x)=\begin{pmatrix}Px^2& tab\sqrt{k}\,x\\tab\sqrt{k}\,x&Q\end{pmatrix}.
\]
Its determinant is \(x^2(PQ-t^2a^2b^2k)=x^2(1+t(a^2+kb^2))>0\). Its eigenvalues \(\lambda_+(x)>\lambda_-(x)>0\) satisfy \(\lambda_+(x)>1\), and
\[
 \det(B(x)-I_2)=t k b^2(x^2-1).
\]
Therefore \(\lambda_-<1\) for \(0<x<1\), \(\lambda_-=1\) for \(x=1\), and \(\lambda_->1\) for \(x>1\). The full matrix has spectrum \(\{1\ \text{(multiplicity }n-2),\lambda_-(x),\lambda_+(x)\}\).

**3. Optimize all two-level scalings.** For \(0<x\le1\), the full condition number equals \(\lambda_+(x)/\lambda_-(x)\). For a positive \(2\times2\) matrix with ordered eigenvalues, this quotient is strictly increasing in \(\operatorname{tr}(B)/\sqrt{\det(B)}\). Here the latter is
\[
 \frac{Px+Q/x}{\sqrt{PQ-t^2a^2b^2k}}.
\]
By the arithmetic–geometric mean inequality, it has its unique minimum over positive \(x\) at \(x_0=\sqrt{Q/P}\). Its constrained minimum over \((0,1]\) is attained at \(\min\{1,x_0\}\). For \(x\ge1\), the full condition number equals \(\lambda_+(x)\), which is strictly increasing: the symmetric \(B(x)\) has strictly positive entries, its top eigenvector can be chosen strictly positive, and \(d\lambda_+(x)/dx>0\) by differentiating the Rayleigh quotient. Hence the global minimizer in the two-level class is \(x_*=\min\{1,\sqrt{Q/P}\}\), giving the claimed threshold \(a^2=kb^2\).

At \(x_*=1\), \(DAD=A\) has eigenvalues \(1\) and \(1+t(a^2+kb^2)\). For \(P>Q\), the optimal block has equal diagonal entries \(Q\), and off-diagonal entry \(Q r\), so its eigenvalues are \(Q(1\pm r)\). Since \(x_*<1\), their quotient is the full condition number. This proves the piecewise expression, including the equality boundary.

**4. Exact Jacobi comparison.** For the given five-dimensional example, \(P=10,Q=5,k=4\); thus \(x_*=1/\sqrt2\), \(r=6/\sqrt{50}=3\sqrt2/5\), and the stated optimal ratio follows. The Jacobi congruence factor is proportional to \({\rm diag}(1/\sqrt5,1,1,1,1)\); its two exceptional eigenvalues are \((7\pm\sqrt{189/5})/2\), straddling the other three eigenvalues \(1\). The strict inequalities follow by squaring positive radicals (or by direct rational comparison), completing the example.

## Verification
A standalone standard-library Python script `verify.py` checks the closed formulas against independent eigenvalue computations for deterministic random inputs and tests nonexchangeable diagonal scalings. It also checks the stated exact five-dimensional example. These finite computations are sanity checks only; global optimality in every dimension follows from the exact Löwner symmetrization and scalar optimization above.

## Relationship to prior work
The optimal-diagonal-preconditioning problem and its semidefinite feasibility formulations are established by Qu, Gao, Hinder, Ye and Zhou (2022). Kunstner, Portella, Schmidt and Harvey (2023) motivate searching for optimal per-coordinate steps. Braatz and Morari (1994) give general convex-optimization formulations for minimizing scaled Euclidean condition numbers; Demmel (2023) gives general near-optimality results for Jacobi and block-Jacobi. The proved contribution here is a closed, dimension-uniform phase classification and exact minimizer for a structured one-spike family, together with an exact example where Jacobi equilibration degrades a matrix for which another diagonal scaling strictly helps. General-purpose optimizers do not themselves state this threshold or exact model-specific formula. Related older scaling literature may contain differently formulated special cases; this remains a priority for independent verification.

## Limitations
This is a closed-form special-family theorem, not an algorithm or general diagonal-scaling solution for arbitrary SPD matrices. No uniqueness is asserted among **all** optimal diagonal matrices; only a globally optimal exchangeable representative is exhibited. No statement about convergence rates beyond their condition-number dependence is made. The identity baseline is optimal in one parameter regime, not universally. The older special-case scaling literature, notably Shapiro (1985) and the inaccessible full text of Demmel (2023), has not been exhaustively ruled out as containing an equivalent exact formula.

## References
1. Z. Qu, W. Gao, O. Hinder, Y. Ye and Z. Zhou, *Optimal Diagonal Preconditioning*, arXiv:2209.00809v1, first public 2022-09-02, https://arxiv.org/abs/2209.00809.
2. F. Kunstner, V. S. Portella, M. Schmidt and N. Harvey, *Searching for Optimal Per-Coordinate Step-sizes with Multidimensional Backtracking*, arXiv:2306.02527v1, first public 2023-06-05, https://arxiv.org/html/2306.02527v1.
3. R. D. Braatz and M. Morari, *Minimizing the Euclidean Condition Number*, SIAM Journal on Control and Optimization 32 (1994), 1763–1768, https://web.mit.edu/braatzgroup/Minimizing_the_Euclidean_condition_number.pdf.
4. J. Demmel, *Nearly Optimal Block-Jacobi Preconditioning*, SIAM Journal on Matrix Analysis and Applications 44 (2023), 408–413, https://doi.org/10.1137/22M1504901.
5. A. Shapiro, *Optimal Block Diagonal l2-Scaling of Matrices*, SIAM Journal on Numerical Analysis 22 (1985), 81–94, https://doi.org/10.1137/0722005.
