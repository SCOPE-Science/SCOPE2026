# Nicollier's exterior-solution conjecture for the gravitational-center equation
## Finding
Let \(ABC\) be a nondegenerate Euclidean triangle, with \(a=BC\), \(b=CA\), and \(c=AB\). For a point \(P\) in the exterior of the closed triangle, write \(r_A=PA\), \(r_B=PB\), and \(r_C=PC\). Then
\[
\left(\frac{r_A+r_B+c}{r_A+r_B-c}\right)^{1/c},\qquad
\left(\frac{r_B+r_C+a}{r_B+r_C-a}\right)^{1/a},\qquad
\left(\frac{r_C+r_A+b}{r_C+r_A-b}\right)^{1/b}
\]
cannot all be equal.

This proves the exterior-solution conjecture stated by Grégoire Nicollier in 2015 for the distance equation defining the gravitational center \(X(5626)\).

## Assumptions and scope
The triangle is nondegenerate and is regarded as a closed convex subset \(T\subset\mathbb{R}^2\). “Exterior” means \(P\in\mathbb{R}^2\setminus T\). For such \(P\), strict triangle inequality gives \(r_B+r_C>a\), \(r_C+r_A>b\), and \(r_A+r_B>c\), so every displayed logarithm below is finite and positive.

For each side, let \(n_a,n_b,n_c\) be the outward unit normals to \(BC,CA,AB\), respectively. Define
\[
J_a=\log\!\left(\frac{r_B+r_C+a}{r_B+r_C-a}\right),\quad
J_b=\log\!\left(\frac{r_C+r_A+b}{r_C+r_A-b}\right),\quad
J_c=\log\!\left(\frac{r_A+r_B+c}{r_A+r_B-c}\right).
\]
The claim concerns only exterior solutions of Nicollier's equation. It does not change the already known existence and uniqueness of the interior gravitational center.

## Proof
We use two elementary lemmas.

First, if \(U,V\) are the endpoints of a segment of length \(\ell\), and \(P\) is not on that segment, then
\[
\int_{UV}\frac{ds}{|P-Q|}
=\log\!\left(\frac{PU+PV+\ell}{PU+PV-\ell}\right).
\]
To verify this, put the segment on a coordinate axis and integrate \(1/\sqrt{(x-x_0)^2+h^2}\). Endpoint evaluation gives a difference of inverse hyperbolic sines; rewriting each inverse hyperbolic sine as a logarithm and using \(PU^2=(x_U-x_0)^2+h^2\) and \(PV^2=(x_V-x_0)^2+h^2\) yields the displayed symmetric endpoint form. The collinear exterior case follows directly by integrating \(1/|x-x_0|\), or by a limit.

Consequently,
\[
J_a=\int_{BC}\frac{ds}{|P-Q|},\qquad
J_b=\int_{CA}\frac{ds}{|P-Q|},\qquad
J_c=\int_{AB}\frac{ds}{|P-Q|}.
\]

Second, define the inverse-distance field of the filled triangle by
\[
E(P)=\iint_T\frac{P-Q}{|P-Q|^3}\,dA(Q).
\]
Because \(P\) is exterior, this integral is absolutely convergent. Since
\[
\nabla_Q\frac1{|P-Q|}=\frac{P-Q}{|P-Q|^3},
\]
the planar divergence theorem, applied componentwise, gives
\[
E(P)=n_aJ_a+n_bJ_b+n_cJ_c.
\]
For a counterclockwise orientation of \(ABC\), rotating the three directed edge vectors by \(90^\circ\) to the right gives
\[
a n_a+b n_b+c n_c=0.
\]
Moreover, because the triangle is nondegenerate, this is the only linear relation among the three side normals up to a scalar multiple.

Suppose now that Nicollier's three quantities were equal at an exterior point. Taking logarithms gives
\[
\frac{J_a}a=\frac{J_b}b=\frac{J_c}c=\kappa
\]
for some \(\kappa>0\). Therefore
\[
E(P)=\kappa\bigl(a n_a+b n_b+c n_c\bigr)=0.
\]

This is impossible outside a convex triangle. Indeed, because \(P\notin T\) and \(T\) is compact and convex, strict separation provides a unit vector \(u\) and a number \(\delta>0\) such that
\[
u\mathbin{\cdot}(P-Q)\ge\delta
\]
for every \(Q\in T\). Hence
\[
u\mathbin{\cdot}E(P)
=\iint_T\frac{u\mathbin{\cdot}(P-Q)}{|P-Q|^3}\,dA(Q)>0,
\]
contradicting \(E(P)=0\). Thus no exterior solution exists.

## Verification
The proof is exact and does not use a numerical search. The critical checks are: the segment integral identity; the componentwise divergence-theorem conversion from the area field to the weighted side-normal sum; the polygonal balance \(a n_a+b n_b+c n_c=0\); and strict positivity of a separating component of \(E(P)\) for every exterior point.

A direct sign audit shows that the convention for \(E(P)\) is immaterial to the contradiction: reversing the global sign of the field reverses the separating component but cannot make it zero. Denominators in the logarithms are strictly positive in the exterior by triangle inequality.

## Relationship to prior work
Abraham and Kovač introduced the inverse-distance potential for a uniformly filled triangle and derived the same distance relation as a necessary condition for an interior stationary point. Their paper also proves directly that the field cannot vanish at an exterior point. Nicollier reformulated the interior solution through three focus-sharing ellipses and explicitly conjectured that the distance equation itself has no solution outside the triangle.

The missing implication is supplied here: for an exterior point, Nicollier's normalized logarithms are exactly normalized side integrals of the inverse-distance kernel, so their equality forces the full triangle field to vanish. The earlier interior derivation does not provide this exterior converse because it starts from an interior stationary point and uses a polar decomposition about that point.

Targeted searches for the exact conjecture, \(X(5626)\), exterior solutions, focus-sharing ellipses, and the boundary-integral formulation found no published statement resolving the exterior equation. General radial-center uniqueness results address the extremum of the potential, not the extra algebraic solutions of Nicollier's distance equation.

## Limitations
This result settles only the exterior-solution question for Nicollier's equation. It does not give a new closed form for the coordinates of \(X(5626)\), nor does it claim a new uniqueness theorem for radial centers of general convex bodies. The literature search cannot exclude an unindexed or differently phrased prior resolution.

## References
1. Grégoire Nicollier, “A Simple Dynamic Localization of the Gravitational Center of a Triangle,” Forum Geometricorum 15 (2015), 263–265. Publication date: 13 November 2015. Repository record: https://arodes.hes-so.ch/record/9807
2. Hrvoje Abraham and Vjekoslav Kovač, “From Electrostatic Potentials to Yet Another Triangle Center,” arXiv:1312.3176, first submitted 11 December 2013; Forum Geometricorum 15 (2015), 73–89. The manuscript lists primary MSC 51M04 and 51N20.
3. Irmina Herburt, “On the Uniqueness of Gravitational Centre,” Mathematical Physics, Analysis and Geometry 10 (2007), 251–259, doi:10.1007/s11040-007-9031-6.
