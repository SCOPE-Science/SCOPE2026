# Sharp real \(\ell_4\) frustration deficit for a signed cycle

## Finding

For every integer \(n\ge 2\), define the antiperiodic signed cyclic shift on real \(\ell_4^n\) by
\[
(U_nx)_j=x_{j+1}\quad(1\le j<n),\qquad (U_nx)_n=-x_1.
\]
In the induced real operator norm, the following sharp leading asymptotic holds:
\[
\boxed{\lim_{n\to\infty}n^2\left(2-\|I+U_n\|_{\ell_4^n\to\ell_4^n}\right)=\frac{3\pi^2}{16}.}
\]
Equivalently, let \(A_{2n}\) be the signed adjacency matrix of a \(2n\)-vertex cycle with exactly one negative edge and all other edges positive. Then
\[
\boxed{\lim_{n\to\infty}n^2\left(2-\|A_{2n}\|_{\ell_4^{2n}\to\ell_4^{2n}}\right)=\frac{3\pi^2}{16}.}
\]
All spaces and operator norms in these statements are **real**. The coefficient is exact; numerically it is \(1.8505508252042546\ldots\).

## Assumptions and scope

The operator \(U_n\) is a signed permutation isometry satisfying \(U_n^n=-I\). It is not a positive cyclic shift. The maximum defining \(\|I+U_n\|\) exists in each finite dimension. In the signed graph formulation, the negative-edge product is invariant under vertex sign-switching, so the position of the sole negative edge does not matter. The theorem concerns the induced \(\ell_4\) norm, **not** the spectral radius on \(\ell_2\), the Schatten \(4\)-norm, or the \(4\)-spectral graph quadratic form.

## Proof

**1. Exact fourth-power defect.** For an arbitrary real vector \(x=(x_1,\ldots,x_n)\), extend the coordinates by \(x_{n+1}=-x_1\). Define
\[
 m_j=\frac{x_j+x_{j+1}}2,\quad d_j=\frac{x_{j+1}-x_j}2,\quad
 E_j=6m_j^2d_j^2+d_j^4\ge0.
\]
The polynomial identity
\[
 \frac{x_j^4+x_{j+1}^4}{2}=m_j^4+6m_j^2d_j^2+d_j^4
\]
gives, after summation using \(x_{n+1}^4=x_1^4\),
\[
 \|(I+U_n)x\|_4^4=16\sum_{j=1}^n m_j^4
 =16\left(\|x\|_4^4-\sum_{j=1}^n E_j\right).
\]
By homogeneity, set
\[
 e_n=\min\left\{\sum_{j=1}^n E_j:\;x\in\mathbb R^n,\quad\sum_{j=1}^n x_j^4=n\right\}.
\]
This minimum is attained, and
\[
 \|I+U_n\|_{4\to4}^4=16\left(1-\frac{e_n}{n}\right).\tag{1}
\]
Thus the leading norm deficit is determined by the limit of \(ne_n\).

**2. A transformed gradient and two exact comparison inequalities.** Put \(h(t)=t|t|\) and \(g_j=h(x_j)\), with \(g_{n+1}=-g_1\). For each edge one has
\[
 \frac14(g_{j+1}-g_j)^2\le E_j\le\frac74(g_{j+1}-g_j)^2.\tag{2}
\]
Indeed, when the endpoints have the same sign, \(|m_j|\ge|d_j|\) and
\( (g_{j+1}-g_j)^2=16m_j^2d_j^2\). The defect then lies between \(6m_j^2d_j^2\) and \(7m_j^2d_j^2\); in particular,
\[
 E_j\ge\frac38(g_{j+1}-g_j)^2\quad\text{on same-sign edges}.\tag{3}
\]
For opposite signs, \(|d_j|\ge|m_j|\) and
\( (g_{j+1}-g_j)^2=4(m_j^2+d_j^2)^2\). Direct subtraction gives
\[
 E_j-\frac14(g_{j+1}-g_j)^2=m_j^2(4d_j^2-m_j^2)\ge0,
\]
while \(E_j\le7d_j^4\le\tfrac74(g_{j+1}-g_j)^2\). These formulas also cover zero endpoints by continuity. Notice that the coefficient \(3/8\) in (3), rather than the coarse \(1/4\) in (2), governs the macroscopic limit away from zeros.

**3. Compactness and the sharp lower limit.** Let \(x^{(n)}\) minimize \(e_n\), and construct the continuous piecewise-linear interpolant \(G_n:[0,1]\to\mathbb R\) with values \(g_j\) at grid points \((j-1)/n\) and \(G_n(1)=-g_1\). The normalization is
\(n^{-1}\sum_j g_j^2=1\). The upper comparison in (2), applied to the smooth trial in Step 4, implies \(\sup_n ne_n<\infty\). By the lower comparison in (2),
\[
 \int_0^1|G_n'(t)|^2dt
 =n\sum_j(g_{j+1}-g_j)^2\le4ne_n\le C.
\]
The exact piecewise-linear quadrature identity is
\[
 \int_0^1G_n(t)^2dt
 =\frac1n\sum_jg_j^2-\frac1{6n}\sum_j(g_{j+1}-g_j)^2
 =1+O(n^{-2}).
\]
Consequently, after a subsequence, \(G_n\) converges uniformly and weakly in \(H^1(0,1)\) to some \(G\) satisfying \(G(1)=-G(0)\) and \(\int_0^1G^2=1\).

On every closed subinterval compactly contained in \(\{t:G(t)\ne0\}\), uniform convergence forces all sufficiently fine neighboring nodal values to have the same sign. Formula (3), lower semicontinuity of the \(H^1\) energy, and exhaustion of these subintervals show
\[
 \liminf_{n\to\infty}ne_n
 \ge\frac38\int_{\{G\ne0\}}|G'(t)|^2dt
 =\frac38\int_0^1|G'(t)|^2dt.\tag{4}
\]
The last equality uses the standard one-dimensional Sobolev fact that the weak derivative of an absolutely continuous function vanishes almost everywhere on any of its level sets, here \(\{G=0\}\). An antiperiodic \(H^1\) function obeys the sharp Poincaré inequality
\[
 \int_0^1|G'|^2\ge\pi^2\int_0^1|G|^2.
\]
To prove this, extend \(G\) to a period-two function by \(G(t+1)=-G(t)\). Its Fourier series has no even harmonic and thus no frequency smaller in magnitude than \(\pi\); Parseval gives the inequality. Hence
\[
 \liminf_{n\to\infty}ne_n\ge\frac{3\pi^2}{8}.\tag{5}
\]

**4. A recovery sequence attaining the bound.** Take \(G_*(t)=\sqrt2\cos(\pi t)\), so that \(G_*(1)=-G_*(0)\), \(\int G_*^2=1\), and \(\int|G_*'|^2=\pi^2\). For each \(n\ge2\), choose
\[
 x_j=\operatorname{sgn}\!\left(G_*\left(\frac{j-1}{n}\right)\right)
 \sqrt{\left|G_*\left(\frac{j-1}{n}\right)\right|},\qquad 1\le j\le n.
\]
The root-of-unity identity \(\sum_{j=0}^{n-1}2\cos^2(\pi j/n)=n\) shows exactly that \(\sum_j x_j^4=n\); no approximate normalization is needed. The transformed nodal values equal \(G_*((j-1)/n)\).

On closed sets separated from the sole zero of \(G_*\) at \(t=1/2\), neighboring samples have the same sign and \(d_j^2/m_j^2\to0\) uniformly. The exact same-sign formula therefore yields
\[
 E_j=\left(\frac38+o(1)\right)(g_{j+1}-g_j)^2
\]
uniformly on those sets. Edges in an interval of length \(2\varepsilon\) about the zero contribute at most \(\tfrac74\sum(\Delta g_j)^2\) by (2). Since \(G_*\) is Lipschitz, their contribution to \(n\sum E_j\) is \(O(\varepsilon)+O(n^{-1})\). Taking \(n\to\infty\) and then \(\varepsilon\downarrow0\) gives
\[
 \limsup_{n\to\infty}ne_n\le
 \lim_{n\to\infty}n\sum_jE_j
 =\frac38\int_0^1|G_*'(t)|^2dt
 =\frac{3\pi^2}{8}.\tag{6}
\]
Combining (5) and (6), \(ne_n\to3\pi^2/8\). Equation (1) now implies
\[
 2-\|I+U_n\|_{4\to4}
 =2-2\left(1-\frac{e_n}{n}\right)^{1/4}
 =\frac{e_n}{2n}+o(n^{-2}),
\]
which proves the first boxed limit.

**5. The signed-cycle adjacency formulation.** Let \(B_n=I+U_n\). The real symmetric block matrix
\[
 A_{2n}=\begin{pmatrix}0&B_n\\ B_n^{\mathsf T}&0\end{pmatrix}
\]
is the adjacency matrix of a connected \(2n\)-cycle with one negative edge. Its induced \(\ell_4\)-norm is
\[
 \|A_{2n}\|_{4\to4}=\max\{\|B_n\|_{4\to4},\|B_n^{\mathsf T}\|_{4\to4}\}.
\]
Since \(U_n\) is a signed permutation isometry,
\(\|B_n^{\mathsf T}\|_{4\to4}=\|I+U_n^{-1}\|_{4\to4}=\|U_n^{-1}(I+U_n)\|_{4\to4}=\|B_n\|_{4\to4}\). This proves the second boxed limit. Other placements of the negative sign yield isometrically conjugate matrices.

## Verification

All critical algebraic inequalities (the fourth-power defect and the two cases of the transformed gradient) follow from explicit polynomial identities in Step 2. The compactness proof handles arbitrary minimizers, including coordinate zeros; the smooth recovery handles attainability of the limiting coefficient, not merely a lower bound. The included optional `verify.py` uses exact rational arithmetic to test these algebraic inequalities on a finite diagnostic grid, and reproduces numerical recovery-sequence values from the displayed formula. Such finite tests are not used in place of the infinite-dimensional limit argument.

For reference, the recovery sequence gives approximate values \(n^2(2-\|B_nx\|_4/\|x\|_4)\) of \(1.871110\) at \(n=64\), \(1.855668\) at \(n=256\), and \(1.851829\) at \(n=1024\); its target is \(3\pi^2/16\approx1.850551\). The actual operator norm may be larger than the trial ratio, hence its gap smaller. No finite optimizer or numerical extrapolation enters the proof.

## Relationship to prior work

The signed-graph literature motivates measurement of imbalance and gives exact quadratic-spectrum formulas and bounds. Guo–Mohar's work provides skew-circulant eigenvalue theory for oriented/mixed cycles; this concerns Hermitian \(\ell_2\) spectra. Li–Li establish bounds relating the least signed Laplacian eigenvalue to frustration indices; again the object is quadratic spectral data. Hameed–Biju–Stanić explicitly compute spectral balance measures for negative cycles: their Theorem 2.2 concerns eigenvalue differences and the largest \(\ell_2\) eigenvalue, and does not determine an induced real \(\ell_4\) operator norm. For a negative cycle of length \(2n\), the Hilbert norm is \(2\cos(\pi/(2n))\), whose scaled deficit tends to \(\pi^2/4\), rather than \(3\pi^2/16\). These statements are not equivalent under Fourier diagonalization because a Fourier basis change is not generally an \(\ell_4\)-isometry.

## Limitations

The theorem gives only the sharp leading-order coefficient as the size tends to infinity. It neither determines the exact finite-dimensional \(\ell_4\) norm for each \(n\) nor supplies second-order error constants. It applies to a real, unweighted, singly frustrated cycle and does not assert the same coefficient for complex scalars, other exponents, multiply frustrated graphs, or arbitrary weighted edges. Literature coverage is not exhaustive; historical literature on induced norms of skew-circulant matrices may be incompletely indexed.

## References

1. K. Guo and B. Mohar, *Hermitian adjacency matrix of digraphs and mixed graphs*, arXiv:1505.01321v1 (publicly submitted 6 May 2015), especially Sections 8.1 and 10. https://arxiv.org/html/1505.01321v1
2. H.-S. Li and H.-H. Li, *A note on the least (normalized) Laplacian eigenvalue of signed graphs*, Tamkang J. Math. 47 (2016), 271–278, especially Section 2. https://journals.math.tku.edu.tw/index.php/TKJM/article/download/1942/999/5794
3. Shahul Hameed K., Biju K., and Z. Stanić, *Spectral measures of balance for signed graphs*, Australas. J. Comb. 93 (2025), 198–210, especially Theorem 2.2. https://ajc.maths.uq.edu.au/pdf/93/ajc_v93_p198.pdf
