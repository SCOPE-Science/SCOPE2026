# A sharp five-coordinate failure of angular pivot-rank Schur monotonicity for central prism sections

## Finding

The central slice of a rectangular box has a Gaussian normal-cone distribution whose rank statistics need not become more concentrated when the box's side lengths are balanced. This failure first occurs for five coordinates, or intrinsic dimension four. All possible five-coordinate rank distributions admit an exact six-class classification.

More precisely, fix an integer \(n\ge2\) and a positive real capacity vector \(c=(c_1,\ldots,c_n)\). Put \(C=\sum_i c_i\) and assume the **nonresonance condition**
\[
\sum_{i\in S}c_i\ne C/2\qquad\text{for every }S\subseteq\{1,\ldots,n\}.
\]
Define the central prism section in its intrinsic Euclidean metric by
\[
P(c)=\{x\in\mathbb R^n:0\le x_i\le c_i,\ \sum_i x_i=C/2\}.
\]
Choose a unit vector uniformly from its \((n-1)\)-dimensional normal sphere, maximize the associated linear functional over \(P(c)\), and let \(T_c\) be one plus the number of coordinates at their upper bound at the maximizing vertex. The maximizer is almost surely unique and exactly one coordinate is strictly between zero and its upper bound.

For every \(0\le r\le n\), the exact Gaussian angular-tail identity is
\[
\Pr(T_c>r)=\frac{\#\{S\subseteq[n]:|S|=r,\ \sum_{i\in S}c_i<C/2\}}{\binom nr}.
\tag{1}
\]
In particular \(T_c\) has the same distribution as \(n+1-T_c\). For a vertex indexed by its upper-bound coordinate set \(H\) and its unique fractional coordinate \(j\), its Gaussian normal-cone angle is precisely
\[
\alpha(H,j)=\frac{|H|!\,(n-|H|-1)!}{n!}.
\tag{2}
\]

**Sharp majorization boundary.** Whenever \(n\le4\), two nonresonant positive capacity vectors of equal total satisfying \(c\succeq d\) (ordinary vector majorization) obey
\[
T_c\succeq_{\mathrm{cx}}T_d,
\]
meaning \(\mathbb E\phi(T_c)\ge\mathbb E\phi(T_d)\) for every convex real function \(\phi\). This statement fails at \(n=5\) in the **opposite** strict direction for the concrete balanced transfer
\[
c=(6,6,2,2,2),\qquad d=(6,4,4,2,2).
\]
Both have total \(18\), central level \(9\), satisfy nonresonance, and \(c\succeq d\). Yet, in rank order \(1,\ldots,5\),
\[
\Pr(T_c=\cdot)=(0,1/10,4/5,1/10,0),\qquad
\Pr(T_d=\cdot)=(0,1/5,3/5,1/5,0),
\]
so \(T_d\succeq_{\mathrm{cx}}T_c\), with strict inequality for any convex \(\phi\) having \(\phi(2)+\phi(4)>2\phi(3)\). In particular,
\[
\operatorname{Var}(T_c)=1/5,\qquad \operatorname{Var}(T_d)=2/5.
\]

**Complete five-coordinate classification.** If no capacity exceeds \(C/2\), let \(h\) count the two-element subsets whose capacities sum to more than \(C/2\). Necessarily \(h\in\{0,1,2,3,4\}\), and the entire law is
\[
\Pr(T_c=2)=\Pr(T_c=4)=h/10,\qquad
\Pr(T_c=3)=1-h/5,
\tag{3}
\]
with zero mass elsewhere. All five values occur for generic strictly positive capacities. If a capacity exceeds \(C/2\), necessarily uniquely, \(T_c\) is uniform on \(\{1,2,3,4,5\}\). Thus there are exactly **six** possible rank laws. For example, the respective realizations of \(h=0,1,2,3,4\) are
\[
(2,2,2,2,2),\ (2,2,2,6,6),\ (2,2,4,4,6),\
(2,2,6,6,6),\ (2,2,2,2,6),
\]
and \((2,2,2,2,10)\) realizes the sixth, uniform law.

## Assumptions and scope

The ambient dimension is \(n\ge2\), all capacities are strictly positive, the slice is precisely at half the total capacity, and **every** subset sum differs from that half. This last genericity condition rules out slice vertices with no fractional coordinate and makes rank unambiguous. The assertion concerns the solid-angle distribution on intrinsic Euclidean **normal cones**, not vertex counts, volumes, an arbitrary non-isotropic objective distribution, or the identities of individual pivotal coordinates. The main classification is for \(n=5\); majorization monotonicity and its sharp failure are statements about all admissible capacities for each indicated dimension.

For equal-length vectors, \(c\succeq d\) means the decreasing rearrangements have equal total and all leading partial sums of \(c\) dominate those of \(d\). Convex order has its usual expectation characterization; its use here is legitimate because the two rank distributions have the common mean \((n+1)/2\).

## Proof

**1. Geometry and angular reduction.** Because the level \(C/2\) is strictly between zero and \(C\), the section has intrinsic dimension \(n-1\). At any vertex, at least \(n-1\) independent box constraints are active. The nonresonance assumption precludes all \(n\) coordinates being at endpoints, so exactly one index \(j\) has \(0<x_j<c_j\), while the others partition into an upper-bound set \(H\) and a zero set \(L\). Conversely, whenever \(\sum_{i\in H}c_i<C/2<\sum_{i\in H}c_i+c_j\), these prescriptions determine a vertex.

For any linear functional with pairwise distinct coordinate coefficients, the elementary exchange argument proves that the optimum is obtained by sorting coefficients from largest to smallest, filling each coordinate to capacity before proceeding, and using the unique remaining fractional coordinate at the first threshold crossing. Indeed, if a lower-coefficient coordinate is positive while a higher-coefficient coordinate remains below capacity, shifting a small feasible amount from the former to the latter strictly increases the objective. This also proves optimality and uniqueness of the sorted greedy vertex.

The orthogonal projection of an isotropic Gaussian in \(\mathbb R^n\) onto \(\mathbf 1^\perp\) is an isotropic Gaussian in the section's tangent space. Subtracting the same number from every coefficient changes no ordering or objective comparison on the constant-sum section. Consequently all \(n!\) strict total orders have equal Gaussian probability. Each vertex \((H,j,L)\) arises from exactly the orders listing the indices of \(H\), then \(j\), then those of \(L\), allowing arbitrary internal permutations within \(H\) and \(L\). This proves (2). The event \(T_c>r\) is exactly that the first \(r\) indices have cumulative capacity less than \(C/2\). The first \(r\) indices form a uniform \(r\)-subset; (1) follows. Reversal of the order exchanges a crossing index \(t\) with \(n+1-t\), since no subset sum equals \(C/2\), proving symmetry.

**2. Low-dimensional convex-order rigidity.** Call a capacity **dominant** when it exceeds \(C/2\); at most one such capacity exists. If there is one, its position in the random ordering is necessarily the threshold-crossing position, giving the discrete uniform distribution on \(\{1,\ldots,n\}\). Otherwise, crossing cannot happen at position one or at position \(n\). For \(n=3\) this forces \(T_c=2\); for \(n=4\) it forces \(T_c\in\{2,3\}\), with probability \(1/2\) each by order reversal. For \(n=2\), genericity always creates a dominant capacity, and \(T_c\) is uniform on the two ranks. These exhaust all rank laws through \(n=4\).

If \(c\succeq d\), then \(\max_i c_i\ge\max_i d_i\). In particular, balancing cannot create a dominant capacity. Any possible transition among the displayed laws can therefore only replace a symmetric discrete uniform law by the more concentrated central law. For any convex \(\phi\), the uniform law dominates the corresponding central law by midpoint convexity: in dimension three \([\phi(1)+\phi(3)]/2\ge\phi(2)\); in dimension four \(\phi(1)+\phi(4)\ge\phi(2)+\phi(3)\). This proves convex-order monotonicity for every \(n\le4\).

**3. Five-coordinate classes.** Suppose \(n=5\) and there is no dominant capacity. Crossing occurs only at ranks two, three, or four. Formula (1) for \(r=2\) shows that \(\Pr(T_c=2)=h/\binom52=h/10\). Order reversal gives the same probability at rank four, and the remaining probability is the rank-three mass. Any two winning pairs intersect: otherwise their four positive capacities would already sum to more than the total \(C\). A pairwise-intersecting simple graph on five vertices has at most four edges. To see this, if all edges contain a common vertex it is a star with at most four edges. Otherwise, choosing edges \(12\), \(13\), and an edge avoiding vertex \(1\) forces that third edge to be \(23\); no further edge can intersect all three. Thus \(0\le h\le4\). The five listed capacity vectors have odd half-total while each subset sum is even, hence are nonresonant, and counting their winning pairs yields exactly \(h=0,1,2,3,4\). In the dominant case the uniform law gives a sixth distinct distribution, realized by the final vector. Hence the classification is complete.

**4. Sharp balancing reversal.** Both vectors in the stated pair are generic because all coordinates are even but the half-total is the odd integer \(9\). Sorting, their leading prefix sums are respectively \((6,12,14,16,18)\) and \((6,10,14,16,18)\), so \(c\succeq d\). Their winning pairs are respectively the single pair of two sixes and the two pairs consisting of a six and one of the fours, hence \(h(c)=1\) and \(h(d)=2\). Applying (3) gives both displayed probability vectors. Their expected ranks equal three, and
\[
\mathbb E\phi(T_d)-\mathbb E\phi(T_c)
=\frac{\phi(2)+\phi(4)-2\phi(3)}{10}\ge0
\]
for every convex \(\phi\), with strictness when its midpoint inequality is strict. The two variances are the corresponding probabilities of deviating by one from mean three. Combined with step 2, this proves the claimed minimal dimension.

## Verification

A standalone Python program `CHECK.py` uses only the standard library and exact rational arithmetic. It enumerates all random coefficient orderings, all generic capacity profiles from the stated finite test ranges, all vertices of sample prism sections, and the corresponding greedy objective values. Its checks confirm (1), distributional reversal, (2), the six explicit five-coordinate distributions, the majorization witness, the exact variances, and all-rank low-dimensional rigidity. It performs **520** generic profile verifications and **750** independent direct ordering-to-vertex maximization checks. The program's finite tests are not used as a proof of the universal claims, which are established in the preceding steps.

Run `python CHECK.py` in the extracted package directory. The program does not require network access or nonstandard packages.

## Relationship to prior work

Ferroni and McGinnis introduced and studied these box-section polytopes in their 2022 preprint, including their weighted-permutation and Ehrhart structures, and identified them as polymatroid base polytopes and polypositroids. Castillo and Liu explain general braid-fan and normal-fan coarsening; these results motivate the ordering-cone reduction, which is **not** itself presented as new. Shapley and Shubik introduced the classical pivotal-player construction for weighted majority games: the random crossing position here is precisely its pivotal *position*, although their power index concerns which player is pivotal. Those established correspondences are credited, not claimed as discoveries.

The present claim is confined to the exact Gaussian angular-rank classification at five capacities and the sharp convex-order majorization failure, rather than to the basic greedy algorithm or coalition pivot formula. Published related records concerning prism-slice inradii or stochastic counts of random central sections of boxes concern different geometric invariants. No statement determining this complete six-class angular-rank law **and** its first majorization reversal was identified in the checked primary literature and mathematical record. The literature search is not an exhaustive novelty certification.

## Limitations

The central-level and subset-sum genericity assumptions are essential to the formulation and are not removed here. The law concerns a coarse **rank of the exposed vertex**, not the complete joint distribution of all vertices or an optimality theorem about sampling orientations. All coordinate capacities can be real, but integer profiles suffice for sharp realizations. Complete statements for arbitrary higher dimensions, noncentral levels, and arbitrary elliptical objective distributions are not claimed. Independent mathematical review has not been conducted. There remains risk of an earlier equivalent result in weighted-majority pivotal-position theory or in the geometry of generalized permutohedra under different terminology.

## References

1. L. Ferroni and D. McGinnis, *Lattice points in slices of prisms*, arXiv:2202.11808, first posted 2022-02-23; *Canadian Journal of Mathematics* 77 (2025), 1013–1040. https://arxiv.org/abs/2202.11808
2. F. Castillo and F. Liu, *Deformation Cones of Nested Braid Fans*, arXiv:1710.01899, first posted 2017-10-05; *International Mathematics Research Notices* 2022, 1973–2026. https://arxiv.org/abs/1710.01899
3. L. S. Shapley and M. Shubik, *A Method for Evaluating the Distribution of Power in a Committee System*, *American Political Science Review* 48 (1954), 787–792. https://doi.org/10.2307/1951053
