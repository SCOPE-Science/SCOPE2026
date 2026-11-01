# The complete uniform-offset section law and its inverse phase boundary for parallelotopes

## Finding

Let a three-dimensional parallelotope be cut by planes of one fixed orientation, with the offset chosen uniformly over all intersecting planes. The number \(N\) of sides of the section is almost surely in \(\{3,4,5,6\}\). Its entire law is determined by three normalized absolute projections, as given below. As the plane orientation varies over all directions in **any fixed parallelotope**, the possible laws comprise exactly the complete simplex of probability measures on \(\{3,4,5,6\}\) with mean \(4\).

The direction's three sorted normalized absolute generator projections can be recovered uniquely from the law if \(\Pr(N=6)>0\), but not generally if \(\Pr(N=6)=0\). This is a sharp inverse-identifiability boundary. Furthermore, \(0\le \operatorname{Var}(N)\le 2\), with equality at the upper bound exactly when the three absolute generator projections coincide and at the lower bound exactly when at least one vanishes.

## Assumptions and scope

Fix a nondegenerate Euclidean parallelotope
\[
P=c+\left\{\sum_{i=1}^{3}s_i v_i:-1\le s_i\le1\right\}\subset\mathbb R^3,
\]
where \(v_1,v_2,v_3\) are linearly independent. Choose any \(u\in\mathbb R^3\setminus\{0\}\), put \(W=\sum_i|\langle u,v_i\rangle|>0\), and sample a real offset \(T\) uniformly from \((\langle u,c\rangle-W,\langle u,c\rangle+W)\). The random section is \(P\cap\{x:\langle u,x\rangle=T\}\). At a finite set of offsets through vertices the combinatorics can be exceptional; these null events do not affect the law.

Sort the projection magnitudes as \(A\ge B\ge C\ge0\), where \(\{A,B,C\}=\{|\langle u,v_i\rangle|:1\le i\le3\}\), and define \(p_j=\Pr(N=j)\).

If \(A\ge B+C\), the exact probabilities are
\[
(p_3,p_4,p_5,p_6)=\left(\frac{2C}{W},\;1-\frac{4C}{W},\;\frac{2C}{W},\;0\right).
\]
If \(A<B+C\), they are
\[
(p_3,p_4,p_5,p_6)=\left(\frac{2C}{W},\;\frac{2(B-C)}{W},\;\frac{2(A-B)}{W},\;\frac{B+C-A}{W}\right).
\]
Both formulas include their stated equality boundaries by continuity; no general-position assumption on \(u\) is required.

## Proof

**Crossing count.** Affine coordinates reduce the parallelotope to a cube with signed height function \(\sum_i \sigma_i |\langle u,v_i\rangle|\), where each \(\sigma_i\in\{-1,1\}\). A plane not passing through a vertex meets the interior of a cube edge exactly when the two endpoint heights straddle its level. Distinct such edge intersections are precisely the vertices of its convex polygonal section. The count is invariant under reflection of the offset about the center, so it suffices to use the positive half-range \(0<t<W\).

The four nonnegative levels obtained from the eight cube vertices are
\[
W,\quad A+B-C,\quad A-B+C,\quad |A-B-C|.
\]
They are ordered as written because \(A\ge B\ge C\). Immediately below \(W\), three incident edges are cut, so \(N=3\). Each time the level moves downward past a vertex, the net crossing count changes by the number of newly intersected incident edges minus the number that cease intersecting. Equivalently, one can enumerate the twelve edges directly: for each coordinate \(i\), the four edges parallel to \(v_i\) are cut precisely when \(t\) belongs to the open interval of radius \(|\langle u,v_i\rangle|\) about one of the four signed sums of the other two projections. This remains valid when a projection vanishes, because those parallel edges then do not contribute except at null offsets.

If \(A\ge B+C\), the successive positive-level intervals \((A+B-C,W)\), \((A-B+C,A+B-C)\), \((A-B-C,A-B+C)\), \((0,A-B-C)\) have edge-crossing counts \(3,4,5,4\), respectively. Their lengths are \(2C,2(B-C),2C,A-B-C\). In the case \(A<B+C\), the intervals \((A+B-C,W)\), \((A-B+C,A+B-C)\), \((B+C-A,A-B+C)\), \((0,B+C-A)\) have counts \(3,4,5,6\) and lengths \(2C,2(B-C),2(A-B),B+C-A\). Dividing the total length associated with each count by \(W\) gives the displayed laws; in the first case the two four-sided intervals have total length \(W-4C\).

**Image simplex.** In either case \(\mathbb E N=4\) (also known from the general mean theorem in [1]), since the formulas yield \(p_3=p_5+2p_6\). Conversely, any nonnegative vector summing to one with that relation is realized. If \(p_6>0\), take the normalized projections
\[
\left(\frac AW,\frac BW,\frac CW\right)=
\left(\frac{p_3+p_4+p_5}{2},\;\frac{p_3+p_4}{2},\;\frac{p_3}{2}\right).
\]
They sum to one, are nonincreasing, satisfy \(B+C>A\), and recover the proposed probabilities. If \(p_6=0\), write \(p_3=p_5=\rho\in[0,1/2]\) and \(p_4=1-2\rho\); choosing \((A/W,B/W,C/W)=(1/2,(1-\rho)/2,\rho/2)\) realizes that law. For every chosen nonnegative normalized triple, the equations \(\langle u,v_i\rangle\) equal to its components (in any chosen order and signs) have a nonzero solution \(u\), because the generator matrix is invertible. Thus the complete mean-four simplex is attained within each fixed parallelotope. Its three vertices are the laws \((0,1,0,0)\), \((1/2,0,1/2,0)\), and \((2/3,0,0,1/3)\).

**Inverse and variance.** If \(p_6>0\), the preceding inversion formula is forced by the second branch, proving uniqueness of the sorted projection ratios. On the boundary \(p_6=0\), the complete inverse fiber for the law \((\rho,1-2\rho,\rho,0)\) is
\[
\frac CW=\frac\rho2,\qquad
\frac BW\in\left[\frac\rho2,\frac{1-\rho}{2}\right],\qquad
\frac AW=1-\frac BW-\frac\rho2.
\]
This interval has positive length for \(0\le\rho<1/2\) and reduces to a point for \(\rho=1/2\), proving the exact uniqueness boundary, including degenerate-normal cases. Since the mean equals four, the squared deviation is one for \(N=3,5\), four for \(N=6\) and zero for \(N=4\); hence
\[
\operatorname{Var}(N)=p_3+p_5+4p_6
=2(p_3+p_6)
=\frac{4C+2(B+C-A)_+}{W}.
\]
On the feasible triangle this affine statistic has range \([0,2]\), with its maximum only at the vertex law \((2/3,0,0,1/3)\), equivalent to \(A=B=C>0\); and minimum only at the vertex law \((0,1,0,0)\), equivalent to \(C=0\). This proves sharpness.

## Verification

The standalone Python 3 standard-library script `verify.py` computes the theoretical probabilities in exact rational arithmetic. Independently, it constructs the eight cube vertices and twelve edges, determines exact offset subintervals, and counts intersected edges at a rational sample point of each nonempty interval. It compares all cases in a seeded finite test, boundary and zero-projection cases, the feasible-law simplex grid, the inverse formula and the extremal variance bounds. Running `python verify.py` reports `ALL_CHECKS_PASSED`. The infinite-dimensional quantifiers over orientations and real projection ratios follow from the analytic crossing-count proof above, not from finite tests.

## Relationship to prior work

Bárány and Domokos [1] prove the orientation-independent **mean** section-side count of four for parallelotopes; their full text (especially Section 3, equation (3.1)) gives an edge-integral formula for the mean. They do not state the four-point probability law, the exact feasible simplex, or the inverse phase boundary. Brandenburg, De Loera and Meroni [2] give a general chamber decomposition for affine hyperplane sections, which explains why types remain constant between projected vertex levels but does not provide this law or its inverse realization theorem. Heerten, Hübner and Thäle [3] determine triangle-through-hexagon probabilities of typical cells in *tri-directional Poisson line tessellations*, a different random object and sampling distribution; their probabilities and variance bound differ from the present ones. Brandenburg and Meroni [4] classify cube-section types, but their enumerative type distribution is not the present probability measure over uniform offsets at one prescribed normal.

A plausible older source, Chakerian and Logothetti [5], studies cube slices and probability. The complete text was not accessible for material comparison; it remains a specific historical-priority risk, particularly for any special cube case. No claim is made that search noncoverage proves priority.

## Limitations

This is an exact law for a fixed orientation with offset uniform in its intersecting interval. It is *not* the law for a Haar-uniform orientation or a uniformly area- or volume-sampled point, and it does not generalize here to arbitrary non-parallelotopal polytopes or higher-dimensional hyperplanes. The inverse recovers only the unordered relative magnitudes of the three normal projections, not the normal's signs, the parallelotope itself, or its Euclidean dimensions. The result has not undergone independent mathematical audit. Exhaustive historical priority, notably against [5], remains unresolved.

## References

[1] I. Bárány and G. Domokos, *Same average in every direction*, arXiv:2310.18960v1, first posted 2023-10-29; https://arxiv.org/abs/2310.18960.

[2] M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1, first posted 2023-04-27; https://arxiv.org/abs/2304.14239.

[3] N. Heerten, J. Hübner and C. Thäle, *Vertex number of the typical cell in a tri-directional Poisson line tessellation*, arXiv:2309.12771v1, first posted 2023-09-22; https://arxiv.org/abs/2309.12771.

[4] M.-C. Brandenburg and C. Meroni, *Combinatorics of slices of cubes*, arXiv:2510.09265v1, first posted 2025-10-10; https://arxiv.org/abs/2510.09265.

[5] G. D. Chakerian and D. Logothetti, *Cube Slices, Pictorial Triangles, and Probability*, Mathematics Magazine 64 (1991), 219–241; https://doi.org/10.2307/2690829 (full text not inspected).
