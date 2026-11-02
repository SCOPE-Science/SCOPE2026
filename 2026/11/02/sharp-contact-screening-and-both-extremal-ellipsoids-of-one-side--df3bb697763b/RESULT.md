# Sharp contact screening and both extremal ellipsoids of one-sided cross-polytopes

## Finding

For every integer \(n\ge3\) and every \(a\ge1\), let
\[
P_{n,a}=\operatorname{conv}\{-e_1, a e_1,\pm e_2,\ldots,\pm e_n\}\subset\mathbb R^n.
\]
The unique largest-volume inscribed (John) and smallest-volume containing (Löwner) Euclidean ellipsoids admit exact formulas in all dimensions and for every spike length. Both have the form
\[
E(c,b,r)=\left\{x:\frac{(x_1-c)^2}{b^2}+\frac{\sum_{j=2}^n x_j^2}{r^2}\le1\right\},\qquad b,r>0.
\]

**John ellipsoid.** When \(a=1\), it is \(E(0,1/\sqrt n,1/\sqrt n)\). For \(a>1\) define
\[
B=\frac{2na}{a-1}-(a-1),\quad
c_J=\frac{\sqrt{B^2+4a(n+1)}-B}{2(n+1)},\quad
b_J^2=\frac{(a-c_J)(1+c_J)}n,\quad
r_J^2=\frac{1-2c_J/(a-1)}{n-1}.
\]
Then \(E(c_J,b_J,r_J)\) is the unique John ellipsoid. Every one of the \(2^n\) simplex facets of \(P_{n,a}\) is tangent to this ellipsoid, for every \(a\ge1\).

**Löwner ellipsoid.** Let \(a_*=(n+1)/(n-1)\). Its unique containing ellipsoid is
\[
(c_L,b_L,r_L)=
\begin{cases}
\left((a-1)/2,(a+1)/2,(a+1)/(2\sqrt a)\right),&1\le a\le a_*,\\
\left(a/(n+1),na/(n+1),n/\sqrt{n^2-1}\right),&a\ge a_*.
\end{cases}
\]
For \(1\le a\le a_*\), **all** \(2n\) vertices touch this ellipsoid. For \(a>a_*\), precisely the \(2n-1\) vertices other than \(-e_1\) touch; \(-e_1\) lies strictly inside. Thus the optimum drops a genuine vertex at the sharp threshold even though the John ellipsoid continues to touch every facet.

Writing \(V_L(a)\) for the Löwner ellipsoid's volume, \(\log V_L(a)\) is continuously differentiable but not twice differentiable at \(a_*\), with the exact one-sided jump
\[
(\log V_L)''(a_*^-)-(\log V_L)''(a_*^+)
=\frac{(n-1)^3}{4n(n+1)}>0.
\]
The volume ratio satisfies \(V_L(1)/V_J(1)=n^{n/2}\) and
\[
\lim_{a\to\infty}\frac{V_L(a)}{V_J(a)}
=\frac{n^n}{(n-1)^{(n-1)/2}}.
\]

## Assumptions and scope

The ambient inner product is the standard Euclidean one; volume is ordinary \(n\)-dimensional Lebesgue volume. All ellipsoids, not merely axisymmetric ellipsoids, are eligible in the optimization problems. The theorem's main all-dimensional classification is stated for \(n\ge3\); the same formulas remain true for \(n=2\), but the planar case falls under classical quadrilateral-ellipse geometry and is not claimed as a novel standalone result. The parameter \(a\ge1\) replaces only the positive first-coordinate vertex of the regular cross-polytope. The polar with respect to the origin is the off-center box \([-1,1/a]\times[-1,1]^{n-1}\), which motivates this canonical family of nonsymmetric polars of coordinate boxes.

## Proof

**1. Facets and the inscribed ellipsoid.** For \(\epsilon=(\epsilon_2,\ldots,\epsilon_n)\in\{\pm1\}^{n-1}\), the complete irredundant facet inequalities are
\[
\frac{x_1}{a}+\sum_{j=2}^n\epsilon_j x_j\le1,
\qquad
-x_1+\sum_{j=2}^n\epsilon_j x_j\le1.
\]
An ellipsoid \(E(c,b,r)\) is contained in \(P_{n,a}\) precisely when
\[
\frac ca+\sqrt{\frac{b^2}{a^2}+(n-1)r^2}\le1,
\qquad
-c+\sqrt{b^2+(n-1)r^2}\le1.
\]
At \(a=1\), the proposed ball satisfies both inequalities with equality and its symmetric facet-contact distribution has normalized covariance \(I_n/n\).

Assume \(a>1\). Define the polynomial
\[
Q(t)=(n+1)t^2+\left(\frac{2na}{a-1}-(a-1)\right)t-a.
\]
It has exactly one positive root \(c=c_J\); indeed \(Q(0)=-a<0\) and \(Q((a-1)/2)=(n-1)(a+1)^2/4>0\). Consequently \(0<c<(a-1)/2\), so the stated \(b,r\) are positive. The equation \(Q(c)=0\) is equivalent to
\[
b^2=c^2+\frac{2ac}{a-1}=\frac{(a-c)(1+c)}n.
\]
The defining relation for \(r\) then gives
\[
b^2+(n-1)r^2=(1+c)^2,\qquad
\frac{b^2}{a^2}+(n-1)r^2=(1-c/a)^2.
\]
Thus every facet-support inequality is attained with equality, and the proposed ellipsoid is inside the body.

Apply \(x=(c,0,\ldots,0)+\operatorname{diag}(b,r,\ldots,r)u\) to send the proposed ellipsoid to the unit ball. Its \(2^n\) facet tangencies have unit-ball coordinates
\[
u_+^\epsilon=\left(\frac b{a-c},\frac{ar}{a-c}\epsilon\right),
\qquad
u_-^\epsilon=\left(-\frac b{1+c},\frac r{1+c}\epsilon\right).
\]
Assign total mass \(p_+=(a-c)/(a+1)\) to the positive-facet orbit and \(p_-=(1+c)/(a+1)\) to the negative-facet orbit, spread equally across signs within each orbit. Both masses are positive and sum to one. The axial mean is
\[
p_+\frac b{a-c}-p_-\frac b{1+c}=0,
\]
and the axial second moment is
\[
p_+\frac{b^2}{(a-c)^2}+p_-\frac{b^2}{(1+c)^2}
=\frac{b^2}{(a-c)(1+c)}=\frac1n.
\]
All mixed moments vanish by sign symmetry. Since every contact vector has unit norm, all \(n-1\) equal transverse diagonal second moments are likewise \(1/n\). Thus these contacts have mean zero and covariance \(I_n/n\). John's contact characterization (multiply probabilities by \(n\)) proves **global**, unrestricted maximum-volume optimality and uniqueness. It also proves the assertion about every facet.

**2. Containing ellipsoid, lower regime.** Suppose \(1\le a\le a_*\). Take \(c=(a-1)/2\), \(b=(a+1)/2\), and \(r=(a+1)/(2\sqrt a)\). The pole vertices map to \(+e_1\) and \(-e_1\); each equatorial vertex \(\pm e_j\), \(2\le j\le n\), maps to \((z,\pm e_j/r)\), where \(z=-c/b=-(a-1)/(a+1)\) and \(z^2+1/r^2=1\). Hence every vertex is on the ellipsoid and the whole polytope is contained.

Let
\[
q=\frac{n-1}{n(1-z^2)},\qquad
w_+=\frac{1-q-qz}{2},\qquad
w_-=\frac{1-q+qz}{2}.
\]
For \(-1/n\le z\le0\), equivalently \(1\le a\le a_*\), these are nonnegative, sum to one together with \(q\), and \(w_-=0\) only at the right endpoint. Distribute total mass \(q\) uniformly over the \(2(n-1)\) equatorial points, and put masses \(w_+,w_-\) on the two poles (omit the zero-mass point at the endpoint). The mean is zero because \(w_+-w_-+qz=0\). The axial second moment is \(1-q+qz^2=1/n\), while each transverse second moment is \(q(1-z^2)/(n-1)=1/n\). All off-diagonal moments vanish. The Löwner contact criterion gives unrestricted optimality and uniqueness.

**3. Containing ellipsoid, upper regime.** For \(a\ge a_*\), take \(c=a/(n+1)\), \(b=na/(n+1)\), \(r=n/\sqrt{n^2-1}\). The positive pole maps to \(+e_1\), while the equatorial points map to \((-1/n,\pm e_j/r)\), all on the unit sphere. The negative pole lies in or on the sphere because
\[
\frac{1+c}{b}=\frac{a+n+1}{na}\le1
\quad\Longleftrightarrow\quad a\ge a_*.
\]
It lies strictly within the sphere for \(a>a_*\). A contact probability distribution of mass \(1/(n+1)\) at the positive pole and total mass \(n/(n+1)\) uniformly over the \(2(n-1)\) equatorial contacts has zero mean and covariance \(I_n/n\). This proves unrestricted optimality and uniqueness again. Both formulas coincide at \(a_*\), and the explicit strict containment proves the stated sharp contact screening.

**4. Volume regularity and limiting ratio.** The volume of \(E(c,b,r)\) is \(\kappa_n br^{n-1}\), where \(\kappa_n\) is the unit-ball volume. Thus the two branches of \(\log(V_L/\kappa_n)\) are
\[
n\log\frac{a+1}{2}-\frac{n-1}{2}\log a,
\qquad
\log\frac{na}{n+1}+(n-1)\log\frac n{\sqrt{n^2-1}}.
\]
They and their first derivatives agree at \(a_*\). Their second derivatives differ by \((n-1)^3/[4n(n+1)]\), as claimed. At \(a=1\), the John radius is \(1/\sqrt n\) and the Löwner radius is \(1\), giving \(n^{n/2}\). As \(a\to\infty\), the John parameters satisfy \(c_J/a\to1/(n+1)\), \(b_J/a\to1/(n+1)\), and \(r_J\to1/\sqrt{n+1}\), whereas \(b_L/a\to n/(n+1)\) and \(r_L=n/\sqrt{n^2-1}\); multiplying semiaxis ratios gives the stated limiting volume ratio. This completes the proof.

## Verification

The complete standalone script `VERIFY.py` evaluates the facet containment, unit-sphere contact equations, zero first moments, and identity covariance for both ellipsoids in 216 deterministic test configurations across dimensions \(2\) through \(10\). It also runs 40 pairs of numerical constrained optimizations as independent cross-checks inside the symmetry-reduced parameter family. A passing run reports maximum moment/constraint error below \(2\times10^{-13}\), and maximum log-volume discrepancy below \(6\times10^{-15}\). The finite computations are corroboration: global optimality follows from the exact contact identities and the general ellipsoid contact theorem, not from numerical optimization.

Reproduce with `python VERIFY.py` in an environment with Python 3 and SciPy. Symbolic identities used in the proof have been checked independently by direct expansion; the proof itself lists the identities needed to verify them without software.

## Relationship to prior work

The general contact decomposition is classical; the specific theorem and its all-dimensional parameters do not follow merely from the existence/uniqueness statement or the general criterion. Henk's 2012 chapter gives the precise global optimality condition, which is applied here to an explicit nonsymmetric one-point deformation. Horwitz's 2003 and 2007 investigations cover ellipses of inscribed/circumscribed quadrilaterals in dimension two, and therefore limit any novelty assertion about the planar specialization. A diagonally capped hypercube and a cube enlarged by one axial vertex have different vertices, facets, and supporting constraints; neither of their reported classifications gives the one-sided cross-polytope formulas by specialization. The distinguishing result here is the simultaneous classification of both ellipsoids in arbitrary dimension and the exact screening of precisely one extremal vertex at \(a_*\).

## Limitations

Historical priority remains subject to independent specialist checking; absence of a detected equivalent is not a proof of novelty. The theorem concerns one-axis perturbations of a regular cross-polytope and does not classify general nonorthogonal or multi-axis asymmetric bipyramids. The planar instance is related to already-developed quadrilateral ellipse theory and is not independently claimed as new. The numerical checks alone do not prove any universal statement, and the claimed uniqueness uses the cited exact contact characterization. Independent audit has not been performed.

## References

- M. Henk, *Löwner–John ellipsoids*, Documenta Mathematica Extra Volume ISMP (2012), 95–106, https://doi.org/10.4171/DMS/6/15 (full chapter https://ems.press/content/book-chapter-files/27356?nt=1).
- A. Horwitz, *The locus of centers of ellipses inscribed in quadrilaterals*, arXiv:math/0312403 (first public posting 2003-12-22), https://arxiv.org/abs/math/0312403.
- A. Horwitz, *Ellipses of minimal area and of minimal eccentricity circumscribed about a convex quadrilateral*, arXiv:0707.2092 (first public posting 2007-07-13), https://arxiv.org/html/0707.2092v1.
