# Exact cylinder shadow mixed moment and sharp positive covariance

## Finding

Let \(K(r,h)=\{(u,v,z)\in\mathbb R^3:u^2+v^2\le r^2,\ |z|\le h/2\}\), where \(r,h>0\). Choose a plane through the origin according to Haar probability on the Grassmannian and let \(A\) and \(P\) be the Euclidean area and perimeter of the orthogonal shadow of \(K(r,h)\) in that plane. Put
\[
I=\int_0^1\sqrt{1-x^2}\,E(1-x^2)\,dx,
\qquad C=\frac23-\frac{\pi^2}{16},
\qquad B=2\pi\left(\frac13-\frac{\pi}{8}\right)+8\left(I-\frac{\pi^3}{32}\right),
\]
where \(E(m)=\int_0^{\pi/2}\sqrt{1-m\sin^2\varphi}\,d\varphi\) is the complete elliptic integral of the second kind with **parameter** \(m\). Then
\[
\boxed{\mathbb E[AP]=\frac{8\pi}{3}r^3+\left(\frac{2\pi}{3}+8I\right)r^2h+\frac83rh^2}
\]
and, for every \(r,h>0\),
\[
\boxed{\operatorname{Cov}(A,P)=r^3\left[4C\left(\frac hr\right)^2+B\frac hr+4\pi C\right]>0.}
\]
At fixed radius \(r\), this covariance is minimized at the **unique** aspect ratio
\[
\boxed{\frac hr=t_*=-\frac{B}{8C}=1.68126868048556\ldots,\qquad
\min_{h>0}\operatorname{Cov}(A,P)
=r^3\left(4\pi C-\frac{B^2}{16C}\right)
=0.06275436161117\ldots\,r^3.}
\]
The minimum coefficient is sharp and strictly positive. These statements concern the same randomly oriented shadow, not independently sampled orientations for its two measurements.

## Assumptions and scope

The cylinder is solid, right, circular, and nondegenerate; the ambient and projected spaces are Euclidean of dimensions three and two. A uniformly random plane means Haar-uniform normal direction, with opposite normals identified. All expectations use this normalization. The perimeter is the actual boundary length of the planar convex shadow, including straight and elliptic arcs; no ellipse-perimeter approximation is made. At fixed \(r\), \(h\) ranges over all positive real values. No assertion is made for oblique or elliptic cylinders, biased direction distributions, or arbitrary convex bodies.

## Proof

**Shadow decomposition.** Write \(x=|\langle U,e_3\rangle|\), where \(U\) is a Haar-uniform spherical unit normal, and \(y=\sqrt{1-x^2}\). Then \(x\) is uniform on \([0,1]\). The projected base disk is an ellipse with semiaxes \(r\) and \(rx\); the projected axial segment has length \(hy\) along the minor-axis direction. Projection commutes with Minkowski addition. Adding that segment increases area by its length times the ellipse's width perpendicular to the segment, namely \(2rhy\), and increases perimeter by twice its length (Cauchy's perimeter formula). Thus, with \(J(x)=E(1-x^2)\),
\[
A(x)=\pi r^2x+2rhy,\qquad P(x)=4rJ(x)+2hy. \tag{1}
\]
These formulas include both endpoint orientations by continuity.

**Needed expectations.** Elementary beta integrals give
\[
\mathbb E x=\frac12,\quad \mathbb E y=\frac\pi4,
\quad\mathbb E[xy]=\frac13,\quad\mathbb E[y^2]=\frac23.\tag{2}
\]
Cauchy's planar perimeter formula, averaged over Haar planes and then Haar lines within each plane, gives \(\mathbb E[4J(x)]=\pi\,\mathbb E[2\sqrt{1-Z^2}]=\pi^2/2\), with \(Z\) uniform on \([0,1]\). Hence \(\mathbb EJ=\pi^2/8\). Furthermore, reversing the two integrals and writing \(c=\cos\varphi\),
\[
\mathbb E[xJ(x)]
=\int_0^{\pi/2}\!\int_0^1 x\sqrt{c^2+(1-c^2)x^2}\,dx\,d\varphi
=\frac13\int_0^{\pi/2}\left(c+\frac1{1+c}\right)d\varphi
=\frac23.\tag{3}
\]
Finally \(\mathbb E[yJ(x)]=I\) by definition. Consequently,
\[
\mathbb EA=\frac\pi2r(r+h),\quad
\mathbb EP=\frac12(\pi^2r+\pi h),\tag{4}
\]
and multiplication of (1), followed by (2)--(3), gives the stated formula for \(\mathbb E[AP]\). Subtracting the product in (4) yields the claimed covariance polynomial and its coefficients \(B,C\).

**Rigorous strict positivity.** We give a rational sign certificate, rather than infer positivity from plotted values. Expand \(E(1-x^2)\) in its absolutely convergent hypergeometric series and integrate term by term:
\[
I=\frac{\pi^2}{8}\sum_{n=0}^\infty t_n,
\qquad t_0=1,\quad
\frac{t_{n+1}}{t_n}=\frac{(n-1/2)(n+1/2)(n+3/2)}{(n+1)^2(n+2)}.\tag{5}
\]
Every term after \(t_0\) is negative. To bound the tail, let \(p_n=(1/2)_n/n!=\binom{2n}{n}/4^n\); induction gives \(p_n^2\le1/(n+1)\). For \(n\ge1\), the coefficient of (5) satisfies
\[
|t_n|=\frac{p_n^2}{2n-1}\frac{2n+1}{n+1}p_n
\le\frac{2}{n^{5/2}}.
\]
Therefore, with \(S_{144}=\sum_{n=0}^{144}t_n\),
\[
S_{144}-\frac{1}{1296}<\sum_{n=0}^\infty t_n<S_{144}.\tag{6}
\]
The finite sum is rational. Compute it with the recurrence in (5), bound \(\pi\) using the alternating Taylor sums of Machin's identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\), and use (6). Exact rational comparisons give
\[
0.930<I<0.933,\qquad C>0.0498,\qquad -0.69<B<-0.65,\qquad\pi>3.14.\tag{7}
\]
In particular, the quadratic's discriminant is strictly negative, since
\[
B^2<(0.69)^2=0.4761
<64(3.14)(0.0498)^2<64\pi C^2.
\]
Its leading coefficient \(4C\) is positive. This proves strict covariance positivity for all real \(h/r\), hence in particular for all positive cylinder heights.

**Sharp minimizer.** Because \(B<0<C\), the unique vertex of the quadratic on \((0,\infty)\) is \(t_*=-B/(8C)>0\). Completing the square gives
\[
\operatorname{Cov}(A,P)=r^3\left[
4C(t-t_*)^2+4\pi C-\frac{B^2}{16C}\right],\qquad t=h/r.
\]
The previous strict discriminant bound proves the displayed sharp positive minimum and equality condition.

## Verification

The standalone `verify.py` re-evaluates the \(144\)-term rational recurrence, proves the tail and coefficient inequalities using exact fractions and Machin's alternating arctangent bounds, and checks all discriminant comparisons using integers. It also performs independent two-variable quadrature of the geometric formulas for four aspect ratios, plus actual polygonal orthogonal shadows of finely sampled cylinders at fifteen parameter combinations. Run from the extracted package directory using `python3 verify.py`. The numerical checks confirm the analytic formulas within stated tolerances; the positivity claim follows from the rational inequalities, not from the experiments.

## Relationship to prior work

Finch's 2012 analysis of planar projections tabulates mixed shadow-area/perimeter moments for regular tetrahedra, cubes and crosspolytopes and notes differing correlation signs. Finch's Section 5 already contains the **same weighted elliptic integral** (in the second moment of the cube-shadow perimeter); the integral itself and its hypergeometric representation are not claimed new. The distinct right-cylinder cross moment and sharp all-aspect covariance theorem do not follow from that cube calculation. Kim--Yaskin--Zvavitch (2015) study distribution functions of projection **volumes** and related comparison questions without the joint area--perimeter cylinder statistic. Cauchy's classical projection and perimeter formulas underlie the reductions but do not by themselves imply the sign of the cross-covariance, the elliptic integral \(I\), or the sharp minimizing aspect ratio. The mathematical comparisons concern the implications of the inspected results, not novelty inferred from absent keywords.

## Limitations

The theorem does not assert positivity for all zonoids or centrally symmetric bodies and does not determine joint densities of \((A,P)\). The exact coefficient \(I\) is given by a convergent special-function integral/series, not an elementary constant. Approximate decimal values are informational; rigorous positivity is certified by (5)--(7). The originality comparison is based on the specified inspected literature and research records; an earlier equivalent calculation outside these sources cannot be excluded. Independent audit has not been performed.

## References

1. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1, first public 12 March 2012, https://arxiv.org/html/1203.2464v1 .
2. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, first public 22 December 2015, https://arxiv.org/html/1512.07289v1 .
3. Cauchy's planar perimeter formula, e.g. E. Weisstein, *Cauchy's Perimeter Formula*, MathWorld, https://mathworld.wolfram.com/CauchysPerimeterFormula.html .
