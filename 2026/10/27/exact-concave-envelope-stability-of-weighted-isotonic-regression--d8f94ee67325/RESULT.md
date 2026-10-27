# Exact concave-envelope stability of weighted isotonic regression in path variation

## Finding

Fix an integer \(n\ge 2\), positive observation masses \(a_1,\ldots,a_n\), and positive edge-variation weights \(q_1,\ldots,q_{n-1}\). Let \(P_a\) be weighted least-squares isotonic regression, defined for every \(y\in\mathbb R^n\) by
\[
P_a(y)=\operatorname*{argmin}_{z_1\le\cdots\le z_n}
\sum_{i=1}^{n}a_i(z_i-y_i)^2.
\]
Define the path-variation seminorm
\[
V_q(y)=\sum_{j=1}^{n-1}q_j|y_{j+1}-y_j|.
\]
Set \(A_0=0\), \(A_j=\sum_{i=1}^j a_i\), \(Q_0=Q_n=0\), and \(Q_j=q_j\) at the interior indices. Let \(H\) be the **least concave majorant** of the points \((A_j,Q_j)\) on \([0,A_n]\), with linear interpolation between its consecutive vertices. Then the exact global two-data variation Lipschitz constant is
\[
\boxed{\sup_{V_q(x-y)>0}
\frac{V_q(P_a(x)-P_a(y))}{V_q(x-y)}
=K(a,q):=\max_{1\le j<n}\frac{H(A_j)}{q_j}.}
\]
The supremum is attained by an actual pair of finite real input vectors for every choice of positive masses and variation weights. It has the equivalent fully explicit form
\[
K(a,q)=\max\!\left\{1,\max_{\substack{0\le L<j<R\le n}}
\frac{Q_L(A_R-A_j)+Q_R(A_j-A_L)}{q_j(A_R-A_L)}\right\}.
\]
In particular, isotonic regression is **nonexpansive for the variation of differences** exactly when the following weighted discrete concavity inequalities hold:
\[
\boxed{\frac{q_j-q_{j-1}}{a_j}\ge
\frac{q_{j+1}-q_j}{a_{j+1}}
\quad(1\le j<n),\qquad q_0=q_n=0.}
\]
The exact constant and a maximizing witness block can be computed with \(O(n)\) arithmetic operations by constructing the upper concave hull of the \(n+1\) mass-coordinate nodes.

## Assumptions and scope

All data are scalar and real, the order is the finite total order on the coordinates, and both the observation masses and interior edge weights are **strictly positive**. The fit is the unique weighted Euclidean projection onto the nondecreasing cone; it is not projection under the edge-variation seminorm. The same edge weights are used to measure the input difference and the output difference. The seminorm vanishes exactly on constant vectors. Since \(P_a(y+c\mathbf 1)=P_a(y)+c\mathbf 1\), constant input differences cause constant output differences and therefore pose no ambiguity for the Lipschitz bound.

The piecewise-linear function \(H\) is the smallest concave function lying above the finitely specified heights \(Q_j\). Its value at any mass node is the largest linear interpolation through two of the source heights that surround that node. This includes an endpoint equal to the node itself, giving a value at least \(Q_j\).

## Proof

**1. Weighted block-averaging pieces.** The pool-adjacent-violators description of weighted isotonic regression partitions the coordinates into consecutive blocks. On the interior of a region where the fitted blocks are fixed and their levels strictly increasing, the map is the linear operator \(B_\mathcal P\) which replaces every coordinate in a block \(I\) by the mass-weighted average
\[
(B_\mathcal P h)_i=
\frac{\sum_{r\in I}a_rh_r}{\sum_{r\in I}a_r},\qquad i\in I.
\]
There are finitely many consecutive block partitions. The isotonic projection is continuous and piecewise linear, with these operators as its full-dimensional linear pieces. Therefore its global Lipschitz modulus in \(V_q\) is at most the largest \(V_q\)-operator seminorm of the \(B_\mathcal P\); this follows by subdividing a generic line segment into finitely many linearity regions and then using continuity for nongeneric segments. Every such block-averaging operator fixes constant vectors.

**2. Step vectors are an exact test family.** For \(1\le j<n\) let \(h^{(j)}\) equal zero at coordinates up to \(j\) and one at all later coordinates. Every \(h\in\mathbb R^n\) has the exact decomposition
\[
h=h_1\mathbf1+\sum_{j=1}^{n-1}(h_{j+1}-h_j)h^{(j)}.
\]
Thus the triangle inequality and \(B_\mathcal P\mathbf1=\mathbf1\) imply
\[
\|B_\mathcal P\|_{V_q\to V_q}
=\max_{1\le j<n}\frac{V_q(B_\mathcal P h^{(j)})}{q_j}.
\]
The lower bound is obtained by using the individual step vectors, so no approximation or infinite-dimensional argument is involved.

**3. Exactly two boundary contributions.** If the cut after coordinate \(j\) lies between two averaging blocks, then \(B_\mathcal P h^{(j)}=h^{(j)}\), giving quotient one. Otherwise the cut lies strictly inside one block of coordinates \(L+1,\ldots,R\), for some \(0\le L<j<R\le n\). All earlier blocks have output zero, all later blocks output one, and the crossing block takes the weighted mean
\[
\theta=\frac{A_R-A_j}{A_R-A_L}.
\]
The only output jumps occur at the left and right ends of this block (when they exist). Consequently
\[
V_q(B_\mathcal P h^{(j)})
=\frac{Q_L(A_R-A_j)+Q_R(A_j-A_L)}{A_R-A_L}.
\]
The conventions \(Q_0=Q_n=0\) remove nonexistent boundary edges. Maximizing these exact expressions over blocks and step locations yields the displayed finite-chord formula.

**4. Concave-envelope identification.** On increasing abscissae \(A_0<\cdots<A_n\), the value of the least concave majorant at a node is the maximum of the affine interpolants through two surrounding nodes. Indeed, points in the convex hull of the downward rays below the given heights have largest possible height on the upper polygonal boundary; a boundary point at a fixed abscissa is a convex combination of two adjacent vertices of that upper hull. Conversely, each such chord lies at or below the upper hull at the chosen abscissa by concavity and the hull's domination of both endpoint heights. The chord expression in Step 3 is therefore \(H(A_j)\). This proves the upper bound and identifies the candidate sharp constant.

**5. Every maximizing chord can be attained.** Fix \(L<j<R\). Choose input data strictly decreasing on the block \(L+1,\ldots,R\), with successive drops of one, and choose all coordinates outside that block strictly increasing and separated from its mean by sufficiently large gaps. Weighted pool-adjacent-violators regression then has exactly that fused block, with singleton blocks elsewhere. Its fitted block inequalities hold strictly, so the same block partition persists under a sufficiently small perturbation. Perturb the input by \(\varepsilon h^{(j)}\) with \(\varepsilon>0\) sufficiently small. The difference between the two fitted outputs is exactly \(\varepsilon B_\mathcal P h^{(j)}\), and the ratio of output to input variation is the selected chord ratio. The executable rational witness construction in `CHECK.py` implements these data explicitly. If the maximum is one, start instead from strictly increasing data, where the projection is locally the identity; a small step perturbation gives quotient one. This proves attainment for all positive parameters and completes the sharp formula.

**6. Concavity criterion and algorithm.** The sharp factor equals one precisely when each \(H(A_j)=Q_j\), namely when the polygonal interpolation of the \(Q_j\) against the cumulative masses is concave. Since consecutive abscissa increments are \(a_j\), this is equivalent to the stated adjacent-slope inequalities. Constructing the upper hull by a stack which deletes a middle vertex whenever the successive chord slopes increase takes linear time: every vertex enters once and leaves at most once. A single forward sweep evaluates \(H(A_j)/q_j\) at every interior node and returns a maximizing pair of hull vertices and a cut. Thus the exact modulus and an attaining perturbation pattern require only \(O(n)\) arithmetic operations.

## Verification

The standalone Python standard-library script `CHECK.py` uses exact rational arithmetic. It independently compares the concave-hull formula with every contiguous block-partition operator for many finite rational parameter profiles, tests inequalities on pairs of rational signals using a weighted PAV implementation, and checks explicitly attained chord ratios. Its completed execution reported 45,900 enumerated block-partition norms, 17,245 valid two-data inequalities, 571 attaining-pair checks, and 720 comparisons of the linear-time hull calculation with the direct chord formula. It also checked a mass-dependent concave example and a family exhibiting unbounded amplification as one edge weight decreases. These finite computations supplement, and do not replace, the all-dimensional mathematical proof above.

For example, with three equal observation masses and variation weights \((1,\varepsilon)\), the formula gives
\[
K=\max\left\{1,\frac{1}{2\varepsilon}\right\},
\]
so the amplification is unbounded as \(\varepsilon\downarrow0\). By contrast, for **any** positive observation masses, constant positive interior variation weights give \(K=1\). More generally, weights proportional to \(q_j=A_j(A_n-A_j)\) satisfy strict cumulative-mass concavity and hence also give \(K=1\).

## Relationship to prior work

Weighted PAV and the weighted-average structure of fitted blocks are classical; in particular, Yeganova and Wilbur describe them explicitly in their 2009 article. Guyader, Jégou, A. Németh and S. Németh study order-cone projection geometry and iterative regression in a bounded-variation setting, but do not give the present weighted two-input variation modulus. Yang and Barber later prove that **unweighted** isotonic projection is contractive with respect to a seminorm if and only if that seminorm is nonincreasing under equal neighbor averaging. Their theorem is stronger than the simple unweighted *qualitative* contraction question; the contraction-versus-expansion distinction is not claimed here as new in that generality. It does not furnish the exact factor when nonexpansivity fails, nor a mass-dependent concave-envelope formula for arbitrary positive observation masses. The contribution assessed here is the complete sharp quantitative modulus, attainability, and cumulative-mass hull computation. A possible implicit equivalent in other classical projection or shape-constrained estimation literature remains a residual originality risk.

## Limitations

The statement applies to finite totally ordered real vectors, strictly positive quadratic observation masses and variation weights, and the unregularized isotonic projection. It does not assert the same formula for partial orders, nonlinear or nonquadratic losses, multivariate targets, or a continuum isotonic projection. The literature search does not establish absolute uniqueness of the mathematical statement. The self-review does not constitute independent validation.

## References

1. L. Yeganova and W. J. Wilbur, *Isotonic Regression under Lipschitz Constraint*, Journal of Optimization Theory and Applications 141 (2009), 429–443, doi:10.1007/s10957-008-9477-0. Publicly dated 2009-01-07; open article at https://pmc.ncbi.nlm.nih.gov/articles/PMC5815842/.
2. A. Guyader, N. Jégou, A. B. Németh and S. Z. Németh, *A Geometrical Approach to Iterative Isotone Regression*, arXiv:1211.3930, first submitted 2012-11-16, https://arxiv.org/abs/1211.3930.
3. F. Yang and R. Foygel Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852, first submitted 2017-06-06, https://arxiv.org/abs/1706.01852.
