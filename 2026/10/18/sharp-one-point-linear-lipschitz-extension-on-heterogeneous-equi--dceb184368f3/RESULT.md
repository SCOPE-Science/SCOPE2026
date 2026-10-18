# Sharp one-point linear Lipschitz extension on heterogeneous equilateral clusters

## Finding
Let \(X\) be the disjoint union of \(k\ge2\) nonempty clusters \(C_i\), of sizes \(m_i\), with within-cluster distance \(a_i\) (for distinct members) and every cross-cluster distance equal to \(c\). Adjoin one point \(o\) at distance \(r_i\) from every member of \(C_i\), under the metric conditions below. For real scalar Lipschitz functions, the smallest operator norm of a **linear simultaneous extension** \(E:\operatorname{Lip}(X)\to\operatorname{Lip}(X\cup\{o\})\), satisfying \((Ef)|_X=f\), is
\[
\boxed{\Lambda=\max\{1,L_*\}},\qquad
\boxed{\sum_{i=1}^k\frac{(c-L_*r_i)_+}{c-a_i(1-1/m_i)}=1},
\]
where \(L_*>0\) is the unique solution and \((t)_+=\max\{0,t\}\). The operator norm uses only the Lipschitz seminorm (equivalently the norm on functions modulo constants). The formula holds for unequal cluster cardinalities, unequal within-cluster distances, unequal new-point distances, and singleton clusters.

A minimizing extension is obtained by the *explicit positive barycenter*
\[
(Ef)(o)=\sum_{i=1}^k\frac{\alpha_i}{m_i}\sum_{x\in C_i}f(x),\quad
\alpha_i=\frac{(c-L_*r_i)_+}{c-a_i(1-1/m_i)},\quad\sum_i\alpha_i=1.
\]
The weights minimizing just the new-point Lipschitz seminorm are the unique permutation-invariant minimizer; no uniqueness is claimed among unrestricted extension operators. Only clusters with \(r_i<c/L_*\) receive positive weight, and these form an initial segment after sorting \(r_i\). Their weights and \(L_*\) are exactly computable in \(O(k\log k)\) rational arithmetic operations when all distances are rational.

## Assumptions and scope
Fix \(k\ge2\), integers \(m_i\ge1\), and \(c>0\). If \(m_i\ge2\), choose \(0<a_i\le c\); for \(m_i=1\), set \(a_i=0\). Set \(d(x,y)=a_i\) for different \(x,y\in C_i\) and \(d(x,y)=c\) for points of different clusters. The distances from the added point satisfy \(r_i>0\), \(a_i\le2r_i\), and \(|r_i-r_j|\le c\le r_i+r_j\) for every \(i\ne j\). These conditions make the full distance assignment a metric. For \(m_i=1\), the within-cluster condition is vacuous. There are no further hidden genericity or strict-inequality assumptions; tied radii and equality in metric constraints are allowed.

For a real-valued function on a finite metric space, define \([f]_{\rm Lip}=\max_{x\ne y}|f(x)-f(y)|/d(x,y)\). A linear extension preserves each old value. Its seminorm operator norm is the least \(K\) such that \([Ef]_{\rm Lip}\le K[f]_{\rm Lip}\) for all \(f\). Every bounded operator in this sense preserves constants, and is determined at \(o\) by a signed mass \(\mu\) on \(X\) with total mass one. Equivalently one can work with functions vanishing at a chosen base point and restore constants afterward.

## Proof
**1. Symmetry and the free-space minimax.** Permuting the members of each cluster preserves the entire metric, including \(o\). Average any linear extension over the finite product of these permutation groups. Its norm cannot increase. Every invariant extension has the form
\[
(Ef)(o)=\sum_{j=1}^k\frac{\alpha_j}{m_j}\sum_{x\in C_j}f(x),\qquad \sum_j\alpha_j=1,
\]
with real, initially possibly negative \(\alpha_j\). For a fixed \(x\in C_i\), the largest possible value of \(|(Ef)(o)-f(x)|\) over \([f]_{\rm Lip}\le1\) is the Kantorovich--Rubinstein norm \(\|\mu-\delta_x\|_{\rm KR}\). Therefore
\[
\|E\|=\max\left\{1,\max_i \frac{T_i(\alpha)}{r_i}\right\},\quad
T_i(\alpha)=\|\mu-\delta_x\|_{\rm KR}\quad (x\in C_i).
\]

**2. Exact transportation norm.** Realize \(X\) as leaves of a weighted tree. For each cluster put an edge of length \((c-a_i)/2\) from a common root to its cluster center, and an edge of length \(a_i/2\) from that center to each leaf. Zero-length edges are contracted when necessary. The induced leaf distances are exactly \(a_i\) within clusters and \(c\) between clusters. For any signed leaf mass \(\nu\) of total zero, its KR norm is the sum, over tree edges, of edge length times the absolute mass of the hanging subtree. Indeed every one-Lipschitz leaf potential extends to the tree; conversely independent edge-potential signs attain that sum. Applying this formula to \(\mu-\delta_x\) gives the *exact identity*, valid for all signed \(\alpha\):
\[
\begin{aligned}
2T_i(\alpha)={}&c\sum_{j\ne i}|\alpha_j|\\
&+a_i\left(\left|\frac{\alpha_i}{m_i}-1\right|
 +\frac{m_i-1}{m_i}|\alpha_i|\right)
 +(c-a_i)|\alpha_i-1|.
\end{aligned}
\tag{1}
\]

**3. Signed coefficients cannot improve the infimum.** Suppose \(\alpha_u>0\) and \(\alpha_v<0\). Transfer \(t=\min\{\alpha_u,-\alpha_v\}\) by replacing the pair with \((\alpha_u-t,\alpha_v+t)\). This keeps the coefficient sum equal to one. For \(i\notin\{u,v\}\), formula (1) decreases \(2T_i\) by \(2ct\). For \(i=v\), the self-term in (1) equals \(c(1-\alpha_v)\) while \(\alpha_v\le0\), so increasing \(\alpha_v\) decreases that self-term by \(ct\); the contribution \(c|\alpha_u|\) also decreases by \(ct\). For \(i=u\), the other-cluster term decreases by \(ct\), while decreasing positive \(\alpha_u\) increases its self-term by *at most* \(ct\): that piecewise-affine self-term has slopes \(2a_u(1-1/m_u)-c\), \(c-2a_u/m_u\), and \(c\) on its three positive-coordinate pieces (empty pieces for singleton clusters), all at least \(-c\). Thus none of the \(T_i\) increases. Repeating this operation terminates when every coefficient is nonnegative, because each transfer removes a negative or a positive coordinate. Therefore a positive minimizing barycenter always exists, with no sign assumption smuggled into the optimization.

**4. Solve the positive minimax exactly.** On the simplex \(\alpha_j\ge0\), \(\sum\alpha_j=1\), formula (1) simplifies to
\[
T_i(\alpha)=c-d_i\alpha_i,\qquad d_i=c-a_i(1-1/m_i)>0.
\]
Hence the sharp *new-point* constant minimizes \(\max_i(c-d_i\alpha_i)/r_i\). A proposed bound \(L\) is feasible exactly when
\[
\alpha_i\ge\frac{(c-Lr_i)_+}{d_i}\quad\forall i,\qquad\sum_i\alpha_i=1,
\]
which holds if and only if \(F(L)=\sum_i(c-Lr_i)_+/d_i\le1\). Since \(d_i\le c\) and \(k\ge2\), we have \(F(0)\ge2\), while \(F(L)=0\) for sufficiently large \(L\); \(F\) is continuous and strictly decreasing while positive. Thus the unique root \(L_*>0\) with \(F(L_*)=1\) is the minimum. At that root, all the lower bounds on the weights sum to one, so the stated positive weights are forced. Restoring the old-pair Lipschitz seminorm gives \(\Lambda=\max\{1,L_*\}\).

**5. Exact active-set algorithm and phase boundaries.** Sort clusters so \(r_1\le\cdots\le r_k\). For a proposed active initial segment \(I\), solve the root equation without positive parts:
\[
L_I=\frac{c\sum_{i\in I}d_i^{-1}-1}{\sum_{i\in I}r_i d_i^{-1}}.
\]
Choose the first segment for which \(L_Ir_i\le c\) on \(I\) and \(L_Ir_i\ge c\) off \(I\); boundary terms give zero weights. A sort followed by cumulative reciprocal-weight sums finds it in \(O(k\log k)\) arithmetic operations. The exact active set changes only when an equality \(L_*r_i=c\) is reached. This proves the asserted piecewise-rational sharp phase diagram in the metric parameters.

## Verification
The accompanying `verify_cluster_extension.py` checks the exact root, exact signed-coefficient inequalities, and center-attainment identities using rational arithmetic. It also formulates a *separate unrestricted linear program* directly in leaf-level signed coefficients and tree-edge absolute flows, with no prior symmetry or positivity constraints. The saved checker passed 6,272 assertions across random admissible heterogeneous instances with two to five clusters, including independently solved unrestricted linear programs for small cases. Run `python3 verify_cluster_extension.py` with Python 3 and SciPy installed. Finite computations test and reproduce the formula; all quantifiers in the theorem are established by the preceding analytic proof.

For example, when \(k=3\), all \(m_i=10\), all \(a_i=19/10\), \(c=2\), and \((r_1,r_2,r_3)=(1,11/10,19/10)\), then \(L_*=53/30\) and \((\alpha_1,\alpha_2,\alpha_3)=(70/87,17/87,0)\). The third cluster is excluded *exactly*, even though it contains ten points; this is a genuine active-set transition rather than a small-weight approximation.

## Relationship to prior work
Bruè, Di Marino, and Stra construct linear Lipschitz extension operators through regular random projections (arXiv:1801.07533, Theorem 4.1 and its proof); that general doubling-space estimate does not evaluate the optimal finite-cluster operator norm or its active-set thresholds. Ambrosio and Puglisi (arXiv:1609.01450) develop the equivalence between random projections, transportation geometry, and linear extension, but do not supply the present exact finite clustered minimax. Albiac, Ansorena, Cúth, and Doucha (arXiv:2005.06555, especially Lemmas 2.7–2.8 and Section 5) give broad complementability and one-point bounds without these exact heterogeneous formulas. Sofi (arXiv:2001.09303) concerns general existence and Banach-space structure; Basso (arXiv:1707.06593, especially Section 4) studies universal extensions into Banach targets and Walsh-vector lower bounds, not this finite sharp scalar linear computation.

Among other relevant public results, *Sharp optimal projection constants for clustered finite metric free spaces* determines a projection norm **within the original free space**, for its within-cluster fluctuation subspace; it does not adjoin a point, vary new-point radii, or optimize the extension value. *Sharp leaf-count transitions in one-point \(p\)-Banach Lipschitz extensions* determines universal extension constants for equilateral leaves and arbitrary \(p\)-Banach targets; our result is specifically the real-linear scalar operator optimum for multiple unequal clusters, and is not a corollary of that equilateral formula. Explicit comparisons use the actual different objects and norm quantifiers, not merely dissimilar titles.

## Limitations
The theorem requires real scalar functions, the described finite clustered equilateral metric, and one added point with constant radius on each cluster. It does not cover arbitrary non-equilateral within-cluster distances, nonlinear extension of vector-valued functions, or multiple newly added points. The \(O(k\log k)\) count is of rational arithmetic operations, not bit complexity. Unindexed equivalent literature cannot be excluded merely by unsuccessful searches, and no independent scientific audit has been performed.

## References
- E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533v1 (first posted 23 January 2018), Theorem 4.1. https://arxiv.org/abs/1801.07533.
- L. Ambrosio, D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, arXiv:1609.01450 (2016), https://arxiv.org/abs/1609.01450.
- F. Albiac, J. L. Ansorena, M. Cúth, M. Doucha, *Lipschitz free spaces isomorphic to their infinite sums and geometric applications*, arXiv:2005.06555 (2020), especially Lemmas 2.7–2.8 and Section 5. https://arxiv.org/abs/2005.06555.
- M. A. Sofi, *Extension operators and nonlinear structure of Banach spaces*, arXiv:2001.09303 (2020), especially Section 2. https://arxiv.org/abs/2001.09303.
- G. Basso, *Lipschitz extensions to finitely many points*, arXiv:1707.06593 (2017), especially Section 4. https://arxiv.org/abs/1707.06593.
- Public mathematical results: *Sharp optimal projection constants for clustered finite metric free spaces* (record bd13acd51aa3); *Sharp leaf-count transitions in one-point \(p\)-Banach Lipschitz extensions* (record b03e5cc2b3f1). Those are compared for distinct implication scopes, not offered as certification.
