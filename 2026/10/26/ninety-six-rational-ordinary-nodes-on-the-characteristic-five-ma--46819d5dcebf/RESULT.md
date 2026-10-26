# Ninety-six rational ordinary nodes on the characteristic-five Maschke octic

## Finding

Let \(k\) be an algebraic closure of \(\mathbb F_5\), and let \(S\subset\mathbb P^3_k\) be the coefficientwise special fibre of the integral Maschke octic
\[
F=\sum_{i=0}^3x_i^8+14\sum_{0\le i<j\le3}x_i^4x_j^4+168\prod_{i=0}^3x_i^2.
\]
The projective singular scheme of \(S\) is reduced and supported on **exactly 96 geometric points, all \(\mathbb F_5\)-rational and all ordinary double points**. Precisely, they form the following two disjoint sets, where \(a\in k^\times\) denotes the common nonzero fourth power:

1. **64 points:** exactly one coordinate vanishes and the other three have equal fourth powers \(a\).
2. **32 points:** all four coordinates have equal fourth powers \(a\), and \(\prod_{i=0}^3x_i^2=-a^2\).

The two sets are orbits of the coordinate-permutation and fourth-root diagonal symmetry group. Moreover \(S(\mathbb F_5)\) consists of exactly these 96 singular points; in particular, \(S\) has no smooth \(\mathbb F_5\)-point. The octic is geometrically integral and normal.

## Assumptions and scope

All assertions concern the given integral homogeneous degree-eight polynomial reduced modulo \(5\), not arbitrary models, minimal semistable reduction, or the associated double cover. The geometric singular points are computed over the full algebraic closure, not merely by enumerating finite-field points. An ordinary double point means a hypersurface germ whose quadratic term is nondegenerate in three affine local coordinates, equivalently an \(A_1\) singularity in odd characteristic.

## Proof

**1. Reduction and critical equations.** Work in characteristic \(5\). Put \(y_i=x_i^2\), \(z_i=y_i^2=x_i^4\), \(P=\prod_i y_i\), and \(T=\sum_i z_i\). The defining equation becomes
\[
F=\sum_i y_i^4-\sum_{i<j}y_i^2y_j^2+3P.
\]
For each nonzero \(x_i\), the equation \(\partial F/\partial x_i=0\), after division by the invertible factor \(2x_iy_i\), is
\[
4z_i-2(T-z_i)+3P/y_i^2=0.
\]
Equivalently, multiplying by \(z_i\),
\[
z_i^2-2Tz_i+3P=0. \tag{1}
\]
When \(x_i=0\), its partial derivative vanishes automatically. Euler's identity \(8F=\sum_i x_i\partial F/\partial x_i\), with \(8\ne0\) in \(k\), ensures that every common nonzero zero of the partial derivatives lies on \(S\).

**2. Number of nonzero coordinates.** If there are \(r\le3\) nonzero coordinates, then \(P=0\), and the undivided equation of the corresponding nonzero \(x_i\) simplifies to \(z_i=2T\). Therefore every nonzero \(z_i\) has one common value \(a\), and \(a=2ra\). Since \(a\ne0\), this forces \(r=3\) in characteristic five. Hence these solutions are precisely the 64 points described in the first set: choose the zero coordinate in four ways, scale one remaining coordinate to \(1\), and choose each other remaining coordinate independently among the four fourth roots of unity.

If \(r=4\), equation (1) says that all four nonzero numbers \(z_i\) are roots of one quadratic, so they assume at most two values. If there are two distinct values \(a,b\) with multiplicities \(m,4-m\), Vieta's relation \(a+b=2T\) gives
\[
(2m-1)a+(2-2m)b=0.
\]
For \(m=1\) this forces \(a=0\); for \(m=3\) it forces \(b=0\); both are impossible. For \(m=2\) it gives \(b=-a\). Their product is \(ab=3P\), so \(P=3a^2\). But \(P^2=\prod_i z_i=a^4\), whereas \((3a^2)^2=4a^4\), a contradiction. Thus all four \(z_i=a\). Substituting into (1), with \(T=4a\), gives \(P=-a^2\). Normalizing \(x_0=1\), the remaining three coordinates range over the four elements of \(\mathbb F_5^\times\); exactly half the \(4^3\) choices satisfy the product-of-squares condition, giving 32 points. Conversely each described point satisfies every partial derivative. This completes the geometric classification over \(k\).

**3. Orbit structure and ordinary nodes.** Each fourth root of unity lies in \(\mathbb F_5\). Coordinate permutations and diagonal changes \(x_i\mapsto\zeta_i x_i\), with \(\zeta_i^4=1\) and \(\prod_i\zeta_i^2=1\), preserve \(F\). These transformations act transitively on each of the two sets: the missing coordinate in the 64-point set provides freedom to enforce the product constraint, and for the 32-point set the two target square-products are equal.

At representatives \([0:1:1:1]\) (chart \(x_1=1\), coordinates \(x_0,x_2,x_3\)) and \([1:1:1:2]\) (chart \(x_0=1\), coordinates \(x_1,x_2,x_3\)), the affine Hessian matrices modulo \(5\) are respectively
\[
\begin{pmatrix}1&0&0\\0&2&4\\0&4&2\end{pmatrix},
\qquad
\begin{pmatrix}4&2&1\\2&4&1\\1&1&1\end{pmatrix}.
\]
Both determinants are \(3\in\mathbb F_5^\times\). Hence all 96 isolated singularities have nondegenerate tangent quadrics and are ordinary double points. Their local Jacobian ideals are reduced by the invertible linear terms of the gradient, so the entire projective Jacobian singular scheme is reduced of length \(96\).

**4. Arithmetic and global geometry.** Every projective \(\mathbb F_5\)-point has either one, two, three, or four nonzero coordinates. For a nonzero field coordinate \(x\), one has \(x^4=1\). With \(r<4\) nonzero coordinates the value of \(F\) is \(r-\binom r2\), vanishing only for \(r=3\). With \(r=4\) it is \(3(1+P)\), vanishing exactly when \(P=-1\). Thus the 96 singular points already exhaust \(S(\mathbb F_5)\).

If \(F\) were reducible over \(k\), any two positive-degree components would meet in a curve in projective three-space; that curve would lie in the singular locus, contradicting its finiteness. Repeated factors would similarly force positive-dimensional singular support. Hence \(S\) is geometrically integral. A hypersurface is Cohen–Macaulay, and its isolated singularities give regularity in codimension one. Serre's criterion then makes \(S\) normal.

## Verification

The standalone `CHECK.py` uses exact symbolic differentiation modulo five, directly verifies the reduced equation and the diagonal symmetry identity, enumerates all \(156\) projective prime-field points, finds precisely the prescribed 96 singular points and no other rational points, and checks both displayed Hessian matrices and their determinants. Execute `python CHECK.py` with Python 3 and SymPy. These finite checks support the proof; they are not used to infer completeness over \(\overline{\mathbb F}_5\).

## Relationship to prior work

Boissière and Sarti introduced the same symmetric octic and proved that it has \(352\) lines over the complex numbers (2006 preprint, Section 5.3). Bini and van Geemen studied the smooth complex Maschke surface and its double-octic threefold (2011, especially introduction, Sections 5 and 6), with arithmetic formulas explicitly discussed at primes greater than five. Bonnafé subsequently identified \(96\) pairwise skew **complex lines** on the smooth octic (2025 preprint). The last number is numerically equal to the present characteristic-five node count, but the assertions concern different varieties and different geometric objects; no specialization correspondence between those line and node configurations is asserted. These source results do not state or directly imply the complete geometric Jacobian singularity classification in characteristic five.

## Limitations

This result concerns only the specified integral model in characteristic five. It does not determine a semistable model of the associated double cover, its monodromy, a correspondence between the 96 nodes and 96 complex skew lines, or a resolution of the resulting threefold. The novelty comparison is limited to the cited inspected primary literature, targeted literature searches, and relevant mathematical records; an equivalent older calculation under another model cannot be categorically excluded. Independent validation remains outstanding.

## References

1. S. Boissière and A. Sarti, *Counting lines on surfaces*, arXiv:math/0606100v1, first posted 2006-06-05, Section 5.3, https://arxiv.org/pdf/math/0606100 .
2. G. Bini and B. van Geemen, *Geometry and arithmetic of Maschke's Calabi–Yau threefold*, arXiv:1110.0106v1, first posted 2011-10-01, https://arxiv.org/pdf/1110.0106 .
3. C. Bonnafé, *The Maschke octic contains 96 pairwise disjoint lines*, arXiv:2601.00033v1, first posted 2025-12-30, https://arxiv.org/pdf/2601.00033 .
