# Unique optimal two-sided disk approximation within rotationally symmetric disk-polygons

## Finding
Let \(K=\overline B_r(0)\), where \(0<r<1\), and let
\[
Q_{n,c}=\bigcap_{j=0}^{n-1}\overline B_1\!\left(c\left(\cos\frac{2\pi j}{n},\sin\frac{2\pi j}{n}\right)\right),\qquad n\ge3,\quad 0\le c<1.
\]
For arbitrary positive weights \(p,q\), define
\[
E_n(c)=p\,\operatorname{area}(K\setminus Q_{n,c})+q\,\operatorname{area}(Q_{n,c}\setminus K).
\]
Put \(h=\pi/n\), \(s=q/(p+q)\), and
\[
\rho(c,t)=\sqrt{1-c^2\sin^2t}-c\cos t,\quad
c_0=1-r,\quad c_1=\sqrt{1-r^2\sin^2h}-r\cos h.
\]
There is exactly one global minimizer \(c_n\) of \(E_n\) on \([0,1)\), and \(c_0<c_n<c_1\). It is uniquely characterized by
\[
\rho(c_n,\alpha_n)=r,\qquad
r\sin\alpha_n=s\rho(c_n,h)\sin h,\qquad 0<\alpha_n<h.
\]
For each fixed \(r,p,q\), as \(n\to\infty\),
\[
c_n=1-r+\frac{\pi^2r(1-r)s^2}{2n^2}+O_{r,p,q}(n^{-4}),
\]
\[
\min_{0\le c<1}E_n(c)=\frac{\pi^3r^2(1-r)(p+q)s(1-s^2)}{3n^2}+O_{r,p,q}(n^{-4}).
\]
At fixed \(n,r\), \(c_n\) is strictly increasing as a function of \(s\in(0,1)\), with one-sided endpoint limits \(c_0,c_1\).

## Assumptions and scope
All disks are *closed Euclidean disks*. \(\overline B_a(x)\) denotes the closed disk of radius \(a\) centered at \(x\). The optimization variable is only the common radius \(c\) of a *regularly spaced circle of centers* for \(n\) unit-disk translates. Simultaneous rotation of all centers is immaterial. The target is a concentric disk of radius strictly between zero and one; weights are strictly positive and independent of \(n\). The central geometry concerns finite intersections of equal circular disks and two-sided, not necessarily nested, area deviation.

## Proof
**1. Radial reduction.** For \(c<1\), the origin is interior to every generating unit disk. In the direction opposite a generating center, the ray meets that disk at radius \(\rho(c,t)\), where \(t\) is the angular separation from the opposite-center direction. Among the \(n\) generators, the most restrictive one is the center with the most negative angular scalar product with the ray. Consequently the radial boundary of the intersection is \(\rho(c,|t|)\) in every cell \(-h\le t\le h\). Direct differentiation or the defining quadratic relation
\[
\rho^2+2c\rho\cos t+c^2=1
\]
gives
\[
\rho_c=-\frac{\rho\cos t+c}{\rho+c\cos t}<0,\qquad
\rho_t=\frac{c\rho\sin t}{\rho+c\cos t}>0\quad(0<t\le h,c>0).
\]
Here all denominators are positive, because \(h\le\pi/3\) and \(\rho>0\). The polar area formula therefore gives the exact loss
\[
E_n(c)=n\int_0^h\!\left[p\bigl(r^2-\rho(c,t)^2\bigr)_++q\bigl(\rho(c,t)^2-r^2\bigr)_+\right]dt.
\]

**2. Localization.** If \(c\le c_0\), then \(\rho(c,0)\ge r\), so \(K\subseteq Q_{n,c}\). As \(c\) increases in this interval, \(\rho\) decreases strictly and the loss decreases strictly. Likewise \(\rho(c_1,h)=r\), and for \(c\ge c_1\) the inclusion \(Q_{n,c}\subseteq K\) holds, with loss strictly increasing in \(c\). The strict inequalities \(0<c_0<c_1<1\) follow from \(\rho(c_0,h)>r\) and \(\rho(1,h)<r\). Thus a global minimizer must lie in \((c_0,c_1)\).

**3. Exact derivative and uniqueness.** For \(c\in(c_0,c_1)\), there is exactly one angle \(\alpha(c)\in(0,h)\) at which \(\rho(c,\alpha(c))=r\); below this angle the approximant lies inside \(K\), above it outside. Differentiating the loss, with the crossing contributions canceling because the two integrands vanish at the crossing, and using the exact derivative identity
\[
-\rho\rho_c=\frac{\partial}{\partial t}\bigl(\rho(c,t)\sin t\bigr),
\]
yields
\[
E'_n(c)=2n\left((p+q)r\sin\alpha(c)-q\rho(c,h)\sin h\right).
\]
The angle \(\alpha(c)\) strictly increases with \(c\), because \(\rho_c<0\) and \(\rho_t>0\). Meanwhile \(\rho(c,h)\) strictly decreases. Hence
\[
H(c)=\frac{r\sin\alpha(c)}{\rho(c,h)\sin h}
\]
is a continuous strictly increasing bijection from \((c_0,c_1)\) onto \((0,1)\). The derivative has the sign of \(H(c)-s\), yielding the unique minimizer from \(H(c_n)=s\). This bijection also establishes strict dependence of \(c_n\) on the weight fraction \(s\), with the stated endpoint limits.

**4. Sharp asymptotics.** Write \(\delta=c_n-(1-r)\) and \(h=\pi/n\). First, \(0<\delta<c_1-c_0=O_r(h^2)\). For \(0\le t\le h\), Taylor's theorem, uniformly for such \(\delta\), gives
\[
\rho(c_n,t)=r-\delta+A t^2+O_r(h^4),\qquad A=\frac{r(1-r)}2>0.
\]
The exact stationarity identity and \(\rho(c_n,h)=r+O_r(h^2)\) imply
\[
\alpha_n=s h+O_{r,p,q}(h^3).
\]
The crossing identity consequently gives \(\delta=A s^2h^2+O_{r,p,q}(h^4)\), proving the expansion of \(c_n\).

For the optimal loss, substitute \(t=h x\) into the polar formula. Since \(r^2-\rho(c_n,hx)^2=2rAh^2(s^2-x^2)+O_{r,p,q}(h^4)\), and since the positive-part map is \(1\)-Lipschitz, the error caused by replacing the integrand by its quadratic approximation is \(O_{r,p,q}(n h^5)=O_{r,p,q}(n^{-4})\). The leading integral is
\[
2nrAh^3\left[p\int_0^1(s^2-x^2)_+\,dx+q\int_0^1(x^2-s^2)_+\,dx\right].
\]
Its bracket equals \((p+q)s(1-s^2)/3\) after using \(q=(p+q)s\). Since \(n h=\pi\), the claimed coefficient and remainder follow.

## Verification
The derivation supplies an infinite-\(n\) proof; finite numerical tests are supplemental. The standalone program `verify.py` computes the stationary root independently by bisection, checks its optimality against neighboring parameters, and compares scaled errors with the asymptotic coefficient for several radii and weight pairs. It requires only the Python standard library. Its computations cannot establish the general theorem on their own.

## Relationship to prior work
Basit and Lángi, *Dowker-type theorems for disk-polygons in normed planes*, arXiv:2307.04026, introduce weighted area deviation and leave its disk-polygonal sequence behavior as open questions (particularly Problems 2–3). The present result treats the precisely specified rotationally symmetric regular-center family, not the unrestricted optimum or sequence convexity. Nagy and Vígh, *Best and random approximations with generalized disc-polygons*, study one-sided inscribed and circumscribed approximations and associated sharp \(n^{-2}\) area asymptotics; these do not give the exact finite-\(n\) weighted two-sided critical equation. Public geometric records concerning circular-gap area or regular polygon approximation concern different single-sided or unweighted objects. The identity of the optimizing one-parameter disk intersection and the displayed two-sided constant require the additional crossing analysis above.

## Limitations
This theorem does **not** determine the best weighted approximation among arbitrary disk-\(n\)-gons, does **not** establish convexity of an unrestricted optimal-deviation sequence, and does **not** treat zero or infinite weights as part of the theorem. The asymptotic remainder is for fixed \(r,p,q\), not uniform at \(r=0\), \(r=1\), or degenerate weight limits. Priority has been examined against accessible primary papers and indexed descriptions, but inaccessible or unindexed work may contain related formulae. Independent mathematical review has not been performed.

## References
1. B. Basit and Z. Lángi, *Dowker-type theorems for disk-polygons in normed planes*, arXiv:2307.04026 (first public version: 8 July 2023), https://arxiv.org/abs/2307.04026 .
2. K. Nagy and V. Vígh, *Best and random approximations with generalized disc-polygons*, Discrete & Computational Geometry, DOI:10.1007/s00454-023-00554-5, author preprint https://www.math.u-szeged.hu/~vigvik/preprints/Lconvexapproximations.pdf .
3. F. Fodor, D. I. Papvári, and V. Vígh, *On random approximations by generalized disc-polygons*, Mathematika 66 (2020), 498–513, DOI:10.1112/mtk.12027 (different random model).
