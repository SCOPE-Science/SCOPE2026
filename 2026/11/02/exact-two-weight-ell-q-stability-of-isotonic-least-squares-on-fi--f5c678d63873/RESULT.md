# Exact two-weight \(\ell_q\) stability of isotonic least squares on finite orders

## Finding

Let \(P=(V,\preceq)\) be a **nonempty finite poset**, and let \(m_i,h_i>0\) be fixed fitting and monitoring masses, respectively. Define
\[
T(x)=\operatorname*{argmin}_{y_i\le y_j\text{ if }i\preceq j}
\sum_{i\in V}m_i(y_i-x_i)^2,
\qquad
\|z\|_{q,h}=\Big(\sum_{i\in V}h_i|z_i|^q\Big)^{1/q}
\]
for \(1\le q<\infty\), and take \(\|z\|_{\infty,h}=\max_{i\in V}|z_i|\). The minimizer exists and is unique, since the feasible cone is closed and nonempty and the quadratic objective is strictly convex and coercive. Write \(q'\) for the Hölder conjugate of \(q\), with \(1/\infty=0\).

Let \(\mathcal B(P)\) be the family of nonempty order-convex subsets \(B\subseteq V\) that induce a connected undirected Hasse graph. Order convexity means that \(a\preceq v\preceq b\) and \(a,b\in B\) imply \(v\in B\); singleton sets qualify. The exact Lipschitz coefficient is
\[
\operatorname{Lip}_{q,h}(T)=\max_{B\in\mathcal B(P)} K_q(B),\qquad
K_q(B)=\frac{(\sum_{i\in B}h_i)^{1/q}\|(m_i h_i^{-1/q})_{i\in B}\|_{q'}}{\sum_{i\in B}m_i}.
\]
For each admissible block there exists a pair of distinct data vectors whose distance ratio is \(K_q(B)\); thus the maximum is attained. At \(q=\infty\), the coefficient is always \(1\). For \(1\le q<\infty\), it is \(1\) exactly when \(h_i/m_i\) is constant on each weakly connected Hasse component; different components can have different constants.

For \(q=1\), \(K_1(B)=(\sum_B h_i)\max_{i\in B}(m_i/h_i)/(\sum_B m_i)\). For \(q=2\), \(K_2(B)^2=(\sum_B h_i)(\sum_B m_i^2/h_i)/(\sum_B m_i)^2\). On a two-point chain with \(m=(9,1)\) and \(h=(1,1)\) the coefficients are \(9/5\), \(\sqrt{41}/5\), and \(1\) at \(q=1,2,\infty\), respectively.

## Scope

The data and fits are real. The coefficient is the supremum of the monitored distance ratio over distinct data vectors. A nonempty ground set allows distinct data and ensures a nonempty maximum over blocks; if one includes the empty order, its domain is a singleton and the smallest nonnegative Lipschitz bound is \(0\), with no distinct pair to attain it. The result permits disconnected and branching orders. It does not address nonquadratic objectives, infinite orders, data-dependent weights, or the computational complexity of finding a maximizing block.

## Proof

**Equality components and linear branches.** For data \(x\) and fit \(y=T(x)\), retain the Hasse edges whose fitted values agree and take their undirected connected components. If \(a,b\) lie in one component and \(a\preceq v\preceq b\), any directed path from \(a\) to \(b\) through \(v\) has constant fitted value, so all its edges are retained and \(v\) is in the same component. Thus every block is in \(\mathcal B(P)\). Edges crossing different blocks are strict. One can perturb the common level of any block \(B\) slightly in either direction and remain feasible. Stationarity yields the fitted value \(\sum_{i\in B}m_ix_i/\sum_{i\in B}m_i\) on \(B\). Thus the projection agrees pointwise with one of finitely many linear maps formed by taking a direct sum of weighted block means.

**Norms and global bound.** For the block mean operator \(A_B\), set \(u_i=h_i^{1/q}z_i\) on \(B\). The scalar mean is the functional with coefficients \(m_i h_i^{-1/q}/\sum_{j\in B}m_j\) on \(u\), and its constant output is multiplied in norm by \((\sum_B h_i)^{1/q}\). The endpoint conventions give the same statement at infinity. Hölder duality gives precisely \(\|A_B\|=K_q(B)\); the norm is attained on the unit sphere. A direct sum has norm equal to its largest block norm. The weighted metric projection is continuous. Along any line segment, its finitely many possible branches are affine functions of the segment parameter; two different such functions can coincide at at most one parameter unless identical on the segment. Between these finitely many coincidence points continuity requires a single branch, up to identical restrictions. Summing the norm bounds on the subsegments proves the upper bound.

**Local attainability.** Fix \(B\in\mathcal B(P)\). Contract \(B\) to a vertex, discard internal edges, and leave all other vertices separate. Any directed cycle would have to pass through the contracted vertex and yield a directed path from a member of \(B\) to another through an outside vertex, impossible by order convexity (or acyclicity if the endpoints are the same). Assign strictly increasing levels on the quotient by a topological ordering, and lift to \(y\) on \(V\). Write \(M=\operatorname{diag}(m_i)\), and for an internal Hasse edge \(e=(i,j)\) let \(b_e=e_i-e_j\). Choose \(x=y+M^{-1}\sum_e b_e\). This is a projection witness: the weighted residual \(M(x-y)\) is a nonnegative combination of active inequality normals for \(b_e^Ty\le0\).

Let \(A\) be the block-mean map for the partition consisting of \(B\) and the remaining singletons. Then \(Ax=y\). For small \(z\), \(A(x+z)\) is still feasible because external inequalities are strict at \(y\). The residual change \(M(z-Az)\) vanishes outside \(B\) and sums to zero on \(B\). Internal edge vectors span that subspace, by Hasse connectivity on \(B\). Choose coefficients for this change by using a fixed basis of edge vectors, so the coefficients tend to zero as \(z\) tends to zero. The original multipliers were all one; hence the new multipliers remain nonnegative and the same projection condition proves \(T(x+z)=A(x+z)\). For a singleton the residual change is simply zero. Taking a nonzero norm-maximizing direction for \(A_B\), extended by zero outside \(B\) and scaled sufficiently small, attains the ratio exactly.

**Rigidity.** The block operator fixes constants, so \(K_q(B)\ge1\). For \(1<q<\infty\), equality in Hölder applied to \(\sum_B m_i=\sum_B h_i^{1/q}(m_i h_i^{-1/q})\) gives equality precisely when \(m_i/h_i\) is constant on \(B\); at \(q=1\) use the equality case of a weighted mean bounded by its maximum. Every Hasse cover pair is an admissible block, so unequal ratios on a cover force amplification. Ratios agreeing on all covers are constant on each weak component, giving equality on all admissible blocks. At \(q=\infty\) a weighted mean is always a convex combination and has norm one.

## Verification

The accompanying standard-library `verify_weighted_isotonic.py` checks seven nonempty orders, with four fitting profiles and three monitoring profiles per fitting choice, for 84 weighted graph cases. It compares exact rational \(\ell_1\) and squared \(\ell_2\) norms on candidate blocks and feasible partitions, checks normal-cone witnesses, tests rigidity, and includes the two-point witness. These bounded diagnostics do not replace the proof.

## Related work

Németh and Németh study coordinatewise order preservation for weighted isotonic regression projections. Kyng, Rao, and Sachdeva provide algorithms for regression on weighted finite directed acyclic graphs. Yang and Barber characterize the norms for which unweighted Euclidean isotonic projection on a chain is nonexpansive. The calculation here identifies all locally realizable single pools and computes their sharp response to a separate weighted monitoring norm. General polyhedral projection theory accounts for the piecewise-linear structure; the stated maximum and rigidity use the order-specific block geometry. These comparisons do not establish publication priority.

## References

1. A. B. Németh and S. Z. Németh, *Isotonic regression and isotonic projection*, [arXiv:1503.08458](https://arxiv.org/abs/1503.08458), Linear Algebra Appl. **494** (2016), 80–89.
2. R. Kyng, A. Rao, and S. Sachdeva, *Fast, Provable Algorithms for Isotonic Regression in all \(\ell_p\)-norms*, [arXiv:1507.00710](https://arxiv.org/abs/1507.00710), 2015.
3. F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, [arXiv:1706.01852](https://arxiv.org/abs/1706.01852), 2017.
4. J. de Leeuw, K. Hornik, and P. Mair, *Isotone Optimization in R: Pool-Adjacent-Violators Algorithm (PAVA) and Active Set Methods*, J. Stat. Softw. **32** (2009), no. 5.
