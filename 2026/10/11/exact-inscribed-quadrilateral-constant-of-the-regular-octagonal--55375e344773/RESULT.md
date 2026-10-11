# Exact inscribed-quadrilateral constant of the regular octagonal Banach plane
## Finding
Let \(X_8=(\mathbb R^2,N)\) be the real Banach plane with
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For the Ahmad--Liu--Li inscribed-quadrilateral constant
\[
J_{\mathrm{in}}(X)=\sup\left\{\sum_{1\le i<j\le4}\|x_i-x_j\|^2:\ x_1,x_2,x_3,x_4\in S_X,\ \sum_{i=1}^4x_i=0\right\},
\]
one has
\[
J_{\mathrm{in}}(X_8)=40-16\sqrt2.
\]
Moreover
\[
C'_{\mathrm{NJ}}(X_8)=4-2\sqrt2,
\qquad
J_{\mathrm{in}}(X_8)=8+8C'_{\mathrm{NJ}}(X_8).
\]
Hence the general lower comparison between these two constants is sharp for the regular octagon even though its unit sphere has line segments.

## Assumptions and scope
The scalar field is real. The norm is exactly the displayed regular-octagonal norm. The four vectors in the definition of \(J_{\mathrm{in}}\) are required to lie on the unit sphere and to have zero sum. No assertion is made for arbitrary octagonal norms, arbitrary centrally symmetric polygons, or higher dimensions.

## Proof
Put \(a=\sqrt2-1\). The unit ball has cyclic vertices
\[
(1,a),(a,1),(-a,1),(-1,a),(-1,-a),(-a,-1),(a,-1),(1,-a).
\]
For the lower bound take
\[
x_1=(1,a),\quad x_2=(a,1),\quad x_3=-x_1,\quad x_4=-x_2.
\]
These four vectors are on the unit sphere and have zero sum. Two of their six mutual distances equal \(2a\), and the remaining four equal \(2\). Therefore
\[
\sum_{i<j}N(x_i-x_j)^2
=2(2a)^2+4\cdot2^2
=40-16\sqrt2.
\]

For the upper bound, parameterize each of the eight unit-sphere edges affinely. Fix an ordered four-tuple of edges and write the four points as \(p_i+t_i d_i\) with \(0\le t_i\le1\). The centroid condition gives two affine equations in the four parameters, so the feasible set is a compact polytope of dimension at most two. On this polytope the objective
\[
F=\sum_{i<j}N(x_i-x_j)^2
\]
is convex: each difference is affine, the norm is convex and nonnegative, squaring is increasing and convex on the nonnegative half-line, and finite sums preserve convexity. A convex function on a compact polytope attains its maximum at an extreme point.

The bundled exact-arithmetic checker enumerates every ordered edge four-tuple. For rank-two centroid systems it fixes two parameters at endpoints and solves the remaining two; for rank-one systems it fixes three parameters and solves the last one. Every feasible polytope vertex is therefore included. Arithmetic is performed exactly in \(\mathbb Q(\sqrt2)\). Across all edge tuples there are \(11712\) feasible candidate occurrences: \(11136\) from rank-two systems and \(576\) from rank-one systems. Every candidate satisfies
\[
F\le40-16\sqrt2,
\]
and the displayed quadruple attains equality. This proves the exact value.

For completeness, the same checker independently computes the modified von Neumann--Jordan constant. On the Cartesian product of two fixed unit-sphere edges,
\[
\frac{N(x+y)^2+N(x-y)^2}{4}
\]
is convex, so its maximum occurs at a pair of edge endpoints. Evaluation of the \(64\) ordered vertex pairs gives
\[
C'_{\mathrm{NJ}}(X_8)=4-2\sqrt2.
\]
Substitution yields \(40-16\sqrt2=8+8(4-2\sqrt2)\).

## Verification
Run `verify_jin_octagon.py` with the Python standard library. It uses exact rational pairs for \(u+v\sqrt2\), enumerates all feasible edge-polytope vertices, checks the explicit maximizing quadruple, independently evaluates the \(64\) vertex pairs for \(C'_{\mathrm{NJ}}\), and prints `VERIFY_OK` only after the exact identities pass. The bundled `verification_output.txt` records the replay output.

## Relationship to prior work
Ahmad, Liu, and Li introduced \(J_{\mathrm{in}}\), proved
\[
J_{\mathrm{in}}(X)\ge8C'_{\mathrm{NJ}}(X)+8,
\]
and established the universal range \(16\le J_{\mathrm{in}}(X)\le24\). Their explicit polygonal examples are the square-type planes \(\ell_1^2\) and \(\ell_\infty^2\), where the value is \(24\); the regular octagon is not evaluated there.

A later published result proves the identity \(J_{\mathrm{in}}(X)=8+8C'_{\mathrm{NJ}}(X)\) for real strictly convex normed planes. That theorem does not cover \(X_8\), because every side of the regular octagon is a nontrivial line segment. The present computation shows that the same lower comparison is nevertheless sharp at this canonical flat polygonal norm. A previously available exact computation of \(C'_{\mathrm{NJ}}(X_8)\) supplies only the lower bound through the 2021 inequality; it does not imply the required four-point upper bound.

## Limitations
The proof is specific to the real regular octagon. The finite certificate establishes the complete continuous optimization because convexity reduces each edge cell to its vertices; it is not an inference from sampling. No classification of all maximizing quadruples is claimed. A finite literature search can miss an uncatalogued equivalent computation.

## References
1. A. Ahmad, Q. Liu, Y. Li, “Geometric Constants in Banach Spaces Related to the Inscribed Quadrilateral of Unit Balls,” *Symmetry* 13 (2021), 1294, DOI 10.3390/sym13071294.
2. Published record 269b2acc-f6dc-4ee0-a88c-f21f624f3cd7, “Inscribed-quadrilateral collapse in strictly convex normed planes.”
