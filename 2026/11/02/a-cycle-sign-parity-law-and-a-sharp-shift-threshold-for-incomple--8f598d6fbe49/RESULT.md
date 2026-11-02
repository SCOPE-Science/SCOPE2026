# A cycle-sign parity law and a sharp shift threshold for incomplete Cholesky breakdown

## Finding

For every integer \(n\ge4\), let \(s_1,\ldots,s_n\in\{-1,1\}\), and let \(A_n(t,s)\) be the real symmetric \(n\)-by-\(n\) matrix with unit diagonal, entries \(s_jt\) at the two positions joining vertices \(j\) and \(j+1\) (indices cyclically modulo \(n\)), and all other entries zero. Assume \(t>0\). Define
\[
\sigma=\prod_{j=1}^n s_j,\qquad
c_j=\cos(\pi/j),\qquad
t_{\mathrm{IC}}(n)=\frac1{2c_{n+2}}.
\]
Use natural vertex order \(1,2,\ldots,n\) and zero-fill incomplete Cholesky, retaining exactly the original lower-triangular sparsity pattern and performing all arithmetic exactly, without a pivot shift or drop compensation.

**Sharp phase diagram.** If \(\sigma=(-1)^n\), then \(A_n(t,s)\) is positive definite exactly when \(0<t<1/2\), and the stated IC(0) factorization succeeds throughout that entire interval. If \(\sigma\ne(-1)^n\), then \(A_n(t,s)\) is positive definite exactly when
\[
0<t<t_{\mathrm{SPD}}(n):=\frac1{2c_n},
\]
but IC(0) succeeds only when \(0<t<t_{\mathrm{IC}}(n)\). At equality with \(t_{\mathrm{IC}}(n)\), the last incomplete pivot is zero; throughout the nonempty interval
\[
\frac1{2c_{n+2}}<t<\frac1{2c_n}
\]
that pivot is strictly negative while the input matrix remains positive definite. All preceding incomplete pivots remain strictly positive. The IC(0) pivot sequence depends only on \(n\) and \(t\), not on the locations or number of negative signs.

**Exact global shift threshold.** For any positive-definite member of this family and any \(\alpha\ge0\), the ordinary IC(0) factorization of \(A_n(t,s)+\alpha I\) succeeds if and only if
\[
\frac{t}{1+\alpha}<\frac1{2c_{n+2}}.
\]
Its infimum admissible global shift is therefore
\[
\alpha_*=\max\{0,\,2t c_{n+2}-1\}.
\]
When \(t\ge t_{\mathrm{IC}}(n)\), the inequality is strict and the infimum is not attained; when \(t<t_{\mathrm{IC}}(n)\), zero shift succeeds.

**Sharp condition-number boundary.** In the sign class \(\sigma\ne(-1)^n\), write \(\kappa_2\) for the spectral condition number of the positive-definite input. The factorization fails exactly when \(\kappa_2\ge\kappa_*(n)\), where
\[
\kappa_*(n)=
\begin{cases}
\dfrac{c_{n+2}+c_n}{c_{n+2}-c_n},&n\text{ even},\\[4pt]
\dfrac{c_{n+2}+1}{c_{n+2}-c_n},&n\text{ odd}.
\end{cases}
\]
As \(n\to\infty\), both parity cases obey \(\kappa_*(n)\sim n^3/\pi^2\), and the width of the positive-definite breakdown window is
\[
t_{\mathrm{SPD}}(n)-t_{\mathrm{IC}}(n)
=\frac{\pi^2}{n^3}+O(n^{-4}).
\]

The four-vertex example with edge signs \((1,1,1,-1)\) and \(t=3/5\) is positive definite, having eigenvalues \(1\pm3\sqrt2/5\) (each twice), but its unshifted IC(0) pivots are \(1,16/25,7/16,-32/175\). Thus failure occurs in exact arithmetic even though the matrix is strictly positive definite.

## Assumptions and scope

The graph is the simple cycle of length \(n\ge4\), the diagonal is one, all edges have the same positive magnitude \(t\) and arbitrary signs, and the factor is computed in the natural cyclic order with zero retained fill. All claims about breakdown concern a zero or negative pivot in this precise exact-arithmetic algorithm. They do not apply to modified IC, reordering, adaptive dropping, positive-definite completion, or methods that add a diagonal shift automatically. The symbol \(\kappa_2\) is the ratio of the largest to smallest eigenvalue for the stated positive-definite matrix.

## Proof

1. **Gauge classification of the input.** Conjugation by a diagonal matrix with entries in \(\{-1,1\}\) preserves eigenvalues and changes edge signs without changing their product \(\sigma\). If \(\sigma=(-1)^n\), all edges may be switched to \(-t\), giving the eigenvalues \(1-2t\cos(2\pi j/n)\), where \(j=0,\ldots,n-1\); their minimum is \(1-2t\). In the opposite sign class, switch the first \(n-1\) edges to \(-t\) and the closing edge to \(+t\). A Fourier mode satisfies the antiperiodic boundary relation and has eigenvalue \(1-2t\cos((2j+1)\pi/n)\). The minimum is \(1-2t\cos(\pi/n)\). These formulas prove both input positive-definiteness ranges, including equality endpoints.

2. **Exact incomplete pivots.** Write \(p_j\) for the unsquared diagonal pivot produced by zero-fill IC(0). For \(n\ge4\), the only nonzeros permitted below the diagonal are the path edges and the closing edge. Every discarded fill lies outside this pattern, and retained consecutive-edge entries have no common earlier predecessor. Hence their magnitudes before division by the pivot are still \(t\), and
\[
p_1=1,\qquad p_j=1-\frac{t^2}{p_{j-1}}\quad(2\le j\le n-1),\qquad
p_n=1-t^2-\frac{t^2}{p_{n-1}}.
\]
The closing edge contributes the additional term \(-t^2/p_1=-t^2\). Squaring eliminates the signs from every recurrence, so placement of edge signs has no effect on the incomplete pivots.

3. **Unexpected path extension.** Define \(D_0=D_1=1\) and \(D_j=D_{j-1}-t^2D_{j-2}\). This is the determinant recurrence for the \(j\)-vertex tridiagonal path matrix with diagonal one and edge magnitude \(t\). The exact recurrence in Step 2 gives
\[
p_j=\frac{D_j}{D_{j-1}}\quad(1\le j\le n-1),\qquad
p_n=\frac{D_{n+1}}{D_{n-1}}.
\]
The latter identity follows from \((1-t^2)D_{n-1}-t^2D_{n-2}=D_n-t^2D_{n-1}=D_{n+1}\). Thus the last incomplete pivot is governed by a path with **two more vertices than the last ordinary path recurrence**.

4. **Sign of every pivot in the input-SPD range.** The eigenvalues of the \(j\)-vertex path adjacency matrix are \(2\cos(k\pi/(j+1))\), for \(k=1,\ldots,j\). Consequently, the first positive zero of \(D_j\) is \([2\cos(\pi/(j+1))]^{-1}\). Every \(D_j\) for \(j\le n-1\) is positive throughout \(0<t<t_{\mathrm{SPD}}(n)\). The first zero of \(D_{n+1}\) is \(t_{\mathrm{IC}}(n)\); its second positive zero occurs after \(t_{\mathrm{SPD}}(n)\), because \(2\pi/(n+2)>\pi/n\). Thus its sign is positive below \(t_{\mathrm{IC}}(n)\), zero there, and negative between \(t_{\mathrm{IC}}(n)\) and \(t_{\mathrm{SPD}}(n)\). Since \(1/2<t_{\mathrm{IC}}(n)<t_{\mathrm{SPD}}(n)\), the two claimed sign-class phase diagrams follow.

5. **Shift and condition number.** Factoring \(A+\alpha I=(1+\alpha)A_n(t/(1+\alpha),s)\) scales all IC pivots by \(1+\alpha\), proving the shift law. In the opposite sign class, the smallest eigenvalue is \(1-2tc_n\); the largest is \(1+2tc_n\) for even \(n\) and \(1+2t\) for odd \(n\). Their ratio increases strictly with \(t\), so evaluation at \(t=t_{\mathrm{IC}}(n)\) gives the stated sharp \(\kappa_*\). Standard Taylor expansions of \(\cos(\pi/n)\) and \(\cos(\pi/(n+2))\) yield the two asymptotic formulas. No numerical experiment is used for these infinite-family conclusions.

6. **Four-vertex witness.** With the specified signs and \(t=3/5\), the antiperiodic spectrum from Step 1 is \(1\pm3\sqrt2/5>0\). Direct substitution into Step 2 gives the four rational pivots stated above and verifies strict breakdown at the final pivot.

## Verification

The standalone script `verify_cycle_ic.py` performs exact rational checks of the determinant and pivot identities for sizes \(4\) through \(40\), compares direct sparse-pattern IC(0) against the closed formulas for all signings at size four and multiple pseudorandom signings through size twenty-eight, checks spectral definiteness and failure intervals, and tests both the global shift and condition-number transitions. It reports 3,667 passing consistency checks. Run `python3 verify_cycle_ic.py` in an environment with NumPy. These finite checks support implementation and arithmetic reproducibility; they do not establish the all-size theorem, which follows from the proof above.

## Relationship to prior work

Breakdown of incomplete Cholesky on positive-definite matrices, safe zero-fill patterns for symmetric M-matrices, and global diagonal shifts are established subjects. Scott and Tůma (2024, arXiv:2403.13123) discuss exact-arithmetic pivot breakdown and practical shifting, but the inspected paper does not state a signed-cycle spectral or sharp shift classification. Ferronato (2012) surveys M-matrix existence conditions and general breakdown for non-M-type matrices; these facts imply the safe sign class, but neither they nor the existence of an unsafe example determines the exact all-size thresholds for the opposite sign class. The present claim is the explicit, two-sign-class complete cycle calculation and its optimal shift and condition-number consequences, not a new generic failure mechanism or a new incomplete-factorization algorithm.

## Limitations

The uniform edge magnitude, simple-cycle graph, fixed natural ordering, and exact unmodified IC(0) rule are essential. Other graphs, nonuniform edge strengths, block methods, reordering, finite-precision rounding, or performance of the resulting preconditioned Krylov solve are not covered. The general historical literature on incomplete factorization is extensive; the earlier existence survey by Eijkhout (1999) could not be checked in full, leaving a publication-priority risk. All arithmetic and mathematical classification claims are independently auditable from the included proof and checker, but no independent scientific validation is represented.

## References

- J. Scott and M. Tůma, *Developing robust incomplete Cholesky factorizations in half precision arithmetic*, first public arXiv version dated 2024-03-19, arXiv:2403.13123, https://arxiv.org/abs/2403.13123.
- M. Ferronato, *Preconditioning for Sparse Linear Systems at the Dawn of the 21st Century: History, Current Developments, and Future Perspectives*, 2012, DOI:10.5402/2012/127647, https://doi.org/10.5402/2012/127647.
- J. A. Meijerink and H. A. van der Vorst, *An iterative solution method for linear systems of which the coefficient matrix is a symmetric M-matrix*, Mathematics of Computation 31 (1977), 148–162, DOI:10.1090/S0025-5718-1977-0438681-4.
- V. Eijkhout, *On the Existence Problem of Incomplete Factorisation Methods*, LAPACK Working Note 144, 1999, https://www.netlib.org/lapack/lawns/downloads/ (full text not accessible in this assessment).
