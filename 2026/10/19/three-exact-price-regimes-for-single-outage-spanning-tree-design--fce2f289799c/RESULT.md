# Three exact price regimes for single-outage spanning-tree design on book networks

## Finding

For every integer \(m\ge2\), price \(t>0\), and budget \(B>0\), consider the book graph \(G_m=K_2\vee\overline{K_m}\). The two hubs are adjacent, and every one of \(m\) other vertices joins both hubs. The \(2m\) hub-to-page edges have unit price; the common hub edge has price \(t\). Assign independently chosen nonnegative conductances \(w_e\), subject to \(\sum_{e\ne e_0}w_e+t w_{e_0}=B\), where \(e_0\) is the hub edge.

For a weighted graph \(H\), define its weighted spanning-tree number by \(\tau(H)=\sum_{T\text{ spanning tree}}\prod_{e\in T}w_e\), with value zero if disconnected. Maximize the fault-tolerant objective
\[
\mathcal R(w)=\min_{e\in E(G_m)}\tau(G_m-e),
\]
where failure means removing exactly one designated edge without reallocating its conductance (including an edge currently assigned zero conductance).

Define two sharp price thresholds
\[
t_1(m)=\frac{4m}{2m^2+m-1},\qquad
t_2(m)=\frac{4m}{m^2-1},\qquad 0<t_1(m)<t_2(m).
\]
The **unique global maximizer among all independent allocations** puts the same positive conductance \(a_*\) on every hub-to-page edge and conductance \(b_*\ge0\) on the common hub edge. Its ratio \(r_*=b_*/a_*\) is exactly
\[
r_*=\begin{cases}
(m+1)/2,&0<t\le t_1(m),\\[2pt]
\big(4m-(m^2-1)t\big)/(2mt),&t_1(m)<t<t_2(m),\\[2pt]
0,&t\ge t_2(m).
\end{cases}
\]
The conductances and global optimum are
\[
a_*=\frac{B}{2m+t r_*},\qquad b_*=r_*a_*,\qquad
\mathcal R_*=\frac{2^{m-2}B^{m+1}}{(2m+t r_*)^{m+1}}\min\{m-1+2r_*,2m\}.
\]
For \(0<t\le t_1(m)\), deletion of any hub-to-page edge and deletion of the hub edge are equally harmful at the optimum; for \(t>t_1(m)\), a hub-to-page edge is the worst failure. For \(t\ge t_2(m)\), the unique optimum buys no hub edge. The two price thresholds obey \(m t_1(m)\to2\) and \(m t_2(m)\to4\).

In contrast, **without edge failures** the nominal weighted spanning-tree objective deletes the hub edge already at price \(4/(m+1)\), which is strictly smaller than \(t_2(m)\). Robustness thus creates a genuine price interval in which the backup edge is worth buying although the nominal optimum would delete it.

## Assumptions and scope

All assertions hold for every integer \(m\ge2\) and every real \(t,B>0\), with no assumed equality among the \(2m\) adjustable conductances. All conductances are nonnegative. The design is chosen before an adversary removes any one of the \(2m+1\) designated edges. The objective is a weighted spanning-tree polynomial, not a claim about exact all-terminal reliability probabilities under arbitrary random-failure laws. The supremum is attained, and all statements about uniqueness refer to the entire unrestricted budget simplex.

## Proof

**1. Concavity and symmetry are globally legitimate.** Delete one vertex from every graph Laplacian to obtain a reduced weighted Laplacian \(M_e(w)\) for the graph after edge \(e\) fails. By the weighted matrix-tree theorem, \(\tau(G_m-e)=\det M_e(w)\). On the domain where every \(M_e\) is positive definite, \(f_e(w)=\log\det M_e(w)\) is concave: \(M_e\) is affine in \(w\) and log-determinant is concave on positive-definite matrices. Therefore \(\phi(w)=\min_e f_e(w)\) is concave as the pointwise minimum of finitely many concave functions. Setting \(\log0=-\infty\) extends this conclusion to disconnected failure scenarios. This objective is invariant under exchanging the hubs and permuting the page vertices. Averaging an arbitrary feasible allocation over this finite automorphism group cannot reduce \(\phi\). Hence some global maximizer has common spoke conductance \(a\) and hub-edge conductance \(b\). Since a positive fully survivable allocation exists, \(a>0\) at every such symmetric maximizer. Compactness of the budget simplex and continuity of the spanning-tree polynomials ensure existence. (Full budget expenditure is also forced by positive homogeneity.)

**2. All possible outage tree-counts have closed forms.** For symmetric conductances \(a,b\), the nonzero Laplacian eigenvalues of the intact book graph are \(2a\) with multiplicity \(m-1\), together with \((m+2)a\) and \(ma+2b\). Thus
\[
\tau(G_m)=2^{m-1}a^m(ma+2b).
\]
Deleting the hub edge leaves \(K_{2,m}\), so
\[
\tau_{\rm hub}=2^{m-1}m a^{m+1}.
\]
The spanning-tree polynomial is multilinear in every individual conductance. Differentiating the symmetric polynomial simultaneously with respect to all \(2m\) spoke weights and using their transitivity shows that deleting any single spoke removes \(a/(2m)\) times the derivative of \(\tau(G_m)\) with respect to the common value \(a\). Consequently
\[
\tau_{\rm spoke}=2^{m-2}a^m((m-1)a+2b).
\]
These are the only two automorphism-orbits of potential failures. Their exact equality occurs when \(b/a=(m+1)/2\).

**3. Exact one-variable optimization.** Set \(r=b/a\ge0\). The budget gives \(a=B/(2m+tr)\). Hence
\[
\mathcal R(r)=2^{m-2}B^{m+1}\frac{\min\{m-1+2r,2m\}}{(2m+tr)^{m+1}}.
\]
For \(r\ge(m+1)/2\), the numerator is constant while the denominator grows strictly; therefore the optimum has \(0\le r\le(m+1)/2\). On this latter interval the numerator is \(m-1+2r\), and the derivative has precisely the sign of
\[
4m-(m^2-1)t-2mt r.
\]
This affine expression is strictly decreasing in \(r\). Its zero is \(r=(4m-(m^2-1)t)/(2mt)\). It reaches the upper endpoint exactly at \(t=t_1(m)\) and reaches zero exactly at \(t=t_2(m)\). This proves the three regimes and the displayed optimum among symmetric designs, including the boundary cases.

**4. The unrestricted optimizer is actually unique.** For the orbit \(S\) of \(2m\) spoke failures define
\[
F_S(w)=\frac1{2m}\sum_{e\in S}\log\tau(G_m-e),
\]
and let \(F_0(w)=\log\tau(G_m-e_0)\) for hub failure. Both are concave and automorphism-invariant, and for any \(\lambda\in[0,1]\) the function \(F_\lambda=\lambda F_S+(1-\lambda)F_0\) satisfies \(\phi(w)\le F_\lambda(w)\). Moreover \(F_S\) is **strictly concave** wherever all spoke-failure Laplacians are positive definite. Indeed, the Hessian of \(\log\det M_e\) has vanishing second variation in a direction \(d\) only if \(\sum_{f\ne e}d_f u_fu_f^{\mathsf T}=0\). For a simple graph, the distinct reduced incidence dyads \(u_fu_f^{\mathsf T}\) are linearly independent: off-diagonal entries identify non-root edges, and then diagonal entries identify root-incident edges. Thus the only null direction for \(\log\det M_e\) changes the deleted edge itself. Averaging over the \(2m\ge4\) different spoke failures leaves no common nonzero null direction. Consequently \(F_\lambda\) is strictly concave for every \(\lambda>0\).

When \(t\ge t_1(m)\), the scalar maximizer of \(F_S\) is exactly \(r_*\); at the symmetric optimum the worst failure is a spoke. Since \(F_S\) is invariant and concave, averaging arbitrary allocations proves this is its global maximum; since \(\phi\le F_S\) with equality there, it is the global maximum of \(\phi\). Strict concavity gives uniqueness, including \(t=t_1(m)\) and \(t=t_2(m)\).

When \(0<t<t_1(m)\), the optimum occurs at \(r_c=(m+1)/2\), where both failure types tie. At that ratio, the derivative of the symmetric restriction of \(F_S\) is strictly positive and that of \(F_0\) is strictly negative. Choose the unique \(\lambda\in(0,1)\) that makes the derivative of the symmetric restriction of \(F_\lambda\) vanish there. Invariance implies that this interior symmetric point is stationary under the full linear budget constraint; concavity makes it a global maximizer of \(F_\lambda\), and strict concavity makes it unique. Equality \(\phi=F_\lambda\) at the point then establishes unique global optimality for \(\phi\) as well. Thus no asymmetric optimum has been overlooked.

**5. Nominal comparison and limits.** In the intact network, maximize \(2^{m-1}a^m(ma+2b)\) under the same budget. Differentiation at \(b=0\) gives a positive benefit from buying the hub edge exactly when \(t<4/(m+1)\). Concavity and symmetry establish the global threshold. The strict inequality \(4/(m+1)<4m/(m^2-1)\) holds for every \(m\ge2\). Finally, multiply the rational threshold expressions by \(m\) and pass to the limit to obtain \(2\) and \(4\).

## Verification

The standalone file `verify_robust_book.py` uses only Python's standard library to construct actual reduced weighted Laplacians and compute exact rational determinants. Execute `python3 verify_robust_book.py` from the same directory. Its finite tests cover seven graph sizes, rational conductances including zero backup, all individual edge failures, price samples in all regimes and both boundaries, independent rational competitor ratios, and budget-preserving asymmetric perturbations. The proof above, not finite computations, justifies every universal quantifier.

## Relationship to prior work

Khosoussi, Sukhatme, Huang, and Dissanayake (arXiv:1604.01116, first posted 2016-04-05) studied weighted spanning-tree maximization, log-submodularity, and discrete edge-selection algorithms and relaxations. Their full-text Sections 2.2, 3, 4, and 5 give the matrix-tree and determinant framework but do not state the priced single-outage robust optimization or its two exact thresholds. Daoud (2013) computed spanning-tree counts of stacked-book graphs defined as Cartesian products of stars and paths, a different graph family and a count rather than a price-constrained robust design. Earlier exact work on fault-tolerant Laplacian algebraic connectivity of the same book graphs studies a different objective and does not entail the spanning-tree-determinant thresholds. General D-optimal-design and determinant-rank-one update principles motivate the formulation but by themselves do not fix the entire optimality phase diagram.

## Limitations

The theorem concerns deterministic deletion of at most one named edge, a linear conductance budget, and this book-graph family only. It does not optimize exact independent-failure reliability, multiple simultaneous failures, other topology classes, discrete edge-selection budgets, or dynamic redistribution after damage. Zero-price \(t=0\) is excluded. A semantically equivalent result could exist in literature indexed only under experimental design, network reliability, or another formulation; independent historical review remains appropriate.

## References

1. K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116 (first publicly posted 2016-04-05). https://arxiv.org/abs/1604.01116
2. S. N. Daoud, *Complexity of stacked book graph and cone graphs*, Journal of Taibah University for Science **7** (2013), 162–172, DOI:10.1016/j.jtusci.2013.04.006. (Related graph count, different family.)
3. G. Kirchhoff, classical matrix-tree theorem, used through the modern weighted formulation in Reference 1, Section 2.2.
