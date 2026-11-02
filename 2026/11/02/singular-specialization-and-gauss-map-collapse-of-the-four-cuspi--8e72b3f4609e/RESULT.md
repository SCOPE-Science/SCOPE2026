# Singular specialization and Gauss-map collapse of the four-cuspidal quintic

## Finding
Let \(k\) be an algebraically closed field of characteristic \(p\ge 0\), and let \(C_p\subset\mathbb P^2_k\) be the integral quintic defined by the reduction of
\[
27X^5+18X^3YZ-2X^2Y^3-X^2Z^3+2XY^2Z^2-Y^4Z=0.
\]
Here \(p=0\) denotes characteristic zero. This is the arithmetic specialization of the unique four-cuspidal complex quintic described by Koras--Palka. The normalization is \(\mathbb P^1_k\), via
\[
[s:t]\longmapsto[s^4t:s^2t^3-s^5:t^5+2s^3t^2].
\]
The complete geometric singularity and Gauss-map classification is:

- If \(p\ne 2,3\), there are four distinct cusps: one with value semigroup \(\langle2,7\rangle\) and three with value semigroup \(\langle2,3\rangle\). The dual curve has degree four and the Gauss map is birational.
- If \(p=3\), there are exactly two cusps, with value semigroups \(\langle2,7\rangle\) and \(\langle3,4\rangle\). The dual curve still has degree four and the Gauss map is birational.
- If \(p=2\), there is exactly one cusp, with value semigroup \(\langle2,13\rangle\). The dual curve is a line; the Gauss map has purely inseparable degree four. Equivalently, every tangent at a smooth point passes through \([0:1:0]\), a smooth point of the quintic.

For the respective singular points, the local \(\delta\)-invariants are \((3,1,1,1)\), \((3,3)\), and \((6)\). These classifications refer to geometric points and singular branches, not to an assertion that ADE terminology survives in small characteristics.

## Assumptions and scope
The field is algebraically closed, including arbitrary positive characteristic. The displayed integral equation is the specified model; changing its integral model could change the reductions. A value semigroup means the set of orders of nonzero functions in the completed local ring of the reduced branch under the normalized parameter. The Gauss map is the rational map from smooth points to their projective tangent lines, extended to the normalization whenever possible.

## Proof
**Integral model and normalization.** Direct substitution of the displayed degree-five forms into the equation gives zero over \(\mathbb Z\). The forms have no common zero on \(\mathbb P^1\) in any characteristic: when \(st\ne0\), the first form is nonzero, and at the two coordinate points the second or third form is nonzero. They remain linearly independent over every field by inspecting the distinct monomials \(s^5\), \(s^4t\), and \(t^5\). Thus the image is not a line. The degree of the morphism onto its image times the degree of the image is five. Since five is prime, the map has generic degree one and image degree five. The displayed polynomial has degree five and a coefficient equal to \(-1\), so its reduction is a nonzero equation for this irreducible degree-five image, hence defines exactly this integral curve. A finite birational morphism from normal \(\mathbb P^1\) is the normalization.

**Locating the branches.** In the chart \(t=1\), write
\[
P(u)=(u^4,u^2-u^5,1+2u^3).
\]
The tangent-line coefficients satisfy the integral factorization
\[
P(u)\times P'(u)=u(u^3+2)(4u^3-1,\,2u^2,\,-u^4).
\]
The residual vector never vanishes simultaneously at a geometric point, in any characteristic. The point \(t=0\) maps to \([0:1:0]\) and is unramified, as its local first coordinate relative to the second has order one. Hence the potential non-smooth branch parameters are \(u=0\), the three distinct roots of \(u^3=-2\) when \(p\ne2,3\), the single root \(u=1\) when \(p=3\), and only \(u=0\) when \(p=2\). Their images are distinct: for \(p\ne2,3\), each root maps to \([-2u:3u^2:-3]\), and \(-3\ne0\) with \(-2\ne0\); in characteristic three the images at \(0\) and \(1\) are \([0:0:1]\) and \([1:0:0]\).

**Local semigroups.** Near \(u=0\) when \(p\ne2\), \(Z\) is a unit, and the local coordinates \(y=Y/Z\) and \(w=(XZ-Y^2)/Z^2\) have respective orders two and seven. Indeed,
\[
XZ-Y^2=u^7(4-u^3).
\]
The change \((x,y)\mapsto(y,x-y^2)\) is a regular formal coordinate change, and the coprime orders \((2,7)\) give semigroup \(\langle2,7\rangle\) and \(\delta=3\). When \(p=3\), set \(u=1+v\). On the \(X\ne0\) chart the two functions \(Z/X\) and \((Y-Z)/X\) have orders three and four, since in characteristic three
\[
Y=-u^2v^3,\qquad Z=-v^3,\qquad Y-Z=v^4(1-v).
\]
They give semigroup \(\langle3,4\rangle\) and \(\delta=3\).

When \(p=2\), \(Z=1\). The affine coordinates are \(x=u^4\), \(y=u^2+u^5\); replacing \(x\) by \(\eta=x+y^2+y^5\) gives
\[
\eta=u^{13}+u^{22}+u^{25}.
\]
The regular coordinate pair \((y,\eta)\) has coprime orders \((2,13)\), giving semigroup \(\langle2,13\rangle\) and \(\delta=6\). The elementary plane-branch semigroup fact used here is: if two formal regular parameters have coprime positive normalized orders \(m,n\), the plane branch has a single characteristic pair and semigroup \(\langle m,n\rangle\), with \(\delta=(m-1)(n-1)/2\); it follows via Weierstrass division into powers of the higher-order parameter, whose orders occupy distinct residue classes modulo the lower order.

For \(p\ne2,3\), each additional root \(u^3=-2\) gives a singular unibranch point (the tangent derivative vanishes). It therefore has \(\delta\ge1\). The arithmetic genus of an integral plane quintic is six, and its normalization has genus zero, so the sum of all \(\delta\)-invariants is exactly six. The \(\delta=3\) branch at \(u=0\) and three other distinct branches already consume six; therefore they are the only singularities, and the other three have \(\delta=1\), hence the ordinary cuspidal semigroup \(\langle2,3\rangle\). The same genus argument proves exhaustiveness in characteristics three and two from the local contributions \(3+3\) and \(6\), respectively. In particular, neither hidden nodes nor extra unramified singular branches exist.

**Dual geometry.** Cancellation of the common factor in the displayed cross product yields the extended Gauss parametrization
\[
\gamma(u)=[4u^3-1:2u^2:-u^4].
\]
In every characteristic other than two it is a degree-four morphism to its image with rational inverse
\[
u=\frac{\gamma_1}{2\gamma_2}-\frac{\gamma_2}{8\gamma_3},
\]
under the usual coordinate convention for \(\gamma_1,\gamma_2,\gamma_3\). Thus its image is a quartic, and the Gauss map is birational; the rational identity holds in all such characteristics, including three. In characteristic two, the map reduces to \([1:0:u^4]\), whose image is the line defined by its second dual coordinate, with purely inseparable parameter degree four. Consequently all such tangent lines pass through \([0:1:0]\).

## Verification
Run `python verify_exact.py` with SymPy. It checks the integral implicit equation, tangent factorization, Gauss inverse, the local order identities in characteristics two and three, and the characteristic-two reduced equation and Gauss line. The genus/semigroup and normalization arguments above supply the proof over algebraic closures; a finite-field sample is not used to infer these conclusions.

## Relationship to prior work
Koras--Palka (first public version May 27, 2019) proved uniqueness over \(\mathbb C\), supplied precisely the integral equation and parametrization, and described the four complex cusps. Those facts are prior work. The new assertion concerns *all characteristic specializations* of that specified integral model and, in particular, the collision of three cusps in characteristic three and the inseparable line-valued Gauss map in characteristic two. Chen--Contreras studied strange curves in positive characteristic in a different degree-and-family setting; the definition of strangeness is standard, but their general theory is not asserted to be new here.

## Limitations
This is not a classification of all plane quintics with the displayed singularity profiles in positive characteristic. Other integral models of the same complex curve may specialize differently. A published unindexed calculation of these particular reductions cannot be excluded. No independent external mathematical audit has been performed.

## References
1. M. Koras and K. Palka, *Complex planar curves homeomorphic to a line have at most four singular points*, arXiv:1905.11376, first version May 27, 2019, Theorem 1.1 and Example 5.13, https://arxiv.org/abs/1905.11376.
2. Q. Chen and R. Contreras, *Plane \(\mathbb A^1\)-curves on the complement of strange rational curves*, arXiv:2108.09024, August 20, 2021, https://arxiv.org/abs/2108.09024.
