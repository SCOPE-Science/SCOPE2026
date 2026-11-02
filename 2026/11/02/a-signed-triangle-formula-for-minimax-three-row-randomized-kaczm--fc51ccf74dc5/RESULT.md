# A signed-triangle formula for minimax three-row randomized Kaczmarz sampling

## Finding
For every invertible real \(3\times3\) matrix with three unit-norm rows, the unique fixed row-sampling distribution that minimizes the largest **one-step expected squared-error contraction factor** has a closed form governed by the signs and reciprocal edge magnitudes of the inverse row Gram matrix. The classification has balanced, frustrated-cut, and frustrated-triangle cases. An explicit one-parameter correlation family changes the multiplicity of its worst contraction direction at \(t=2/5\), where the optimal sampling law is continuous but has a corner.

**Complete formula.** Let \(A\in\mathbb R^{3\times3}\) be invertible, \(\|a_i\|_2=1\), \(G=AA^{\mathsf T}\), and \(C=G^{-1}=(c_{ij})\). For \(i\ne j\) put \(g_{ij}=|c_{ij}|\). Define nonnegative \(q_1,q_2,q_3\) as follows.

1. **Balanced or vanishing cycle:** If \(c_{12}c_{13}c_{23}\ge0\), take \(q_i=\sum_{j\ne i}g_{ij}\).
2. **Frustrated triangle:** If \(c_{12}c_{13}c_{23}<0\), set \(\ell_{ij}=1/g_{ij}\). When all three strict triangle inequalities hold among \(\ell_{12},\ell_{13},\ell_{23}\), take
\[
q_1=\frac{g_{12}g_{13}}{g_{23}},\quad q_2=\frac{g_{12}g_{23}}{g_{13}},\quad q_3=\frac{g_{13}g_{23}}{g_{12}}.
\]
3. **Frustrated cut, including the boundary:** Otherwise there is a unique edge \(jk\) with \(\ell_{jk}\ge\ell_{ij}+\ell_{ik}\), where \(i\) is the remaining index. Take
\[
q_i=g_{ij}+g_{ik},\qquad q_j=g_{ij}-g_{jk},\qquad q_k=g_{ik}-g_{jk}.
\]
(The formulas agree at equality.)

Define \(w_i=c_{ii}+q_i\) and \(T=w_1+w_2+w_3\). Then the **unique** optimal probabilities and corresponding sharp one-step factor are
\[
\boxed{p_i^*=\frac{w_i}{T},\qquad \rho_*=1-\frac1T.}
\]
All three sampling probabilities are strictly positive. The claimed optimality is over all fixed probability distributions, without any symmetry restriction.

**Exact spectral transition.** Let
\[
G(t)=\begin{pmatrix}1&1/2&1/2\\1/2&1&t\\1/2&t&1\end{pmatrix},\qquad -1/2<t<1.
\]
For this positive-definite Gram family, the unique minimax sampler is
\[
(p_1^*,p_2^*,p_3^*)=\begin{cases}
\left(\frac{t+2}{t+5},\frac{3}{2(t+5)},\frac{3}{2(t+5)}\right),&-1/2<t\le2/5,\\
\left(\frac{2t(1-t)}{6t-2t^2-1},\frac{4t-1}{2(6t-2t^2-1)},\frac{4t-1}{2(6t-2t^2-1)}\right),&2/5\le t<1.
\end{cases}
\]
The optimized smallest eigenvalue is respectively
\[
\lambda_* =\begin{cases}\frac{2t+1}{2(t+5)},&t\le2/5,\\
\frac{(1-t)(4t-1)}{2(6t-2t^2-1)},&t\ge2/5.
\end{cases}
\]
The minimum eigenspace is one-dimensional for \(t<2/5\) and two-dimensional for \(t\ge2/5\); the eigenvalue formula and probabilities join continuously, but their first derivatives have a jump at \(2/5\).

## Assumptions and scope
A randomized Kaczmarz update for a consistent linear system \(Ax=b\), at error \(e\), chooses row \(i\) with fixed probability \(p_i\) and replaces \(e\) by \((I-a_i a_i^{\mathsf T})e\). Since the rows are normalized,
\[
\mathbb E\|e^+\|_2^2=\|e\|_2^2-e^{\mathsf T}A^{\mathsf T}\operatorname{diag}(p)Ae.
\]
Thus the sharp worst-direction conditional one-step factor is \(\rho(p)=1-\lambda_{\min}(A^{\mathsf T}\operatorname{diag}(p)A)\). The theorem concerns this one-step minimax objective; it does **not** claim exact long-horizon mean-squared error optimality or optimality among history-dependent sampling strategies. Real, invertible, square systems and fixed iid row probabilities are essential to the stated formulation.

## Proof
**1. Diagonal semidefinite reduction.** Invertibility of \(A\) gives
\[
A^{\mathsf T}\operatorname{diag}(p)A\succeq\lambda I\quad\Longleftrightarrow\quad\operatorname{diag}(p)\succeq\lambda C.
\]
For \(\lambda>0\), put \(w_i=p_i/\lambda\). Maximizing \(\lambda\) is therefore equivalent to minimizing \(T=\sum_i w_i\) subject to \(\operatorname{diag}(w)-C\succeq0\); the optimum has \(\lambda_*=1/T_*\) and \(p_i^*=w_i/T_*\). Write \(w_i=c_{ii}+q_i\) and \(S(q)=\operatorname{diag}(q)-(C-\operatorname{diag}(C))\).

**2. Exact dual.** Minimizing \(\sum q_i\) subject to \(S(q)\succeq0\) is dual to maximizing \(2\sum_{i<j}c_{ij}X_{ij}\) over positive-semidefinite correlation matrices \(X\) with \(X_{ii}=1\). Weak duality follows directly from \(\operatorname{tr}(S(q)X)\ge0\). It suffices to exhibit matching positive-semidefinite primal and dual matrices, with \(S(q)X=0\).

**3. Balanced case.** A signed triangle with positive sign product, or a graph on three vertices with a zero edge, is sign-switchable: choose signs \(s_i\in\{-1,1\}\) such that \(c_{ij}s_is_j=g_{ij}\) for each nonzero edge. For \(q_i=\sum_{j\ne i}g_{ij}\), switching \(S(q)\) by \(\operatorname{diag}(s)\) makes it a weighted graph Laplacian; hence it is positive semidefinite and annihilates \(s\). The dual correlation matrix \(X=ss^{\mathsf T}\) is feasible and complementary.

**4. Frustrated triangle.** If \(c_{12}c_{13}c_{23}<0\), there exists a real nonzero vector \(v\) satisfying \(v_iv_j=-c_{ij}\) for each edge. Its squared coordinates are precisely the three frustrated-triangle \(q_i\) above, so \(S(q)=vv^{\mathsf T}\). The lengths \(|v_i|\) are proportional to the reciprocal opposite-edge magnitudes: \(|v_1|:|v_2|:|v_3|=\ell_{23}:\ell_{13}:\ell_{12}\). The strict triangle inequalities therefore supply planar unit vectors \(u_i\) with \(\sum_i v_i u_i=0\). Their Gram matrix \(X_{ij}=u_i\cdot u_j\) is positive semidefinite, has unit diagonal, and obeys \(S(q)X=0\). The candidate is optimal.

**5. Frustrated cut.** Suppose \(\ell_{jk}\ge\ell_{ij}+\ell_{ik}\). Switch signs to make the two edges from \(i\) positive and the edge \(jk\) negative. For the stated cut \(q\), the quadratic form of the switched matrix is
\[
g_{ij}(z_i-z_j)^2+g_{ik}(z_i-z_k)^2-g_{jk}(z_j-z_k)^2.
\]
Minimizing in \(z_i\) leaves \((g_{ij}g_{ik}/(g_{ij}+g_{ik})-g_{jk})(z_j-z_k)^2\), nonnegative precisely under the stipulated reciprocal inequality. The switched all-ones vector gives a complementary rank-one correlation matrix, proving optimality. The formulas meet at equality.

**6. Uniqueness.** In the balanced and cut regimes a complementary sign vector forces every competing optimum \(S(q')\) to annihilate that vector; its three row equations determine \(q'\) uniquely from the fixed off-diagonal entries. In the strict frustrated triangle, the complementary dual Gram matrix has rank two, so every optimal \(S(q')\) has rank at most one. Its three nonzero prescribed off-diagonal entries uniquely determine its diagonal, hence \(q'=q\). Since \(C\succ0\), each \(c_{ii}>0\), yielding \(p_i^*>0\). This establishes global uniqueness in all cases.

**7. The transition family.** Direct inversion of \(G(t)\) gives \(c_{12}=c_{13}=-1/(2t+1)\) and \(c_{23}=(1/4-t)/((1-t)(t+1/2))\). The cycle is balanced for \(t\le1/4\), a frustrated cut for \(1/4<t\le2/5\), and a strict frustrated triangle for \(2/5<t<1\). Substitution into the complete formula yields the displayed rational branches. The complementary dual correlation matrix has rank one before the cut-to-triangle transition and rank two after it, so the primal slack has rank two then rank one; congruence preserves the claimed minimum-eigenspace dimensions. The formulas agree at the junction, whereas their displayed derivatives differ.

## Verification
Run \(\texttt{python VERIFY.py}\) using Python 3 and only its standard library. It constructs exact rational inverses and semidefinite certificates on a grid of 553 admissible normalized row Gram matrices, covering all three cases, verifies the rational transition formulas on 149 parameters including the phase boundary, and checks additional rational feasible competitors. The supplied replay reports **7,362 exact assertions**; finite checks support but do not establish the infinite-dimensional parameter quantifier or SDP uniqueness proof. A separate independent numerical minimization over 800 random invertible normalized-row matrices agreed to floating-point precision; that numerical cross-check is ancillary to the proof.

## Relationship to prior work
Strohmer–Vershynin developed norm-based randomized Kaczmarz convergence guarantees. Dai–Soltanalian–Pelckmans explicitly formulated the **general** probability-optimized one-step smallest-eigenvalue objective as a semidefinite program; that formulation is prior art and is not claimed anew. Agaskar–Wang–Lu studied a distinct objective based on exact multi-step MSE. Pukelsheim–Torsney gave general optimal-design equivalence conditions and explicit A-optimal weights for linearly independent support points, rather than this E-optimal three-row closed form. Saunderson–Chandrasekaran–Parrilo–Willsky developed the general minimum-trace diagonal/low-rank SDP and correlation-matrix duality; the diagonal SDP/elliptope connection is also prior art. The novel asserted contribution is specifically the complete inverse-Gram signed-triangle **closed formula, uniqueness, and exact \(2/5\) transition** in the randomized Kaczmarz setting. Earlier general frameworks can compute the answer numerically but do not themselves state this classification.

## Limitations
The statement is restricted to real invertible three-row square systems with normalized rows and fixed iid one-step minimax sampling. The classification is not an optimality claim for general rectangular systems, asymptotic annealed MSE, adaptive algorithms, or finite-horizon pathwise mixing. The general SDP and elliptope duality were known; independent expert review and exhaustive historical-literature clearance have not been performed. The code checks finitely many rational and numerical instances and does not constitute formal verification of the proof.

## References
- T. Strohmer and R. Vershynin, *A Randomized Kaczmarz Algorithm with Exponential Convergence*, initial arXiv release 2007-02-08, https://arxiv.org/abs/math/0702226.
- L. Dai, M. Soltanalian, and K. Pelckmans, *On the Randomized Kaczmarz Algorithm*, 2014, https://arxiv.org/abs/1402.2863.
- A. Agaskar, C. Wang, and Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, 2014, https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content.
- F. Pukelsheim and B. Torsney, *Optimal Weights for Experimental Designs on Linearly Independent Support Points*, Annals of Statistics 19 (1991), 1614–1625, https://www.math.uni-augsburg.de/htdocs/emeriti/pukelsheim/1991d.pdf.
- J. Saunderson, V. Chandrasekaran, P. A. Parrilo, and A. S. Willsky, *Diagonal and Low-Rank Matrix Decompositions, Correlation Matrices, and Ellipsoid Fitting*, SIAM J. Matrix Anal. Appl. 33 (2012), 1395–1416, https://arxiv.org/abs/1204.1220.
