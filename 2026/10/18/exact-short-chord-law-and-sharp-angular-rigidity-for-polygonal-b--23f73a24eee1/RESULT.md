# Exact short-chord law and sharp angular rigidity for polygonal boundaries

## Finding

Let \(K\subset\mathbb R^2\) be a nondegenerate convex polygon with \(m\ge3\) genuine corners, perimeter \(L>0\), interior angles \(\theta_1,\ldots,\theta_m\in(0,\pi)\), and exterior turning angles \(\delta_i=\pi-\theta_i\). Let \(X,Y\) be independent points drawn uniformly by Euclidean arclength from the **boundary** \(\partial K\), and set \(F_K(t)=\Pr(\|X-Y\|_2\le t)\). Define the scale-free short-chord corner coefficient
\[
B(K)=\sum_{i=1}^{m}\left(\frac{\delta_i}{\sin\delta_i}-1\right).
\]
There exists a positive \(t_K\), depending on \(K\), such that for **every** \(0\le t<t_K\),
\[
\boxed{F_K(t)=\frac{2t}{L}+\frac{B(K)}{L^2}t^2.} \tag{1}
\]
This is an *exact local probability law*, not only a two-term asymptotic. Its entire nontrivial local coefficient depends on the polygon's angles, not its individual side lengths; the perimeter supplies the dimensional normalization.

For each \(m\ge3\), writing \(b_m=2\pi/m\), the coefficient satisfies the **sharp, quantitative angle-rigidity inequality**
\[
\boxed{B(K)\ge m\left(\frac{b_m}{\sin b_m}-1\right)
+\frac16\sum_{i=1}^{m}(\delta_i-b_m)^2.}\tag{2}
\]
Equality holds exactly for equiangular \(m\)-gons. The factor \(1/6\) is the greatest possible *single constant valid for every number of sides*; it is not asserted optimal when \(m\) is fixed. In fact \(B(K)\) is strictly Schur-convex in the vector of exterior angles among vectors with the same total turning \(2\pi\). The sharp minimum for fixed \(m\) has expansion
\[
m\left(\frac{b_m}{\sin b_m}-1\right)
=\frac{2\pi^2}{3m}+\frac{14\pi^4}{45m^3}+O(m^{-5})\quad(m\to\infty).
\]
There is no finite upper bound on \(B(K)\) over all nondegenerate convex \(m\)-gons with fixed \(m\): it diverges when one interior angle tends to zero.

## Assumptions and scope

The polygon is compact, two-dimensional, and convex; consecutive sides are noncollinear, each side has positive length, and vertices are cyclically ordered. It need not be regular, tangential, equilateral, centrally symmetric, or strictly convex as a body. Both samples are **arclength-uniform on the entire polygon boundary**, not area-uniform in the polygon, not uniform on its vertices, and not independently selected one per side. Corners have zero sampling probability. All angles are in radians. The threshold \(t_K>0\) can be arbitrarily small as the polygon degenerates and is not uniform over polygons. The two endpoints of the random chord are independent.

The exterior turns obey \(0<\delta_i<\pi\) and \(\sum_i\delta_i=2\pi\). A convex equiangular polygon exists for every \(m\), so the equality statement is nonvacuous. The Schur-convexity assertion is about the explicit angle functional on its admissible domain; it does not assert that every formal angle vector necessarily has a particular fixed-perimeter realization.

## Proof

**1. Separation into pairs of sides.** Let the side lengths be \(\ell_1,\ldots,\ell_m\), with \(L=\sum_i\ell_i\). Fix \(t>0\) small enough that \(t<\min_i\ell_i\). If both independently sampled points lie on a given side of length \(\ell_i\), the unnormalized ordered-pair measure of \(\|X-Y\|\le t\) is exactly
\[
\int_0^{\ell_i}\int_0^{\ell_i}{\bf1}\{|u-v|\le t\}\,du\,dv=2\ell_i t-t^2.\tag{3}
\]
Indeed, the complement is two triangles of side \(\ell_i-t\). Summing (3) over all sides gives \(2Lt-mt^2\).

For nonadjacent sides (if any), the Euclidean distance between the two compact segments is positive. There are finitely many side pairs, so choose \(t\) smaller than all these pairwise distances. No ordered pair drawn from nonadjacent sides then contributes. When \(m=3\), every distinct side pair is adjacent and this restriction is empty.

**2. The exact contribution of each corner.** At a vertex of interior angle \(\theta\in(0,\pi)\), write points on the two incident sides as \(s u\) and \(v w\), measured from their common vertex, where \(u,w\) are unit tangent rays forming angle \(\theta\) and \(s,v\ge0\). Their difference is \(su-vw\). The invertible linear map
\[
T:(s,v)\longmapsto su-vw
\]
has absolute Jacobian \(\sin\theta\), and takes the positive coordinate quadrant to a Euclidean cone of opening \(\pi-\theta=\delta\). Consequently the preimage of the radius-\(t\) disk has area
\[
\frac{1}{\sin\theta}\cdot\frac{\delta t^2}{2}=\frac{\delta t^2}{2\sin\delta}.\tag{4}
\]
For a vector of norm at most \(t\), solving the linear system gives \(0\le s,v\le t/\sin\theta\). Thus if \(t\) is smaller than both incident side lengths multiplied by \(\sin\theta\), the region in (4) fits entirely into the actual two finite incident sides: there is **no truncation correction**. Interchanging which sample lies on which side doubles (4). Hence the total ordered-pair contribution from the corner is \(\delta t^2/\sin\delta\).

One positive common \(t_K\) can be chosen smaller than all finitely many side lengths, all incident length-times-sine values, and all nonadjacent-side distances. Combining (3) and (4) then gives unnormalized measure
\[
2Lt-mt^2+t^2\sum_{i=1}^m\frac{\delta_i}{\sin\delta_i}.
\]
Dividing by \(L^2\) proves (1), with endpoints handled by continuity.

**3. Strict convexity and quantitative stability.** Write \(h(x)=x/\sin x\) for \(0<x<\pi\), continuously defined by \(h(0)=1\). The classical Euler product for the sine function gives
\[
h(x)=\prod_{k=1}^{\infty}\left(1-\frac{x^2}{\pi^2k^2}\right)^{-1}
=1+\frac{x^2}{6}+\sum_{j=2}^{\infty}a_jx^{2j},\qquad a_j>0,\quad |x|<\pi.\tag{5}
\]
Every coefficient is positive: each reciprocal factor has a nonnegative power series, while positive contributions to every even degree are present. The coefficient of \(x^2\) is \(\pi^{-2}\sum_{k\ge1}k^{-2}=1/6\). The expansions and their derivatives converge locally uniformly on \((-\pi,\pi)\). In particular
\[
h''(x)=\frac13+\sum_{j\ge2}(2j)(2j-1)a_jx^{2j-2}>\frac13\quad(0<x<\pi),\tag{6}
\]
with \(h''(x)\to1/3\) as \(x\downarrow0\). Thus \(h(x)-x^2/6\) is strictly convex. Jensen's inequality, \(\sum_i\delta_i=2\pi\), and the variance identity \(\sum_i\delta_i^2=m b_m^2+\sum_i(\delta_i-b_m)^2\) yield
\[
\sum_i h(\delta_i)\ge m h(b_m)+\frac16\sum_i(\delta_i-b_m)^2.
\]
Subtracting \(m\) proves (2). Strict convexity gives equality if and only if \(\delta_i=b_m\) for all \(i\). The same strict convexity, by the elementary Robin Hood transfer criterion or Karamata's inequality, proves strict Schur-convexity. Expanding \(x/\sin x=1+x^2/6+7x^4/360+O(x^6)\) at \(x=b_m\) proves the stated large-\(m\) expansion.

**4. Optimality of the universal stability factor.** For even \(m=2q\to\infty\), put \(b=2\pi/m\) and \(\varepsilon=1/(5m)\). Prescribe exterior-angle gaps around the unit circle, in cyclic order, by
\[
\delta_1=\delta_{q+1}=b+\varepsilon,\qquad
\delta_2=\delta_{q+2}=b-\varepsilon,
\]
with all other gaps equal to \(b\). Each half-circle has total gap \(\pi\), and each gap lies strictly between zero and \(\pi\). Consecutive tangents to the unit circle whose outward normals have these gaps bound a genuine centrally symmetric convex tangential \(m\)-gon with the prescribed exterior angles. For this polygon,
\[
\frac{B(K)-m(h(b)-1)}{\sum_i(\delta_i-b)^2}
=\frac{h(b+\varepsilon)+h(b-\varepsilon)-2h(b)}{2\varepsilon^2}
\longrightarrow\frac{h''(0)}2=\frac16.
\]
Consequently any universal constant strictly larger than \(1/6\) in (2) fails for sufficiently large even \(m\). This proves sharpness independently of whether a better coefficient might hold for any particular fixed \(m\).

Finally, an interior angle approaching zero forces its exterior turn to approach \(\pi\); then \(\delta/\sin\delta\to\infty\), proving the no-upper-bound assertion. Such convex polygons exist by degeneration of an appropriate vertex angle.

## Verification

The accompanying standalone Python 3 program `checker.py` has no nonstandard-library dependencies. Run `python3 checker.py` from a directory containing it. It checks the corner-cone area formula by independent numerical integration, Monte Carlo sample-pair probabilities for regular and irregular convex polygons against (1), the stability inequality on varying exterior-angle vectors, and the approach to the sharp factor in the explicit even-order family. It prints `CHECKS_PASSED` on success. Sampling and quadrature corroborate normalization and local geometric formulas; the proof of the universal exact law and the all-polygon inequality is analytic and does not depend on finite experiments.

## Relationship to prior work

Bonnet, Gusakova, Thäle, and Zaporozhets [1] prove sharp mean-distance inequalities for two points distributed **uniformly inside** a convex body, with mean width as normalization. Their sampling measure and observable (mean, not small-distance boundary CDF) are different; their results do not directly imply (1) or (2). Zhang and Carlsson [2] integrate distance to a **fixed** location against uniform polygonal boundary measure for a continuous Fermat–Weber problem. This does not determine the local two-independent-boundary-point CDF or its angular rigidity. Reitzner, Schütt, and Werner [3] study many independent boundary samples and expected random-hull face numbers or missing volume, not the two-point distance CDF.

A related published geometric calculation [4] establishes an exact fourth-degree *interior-point* small-distance law and sharp angular stability for its quartic coefficient. That result has a different area-uniform product measure and coefficient \(1+(\pi-\theta)\cot\theta\); it does not furnish the boundary-pair coefficient \((\pi-\theta)/\sin\theta-1\) or the exact quadratic law. The present theorem is a distinct boundary measure statement, not a special case of [4]. Standard side-conditioned integration could in principle recover an individual polygon's local law, so algorithmic frameworks for complete distance distributions are a residual bibliographic risk; the claim of interest here is the universal corner-only formula together with the sharp global stability constant.

## Limitations

Equation (1) holds only below a polygon-dependent positive threshold; no claim is made about the full CDF at larger radii, smooth boundaries, nonconvex polygons, nonuniform boundary densities, or higher dimensions. Equality in (2) allows nonregular equiangular polygons; it does not characterize Euclidean congruence. The \(1/6\) stability constant is optimal **uniformly over all side counts**, not necessarily at a fixed count. As with any literature comparison, earlier unindexed equivalent formulas are possible. No independent mathematical audit or external certification is asserted.

## References

1. G. Bonnet, A. Gusakova, C. Thäle and D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, arXiv:2010.03351, publicly posted 2020-10-07; later *Advances in Mathematics* 386 (2021), 107813. https://arxiv.org/abs/2010.03351
2. T. T. C. K. Zhang and J. G. Carlsson, *On the Continuous Fermat-Weber Problem for a Convex Polygon Using Euclidean Distance*, arXiv:1403.3715, 2014-03-14. https://arxiv.org/abs/1403.3715
3. M. Reitzner, C. Schütt and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917, first posted 2019-11-14. https://arxiv.org/abs/1911.05917
4. *Sharp uniform angular stability for the short-pair distance coefficient of convex polygons*, public mathematical research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-uniform-angular-stability-for-the-short-pair-distance-coef--24e8bcd8655b
