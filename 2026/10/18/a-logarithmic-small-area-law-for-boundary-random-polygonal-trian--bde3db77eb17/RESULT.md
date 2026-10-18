# A logarithmic small-area law for boundary-random polygonal triangles

## Finding
Let \(K\) be a nondegenerate convex Euclidean polygon with \(m\ge3\) genuine sides, lengths \(\ell_i>0\) in cyclic order, and perimeter \(L=\sum_i\ell_i\). Its interior angle at the vertex joining sides \(i-1\) and \(i\) is \(\theta_i\in(0,\pi)\). For independent arclength-uniform points \(X,Y,Z\in\partial K\), let \(A=\operatorname{area}(\operatorname{conv}\{X,Y,Z\})\). Then
\[
\Pr(A=0)=\sum_{i=1}^m\left(\frac{\ell_i}{L}\right)^3,
\qquad
\Pr(0<A\le t)=C_Kt\log\frac{L^2}{t}+O_K(t),
\]
where
\[
C_K=\frac{12}{L^3}\sum_{i=1}^m\frac{\ell_{i-1}+\ell_i}{\sin\theta_i}.
\]
Consequently the positive part of the small-area distribution is of order \(t\log(1/t)\), not of order \(t\). The logarithm is dimensionless in the displayed normalization; replacing \(L^2\) by another fixed area changes only the remainder.

## Assumptions and scope
The polygon has no collinear consecutive sides: each \(\theta_i\) is strictly between zero and \(\pi\). All lengths are positive and the polygon is fixed while \(t\to0^+\). Sampling is independent, with uniform density \(1/L\) relative to total perimeter arclength. This theorem is not stated uniformly over degenerating polygon families. The area is nonnegative, and coincident points have probability zero except for the three points lying on one common supporting side, which creates a positive atom at zero.

## Proof
Call the edges \(e_1,\dots,e_m\) in boundary order. For three sampled points on one edge the triangle has zero area, and for distinct genuine supporting edges a random triple is collinear with probability zero. If precisely two samples lie on edge \(e\), and the third on a different edge \(f\), write \(d\) for the distance between the two uniform points on \(e\), and \(h_f(z)\) for the perpendicular distance of the third sample from the line supporting \(e\). The triangle area equals \(d h_f(z)/2\). Conditional on the edge choices, \(d\) and \(z\) are independent, and the difference of two independent uniform points on an interval of length \(a=|e|\) has density
\[
g_a(d)=\frac{2(a-d)}{a^2}\quad(0\le d\le a).
\]
If \(f\) is not incident to \(e\), then \(h_f\) is bounded below by a positive constant because \(K\) has genuine, exposed sides. Hence the conditional probability of \(0<A\le t\) is \(O_K(t)\).

Suppose \(f\) and \(e\) meet at a vertex of interior angle \(\theta\). Arclength \(z\) measured from that vertex along \(f\) is uniform on \([0,b]\), where \(b=|f|\), and \(h_f(z)=z\sin\theta\) exactly. With \(\varepsilon=2t/\sin\theta\), the conditional small-area probability is
\[
\frac1b\int_0^b\int_0^a \boldsymbol1_{dz\le\varepsilon}\frac{2(a-d)}{a^2}\,\mathrm d d\,\mathrm dz
=\frac{2\varepsilon}{ab}\log\frac{ab}{\varepsilon}+O_{a,b}(\varepsilon).
\]
To verify the last equality, integrate first in \(z\): \(\min(b,\varepsilon/d)/b\). Split the \(d\)-integral at \(d=\varepsilon/b\). The part below the split is \(O(\varepsilon)\), while above it the integrand is \(\varepsilon g_a(d)/(bd)\), whose \(2/a\) constant term integrates to the displayed logarithm and whose remaining part is \(O(\varepsilon)\). Thus this pair of incident edges contributes, after multiplying by the probability \(3a^2b/L^3\) of choosing two points on \(e\) and one on \(f\),
\[
\frac{12a}{L^3\sin\theta}\,t\log\frac{L^2}{t}+O_K(t).
\]
Every vertex has two ordered incident-edge choices (which edge holds the repeated samples), so their sum is exactly \(C_K\).

It remains to show that triples on three pairwise distinct edges contribute only \(O_K(t)\), and hence do not alter this logarithm. Fix three distinct edges and parameterize each by a variable in \([0,1]\). The signed doubled area of the three points, taken in their cyclic boundary order, is a nonnegative multi-affine function of those three variables. It is strictly positive in the interior of the cube, since a line meets the boundary of a strictly convex polygon in no more than two points apart from segments on a supporting side. Its zero configurations occur only on boundary loci where two points from incident edges coincide at their common vertex. Near such a locus, write \(u,v\ge0\) for the two arclength distances from that vertex and \(w\in[0,1]\) for the third coordinate. If the third edge is away from the vertex, and \(w\) stays in a compact subinterval of \((0,1)\), the area is bounded below by \(c(u+v)\), for some \(c>0\) depending on the edges. At an endpoint of the third edge, one of these first-order coefficients may vanish, but the positive multi-affine expression has locally the lower bound \(c(v+uw)\) or \(c(u+vw)\), after possibly replacing \(w\) by \(1-w\) and permuting variables. Indeed the coefficient of the remaining positive term is a nonzero triangular determinant of genuine polygon vertices; simultaneous vanishing of both first-order coefficients would force three distinct polygon vertices to be collinear or a third edge to contain the common vertex. In the first case the sublevel volume is \(O(t^2)\); in the second it is \(O(t^2\log(1/t))\), by integrating \(u w\le Ct\) and the independent variable bounded by \(Ct\). A finite cover of the compact zero locus, together with a positive minimum away from it, proves a uniform \(O_K(t^2\log(1/t))\) bound for this triple of distinct edges. Summing finitely many choices gives \(O_K(t)\), as required.

## Verification
The main constant was reconstructed by exact evaluation of the product integral. As a numerical diagnostic (not a proof), a seeded experiment with 2,400,000 independently generated triples on the unit-side equilateral triangle yielded \((\Pr(0<A\le t))/(t\log(1/t))\) estimates 2.650, 2.706, 2.730, and 2.775 at \(t=0.003,0.001,0.0003,0.0001\), respectively, consistent with slow logarithmic convergence to the analytic coefficient \(16/(3\sqrt3)=3.079201\ldots\). This last explicit coefficient is from the theorem and simplifies to \(16/(3\sqrt3)\) only if all three sides have length one. [See checker.py for the exact integral-coefficient and equilateral normalization identities; the checker is corroborative rather than an infinite proof.]

## Relationship to prior work
Maesumi, *Triangle Inscribed-Triangle Picking* (arXiv:1804.11007, first posted 2018-04-30), derives the complete area distribution when one independent point is selected from **each of three specified triangle sides**. It therefore excludes the repeated-edge configurations generating the logarithmic term here. Reitzner, Schütt, and Werner, *The convex hull of random points on the boundary of a simple polytope* (arXiv:1911.05917, first posted 2019-11-14), study expected face numbers and missed volume of the hull as sample size increases; they do not give this fixed-three-point lower-tail distribution. Published related work on short boundary distances and small circumradii concerns different observables. The comparison is based on the accessible full-text mathematical statements and methods, not merely title matches.

## Limitations
This is an asymptotic small-area law for each fixed genuine convex polygon; it is not a full probability density or a uniform stability bound over polygons nearing degeneracy. The proof does not assert the absence of unindexed earlier expressions of the same coefficient. The dimensional scale in the logarithm is conventional. Numerical finite-sample tests are auxiliary and never establish asymptotic limits.

## References
1. A. Maesumi, *Triangle Inscribed-Triangle Picking*, arXiv:1804.11007, 2018, https://arxiv.org/html/1804.11007v1.
2. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917, 2019, https://arxiv.org/abs/1911.05917.
3. M. Reitzner, C. Schütt, E. M. Werner, *Discrete & Computational Geometry* 69 (2023), 453–504, DOI 10.1007/s00454-022-00460-2 (later journal version of reference 2).
