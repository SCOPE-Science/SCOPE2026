# Exact variance of acute Euclidean chord triangles on a sphere

## Finding

Choose \(n\ge 3\) independent points \(X_1,\ldots,X_n\) uniformly with respect to normalized surface area on the unit sphere \(S^2\subset\mathbb R^3\). For each unordered triple \(I\) let \(J_I\) indicate that its **Euclidean chord triangle** is strictly acute, meaning that all three ordinary planar Euclidean interior angles are less than \(\pi/2\). Set \(T_n=\sum_{|I|=3}J_I\), the number of acute triangles among **all** \(\binom n3\) triples.

For every such integer \(n\),
\[
\mathbb E[T_n]=\frac12\binom n3,\qquad
\operatorname{Var}(T_n)=\frac14\binom n3+\frac{\pi-3}{4}\binom n2\binom{n-2}{2}.
\]
More precisely, if distinct triples \(I,J\) share exactly two vertices, then
\[
\Pr(J_I=J_J=1)=\frac{\pi-1}{8},\qquad
\operatorname{Cov}(J_I,J_J)=\frac{\pi-3}{8}>0.
\]
If they share zero or one vertex, their indicators are independent. Thus the covariance structure is completely determined by their shared-vertex count. In particular, for a tetrahedron formed by four independent uniform points on \(S^2\), the number of acute triangular faces has mean \(2\) and variance \((3\pi-7)/2\). For growing \(n\), the variance of the unrestricted triple count is \((\pi-3)n^4/16+O(n^3)\), not the order \(n^3\) predicted by treating the triangle indicators as independent.

## Assumptions and scope

The sampling law is the **normalized area measure on the two-dimensional unit sphere**, independently for each labeled point. The triangles are ordinary flat triangles whose edges are Euclidean line segments; they are *not* intrinsic geodesic triangles on the sphere. Right-angled and degenerate triangles occur with probability zero. When \(n>4\), \(T_n\) counts every three-point subset; it is **not** the count of acute facets of the sample's convex hull.

## Proof

**Conditional acute-region lemma.** Fix two distinct, non-antipodal unit vectors \(A,B\) with central separation \(\theta\in(0,\pi)\). Put \(s=\sin(\theta/2)\), \(c=\cos(\theta/2)\), and define perpendicular unit vectors
\[
u=\frac{B-A}{2s},\qquad v=\frac{A+B}{2c}.
\]
Then \(A=cv-su\) and \(B=cv+su\). For a third independent area-uniform point \(C\) on the sphere, the ordinary angle inequalities at \(A\), \(B\), and \(C\) respectively reduce, by taking the dot products of their incident chords, to
\[
 u\cdot C>-s,\qquad u\cdot C<s,\qquad v\cdot C<c.
\]
The two inequalities involving \(u\) specify a spherical belt with probability \(s\), since a uniform unit vector's projection onto a fixed axis is uniform on \([-1,1]\). The excluded region \(v\cdot C\ge c\) is a spherical cap of probability \((1-c)/2\). This cap lies *entirely inside the belt*: because \(u\perp v\) and \(C\) is a unit vector, \(v\cdot C\ge c\) implies \(|u\cdot C|\le\sqrt{1-c^2}=s\). Therefore the exact conditional acute probability is
\[
q(\theta)=\Pr(ABC\text{ acute}\mid A,B)
=s-\frac{1-c}{2}.
\]
The exceptional coincident or antipodal pairs have probability zero and do not affect the integrals.

**First two moments of the conditional probability.** For independent uniform \(A,B\), the variable \(t=A\cdot B=\cos\theta\) is uniform on \([-1,1]\), and \(s=\sqrt{(1-t)/2}\), \(c=\sqrt{(1+t)/2}\). Direct one-dimensional integration gives
\[
 \mathbb E[s]=\mathbb E[c]=\frac23,\quad
 \mathbb E[s^2]=\mathbb E[c^2]=\frac12,\quad
 \mathbb E[sc]=\frac14\int_{-1}^1\sqrt{1-t^2}\,dt=\frac\pi8.
\]
Consequently,
\[
 \mathbb E[q]=\frac12,\qquad
 \mathbb E[q^2]=\mathbb E\left[s^2+\frac{(1-c)^2}{4}-s(1-c)\right]=\frac{\pi-1}{8}.
\]
The first equality recovers the known single-triangle acuteness probability.

**Joint law and counting.** If two triangles share exactly the vertices \(A,B\), their respective third points are conditionally independent given \(A,B\). Their joint acuteness probability is therefore \(\mathbb E[q(\theta)^2]=(\pi-1)/8\), while each has marginal probability \(1/2\). Their covariance is \((\pi-3)/8\).

Triangles with disjoint index sets are independent. If they share just one vertex, condition on that common point. The two remaining pairs of points are conditionally independent. By rotation invariance the conditional acuteness probability of either triangle is \(1/2\) for every position of the common vertex, so unconditional independence follows.

There are \(\binom n3\) individual indicators, each of variance \(1/4\), and there are exactly \(\binom n2\binom{n-2}{2}\) *unordered* pairs of distinct three-point subsets sharing a pair of vertices: choose their common pair, then choose their two different remaining vertices. Expanding \(\operatorname{Var}(\sum J_I)\) and counting the two orders in each nonzero off-diagonal covariance yields
\[
\operatorname{Var}(T_n)
=\frac14\binom n3
 +2\binom n2\binom{n-2}{2}\frac{\pi-3}{8},
\]
which is the claimed formula. Substitution at \(n=4\) gives the tetrahedral variance, and expanding the binomial factors gives the stated fourth-order growth.

## Verification

The included `verify.py` is a stand-alone Python 3 standard-library program. Run it with `python3 verify.py`. It checks the exact rational coefficients of the moments of \(q\) (with \(\pi\) treated symbolically), exhaustively checks pair-overlap multiplicities for \(3\le n\le9\), independently numerically integrates the conditional probability, and compares direct random-sphere simulations of \(T_n\) for \(n=4,5,6\) against the exact means and variances. The original verification run ended with `ALL_CHECKS_PASSED` and simulated variances approximately \(1.217172,3.567963,8.207998\) versus exact \(1.212389,3.561945,8.185835\).

The mathematical proof above, not the finite simulations or numerical quadrature, establishes the identities for all \(n\). The checker independently tests important arithmetic and implementation details but is not an independent proof or mathematical audit.

## Relationship to prior work

Akopyan, Edelsbrunner, and Nikitenko prove the single-triangle probability \(\Pr(ABC\text{ acute})=1/2\) for area-uniform sphere samples (Lemma 4 of arXiv:2007.07783, publicly available July 15, 2020). Their Theorem 6 also proves a related marginal law for a uniformly selected convex-hull facet. These marginal results are explicitly credited; neither specifies the **shared-pair joint probability** or the variance of the complete triple count considered here.

The subsequently posed question about the event that **all four tetrahedral faces** are acute (MathOverflow question 498296, July 26, 2025, with later responses) concerns a different four-way event. Its exact all-face probability does not by itself determine the second moment of the number of acute faces, and the inspected discussion does not provide the formula above. General results on geometric U-statistics explain why pairwise overlap decompositions are useful, but the conditional belt-minus-cap integral evaluates the specific covariance coefficient here.

## Limitations

The result uses independent normalized-area-uniform surface samples in three Euclidean dimensions. It does not provide the full distribution of \(T_n\), the acuteness variance of the *facets* of a convex hull for \(n>4\), nonuniform sampling laws, or analogous formulas in arbitrary dimensions. Search and literature comparisons support a provisional originality assessment, not definitive historical priority. Independent mathematical review has not been performed.

## References

1. Arseniy Akopyan, Herbert Edelsbrunner, Anton Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere*, arXiv:2007.07783 (v1 posted July 15, 2020), especially Lemma 4 and Theorem 6. https://arxiv.org/abs/2007.07783
2. *A tetrahedron's vertices are random points on a sphere. What is the probability that the tetrahedron's four faces are all acute triangles?*, MathOverflow question 498296, asked July 26, 2025, later answers and discussion. https://mathoverflow.net/questions/498296/
