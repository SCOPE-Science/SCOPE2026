# Strict Schur ordering of triangular affine sections of rectangular boxes

## Finding

For a Euclidean rectangular box with positive half-side lengths \(a,b,c\), let \(P_3(a,b,c)\) be the probability that an affine plane drawn from motion-invariant plane measure conditional on hitting the box has a triangular section. At fixed \(a+b+c\), this probability is **strictly Schur-concave**: if \((a,b,c)\) majorizes \((a',b',c')\) and they are not permutations of one another, then \(P_3(a,b,c)<P_3(a',b',c')\).

Equivalently, any transfer between two unequal half-lengths that strictly reduces their gap, leaving their sum and the other half-length unchanged, strictly increases the triangular-section probability. This orders many pairs of unequal boxes, not just their comparison to the cube. The cube is the unique maximizer up to scale, by this ordering.

## Sampling and scope

Represent an unoriented plane by \((u,t)\in S^2\times\mathbb R\) modulo \((u,t)\sim(-u,-t)\); its equation is \(u\cdot x=t\). Use the measure induced by \(d\sigma(u)\,dt\), restricted and normalized to planes meeting the box. In particular the direction of a sampled hitting plane is weighted by the box width, not uniform. The claim compares positive half-side lengths at fixed sum, equivalently after normalizing their sum. It is not a comparison at fixed volume or under a different plane sampling rule.

## Proof

Use the triangular atom of the rectangular-box Crofton law [1], writing \(U\) for a uniform unit vector:
\[
P_3(a,b,c)=\frac{4}{a+b+c}F(a,b,c),\qquad F(a,b,c)=\mathbb E\min\{a|U_1|,b|U_2|,c|U_3|\}.
\]
For completeness, to recover the normalization, fix a normal with no zero coordinate and put \(s_u=a|u_1|+b|u_2|+c|u_3|\) and \(m_u=\min\{a|u_1|,b|u_2|,c|u_3|\}\). The first two vertex levels from the upper end are \(s_u\) and \(s_u-2m_u\). A generic triangular section crosses three graph edges, which requires a singleton on one side: in the cubic graph, a cut with smaller side of size \(k\le 4\) has size \(3k-2e\), where \(e\) is the internal edge count. This can be three only for odd \(k\), and \(k=3\) would require three edges among three vertices in the bipartite cube graph. Thus the triangular offsets have total length \(4m_u\) at the two ends; all hitting offsets have length \(2s_u\). Integrating and using \(\mathbb E|U_i|=1/2\) gives the displayed law. Offsets through vertices can be discarded as null.

For each direction the minimum in \(F\) is a concave function of the half-lengths, and the direction law makes \(F\) symmetric under permutations. Fix \(a>b>0\) and \(c>0\), and compare \(v=(a,b,c)\) with its swap \(v'=(b,a,c)\). Take a direction with \(|u_1|=|u_2|=d>0\), for sufficiently small \(d\) that \(c|u_3|>ad\). At \(v\) the unique minimizing branch is the second coordinate, and at \(v'\) it is the first. Both inequalities persist on a nonempty open set of directions, of positive spherical measure. For any \(0<\eta<1\), every linear branch evaluated at \((1-\eta)v+\eta v'\) strictly exceeds the corresponding convex combination of the endpoint minima on that open set: each branch fails to minimize at at least one endpoint. There are only three branches, so their minimum also strictly exceeds that combination. Elsewhere concavity gives the weak inequality. Integration and permutation symmetry give
\[
F((1-\eta)v+\eta v')>(1-\eta)F(v)+\eta F(v')=F(v).
\]
The new absolute gap is \(|1-2\eta|(a-b)\), so this covers every strictly gap-reducing transfer. The prefactor of \(F\) in \(P_3\) stays constant. By the finite pair-transfer characterization of majorization, together with permutation invariance, a majorization comparison not between permutations requires at least one such strict transfer and yields the claimed strict inequality. The balanced triple is majorized by every triple of its sum, giving the uniqueness statement.

## Verification

The direction and transfer proof establishes the strict inequality for every positive half-length vector. The accompanying `triangular_box_checker.py` is a finite deterministic numerical check of integral values at the cube and selected asymmetric boxes, as well as consistency with the cube's quadratic expansion; it is not an exhaustive test or a proof of the strict ordering.

## Relationship to prior work and limitations

Record [1] gives an elementary all-aspect-ratio formula for the full distribution of affine section types, including the same triangular probability above. It also treats the cube extremizer and stability as existing background; the cube coefficient can be obtained by Taylor expansion of its explicit triangular formula. The distinct statement here is the global strict comparison for **every** nontrivial fixed-sum majorization, which is stronger than a maximum at the cube or a local deficit near the cube. No priority for the probability formula, cube value, or local expansion is claimed. Bray [2] is cited in [1] for the cube's section-type table. These comparisons do not assert comprehensive historical priority for the strict ordering. The proof concerns rectangular boxes, not sheared parallelepipeds, central sections, or other orientation or offset laws.

## References

1. *Elementary Crofton section-type law and quadratic hexagon extinction for rectangular boxes*, Resultary catalogue record ecdb5fa9f8fa, `RESULT.md`, Finding, Assumptions and scope, and Relationship to prior work. https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-elementary-crofton-section-type-law-and-quadratic-hexagon-extinc--ecdb5fa9f8fa/RESULT.md
2. B. M. Bray, *Invariant measures on multifids of convex polytopes*, University of Wollongong, Ph.D. thesis (2009), Chapter 10. https://ro.uow.edu.au/theses/3403
