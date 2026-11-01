# The three-dimensional barycentric Schur–Horn criterion for ellipsoid surface-area maximizers

## Finding

Let \(C\) be any real symmetric positive-definite \(3\times3\) matrix and let \(y\in S^2\). Put \(P=I-yy^{\mathsf T}\), \(b=PCy\), and let \(\Delta\) denote the difference of the two eigenvalues of the compression of \(C\) to \(y^\perp\). The following are equivalent:

1. There is an orthonormal basis \(u_1,u_2,u_3\) satisfying simultaneously \(u_j\cdot y=1/\sqrt3\) and \(u_j^{\mathsf T}Cu_j=\operatorname{tr}(C)/3\) for all \(j\).
2. \(\Delta=2\sqrt2\,\|b\|\).
3. The explicit quartic (restricted to the sphere) vanishes:
   \[
   9(y^{\mathsf T}Cy)^2+2\operatorname{tr}(C)(y^{\mathsf T}Cy)
   -12y^{\mathsf T}C^2y+2\operatorname{tr}(C^2)-(\operatorname{tr}C)^2=0.
   \]

Consequently, for every positive-definite \(A\) and prescribed \(x_0\in\partial\mathcal E_A\), where \(\mathcal E_A=\{x:x^{\mathsf T}A^{-1}x\le1\}\) and \(y=A^{-1/2}x_0\), these conditions with \(C=A^{-1}\) characterize exactly whether a parallelepiped inscribed in \(\mathcal E_A\), having \(x_0\) as a vertex, attains the *unconstrained* global maximum of its total facet area.

If the criterion holds and \(b\ne0\), **the maximizing parallelepiped containing \(x_0\) is unique as an unlabeled geometric set**. If \(b=0\), the criterion forces the compression of \(C\) to \(y^\perp\) to be scalar; all rotations about \(y\) of a barycentric frame then give the full one-parameter family of maximizers (with finite identifications).

For example, with \(C=\operatorname{diag}(1,2,3)\), the non-principal direction \(y=(1,2,1)/\sqrt6\) satisfies the criterion, whereas none of the three principal-axis directions does. Thus the algebraic locus is nonempty even for a triaxial ellipsoid.

## Assumptions and scope

All matrices and vectors are real, \(A,C\) are strictly positive-definite, and \(\|y\|_2=1\). “Inscribed” means all eight vertices lie on the ellipsoid boundary; facet area means the sum of the Euclidean areas of the six facets. The criterion is **specific to dimension three**; it does not assert a solution of the higher-dimensional restricted Schur–Horn question. The value of the global maximum, independently established by Kania, is \(8\sqrt{\det A\,\operatorname{tr}(A^{-1})/3}\).

## Proof

**Geometric reduction.** Kania's Theorem 4.2 and Proposition 5.2 [1] establish, in dimension three, that a surface-area-maximizing inscribed parallelepiped through \(x_0\) exists if and only if there is an orthonormal frame \((u_0,u_1,u_2)\) with
\[
 u_j\cdot y=1/\sqrt3,\qquad
 u_j^{\mathsf T}Cu_j=\operatorname{tr}(C)/3
 \quad(j=0,1,2).
\]
Here the associated ellipsoid parallelepiped has vertices \(A^{1/2}(\pm u_0\pm u_1\pm u_2)/\sqrt3\). The reduction and global extremal formula belong to [1], not to the present criterion.

**Parametrize every admissible frame.** Choose an orthonormal pair \((e,f)\) spanning \(y^\perp\). After possibly reversing the cyclic order of the three columns, any barycentric orthonormal frame has exactly the form
\[
 u_j(\theta)=\frac{y}{\sqrt3}+\sqrt{\frac23}
 [\cos(\theta+2\pi j/3)e+\sin(\theta+2\pi j/3)f],
 \quad j=0,1,2,
 \]
with \(\theta\in\mathbb R/(2\pi\mathbb Z)\). Indeed, the tangential components of the columns are three equal vectors whose mutual inner products are \(-1/3\), hence the vertices of an equilateral triangle; the formula also directly gives an orthonormal frame with the prescribed positive dot products.

**Resolve the harmonic equality condition.** In the chosen tangent frame write
\[
 b_1=e^{\mathsf T}Cy,\qquad b_2=f^{\mathsf T}Cy,\qquad
 p=\frac{e^{\mathsf T}Ce-f^{\mathsf T}Cf}{2},\qquad
 q=e^{\mathsf T}Cf.
\]
The traceless part of the compressed \(2\times2\) matrix is \(\bigl(\begin{smallmatrix}p&q\\q&-p\end{smallmatrix}\bigr)\), so
\[
 \Delta=2\sqrt{p^2+q^2},\qquad \|b\|=\sqrt{b_1^2+b_2^2}.
\]
For \(t_j=\theta+2\pi j/3\), direct expansion yields the exact identity
\[
 \frac32\left(u_j(\theta)^{\mathsf T}Cu_j(\theta)-
 \frac{\operatorname{tr}C}{3}\right)
 =\sqrt2(b_1\cos t_j+b_2\sin t_j)+p\cos(2t_j)+q\sin(2t_j).
\]
Let \(\omega=e^{2\pi i/3}\). Since \(\omega^{2j}=\omega^{-j}\), each right side equals
\[
 \operatorname{Re}\!\left(\left[\sqrt2(b_1-ib_2)e^{i\theta}+
 (p+iq)e^{-2i\theta}\right]\omega^j\right).
\]
The real parts for \(j=0,1,2\) all vanish precisely when the complex coefficient in square brackets vanishes. This is equivalent to
\[
 \sqrt2(b_1-ib_2)e^{3i\theta}=-(p+iq).
\]
An angle \(\theta\) exists if and only if \(p^2+q^2=2(b_1^2+b_2^2)\), equivalently \(\Delta=2\sqrt2\|b\|\). This proves the first two conditions equivalent for every \(C,y\), including the zero-amplitude cases.

**Coordinate-free quartic.** Put \(T=\operatorname{tr}C\), \(T_2=\operatorname{tr}(C^2)\), \(a=y^{\mathsf T}Cy\), and \(v=y^{\mathsf T}C^2y\). Because \(P=I-yy^{\mathsf T}\),
\[
 \operatorname{tr}(PCP)=T-a,\quad
 \operatorname{tr}((PCP)^2)=T_2-2v+a^2,\quad
 \|PCy\|^2=v-a^2.
\]
The nonzero eigenvalues of \(PCP\) are precisely those of the compression to \(y^\perp\). Hence
\[
 \Delta^2=2\operatorname{tr}((PCP)^2)-[\operatorname{tr}(PCP)]^2.
\]
Subtracting \(8\|PCy\|^2\) and simplifying gives exactly
\[
 \Delta^2-8\|PCy\|^2=9a^2+2Ta-12v+2T_2-T^2.
\]
Both sides of \(\Delta=2\sqrt2\|b\|\) are nonnegative, so the vanishing quartic is equivalent to the unsquared criterion without extraneous roots.

**Uniqueness and exceptional family.** If \(b\ne0\) under the criterion, the complex equation determines exactly three values of \(\theta\) modulo \(2\pi\). They differ by \(2\pi/3\), which only cyclically permutes the frame columns; reversing their cyclic order makes no new unlabeled frame. Thus there is a unique geometric maximizer through the prescribed vertex. If \(b=0\), the criterion implies \(p=q=0\); every angle is a solution. Then \(Cy=ay\) and \(C|_{y^\perp}\) is scalar, so the rotationally parametrized family is exhaustive. The converse is immediate. For the given diagonal example, write the coordinate squares of \(y\) as \((1/6,4/6,1/6)\); then \(a=2\), \(v=13/3\), \(T=6\), \(T_2=14\), and the quartic is \(0\). At a coordinate eigenvector, it equals the square of the difference between the other two eigenvalues and is nonzero in the triaxial example.

## Verification

The standalone `verify.py` checks the rational identity for the explicit triaxial example, principal-axis obstructions, rotational examples, and a numerical reconstruction of its unique barycentric equal-diagonal frame. It additionally tests the coordinate-invariant quartic against the tangent-plane spectral expression and the harmonic expansion on deterministic randomly generated positive-definite matrices. Replaying the script with Python 3 and only its standard library prints `PASS: 607 exact and numerical checks; analytic proof required for all dimensions/domain.` The universal proof is the analytic argument above; numerical sampling is not an exhaustive certificate.

## Relationship to prior work

The global facet-area extremal bound, equality conditions, and precise reduction to barycentric equal-diagonal frames were proved by Kania [1]. The same paper identifies the restricted Schur–Horn existence question as Problem 6.1, and establishes the dimension-three *principal-axis* case as Theorem 5.5. The present contribution gives the complete criterion for all points in dimension three, an explicit intrinsic quartic test, and a unique-versus-continuous family classification. In contrast, the classical unrestricted Schur–Horn theorem [2] guarantees equal diagonals without enforcing a barycentric constraint and does not imply this characterization; the classical planar Connes–Zagier theorem [3] concerns the different dimension-two perimeter setting.

## Limitations

No all-dimensional solution or universal surface-area maximum under an incompatible vertex constraint is asserted. The locus may be empty for particular matrix-direction pairs, and the exceptional continuously many maximizers occur only in the rotationally symmetric case relative to the prescribed direction. Historical completeness cannot be proved by searching: an equivalent independent formulation or a later work unindexed in the checked sources might exist. Independent external audit has not been performed.

## References

1. T. Kania, *Parallelepipeds of Maximal Facet Area and Total Edge Length in Ellipsoids, Through Prescribed Boundary Points*, Results in Mathematics **81**, article 186 (2026), DOI: 10.1007/s00025-026-02757-7; first public arXiv version dated 2025-10-18, arXiv:2510.16488. https://arxiv.org/abs/2510.16488 ; https://link.springer.com/article/10.1007/s00025-026-02757-7
2. R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd edition (2013), Schur–Horn theorem.
3. A. Connes and D. Zagier, *A property of parallelograms inscribed in ellipses*, American Mathematical Monthly **114** (2007), 909–914.
