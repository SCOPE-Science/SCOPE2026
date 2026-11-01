# Sharp perimeter deficit for spherical convex hulls in an orthogonal wedge

## Finding
Let \(S^2=\{(x,y,z)\in\mathbb R^3:x^2+y^2+z^2=1\}\) have unit intrinsic curvature, and let \(W=\{(x,y,z)\in S^2:x\geq0,\ y\geq0\}\), the spherical lune of angle \(\pi/2\). For each integer \(n\geq3\), choose independent, normalized-surface-area-uniform points \(X_1,\ldots,X_n\) in \(W\). Write \(K_n=S^2\cap\operatorname{pos}\{X_1,\ldots,X_n\}\) for their spherical convex hull, and \(L_n\) for its intrinsic geodesic perimeter, counted once around the polygon.

Then the expected perimeter deficit from the lune boundary, whose length is \(2\pi\), obeys the **sharp asymptotic law**
\[
\lim_{n\to\infty}\sqrt n\bigl(2\pi-\mathbb E L_n\bigr)
=\frac\pi2 B\!\left(\frac34,\frac12\right)
=\frac{\pi^{3/2}\Gamma(3/4)}{2\Gamma(5/4)}
=3.764068559415685\ldots.
\]

In fact, there is an exact finite-sample representation. Define
\[
p(z,\theta)=\frac12+\frac{\arcsin(\sqrt{1-z^2}\cos\theta)+\arcsin(\sqrt{1-z^2}\sin\theta)}\pi,
\qquad -1\le z\le1,\quad0\le\theta<2\pi.
\]
Then \(0\le p(z,\theta)\le1\) and, for every integer \(n\geq3\),
\[
2\pi-\mathbb E L_n
=\int_{-1}^{1}\int_0^{2\pi}p(z,\theta)^n\,d\theta\,dz.
\]
The leading \(n^{-1/2}\) term comes from a one-dimensional arc of outward great-circle normals that contain the entire lune in a hemisphere. It contrasts with the logarithmic growth of the expected *number of sides* of the same random polygon.

## Assumptions and scope
The sample is independent and uniform with respect to spherical surface area on \(W\), not uniform Euclidean volume or uniform latitude. In the parametrization \((x,y,z)=(\sqrt{1-z^2}\cos\phi,\sqrt{1-z^2}\sin\phi,z)\), the sampling variables are independent with \(z\sim\operatorname{Unif}[-1,1]\) and \(\phi\sim\operatorname{Unif}[0,\pi/2]\). The spherical hull is the unit-sphere intersection of the positive cone of the sample; since \(x+y>0\) almost surely for all sample points, the hull lies inside an open hemisphere and has a well-defined simple polygonal boundary almost surely. Great-circle intersections passing through sample vertices are null events.

## Proof
**1. Crofton normalization.** For any nondegenerate geodesically convex spherical polygon \(K\) inside an open hemisphere, let \(G\) be a Haar-uniform unoriented great circle. An edge of geodesic length \(\ell<\pi\) is crossed by \(G\) with probability \(\ell/\pi\), by uniformity of the antipodal intersection pair on its supporting great circle. A generic \(G\) intersects the polygon boundary either twice or not at all. Summing the expected crossings over its edges therefore gives
\[
\operatorname{per}(K)=2\pi\Pr(G\cap K\ne\varnothing).
\]
Fix a unit normal \(u\) to \(G\), and write \(p(u)=\Pr(u\cdot X_1>0)\). The great circle hits \(K_n\) precisely when the sample contains points on both strict sides of \(G\). Thus, conditionally on \(u\), the hit probability is \(1-p(u)^n-(1-p(u))^n\). Uniform \(u\) and \(-u\) have the same distribution. Consequently
\[
2\pi-\mathbb E L_n=4\pi\mathbb E_u[p(u)^n].
\]

**2. Exact hemisphere fraction.** Represent an area-uniform point on \(S^2\) as the direction of a standard centered Gaussian vector \(Z\in\mathbb R^3\). Then the uniform distribution on \(W\) is obtained by conditioning on \(Z_1\ge0,Z_2\ge0\). For any unit \(u\), the centered Gaussian signs of \(Z_1,Z_2,u\cdot Z\) have pair correlations \(0,u_1,u_2\). The elementary bivariate Gaussian orthant identity
\(\mathbb E[\operatorname{sgn}(G)\operatorname{sgn}(H)]=(2/\pi)\arcsin\operatorname{Corr}(G,H)\), together with cancellation of all odd sign products, gives
\[
\Pr(Z_1\ge0,Z_2\ge0,u\cdot Z\ge0)
=\frac18+\frac{\arcsin u_1+\arcsin u_2}{4\pi}.
\]
Since \(\Pr(Z_1\ge0,Z_2\ge0)=1/4\),
\(p(u)=1/2+(\arcsin u_1+\arcsin u_2)/\pi\). Parameterizing the uniform normal as
\(u=(\sqrt{1-z^2}\cos\theta,\sqrt{1-z^2}\sin\theta,z)\), with surface element \(d\theta\,dz\), yields the asserted exact double integral.

**3. Uniform domination.** At fixed \(z\), the sum \(\arcsin u_1+\arcsin u_2\) is maximized for \(u_1=u_2=\sqrt{1-z^2}/\sqrt2\). Indeed, changing signs to positive can only increase it; if \(a,b\ge0\) and \(a^2+b^2=1-z^2\), then
\[
\cos(\arcsin a+\arcsin b)=\sqrt{z^2+a^2b^2}-ab
\]
is decreasing in \(ab\), which is maximized at \(a=b\). The maximal angle is \(\arccos(z^2)\). Hence, uniformly in \(\theta\),
\[
p(z,\theta)\le1-\frac{\arcsin(z^2)}\pi
\le\exp(-z^2/\pi).
\]
In particular, for \(z=t/\sqrt n\), \(p(z,\theta)^n\le\exp(-t^2/\pi)\), an integrable bound on the real line independent of \(n\) and \(\theta\).

**4. Boundary-layer asymptotic.** For fixed \(0<\theta<\pi/2\), Taylor expansion at \(z=0\) gives
\[
p(z,\theta)=1-\frac{z^2}{\pi\sin(2\theta)}+O_{\theta}(z^4).
\]
Thus for fixed real \(t\),
\(p(t/\sqrt n,\theta)^n\to\exp[-t^2/(\pi\sin(2\theta))]\). For \(\theta\notin[0,\pi/2]\), the value of \(p(0,\theta)\) is strictly less than one, so the same sequence tends to zero. The two endpoint longitudes have measure zero. Substitute \(z=t/\sqrt n\) into the exact finite-sample integral, extend the integrand by zero outside \(|t|\le\sqrt n\), and apply dominated convergence using the uniform Gaussian bound in step 3. This yields
\[
\begin{aligned}
\lim_{n\to\infty}\sqrt n(2\pi-\mathbb E L_n)
&=\int_0^{\pi/2}\int_{-\infty}^{\infty}
\exp\!\left(-\frac{t^2}{\pi\sin2\theta}\right)\,dt\,d\theta\\
&=\pi\int_0^{\pi/2}\sqrt{\sin2\theta}\,d\theta\\
&=\frac\pi2B\!\left(\frac34,\frac12\right),
\end{aligned}
\]
where the final equality follows from the Euler beta integral. This establishes the exact constant and the asymptotic equivalence without using a simulation or assuming a remainder expansion. \(\square\)

## Verification
Run `python3 verify.py` from this directory. The standalone checker numerically evaluates the **exact** great-circle integral, verifies the latitude bound on a mesh, and independently constructs spherical convex hull polygons by gnomonic projection for three finite sample sizes. Its executed output includes `ALL_CHECKS_PASSED`, the coefficient \(3.764068559416\), and the finite-sample scaled deficit near that constant at sample size \(2500\). All numerical checks are corroborative: the exact identity, domination, and limit are proved above and do not depend on discretization or random trials.

## Relationship to prior work
Besau, Gusakova, Reitzner, Schütt, Thäle, and Werner (2022, arXiv:2203.07916v1) introduced and studied precisely this orthogonal spherical-wedge sampling model. Their principal two-dimensional result concerns the expected number of polygon edges, asymptotic to \((4/3)\log n\); the inspected introduction, theorem, and supporting sections do not evaluate the perimeter deficit or its sharp constant. Bárány, Hug, Reitzner, and Schneider (2015, arXiv:1505.04672v1) proved Crofton/mean-width formulas and surface-area asymptotics for the **hemisphere** model. Their halfsphere result is not the orthogonal-wedge asymptotic, and its Crofton mechanism is used here with attribution. The finite-sample integral is a specialized application of established integral geometry; the evaluated degenerate boundary-layer law and beta constant are the claimed contribution.

## Limitations
The theorem treats the curvature-one two-sphere, orthogonal two-hemisphere wedge, independent normalized-area samples, and expected geodesic perimeter. It asserts a first-order sharp limit but not an explicit next term or a limit distribution for the random perimeter. It does not cover other lune angles, higher-dimensional wedges, or nonuniform sampling. Historical priority beyond the inspected accessible literature remains provisional; older spherical integral-geometric literature has not been exhaustively searched. Independent mathematical audit is not claimed.

## References
1. F. Besau, A. Gusakova, M. Reitzner, C. Schütt, C. Thäle, E. M. Werner, *Spherical convex hull of random points on a wedge*, arXiv:2203.07916v1, first publicly posted 2022-03-15; subsequently *Mathematische Annalen*, DOI 10.1007/s00208-023-02704-9. https://arxiv.org/abs/2203.07916
2. I. Bárány, D. Hug, M. Reitzner, R. Schneider, *Random points in halfspheres*, arXiv:1505.04672v1, first publicly posted 2015-05-18; subsequently *Random Structures & Algorithms* 50 (2017), 3–22. https://arxiv.org/abs/1505.04672
