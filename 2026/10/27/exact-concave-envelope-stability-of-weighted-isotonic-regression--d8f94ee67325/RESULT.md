# Exact concave-envelope stability of weighted isotonic regression in path variation

## Finding

Fix an integer \(n\ge 2\), positive observation masses \(a_1,\ldots,a_n\), and positive edge-variation weights \(q_1,\ldots,q_{n-1}\). Let \(P_a\) be weighted least-squares isotonic regression, defined for every \(y\in\mathbb R^n\) by
\[
P_a(y)=\operatorname*{argmin}_{z_1\le\cdots\le z_n}\sum_{i=1}^{n}a_i(z_i-y_i)^2.
\]
Define \(V_q(y)=\sum_{j=1}^{n-1}q_j|y_{j+1}-y_j|\). Set \(A_0=0\), \(A_j=\sum_{i=1}^j a_i\), \(Q_0=Q_n=0\), and \(Q_j=q_j\) at the interior indices. Let \(H\) be the least concave majorant of the points \((A_j,Q_j)\) on \([0,A_n]\), with linear interpolation between its consecutive vertices. Then the exact global two-data variation Lipschitz constant is
\[
\boxed{\sup_{V_q(x-y)>0}\frac{V_q(P_a(x)-P_a(y))}{V_q(x-y)}=K(a,q):=\max_{1\le j<n}\frac{H(A_j)}{q_j}.}
\]
The supremum is attained by a pair of finite real vectors for every choice of positive masses and weights. Equivalently,
\[
K(a,q)=\max\!\left\{1,\max_{0\le L<j<R\le n}
\frac{Q_L(A_R-A_j)+Q_R(A_j-A_L)}{q_j(A_R-A_L)}\right\}.
\]
In particular, the map is nonexpansive for the variation of differences exactly when
\[
\frac{q_j-q_{j-1}}{a_j}\ge\frac{q_{j+1}-q_j}{a_{j+1}}\quad(1\le j<n),\qquad q_0=q_n=0.
\]
The factor and a maximizing cut and block (or an identity-region witness) can be computed in \(O(n)\) arithmetic operations.

## Assumptions and scope

The data are scalar and real, the order is a finite total order, and both observation masses and interior edge weights are strictly positive. The fit is the unique weighted Euclidean projection onto the nondecreasing cone, not a projection under variation. The same weights measure input and output differences. The seminorm vanishes exactly on constants, and \(P_a(y+c\mathbf 1)=P_a(y)+c\mathbf 1\), so constant differences also obey the bound.

## Proof

**Block averages.** Weighted isotonic regression is continuous and piecewise linear. Its pieces replace data on each block of a consecutive partition by the block's mass-weighted mean. This follows from the weighted pool-adjacent-violators characterization or the projection optimality conditions. For a fixed consecutive partition \(\mathcal P\), denote the averaging map by \(B_{\mathcal P}\). Since the projection is continuous, subdividing a segment into finitely many linear pieces (and taking a limit at segments on cell boundaries) gives a global Lipschitz bound by the maximum of their operator seminorms in \(V_q\).

**Test steps.** Let \(h^{(j)}\) be zero up to index \(j\) and one thereafter. Since \(B_{\mathcal P}\) fixes constants, the identity
\[
h=h_1\mathbf 1+\sum_{j=1}^{n-1}(h_{j+1}-h_j)h^{(j)}
\]
and the triangle inequality give
\[
\|B_{\mathcal P}\|_{V_q\to V_q}=\max_{1\le j<n}\frac{V_q(B_{\mathcal P}h^{(j)})}{q_j},
\]
with the reverse bound obtained by testing a maximizing step. If the cut is between blocks, the step is unchanged. If it lies strictly inside the block \(L+1,\ldots,R\), the average there is \(\theta=(A_R-A_j)/(A_R-A_L)\), preceded by zeros and followed by ones. The output variation is \(Q_L\theta+Q_R(1-\theta)\), with the conventions \(Q_0=Q_n=0\) accounting for missing boundary edges.

**Upper hull.** Any chord through two data nodes spanning \(A_j\) is bounded above there by \(H(A_j)\), by concavity. Conversely the upper boundary of the convex hull of the nodes at that abscissa lies on an edge or at a vertex. Its height is therefore either a surrounding chord height or \(Q_j\). This upper boundary is concave, lies above all nodes, and is no greater than any other concave majorant since the latter dominates its chords. This proves the equivalence of the two formulas and the global upper bound.

**Attainment.** Given a cut inside \(L+1,\ldots,R\), choose strictly decreasing data on that block and strictly increasing singleton data outside, with all singleton levels on the left below the block mean and all those on the right above it. Every proper prefix of the block has weighted mean strictly above the block mean. The cumulative residuals \(\sum_{i\le k}a_i(y_i-z_i)\) for the proposed fit \(z\) are therefore strictly positive at internal cuts of the block and zero at all block boundaries. This is the isotonic projection criterion (the residuals are nonnegative and vanish at strict fitted jumps, with total residual zero). The strict inequalities within the block and between its fitted level and neighboring singleton levels persist after a sufficiently small perturbation \(\eta h^{(j)}\), \(\eta>0\). The difference of fits is exactly \(\eta B_{\mathcal P}h^{(j)}\), giving the chosen chord ratio. If the factor is one, choose strictly increasing data and perturb by a small step; both vectors fit themselves. Thus the factor is attained.

**Concavity and computation.** Since \(H(A_j)\ge q_j\), the factor is one exactly when all the heights lie on the least concave majorant. The slopes at successive mass nodes are \((Q_j-Q_{j-1})/a_j\), yielding the criterion. Build the upper hull by pushing nodes in order and deleting the middle of the last three whenever their chord slopes increase. Each node is pushed once and popped at most once. Sweeping the hull against the mass nodes then computes the largest ratio and a maximizing chord when the ratio exceeds one.

## Verification and examples

The accompanying standard-library `CHECK.py` tests the chord and hull formulas, block-averaging partitions, pairs of weighted isotonic fits, and attained ratios using rational arithmetic. The recorded finite run reported 45,900 block-partition norms, 17,245 two-data inequalities, 571 attaining pairs, and 720 chord/hull comparisons. Run with `python3 CHECK.py` to replay those finite tests. The proof, not the tests, gives the stated result for all positive real masses and weights.

With three equal observation masses and variation weights \((1,\varepsilon)\), \(\varepsilon>0\), the two potentially amplifying chords have ratios \(1/(2\varepsilon)\) at the second cut and \(\varepsilon/2\) at the first cut. Thus
\[
K=\max\left\{1,\frac{1}{2\varepsilon},\frac{\varepsilon}{2}\right\},
\]
and the amplification is unbounded as \(\varepsilon\downarrow0\). For any positive masses, constant positive interior weights instead give \(K=1\). Weights proportional to \(A_j(A_n-A_j)\) give another nonexpansive example by strict concavity.

## Relationship to prior work and limitations

The weighted pool-adjacent-violators block structure is classical; see Yeganova and Wilbur. Guyader et al. study isotone projection and regression in a bounded-variation setting. Yang and Barber give a general seminorm characterization of qualitative contractivity for the unweighted isotonic projection by equal-neighbor averaging. For \(V_q\) this already implies the equal-mass discrete concavity criterion. It does not give the sharp factor when there is expansion or the cumulative-mass formula for arbitrary masses. The quantitative factor is useful in that regime: it gives a computable worst-case amplification, with actual perturbations attaining it. The result here assumes a finite path, scalar quadratic-loss data, and strictly positive masses and edge weights; no claim is made for other orders, losses, or a continuum operator.

## References

1. L. Yeganova and W. J. Wilbur, *Isotonic Regression under Lipschitz Constraint*, J. Optim. Theory Appl. **141** (2009), 429–443, DOI: 10.1007/s10957-008-9477-0.
2. A. Guyader, N. Jégou, A. B. Németh and S. Z. Németh, *A Geometrical Approach to Iterative Isotone Regression*, https://arxiv.org/abs/1211.3930.
3. F. Yang and R. Foygel Barber, *Contraction and uniform convergence of isotonic regression*, https://arxiv.org/abs/1706.01852.
