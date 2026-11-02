# Exact two-weight \(\ell_q\) stability of isotonic least squares on finite orders

## Finding

Let \(P=(V,\preceq)\) be any finite poset. Let fitting masses \(m_i>0\) and monitoring masses \(h_i>0\) be prescribed for every \(i\in V\). Define the **weighted isotonic least-squares map** \(T:\mathbb R^V\to\mathbb R^V\) by
\[
T(x)=\underset{y_i\le y_j\ \mathrm{whenever}\ i\preceq j}{\operatorname{argmin}}
\sum_{i\in V}m_i(y_i-x_i)^2.
\]
For \(1\le q<\infty\), put \(\|z\|_{q,h}=(\sum_{i\in V}h_i|z_i|^q)^{1/q}\), and put \(\|z\|_{\infty,h}=\max_i|z_i|\). Let \(q'\) denote the Hölder conjugate, using \(1/\infty=0\).

Let \(\mathcal B(P)\) consist of the nonempty subsets \(B\subseteq V\) that are both *order-convex* (whenever \(a,b\in B\) and \(a\preceq v\preceq b\), then \(v\in B\)) and connected in the undirected Hasse graph induced by \(B\). Every singleton belongs to \(\mathcal B(P)\).

**Theorem.** For all finite \(P\), all fitting/monitoring masses, and all \(1\le q\le\infty\), the exact global data-to-fit Lipschitz coefficient is
\[
\boxed{\operatorname{Lip}_{q,h}(T)
=\max_{B\in\mathcal B(P)}K_q(B),\qquad
K_q(B)=\frac{(\sum_{i\in B}h_i)^{1/q}\big\|(m_i h_i^{-1/q})_{i\in B}\big\|_{q'}}{\sum_{i\in B}m_i}.}
\]
The coefficient is **attained by a pair of distinct data vectors**, not merely approached. In particular, \(\operatorname{Lip}_{\infty,h}(T)=1\). For \(1\le q<\infty\), the coefficient is \(1\) if and only if the ratio \(h_i/m_i\) is constant within every weakly connected Hasse component. This includes disconnected posets, where distinct components may have different proportionality constants.

For \(q=1\), the block expression is \(K_1(B)=(\sum_B h_i)\max_{j\in B}(m_j/h_j)/(\sum_Bm_i)\). For \(q=2\), its square is \(K_2(B)^2=(\sum_Bh_i)(\sum_Bm_i^2/h_i)/(\sum_Bm_i)^2\). An elementary sharp witness is a two-point chain with \(m=(9,1)\), \(h=(1,1)\): the coefficients are \(9/5\), \(\sqrt{41}/5\), and \(1\) at \(q=1,2,\infty\), respectively.

## Assumptions and scope

The order is any finite partial order; Hasse edges are the directed cover relations. All fitting and monitoring masses are strictly positive and fixed while the data vary. Inputs, fits, and perturbations are real. The displayed coefficient is the supremum over distinct pairs of inputs of the ratio of their monitored fit distance to their monitored input distance. No restriction is imposed on the number of cover edges, the number of weakly connected components, or whether the poset is a chain.

## Proof

**1. Equality blocks have exactly the relevant geometry.** Fix data \(x\) and write \(y=T(x)\). Retain the Hasse edges \(i\prec j\) for which \(y_i=y_j\), and let their undirected connected components be \(B_1,\ldots,B_s\). Along every directed path between two elements of a component, isotonicity forces all intermediate fitted values to coincide. Hence each \(B_a\) is order-convex. By definition each is Hasse-connected. Edges joining distinct components have strict fitted inequalities.

Varying the common value of any one equality block slightly up and down does not violate inequalities joining different blocks. First-order stationarity therefore gives
\[
y_i=\frac{\sum_{j\in B_a}m_jx_j}{\sum_{j\in B_a}m_j}
\quad (i\in B_a).
\]
Consequently, at every input the map \(T\) agrees with one of finitely many block-averaging linear maps corresponding to a partition into blocks from \(\mathcal B(P)\).

**2. Norm of a weighted block.** On \(B\), the averaging linear map is \(A_Bz=\mathbf1_B(\sum_Bm_iz_i)/(\sum_Bm_i)\). Weighted Hölder duality gives exactly
\[
\|A_B\|_{\ell_q(h|_B)\to\ell_q(h|_B)}
=\frac{(\sum_B h_i)^{1/q}\|(m_i h_i^{-1/q})_{i\in B}\|_{q'}}{\sum_Bm_i}=K_q(B).
\]
For \(q=1\) the maximizing input is supported at an index maximizing \(m_i/h_i\); for \(1<q<\infty\) use equality in Hölder; and for \(q=\infty\) use a constant input. A direct sum over disjoint blocks has operator norm the largest of its block norms. A continuous piecewise-linear map selected from finitely many linear block maps has Lipschitz coefficient no greater than the largest branch norm: restrict to any line segment and subdivide into its finitely many affine pieces, then sum the inequalities. Weighted metric projection onto a polyhedral order cone is continuous and piecewise linear, proving the asserted global upper bound.

**3. Every listed block is locally attainable.** Fix an order-convex Hasse-connected \(B\). Contract \(B\) to one vertex in the Hasse diagram, leaving all other vertices separate. The quotient remains acyclic: a new directed cycle would contain a path from one element of \(B\) through a vertex outside \(B\) to another element of \(B\), contradicting order convexity. Assign strictly order-preserving real levels to the quotient vertices, and pull them back to a feasible vector \(y\); the only equality Hasse edges now lie inside \(B\).

For every Hasse edge \(e=(i,j)\) internal to \(B\), select a positive multiplier \(\lambda_e\), and put \(b_e=e_i-e_j\). Define data by
\[
x_i=y_i+\frac{1}{m_i}\sum_{e}\lambda_e(b_e)_i.
\]
Then \(\operatorname{diag}(m)(x-y)=\sum_e\lambda_e b_e\), which is precisely the optimality/Karush–Kuhn–Tucker normal-cone condition for the weighted least-squares projection at \(y\). Since all internal multipliers can be chosen strictly positive and the induced undirected Hasse graph on \(B\) is connected, the residual normal lies in the relative interior of the active normal cone on its full \((|B|-1)\)-dimensional span. All external inequalities are strict. Thus in an open neighborhood of this data, the active face remains the one with exactly \(B\) pooled and all outside vertices singleton; the local map is the corresponding weighted block averaging map. Choosing a norm-maximizing perturbation from Step 2 and two nearby inputs attains \(K_q(B)\) exactly. Taking the largest such block proves the formula and attainment.

**4. Nonexpansivity rigidity.** For any \(B\), weighted Hölder applied to \(\sum_B m_i=\sum_B h_i^{1/q}(m_i h_i^{-1/q})\) gives \(K_q(B)\ge1\); equality for finite \(q\) occurs precisely when \(m_i/h_i\) is constant on \(B\) (the same statement follows from the maximum form at \(q=1\)). Every Hasse cover pair is an admissible \(B\), so a monitoring/fitting mass mismatch across any cover produces strict amplification. Conversely, when those ratios agree along each Hasse edge they agree throughout each weak component and hence on every admissible block; every \(K_q(B)=1\). At \(q=\infty\) each block mean is a convex combination, and \(K_\infty(B)=1\) regardless of masses. This proves the classification.

## Verification

The accompanying standard-library script `verify_weighted_isotonic.py` enumerates all nonempty connected order-convex subsets and all feasible equality-face partitions for seven nonisomorphic small directed orders, with three fitting/monitoring profiles each. It compares the exact rational \(\ell_1\) and squared \(\ell_2\) norm formulas and verifies the quotient-face/KKT witnesses. It also tests rigidity and the two-point example. Run `python3 verify_weighted_isotonic.py`. The observed counts are 84 weighted graph cases, 1,164 admissible-block checks, 1,152 feasible-partition comparisons, and 63 further rigidity comparisons. These finite checks are corroboration only; all finite posets and all real positive masses are covered by the proof.

## Relationship to prior work

Németh and Németh's 2015 article treats coordinatewise order preservation of metric projections onto weighted isotonic regression cones, not the sharp response-to-data Lipschitz coefficient for an independently chosen monitoring norm. Kyng, Rao, and Sachdeva (2015) give algorithms for isotonic regression on weighted finite directed acyclic graphs rather than a sharp two-weight perturbation norm. Yang and Barber (2017, first posted after the archival source date) prove a necessary-and-sufficient norm criterion for *unweighted* Euclidean least-squares projection onto a **chain**; the current two-weight/branching finite-poset formula and equality criterion are not special cases of their stated theorem. Published stability calculations for \(\ell_p\)-objective metric projections concern a different projection map when \(p\ne2\). These are comparisons of statements and logical implications; absence of a directly matching title does not certify novelty.

## Limitations

The theorem is finite-dimensional, real, and requires strictly positive masses and exact weighted least-squares minimization. It makes no assertion about noisy estimation risk, computational complexity of finding the maximizing block in arbitrary posets, nonquadratic fitting losses, infinite orders, or data-dependent fitting weights. A broader unlocated theorem on polyhedral projection sensitivity could subsume the calculation; no independent scientific audit has been performed. The computational checks only cover the listed finite examples.

## References

1. A. B. Németh and S. Z. Németh, *Isotonic regression and isotonic projection*, arXiv:1503.08458v1, first posted 2015-03-29; *Linear Algebra and its Applications* **494** (2016), 80–89. https://arxiv.org/abs/1503.08458.
2. R. Kyng, A. Rao, and S. Sachdeva, *Fast, Provable Algorithms for Isotonic Regression in all \(\ell_p\)-norms*, arXiv:1507.00710v1, first posted 2015-07-02. https://arxiv.org/abs/1507.00710.
3. F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852v1, first posted 2017-06-06. https://arxiv.org/abs/1706.01852.
4. J. de Leeuw, K. Hornik, and P. Mair, *Isotone Optimization in R: Pool-Adjacent-Violators Algorithm (PAVA) and Active Set Methods*, *Journal of Statistical Software* **32** (2009), issue 5. https://www.jstatsoft.org/v32/i05/.
