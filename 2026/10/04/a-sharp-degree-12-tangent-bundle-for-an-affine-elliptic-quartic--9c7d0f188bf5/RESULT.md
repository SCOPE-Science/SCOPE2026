# A sharp degree-12 tangent bundle for an affine elliptic quartic
## Finding
Let
\[
X\subset\mathbf P^3_{\mathbf C}
\]
be the complete intersection
\[
x_0^2+x_1^2+x_2^2+x_3^2=0,
\qquad
x_0^2+2x_1^2+3x_2^2+4x_3^2=0,
\]
and let
\[
V=X\cap\{x_0\ne0\}\subset\mathbf A^3_{\mathbf C}.
\]
Then the embedded tangent bundle
\[
TV\subset\mathbf A^6_{\mathbf C}
\]
has geometric degree
\[
\deg(TV)=12.
\]

This realizes equality in the secant-corrected tangent-bundle bound of Lanciano for this nonrational positive-genus space curve:
\[
\deg(TV)
=
\deg(V)^2-2\mu(X)\deg(\operatorname{Sec}(X))
=
16-4
=
12.
\]

## Assumptions and scope
The geometric degree is the usual affine degree, equivalently the degree of the projective closure. For an affine variety of pure dimension \(d\), it is also the maximal finite cardinality of an intersection with an affine linear subspace of complementary dimension.

On the affine chart \(x_0=1\), write coordinates \(x,y,z\). Then
\[
V:
\quad
1+x^2+y^2+z^2=0,
\qquad
1+2x^2+3y^2+4z^2=0.
\]
Writing \(u,v,w\) for tangent-vector coordinates, the embedded tangent bundle is defined by
\[
1+x^2+y^2+z^2=0,
\]
\[
1+2x^2+3y^2+4z^2=0,
\]
\[
xu+yv+zw=0,
\]
\[
2xu+3yv+4zw=0.
\]

The current upper-bound theorem used below applies because \(V\) is a smooth affine curve in \(\mathbf A^3\), its projective closure \(X\) is smooth, and \(2\dim(V)\le3\).

## Proof
First, \(X\) is smooth. If the gradients of its two defining quadrics were dependent at a projective point, then for every nonzero coordinate \(x_i\) the proportionality constant would have to equal the corresponding coefficient among \(1,2,3,4\). Since these coefficients are distinct, at most one coordinate could be nonzero; the first quadric then rules out the point.

As a smooth complete intersection of two quadrics,
\[
\deg(X)=4.
\]
Adjunction gives
\[
K_X=\mathcal O_X(2+2-4)=\mathcal O_X,
\]
so
\[
g(X)=1.
\]

Because \(X\subset\mathbf P^3\) is a smooth nondegenerate curve, its secant variety is all of \(\mathbf P^3\), hence
\[
\deg(\operatorname{Sec}(X))=1.
\]
Projection from a general point of \(\mathbf P^3\) maps \(X\) birationally to a plane quartic with only ordinary nodes. Its arithmetic genus is
\[
\frac{(4-1)(4-2)}2=3,
\]
whereas its normalization has genus \(1\). Therefore the projected quartic has exactly
\[
\mu(X)=3-1=2
\]
nodes, equivalently a general point of \(\mathbf P^3\) lies on exactly two secant lines of \(X\).

Lanciano's secant-corrected inequality therefore gives
\[
\deg(TV)
\le
4^2-2\cdot2\cdot1
=
12.
\]

For the opposite inequality, intersect \(TV\) with the affine codimension-two linear subspace
\[
-2x+y+3z+3u+3v-3w-1=0,
\]
\[
-3x+3z+2w=0.
\]
An exact lexicographic Gröbner-basis computation over \(\mathbf Q\) gives leading monomials
\[
x,\ y,\ z,\ u,\ v,\ w^{12}.
\]
Hence the quotient algebra has basis
\[
1,w,\ldots,w^{11}
\]
and length \(12\). Its univariate eliminant is squarefree, so the intersection consists of \(12\) distinct complex points.

Since geometric degree is the maximal finite cardinality of a complementary affine linear section, this proves
\[
\deg(TV)\ge12.
\]
Together with the upper bound,
\[
\deg(TV)=12.
\]

## Verification
The accompanying `verify.py` reconstructs the affine tangent-bundle ideal and the two stated affine hyperplanes using exact rational arithmetic. It computes the lexicographic Gröbner basis and checks that the leading monomials are exactly
\[
x,\ y,\ z,\ u,\ v,\ w^{12}.
\]
It also verifies that the degree-\(12\) eliminant is squarefree.

The script separately checks the complete-intersection degree and adjunction genus computation, the apparent-double-point count
\[
\mu(X)=2,
\]
and the numerical value \(12\) of the secant-corrected upper bound. The replay output ends in `VERIFY_OK`.

## Relationship to prior work
Jeronimo, Lanciano, and Solernó introduced the systematic study of the geometric degree of tangent bundles of smooth affine varieties and proved several curve formulas and bounds. Their paper does not state this elliptic-quartic example.

Lanciano's 2026 paper proves the universal quadratic bound
\[
\deg(TV)\le\deg(V)^2
\]
and, when the projective closure is smooth and \(2\dim(V)\le n\), the stronger secant-corrected inequality
\[
\deg(TV)
\le
\deg(V)^2
-
2\mu(X)\deg(\operatorname{Sec}(X)).
\]
The same paper gives sharpness examples for the universal bound, including affine Fermat plane curves, but does not state the present elliptic-quartic equality case.

Targeted searches for the source identifier, geometric degree of tangent bundles of elliptic quartics, intersections of two quadrics, the value \(12\), and equivalent secant-count formulations found no statement covering this example. The closest published-finding match concerns tangent birationality of a Calabi–Yau complete intersection of four quadrics, which is a different invariant on a different object.

## Limitations
This is one explicit equality case, not a classification of equality in the secant-corrected bound. It does not assert that every affine chart of every smooth elliptic quartic has tangent-bundle degree \(12\).

The lower bound is certified by one exact complementary affine linear section; it does not enumerate all possible sections. The upper bound relies on the published secant-corrected theorem and on the classical general-projection description of apparent double points for smooth space curves.

## References
1. L. Lanciano, *Degrees and directional defects of embedded algebraic vector bundles*, arXiv:2609.27047v1, 2026.
2. G. Jeronimo, L. Lanciano, P. Solernó, *On the geometric degree of the tangent bundle of a smooth algebraic variety*, arXiv:2403.10661, 2024.
3. Classical general-projection theory for smooth curves in \(\mathbf P^3\), identifying apparent double points with nodes of a general plane projection.
