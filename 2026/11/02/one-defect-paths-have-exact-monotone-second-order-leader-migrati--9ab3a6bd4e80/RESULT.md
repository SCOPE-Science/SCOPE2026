# One-defect paths have exact monotone second-order leader-migration thresholds

## Finding

For every integer \(n\ge3\), every exceptional edge index \(1\le h<n\), and every exceptional resistance \(x>0\), consider the path on vertices \(1,\ldots,n\) with conductance \(1\) on all edges except \(\{h,h+1\}\), whose conductance is \(1/x\). Choose exactly one ideal noise-free grounded leader \(k\). If \(L_{FF}\) is the weighted graph Laplacian with leader row and column deleted, minimize the **second-order grounded coherence**
\[
J(k;x)=\operatorname{tr}(L_{FF}^{-2})
\]
over all \(k\in\{1,\ldots,n\}\).

Define, for nonnegative integers \(m,p\),
\[
F(m)=\frac{m(m+1)[m(m+1)+1]}6,\quad
C(p)=\frac{p(p+1)(2p+1)}6,\quad
g(m)=\frac{2m^3+m}3.
\]
For each \(k\), put
\[
(p,d)=\begin{cases}(n-h,h-k+1),&k\le h,\\(h,k-h),&k\ge h+1.\end{cases}
\]
Then the exact objective, without matrix inversion, is
\[
\boxed{J(k;x)=F(k-1)+F(n-k)+2(x-1)\{p^2(d-1)+C(p)\}+p^2(x-1)^2.}
\]

There is a complete sharp classification of **every** minimizing leader:

**Unequal sides, with the right side larger:** If \(h<n-h\), every optimum lies in \(\{h+1,\ldots,n\}\). For \(h+1\le k\le n-1\), define strictly decreasing thresholds
\[
t_k=1+\frac{g(n-k)-g(k)}{2h^2},\qquad t_h=+\infty,\quad t_n=-\infty.
\]
The optimal leader set is exactly
\[
\boxed{\{k\in\{h+1,\ldots,n\}:t_k\le x\le t_{k-1}\}.}
\]
The conditions are taken with \(x>0\); negative thresholds do not create physical transitions. For all positive \(x\), there is one optimum except at a strictly positive threshold \(x=t_k\), where exactly the adjacent leaders \(k,k+1\) tie. Increasing the exceptional resistance can only move an optimal leader leftward, toward the exceptional edge; at sufficiently large \(x\), \(h+1\) is uniquely optimal.

**Unequal sides, with the left side larger:** If \(h>n-h\), reflect the path by \(k\mapsto n+1-k\) and replace \(h\) by \(n-h\) in the foregoing formula. Every optimum lies in \(\{1,\ldots,h\}\); as \(x\) increases, optimal leaders move only rightward, toward the exceptional edge.

**Equal sides:** If \(h=n-h\) (necessarily even \(n\)), the two and only two global minimizers are \(h\) and \(h+1\), for every \(x>0\).

## Assumptions and scope

The path is undirected and weighted by the specified strictly positive conductances; there is exactly one ideal grounded leader. No exceptional-edge endpoint, path-size, or resistance regime is omitted. The matrix \(L_{FF}\) is the Dirichlet principal submatrix of the full combinatorial weighted Laplacian and is positive definite. Both the scalar objective and the complete argmin set (including ties) are classified; no assertion is made for multiple defects or multiple grounded leaders.

In the commonly used second-order consensus model \(\ddot y+\beta L_{FF}\dot y+\alpha L_{FF}y=\xi\), with \(\alpha,\beta>0\), independent unit-intensity white-noise follower force \(\xi\), and ideal clamped leader, the total stationary follower position variance equals \(J(k;x)/(2\alpha\beta)\). This follows by diagonalizing the positive-definite Dirichlet Laplacian and solving the scalar second-order Ornstein--Uhlenbeck covariance equations. The optimal leader is therefore independent of the positive gains.

## Proof

**1. Anchored Green matrix.** Grounding the path at \(k\) splits the follower graph into independent left and right Dirichlet chains. Number the vertices of an arm outward from the leader, and let successive edge resistances be \(r_1,\ldots,r_L>0\). Its exact inverse Laplacian has entries
\[
G_{ij}=\sum_{e=1}^{\min(i,j)}r_e,
\]
by inversion of the bidiagonal incidence factorization (equivalently, by solving each unit-current potential equation). For an all-unit arm, \(G_{ij}=\min(i,j)\). Its squared Frobenius norm, equal to \(\operatorname{tr}(G^2)\), is
\[
\sum_{i,j=1}^L\min(i,j)^2=\sum_{r=1}^Lr^2(2L-2r+1)=F(L).
\]
Indeed, exactly \(2L-2r+1\) ordered pairs of indices have minimum \(r\); the finite sum reduces by the standard quadratic and cubic sum identities.

**2. One exceptional resistance.** If the exceptional resistor is the \(d\)-th outward edge of an arm of total length \(L=d+p-1\), write \(u=x-1\). Then
\[
G_{ij}=\min(i,j)+u\mathbf1_{i,j\ge d}.
\]
The affected lower-right block has size \(p\). Expanding \(\sum_{i,j}G_{ij}^2\), its quadratic part is \(p^2u^2\), and the cross term is
\[
2u\sum_{i,j=d}^L\min(i,j)=2u\{p^2(d-1)+\sum_{i,j=1}^p\min(i,j)\}
=2u\{p^2(d-1)+C(p)\}.
\]
The unaffected arm has all unit edges, so adding the two block contributions yields the boxed identity for \(J(k;x)\) for both sides of the defect. This proves the identity for every integer \(k\), every \(x>0\), and both endpoint choices.

**3. Excluding the shorter side.** Suppose \(h<p=n-h\), so the right side contains more vertices. For \(1\le k<h\), both successive leaders have the defect on their right arm. The preceding formula gives
\[
J(k+1;x)-J(k;x)=g(k)-g(n-k)+2(1-x)p^2.
\]
Since \(g\) increases strictly and \(k\le h-1<p\), \(n-k\ge p+1\), whence
\[
g(n-k)-g(k)\ge g(p+1)-g(p)=2p^2+2p+1>2p^2.
\]
As \(x>0\), we have \(2(1-x)p^2<2p^2\); every such difference is strictly negative. Across the exceptional edge, a separate exact subtraction yields
\[
J(h+1;x)-J(h;x)=-\frac{(p-h)x}{3}
\left[2(h^2+hp+p^2)+3(h+p)(x-1)+1\right].
\]
The square bracket is strictly positive for \(x>0\): it increases with \(x\), and its value at \(x=0\) is
\[
1+3(h-1)+3(p-1)+2\{(h-1)^2+(h-1)(p-1)+(p-1)^2\}>0.
\]
Therefore \(J(h+1;x)<J(h;x)<J(k;x)\) for every \(k<h\); the smaller side can never contain a minimizer.

**4. Sharp thresholds and monotonicity.** Now restrict to \(h+1\le k\le n\). Both the exceptional resistor and its affected block lie on the left arm, with \(p=h\). For \(h+1\le k<n\), subtraction gives
\[
J(k+1;x)-J(k;x)=g(k)-g(n-k)+2(x-1)h^2=2h^2(x-t_k).
\]
Because \(g\) is strictly increasing on nonnegative integers, successive right-arm differences strictly increase with \(k\): this is strict discrete convexity. A vertex is therefore a global minimizer if and only if the previous difference is nonpositive and the next difference is nonnegative, precisely \(t_k\le x\le t_{k-1}\). A strictly increasing sequence of differences has at most two consecutive minimizers. Since \(t_k\) strictly decreases with \(k\), raising \(x\) can only lower the optimal index. For large \(x\), all successive differences are positive and \(h+1\) alone minimizes. Every stated inequality includes equality cases.

**5. Reflection and equal sides.** Reversing the vertex order maps \((n,h,k)\) to \((n,n-h,n+1-k)\) while preserving the Dirichlet spectrum. It proves the left-larger case. For \(h=p\), the same one-sided strict descent applies until leaders reach \(h,h+1\); the cross-edge difference derived in step 3 vanishes identically, leaving exactly those two minimizers for every \(x>0\). This completes the classification.

## Verification

`verification/verify.py` uses Python 3 and SymPy to construct each full weighted Laplacian, delete the leader row/column, invert the actual Dirichlet matrix over exact rationals, and compare its squared-inverse trace against the formula. It independently enumerates all leader locations, including at positive phase thresholds, and compares argmin sets with the classification.

A direct execution produced 2,296 exact grounded-matrix equalities and 16,519 exact classifications, of which 7,087 are tie cases. The exact output is included in `verification/checks.txt`; the program is standalone apart from its stated SymPy dependency. These finite tests corroborate but do not establish the all-size theorem; the proof above supplies that conclusion.

As a concrete check, for \(n=12\) and \(h=4\), the optimal leaders are \(\{7\}\) at \(x=1/5\), \(\{6,7\}\) at \(x=1\), \(\{6\}\) at \(x=5\), and \(\{5\}\) at \(x=10\). This exhibits actual migration as the exceptional edge weakens.

## Relationship to prior work

Fitch and Leonard (arXiv:1407.1569, first public July 7, 2014) derive first-order noise-free-leader selection in terms of graph centrality. Patterson, McGlohon, and Dyagilev (arXiv:1412.6595 and arXiv:1604.07094) develop efficient exact selection on weighted paths/rings for first-order coherence \(\operatorname{tr}(L_{FF}^{-1})\) and first-order spectral convergence. Those are not the squared inverse performance functional. Sun et al. (DOI:10.1063/1.4897568) study second-order coherence through ungrounded network spectra on tree families, not this pinned one-defect path optimization. Mackin and Patterson (arXiv:1905.09156) consider higher-order coherence with finite diagonal information gains; their soft-pinning matrix is not the Dirichlet principal submatrix, and their general supermodularity methodology does not give this exact sharp phase diagram. The present classification therefore combines the ideal Dirichlet boundary, squared inverse, and a single resistance perturbation in a form not implied by these inspected statements.

## Limitations

The result concerns one exceptional edge and exactly one ideal noise-free grounded vertex. It does not automatically extend to several defects, correlated or non-unit noise covariance, finite leader-information gains, differently weighted damping/stiffness operators, or optimizing over edge weights simultaneously. Numerical experiments alone would not prove the infinite-family claims, and the literature comparison does not establish absolute publication priority. A highly specialized unlocated prior equivalent remains a residual risk; no independent external audit is asserted.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first posted 2014-07-07), https://arxiv.org/abs/1407.1569.
2. S. Patterson, N. McGlohon, and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (2014-12-20), https://arxiv.org/abs/1412.6595.
3. S. Patterson, N. McGlohon, and K. Dyagilev, *Optimal k-Leader Selection for Coherence and Convergence Rate in One-Dimensional Networks*, arXiv:1604.07094 (2016-04-24), https://arxiv.org/abs/1604.07094.
4. W. Sun et al., *Coherence in a family of tree networks with an application of Laplacian spectrum*, Chaos 24 (2014), DOI:10.1063/1.4897568, https://doi.org/10.1063/1.4897568.
5. E. Mackin and S. Patterson, *Submodularity in Systems with Higher Order Consensus with Absolute Information*, arXiv:1905.09156 (2019-05-22), https://arxiv.org/abs/1905.09156 (subsequent supporting comparison; not used to assign focal source age).
