# An octahedral counterexample to the proposed odd-dimensional self-volume minimum

## Finding
Let \(\Omega_d(K)\) denote the recursive self-volume of a centrally symmetric convex body \(K\subset\mathbb R^d\), defined in the next section. For the regular coordinate octahedron
\[
O=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}=\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le1\},
\]
one has the exact value
\[
\boxed{\Omega_3(O)=\frac{16}{3}<6.}
\]
In fact, if \(H\subset\mathbb R^2\) is any centrally symmetric affine-regular hexagon and \(k\ge1\) is an integer, then the centrally symmetric body
\[
B_{2k+1}=O\times H^{k-1}\subset\mathbb R^{2k+1}
\]
satisfies
\[
\boxed{\Omega_{2k+1}(B_{2k+1})=\frac{16}{9}\,3^k=\frac89\bigl(2\cdot 3^k\bigr).}
\]
Thus the proposed lower bound \(2\cdot 3^k\) for centrally symmetric bodies in every odd dimension \(2k+1\ge3\) is false. These examples do not determine the actual minimum in any dimension.

## Assumptions and scope
For an origin-symmetric full-dimensional convex body \(K\subset\mathbb R^d\), set \(\Omega_1(I)=2\) for any centered nondegenerate interval \(I\). Recursively, for \(d\ge2\), with \(\nu_x\) an outer Euclidean unit normal at almost every boundary point, put
\[
\Omega_d(K)=\frac1d\int_{\partial K}
\frac{\Omega_{d-1}(K\cap\nu_x^\perp)}{\operatorname{vol}_{d-1}(K\cap\nu_x^\perp)}\,d\mathcal H^{d-1}(x).
\]
The lower-dimensional self-volume is taken in the central hyperplane with its induced Euclidean structure and the origin as center. In the polygonal case, the associated self-perimeter equals the sum of the Minkowski-gauge lengths of its oriented edges; its self-area is half of that perimeter. This is the self-volume convention of Wolansky, *Self-perimeters of convex sets* (2026), Definition 4.1, not ordinary Euclidean volume and not Holmes–Thompson volume. The result covers all odd \(d\ge3\) by explicit products, not all symmetric bodies and not even-dimensional minima.

## Proof
**Central hexagonal sections.** Every facet of \(O\) is congruent to the triangle with vertices \(e_1,e_2,e_3\), with Euclidean area \(\sqrt3/2\). For this facet the outward normal is \(\nu=(1,1,1)/\sqrt3\). The corresponding central section is
\[
H_0=O\cap\{x_1+x_2+x_3=0\}
=\operatorname{conv}\left\{\frac{e_i-e_j}{2}:i\ne j\right\}.
\]
Indeed, intersecting the section plane with the relevant edges joining \(e_i\) to \(-e_j\), \(i\ne j\), yields precisely these six extreme points. They are the vertices of a regular hexagon of circumradius \(1/\sqrt2\), hence
\[
\operatorname{area}(H_0)=\frac{3\sqrt3}{4}.
\]
By signed-coordinate symmetry this applies to all eight facets.

**Self-area of the section.** Order the six vertices cyclically as
\[
(1,-1,0)/2,\ (1,0,-1)/2,\ (0,1,-1)/2,\ (-1,1,0)/2,\ (-1,0,1)/2,\ (0,-1,1)/2.
\]
Each successive edge difference is itself one of these six vertices. Consequently every edge has length one in the norm with unit ball \(H_0\). The self-perimeter is therefore six and
\[
\Omega_2(H_0)=6/2=3.
\]
This also follows directly from the central-chord definition, without using any regular-polygon extremal theorem.

**Three-dimensional value.** The surface integral in the recursive definition is constant on each facet, so
\[
\Omega_3(O)=\frac13\cdot8\cdot\frac{\sqrt3}{2}
\cdot\frac{3}{3\sqrt3/4}=\frac{16}{3}.
\]
This is strictly below the proposed odd-three-dimensional minimum of six.

**Product propagation.** For centered full-dimensional convex bodies \(A\subset\mathbb R^a\) and \(B\subset\mathbb R^b\), the recursive definition implies
\[
\Omega_{a+b}(A\times B)=\Omega_a(A)\Omega_b(B).
\]
For clarity, prove this by induction on \(a+b\). The base case of two intervals is a centered rectangle, whose four boundary sides give \(\Omega_2=4=2\cdot2\). If \(A=I\) is an interval and \(b\ge2\), the two caps \(\partial I\times B\) contribute \(2\Omega_b(B)\) to the defining boundary integral. On the side \(I\times\partial B\), the central section is \(I\times(B\cap\nu^\perp)\). By induction its self-volume is \(2\Omega_{b-1}(B\cap\nu^\perp)\); the interval's Euclidean length cancels. Thus the side contributes \(2b\Omega_b(B)\), and division by \(b+1\) yields \(\Omega_{b+1}(I\times B)=2\Omega_b(B)\). The same applies when \(B\) is an interval. If \(a,b\ge2\), the boundary is, modulo lower-dimensional sets, the union of \(\partial A\times B\) and \(A\times\partial B\). Over the first part the central normal section is \((A\cap\nu^\perp)\times B\), whose self-volume factors by induction; its Euclidean section volume is \(\operatorname{vol}_{a-1}(A\cap\nu^\perp)\operatorname{vol}_b(B)\). Integration over \(B\) cancels the latter volume, yielding \(a\Omega_a(A)\Omega_b(B)\). The other part similarly contributes \(b\Omega_a(A)\Omega_b(B)\). Division by \(a+b\) proves the identity in all cases.

A centrally symmetric affine-regular hexagon \(H\) has \(\Omega_2(H)=3\), as above and by linear invariance of the planar gauge. Thus for every integer \(k\ge1\),
\[
\Omega_{2k+1}(O\times H^{k-1})=\frac{16}{3}\,3^{k-1}=\frac{16}{9}\,3^k.
\]
Since \(16/9<2\), every one of these products violates the conjectured value \(2\cdot3^k\). This completes the proof.

## Verification
The self-contained \(\texttt{CHECK.py}\) uses exact rational vector arithmetic to enumerate the six hexagon vertices, certify all six edge directions and radii, confirm the squared Euclidean facet and section areas \(3/4\) and \(27/16\), and obtain \(\Omega_3(O)=16/3\). It also evaluates the product comparison exactly in odd dimensions 3 through 51 as supplementary finite checks. The proof above, not the finite product loop, establishes the infinite-dimensional conclusion. Run with \(\texttt{python3 CHECK.py}\); no third-party Python package is required.

## Relationship to prior work
Wolansky (2026), Definition 4.1, introduced the recursive self-volume, and Section 4.4 conjectured that centrally symmetric odd-dimensional bodies have minimum \(2\cdot3^k\) in dimension \(2k+1\), attained by \(k\) hexagons times an interval. The same work proves product multiplicativity (Theorem 4.2) and gives the regular-hexagon self-perimeter formula, but does not calculate the three-dimensional octahedron or give the counterexample. Ghandehari and Martini (2019) study planar self-circumferences, including regular hexagons; their planar conclusions alone do not assert an odd-dimensional minimum or exclude octahedral sections. The contribution here is the exact three-dimensional obstruction and its propagation to every higher odd dimension.

## Limitations
Only the claimed odd-dimensional minimum is disproved: no universal lower bound, true minimizer, or even-dimensional statement is established. The numbers use the specified recursive self-volume, not classical Euclidean or Holmes–Thompson volume. Prior-art searches did not reveal this exact counterexample, but unindexed higher-dimensional normed-volume computations could conceivably contain it. No independent audit has been performed.

## References
1. G. Wolansky, *Self-perimeters of convex sets*, arXiv:2604.01950 (first posted 2026-04-02), Definition 4.1, Theorem 4.2, Section 4.4. https://arxiv.org/abs/2604.01950
2. M. Ghandehari and H. Martini, *On self-circumferences in Minkowski planes*, Extracta Mathematicae 34 (2019), 19–28. DOI:10.17398/2605-5686.34.1.19.
