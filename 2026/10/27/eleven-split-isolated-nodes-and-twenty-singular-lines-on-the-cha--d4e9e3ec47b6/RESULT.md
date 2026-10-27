# Eleven split isolated nodes and twenty singular lines on the characteristic-three Barth–Nieto quintic

## Finding
Let \(k=\overline{\mathbb F}_3\), and write \(e_j\) for the elementary symmetric function of degree \(j\) in six variables \(X_0,\ldots,X_5\). The coefficientwise special fibre of the six-coordinate Barth–Nieto model is
\[
N=V(e_1,e_5)\subset\mathbb P^5_k.
\]
Its **complete reduced geometric singular locus** consists of the twenty lines
\[
L_I=V(e_1,\,X_i\ (i\in I)),\qquad I\subset\{0,1,2,3,4,5\},\quad |I|=3,
\]
and eleven points disjoint from these lines: the all-ones point \(E=[1:1:1:1:1:1]\) and the ten projective sign points with three signs \(+1\) and three signs \(-1\). The latter are indexed by complementary three-subsets and so form ten, not twenty, distinct projective points. Every one of these eleven isolated singularities is an ordinary three-dimensional double point. All components and points are rational over \(\mathbb F_3\).

The lines form an incidence configuration of fifteen rational intersection points, with four lines through each intersection and three intersections on each line. Each line contains one further \(\mathbb F_3\)-rational point. Thus
\[
\#\operatorname{Sing}(N)_{\rm red}(\mathbb F_3)=15+20+11=46,
\qquad \#N(\mathbb F_3)=91.
\]

## Assumptions and scope
The base field has characteristic exactly three. Singularities are computed for the complete intersection with \(e_1\) a smooth linear equation, so singular points are those where the six partial derivatives of \(e_5\) are equal. Here an ordinary double point means that, after passing to an affine four-dimensional chart in \(e_1=0\), the nonzero quadratic tangent term has full rank four. Only the **reduced** singular support is classified; the structure of the nonreduced Jacobian scheme along the twenty lines is not determined.

## Proof
**Jacobian reduction.** Put \(g_i=\partial e_5/\partial X_i=e_4(X_0,\ldots,\widehat{X_i},\ldots,X_5)\). Because \(de_1=(1,\ldots,1)\), a point of \(N\) is singular exactly when \(g_0=\cdots=g_5\).

**Coordinate-stratum exhaustion.** If three or more coordinates vanish then \(e_1=e_5=0\) precisely for points supported on at most three coordinates with coordinate sum zero; all \(g_i\) vanish since each term of degree four uses four distinct variables. Such points are exactly the union of the twenty displayed lines. If exactly two coordinates vanish, the derivatives with respect to either zero coordinate equal the nonzero product of the remaining four coordinates, while derivatives with respect to a nonzero coordinate vanish. Such points are smooth. Exactly one zero coordinate is impossible on \(e_5=0\), because there \(e_5\) is the nonzero product of the other five coordinates. Therefore these lines account for all zero-coordinate singularities, over the whole algebraic closure.

**Nonzero-coordinate exhaustion.** Suppose all six coordinates are nonzero, and put \(P=\prod_i X_i\), \(S=\sum_iX_i^{-1}\). Then \(e_5=PS\). On \(N\) we have \(S=0\), and thus \(g_i=-P/X_i^2\). Equality of all \(g_i\) is equivalent to equality of all \(X_i^2\). After projective scaling the six coordinates are in \(\{+1,-1\}\). The equation \(e_1=0\) says that the number \(m\) of plus signs satisfies \(2m-6=0\) in characteristic three, so \(m\in\{0,3,6\}\). The cases \(m=0\) and \(m=6\) give the single point \(E\); the case \(m=3\) gives ten points after quotienting the twenty sign vectors by projective negation. All obey \(S=0\) and so lie in \(N\).

**Ordinary quadratic germs.** Let \(x\) be any one of the eleven nonzero-coordinate points, with each coordinate \(\pm1\). Along the tangent hyperplane \(H=\{\sum_i u_i=0\}\), the first derivative of \(S\) is \(dS(u)=-\sum_i u_i/x_i^2=-\sum_i u_i=0\). Since \(S(x)=0\), the Hessian of \(PS=e_5\) restricted to \(H\) is \(2P(x)\sum_i u_i^2/x_i^3\). Its associated bilinear form has radical inside \(H\) equal to the projective radial line \(kx\): indeed, its diagonal matrix has inverse proportional to \(\mathrm{diag}(x_i^3)\), and \(x_i^3=x_i\) for signs, so the orthogonal complement of \(H\) is exactly \(kx\). The induced form on \(H/kx\), of dimension four, is nondegenerate; because the characteristic is odd, these singularities are ordinary double points. Direct affine-chart Hessian determinants are \(2\) at \(E\) and \(1\) at a representative with three negative coordinates, as independently checked.

**Incidence and rational points.** Distinct lines intersect exactly when at least four coordinates vanish. Their common points have exactly four vanishing coordinates and remaining coordinates \((a,-a)\), giving \(\binom64=15\) intersections. Exactly four lines pass through each such point, and each of the twenty lines contains three such points. A line is a projective line over \(\mathbb F_3\), hence has four rational points: the fourth is the point where the three potentially nonzero coordinates are all equal (their sum vanishes in characteristic three). These twenty additional rational points are distinct, proving \(15+20+11=46\). An exhaustive projectively normalized enumeration of the \(\mathbb F_3\)-points of the hyperplane \(e_1=0\), using \(e_5=0\), yields exactly \(91\) points on \(N\); the bundled checker independently reproduces this finite count. The geometric singular-locus classification does not rely on that enumeration.

## Verification
Execute the bundled standalone file `barth_nieto_char3_checker.py` using Python 3. It enumerates all \(121\) projective points of \(e_1=0\) over \(\mathbb F_3\), checks \(e_5\) and the six gradients, compares the \(46\) singular points against the predicted zero-coordinate and sign strata, and computes Hessian determinants \(2\) and \(1\) in independent affine charts. A successful run prints `CHECK_OK` twice. This finite check corroborates, but does not substitute for, the algebraic-closure proof above.

## Relationship to prior work
Barth and Nieto introduced the quintic over characteristic zero. Hulek, Spandaw, van Geemen and van Straten (2001, Section 1) record the classical twenty singular lines and ten Segre ordinary nodes; they discuss point counts at good primes and exclude the bad prime three in their modularity comparison. Gritsenko and Hulek (1998) study the related modular form and Calabi–Yau model, not this coefficientwise characteristic-three singular classification. Hulek, Nieto and Sankaran (1997) supply an earlier day-verified public source on the same quintic. The twenty lines, their fifteen intersections, and the ten sign points are classical ingredients; the characteristic-three extra diagonal ordinary node and the complete special-fibre rational incidence are the distinguishing assertions here.

## Limitations
This identifies the reduced singular locus, not its nonreduced Jacobian thickening on any line, and it does not construct semistable reduction or a resolution in characteristic three. The formula for \(91\) points concerns only \(\mathbb F_3\), not an all-extension-field zeta function. The full original 1994 Barth–Nieto publication was not inspected; equivalent historical coverage remains possible. No independent scientific audit has been performed.

## References
1. K. Hulek, I. Nieto and G. K. Sankaran, *Heisenberg-invariant Kummer surfaces*, arXiv:alg-geom/9712025 (first posted 1997-12-19), https://arxiv.org/abs/alg-geom/9712025.
2. V. Gritsenko and K. Hulek, *The Modular Form of the Barth-Nieto Quintic*, arXiv:math/9806011 (posted 1998-06-03), https://arxiv.org/abs/math/9806011.
3. K. Hulek, J. Spandaw, B. van Geemen and D. van Straten, *The modularity of the Barth–Nieto quintic and its relatives*, Advances in Geometry 1 (2001), 263–289, especially Section 1.
4. W. Barth and I. Nieto, *Abelian surfaces of type (1,3) and quartic surfaces with 16 skew lines*, Journal of Algebraic Geometry 3 (1994), 173–222 (original full text not independently inspected).
