# Vertex laws of boundary-sampled polygons: balancing and inverse side-length rigidity

## Finding
Let \(P\) be a nondegenerate planar convex polygon with \(m\ge3\) genuine sides, each of positive length \(\ell_i\); let \(L=\sum_i\ell_i\) be its perimeter and \(p_i=\ell_i/L\). Independently draw \(n\ge1\) boundary points under normalized arclength measure. Let \(V_n\) denote the number of distinct vertices of their convex hull; a singleton is counted as one vertex and a nondegenerate line segment as two.

The **exact finite-sample vertex-count law** is
\[
\mathbb E[z^{V_n}]=n!\,[t^n]\prod_{i=1}^{m}\left(1+p_i t z+z^2(e^{p_i t}-1-p_i t)\right).
\]
All coefficients are nonnegative and the probabilities sum to one. The expectation is
\[
\mathbb E V_n=\sum_{i=1}^{m}\left[2\bigl(1-(1-p_i)^n\bigr)-n p_i(1-p_i)^{n-1}\right].
\]
These quantities depend on the polygon only through its normalized side lengths, **not its angles or their cyclic order**.

For probability vectors \(p,q\in(0,1)^m\) of realizable polygon side lengths, say \(p\succeq q\) when \(p\) majorizes \(q\) (the decreasingly sorted partial sums of \(p\) dominate those of \(q\)). Then the entire laws satisfy
\[
 p\succeq q\quad\Longrightarrow\quad
 \mathbb P\{V_n(p)\ge k\}\le\mathbb P\{V_n(q)\ge k\}
 \qquad(n\ge1,\ k\in\mathbb Z).
\]
If \(n\ge3\) and the vectors differ beyond a permutation, their means are strictly ordered. Thus **every convex equilateral \(m\)-gon** is a stochastic maximizer. Regularity of the angles is not required, and no assertion of strictness at every threshold is made.

There is also an **inverse rigidity statement**. The entire sequence of expectations \(\bigl(\mathbb E V_n\bigr)_{n\ge1}\) uniquely determines \(m\) and the unordered multiset \(\{p_1,\ldots,p_m\}\). Therefore two convex polygons have the same vertex-count laws at every sample size if and only if their normalized side-length multisets coincide. They may nevertheless be noncongruent and have different angles.

## Assumptions and scope
The polygon is compact, full-dimensional, and convex, and the listed \(m\) sides are maximal straight boundary edges (consecutive collinear edges are merged). Vertices are distinct, side lengths are positive, and samples are independent and uniform with respect to arclength; polygon corners have sampling probability zero. All statements are exact for finite \(n\) and finite \(m\). In the comparison theorem the two polygons have the same number of sides, but arbitrary perimeter and angles. The majorization statement is asserted only for pairs of probability vectors arising from such polygons; its probabilistic proof applies to arbitrary positive probability vectors.

## Proof
**1. Supporting-edge reduction.** Let \(C_i\) count the sample points in the relative interior of the \(i\)-th edge. Because each side lies on a supporting line of \(P\), all sampled points on that side lie on the sampled hull's exposed supporting face. When \(C_i=1\), this face is a singleton and gives exactly one vertex; when \(C_i\ge2\), its two extreme sampled points give exactly two vertices, and its other sample points cannot be vertices. Almost surely the sampled points avoid original corners. No sampled point lies on two sides, so distinct side contributions cannot coincide. Thus
\[
 V_n=\sum_{i=1}^{m}\min(C_i,2),\qquad
 (C_1,\ldots,C_m)\sim\operatorname{Multinomial}(n;p_1,\ldots,p_m).
\]
This also handles degenerate sample hulls (one or two points, or all points on one side).

**2. Complete distribution.** For side \(i\), the exponential generating function for the number of samples allocated to it, with vertex weight \(z\), is \(1+p_i t z+z^2\sum_{j\ge2}(p_it)^j/j!\). The multinomial coefficient \(n!\) converts the product's \(t^n\) coefficient into its probability generating function. For each side, \(\mathbb E\min(C_i,2)=2\mathbb P(C_i\ge1)-\mathbb P(C_i=1)\), and \(C_i\sim\operatorname{Binomial}(n,p_i)\). This gives the expectation formula above.

**3. Full stochastic majorization.** It suffices, by the finite-dimensional characterization of majorization, to prove monotonicity under a single balancing of two components at fixed sum. Condition on the other side counts and on the total \(s\) falling on the selected pair. The split \(B\) is binomial with parameters \(s\) and \(u=p_i/(p_i+p_j)\). The only variable part of the vertex count is
\[
 W_s(B)=\min(B,2)+\min(s-B,2).
\]
It is symmetric and nondecreasing as \(B\) approaches the center \(s/2\). Thus each superlevel set is either empty, all of \(\{0,\dots,s\}\), or a central interval \(\{a,\dots,s-a\}\), with \(1\le a\le\lfloor s/2\rfloor\). For such an interval, differentiating its binomial probability gives
\[
 \frac{d}{du}\mathbb P_u\{a\le B\le s-a\}
 =s\binom{s-1}{a-1}u^{a-1}(1-u)^{a-1}
 \left[(1-u)^{s-2a+1}-u^{s-2a+1}\right].
\]
The derivative is positive for \(0<u<1/2\), zero at \(u=1/2\), and negative on the reflected interval. Bringing the two probabilities closer at fixed sum consequently raises every conditional and unconditional upper tail of \(V_n\). A sequence of such balancing operations gives the stated stochastic comparison. For \(n\ge3\), each expectation summand \(f_n(x)=2[1-(1-x)^n]-nx(1-x)^{n-1}\) obeys
\[
 f_n''(x)=-n(n-1)(n-2)x(1-x)^{n-3}<0\quad(0<x<1).
\]
Strict concavity gives strict inequality of means for any non-permutation majorization pair.

**4. Inverse reconstruction.** Since every \(p_i>0\), the mean increases to \(2m\) as \(n\to\infty\), recovering \(m\). Put \(q_i=1-p_i\in(0,1)\). The generating series of the expectation deficit is the rational function
\[
 D(t)=\sum_{n\ge1}(2m-\mathbb E V_n)t^n
 =\sum_{i=1}^{m}\left[\frac{2q_it}{1-q_it}+\frac{p_it}{(1-q_it)^2}\right].
\]
Every distinct \(q\) has a genuine pole of order two at \(t=1/q\): if this value occurs \(r\) times, the coefficient of \((1-qt)^{-2}\) is \(r(1-q)/q>0\). Other \(q\)-values are analytic there and cannot cancel it. Hence the poles recover all distinct \(q_i\), and their leading coefficients recover the multiplicities. This recovers the normalized side-length multiset. The forward formula proves the converse.

## Verification
The accompanying standalone program `checks/verify.py` computes exact multinomial vertex distributions by summing all composition counts, separately computes the coefficient formula, verifies the expectation identity, and checks pair-balancing stochastic inequalities in exact rational arithmetic for multiple three-, four-, and five-side profiles and sample sizes through ten. It also exhaustively tests central-binomial interval inequalities for integer size up to thirty and, if NumPy and SciPy are installed, compares the capped-count rule against thousands of direct planar convex-hull computations in noncongruent rhombi. It reports `ALL_CHECKS_PASSED` when all checks succeed. The inverse proof is symbolic and does not rely on finite tests.

## Relationship to prior work
Reitzner, Schütt and Werner (arXiv:1911.05917, submitted 14 November 2019) study hulls of random points on simple-polytope boundaries. Their full open-access article explains that sampled vertices within each facet control global vertices and states the planar large-sample limit of twice the polygon's side number. These facts motivate the present setting and already imply the elementary supporting-edge reduction; that reduction by itself is not presented as new. The present claim concerns the full finite-sample law, **stochastic ordering for every threshold and sample size**, and the **inverse determination** of the unordered side-length proportions from the mean sequence.

Zubkov and Tatarenko (2013) study majorization via the number of occupancy cells containing at least \(r\) particles. Their accessible abstract specifies stochastic comparisons for an individual occupancy threshold, not for the joint sum of thresholds \(1\) and \(2\) used here. Their complete text was not obtained, so it remains a material historical priority risk. O'Neill (2023) treats a uniform-bin extended occupancy model and the number of occupied bins, not this nonuniform capped count. General occupancy and convex-geometric results should receive further priority review before external publication.

## Limitations
The result says nothing about reconstruction of interior angles or the cyclic ordering of side lengths; these are intentionally invisible to the statistic. It does not concern samples from polygon interiors, nonuniform boundary densities (unless replaced by known side masses), curved convex boundaries, finite-data statistical accuracy, or dimensions above two. It uses ordinary probabilistic stochastic order, not sample-path domination for every coupled sample size. The strict ordering is of the mean, not necessarily of every tail. Independent mathematical auditing and exhaustive historical priority review have not been performed.

## References
1. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (initially public 14 November 2019); Discrete & Computational Geometry 69 (2023), 453–504. https://arxiv.org/abs/1911.05917 ; https://doi.org/10.1007/s00454-022-00460-2
2. A. M. Zubkov, T. A. Tatarenko, *The Equivalence between the Schur Order and the Stochastic Orders Generated by the Scheme of Allocation of Particles into Cells*, Mathematical Notes 93 (2013), 69–74. https://doi.org/10.1134/S0001434613010070
3. B. O'Neill, *Three Distributions in the Extended Occupancy Problem*, Methodology and Computing in Applied Probability 25 (2023), article 84. https://doi.org/10.1007/s11009-023-10053-y
