# Finite-sample boundary-hull area of parallelograms: rhombus extremality and a thin-shape crossover

## Finding
Let \(P\) be an arbitrary nondegenerate Euclidean parallelogram with adjacent side lengths \(a,b>0\), area \(A>0\), and arbitrary interior angle in \((0,\pi)\). For each integer \(n\ge3\), sample \(n\) independent points uniformly with respect to Euclidean arclength on \(\partial P\), and let \(H_n\) be their convex hull. Put \(u=a/(a+b)\) and \(Q_n=\mathbb E[\operatorname{area}(H_n)]/A\). Then the **exact finite-sample deficit** is
\[
1-Q_n=\frac{2\left[2^{n+2}-(2-u)^{n+2}-(1+u)^{n+2}+u^{n+2}+(1-u)^{n+2}\right]}{2^n(n+1)(n+2)u(1-u)}.
\]
This ratio is independent of the angle between the sides. For every \(n\ge3\), it is strictly increasing in \(u(1-u)\) on \(0<u\le1/2\); therefore **all rhombi and only rhombi maximize the normalized expected hull area among parallelograms**. The exact sharp interval is
\[
\frac{n-3+2^{2-n}}{n+1}<Q_n\le
1-\frac{32-36(3/4)^n+4(1/4)^n}{(n+1)(n+2)}.
\]
The upper equality holds precisely for equal side lengths; the lower endpoint is approached as the ratio of the shorter to longer side tends to zero and is not attained. As a consequence, for any fixed integer \(n\ge3\), the observed population value of \(Q_n\) determines the *unordered ratio of the two adjacent side lengths*, although it cannot determine their angle.

There is also an exact thin-shape crossover. If the parallelogram depends on \(n\) and \(u_n=\min(a_n,b_n)/(a_n+b_n)\) satisfies \(n u_n\to\tau\in[0,\infty)\), then
\[
\lim_{n\to\infty} n(1-Q_n)=G(\tau),\qquad
G(\tau)=\begin{cases}
8(1-e^{-\tau/2})/\tau,&\tau>0,\\
4,&\tau=0.
\end{cases}
\]
By contrast, at every fixed positive \(u\in(0,1)\), the limit is \(\lim_{n\to\infty} n^2(1-Q_n)=8/[u(1-u)]\). Thus fixed-shape deficit scaling is quadratic in the sample count, but the scaling is only linear when the shorter side's relative length is of order the reciprocal sample count.

## Assumptions and scope
The parallelogram is convex and nondegenerate; \(a\) and \(b\) are its *Euclidean edge lengths*, not lengths of coordinate projections. The boundary samples are independent and uniform in *Euclidean arclength* (so a side of length \(a\) has probability mass \(a/[2(a+b)]\)); they are not uniform in area. The convex hull has the usual Euclidean area. All formulas include highly sheared parallelograms and remain valid for every fixed interior angle strictly between zero and \(\pi\). The finite-sample theorem is for all integers \(n\ge3\), and the thin crossover permits varying side lengths and varying angles but requires positive side lengths for each \(n\). At \(n=2\), the hull is a segment and \(Q_2=0\) for every shape, so strict shape ordering cannot begin earlier.

## Proof
**1. Reduction without changing the sampling law.** Parametrize a parallelogram by \(p+s e_1+t e_2\), where \(e_1,e_2\) are unit vectors in the two edge directions and \(0\le s\le a\), \(0\le t\le b\). The linear map from the rectangle \([0,a]\times[0,b]\) to this parallelogram is an isometry *on each coordinate-direction edge*, hence sends its arclength-uniform boundary measure to the parallelogram's arclength-uniform boundary measure. It multiplies all planar areas by the same positive Jacobian \(|\det(e_1,e_2)|\). Therefore the normalized random-hull area law, and in particular \(Q_n\), coincide with those for the axis-aligned rectangle with side lengths \(a,b\).

**2. Exact gap-area identity for arbitrary polygons.** Parametrize any convex polygon counterclockwise by arclength \(\gamma(s)\), with perimeter \(L\), and write \(e(s)=\gamma'(s)\) at the almost-everywhere defined tangent points. If \(s<t\) are two sample points consecutive in counterclockwise boundary order (using a periodic extension of \(\gamma\)), the omitted cap between their boundary arc and its chord has signed area
\[
C(s,t)=\tfrac12\int_s^t\int_q^t\det(e(q),e(r))\,dr\,dq.
\]
This follows from the shoelace line integral on the boundary arc and closing chord; convexity makes the cap area nonnegative. Almost surely sample points are distinct, and the omitted caps for successive sample points partition the area omitted by their convex hull, including configurations with several sampled points on one edge.

For an ordered boundary pair separated by arclength \(v\in(0,L)\), the probability that the remaining \(n-2\) samples avoid the oriented open arc is \((1-v/L)^{n-2}\). Integrating the \(n(n-1)\) choices of ordered endpoints, the preceding cap formula and Fubini, and then integrating the two possible endpoint margins around a fixed oriented tangent pair with separation \(\delta\), gives
\[
\mathbb E[A-\operatorname{area}(H_n)]
=\tfrac12\int_0^L\int_0^L\det(e(s),e(s+\delta))\,(1-\delta/L)^n\,d\delta\,ds.\tag{1}
\]
Indeed the margin integral is exactly
\[
\frac{n(n-1)}{L^2}\int_{\substack{\alpha,\beta\ge0\\\alpha+\beta\le L-\delta}}
\left(1-\frac{\delta+\alpha+\beta}{L}\right)^{n-2}\,d\alpha\,d\beta
=(1-\delta/L)^n.
\]
The formula is valid for every \(n\ge2\) and uses no limiting approximation.

**3. Evaluation for a rectangle.** The tangent takes the four successive values \((1,0),(0,1),(-1,0),(0,-1)\). In (1), tangent pairs on the same or opposite sides have zero determinant. For pairs on adjacent sides in forward cyclic order, the determinant is \(+1\), and for the reverse order it is \(-1\). Pairing corresponding edge positions yields
\[
\mathbb E[A-\operatorname{area}(H_n)]
=2\int_0^a\int_0^b\left[
\left(1-\frac{x+y}{L}\right)^n-\left(\frac{x+y}{L}\right)^n
\right]dy\,dx,\qquad L=2(a+b).
\]
Reflect the two variables in the second integral (replace \(x,y\) by \(a-x,b-y\)) and integrate both powers twice. The result is the exact unnormalized identity
\[
\mathbb E[A-\operatorname{area}(H_n)]=
\frac{2\left[L^{n+2}-(2a+b)^{n+2}-(a+2b)^{n+2}+a^{n+2}+b^{n+2}\right]}{L^n(n+1)(n+2)}.
\tag{2}
\]
Division by \(ab\) and the substitution \(u=a/(a+b)\) give the displayed finite-sample formula. The shear reduction in Step 1 extends it to every parallelogram.

**4. Strict shape ordering.** Let \(X,Y\) be independent uniforms on \([0,1]\) and put \(Z_u=uX+(1-u)Y\). The integral in Step 3, after the reflection of its second term, is exactly
\[
1-Q_n=2\,\mathbb E[\phi_n(Z_u)],\qquad
\phi_n(z)=(1-z/2)^n-((1-z)/2)^n.
\tag{3}
\]
For \(n\ge3\) and \(0\le z\le1\),
\[
\phi_n''(z)=\frac{n(n-1)}4\left[(1-z/2)^{n-2}-((1-z)/2)^{n-2}\right]>0.
\]
Write \(u=1/2+d\). Since \(X,Y\) are exchangeable, the expected value in (3) equals the expectation of
\[
\tfrac12\left[\phi_n\left(\frac{X+Y}{2}+d(X-Y)\right)
+\phi_n\left(\frac{X+Y}{2}-d(X-Y)\right)\right].
\]
Strict convexity shows that this expression is strictly increasing in \(|d|\) whenever \(X\ne Y\). This event has probability one, so the mean deficit is strictly minimized at \(d=0\), and increases with \(|d|\). Since \(u(1-u)=1/4-d^2\), the expected covered fraction is strictly increasing in \(u(1-u)\). Substitution \(u=1/2\) gives the upper endpoint. Letting \(u\downarrow0\) in (2) by differentiation or (3) gives the lower endpoint \((n-3+2^{2-n})/(n+1)\). Both bounds are sharp; equality conditions follow from strict convexity. The same strict ordering proves inversion for the unordered side ratio.

**5. The singular thin-shape regime.** By symmetry in \(a,b\), assume \(0<u_n\le1/2\) and write \(n u_n\to\tau\). Formula (3) gives, after setting \(y=z/n\) in the integral over \(Y\),
\[
n(1-Q_n)=2\int_0^1\int_0^n
\left[\left(1-\frac{u_n x+(1-u_n)z/n}{2}\right)^n
-\left(\frac{1-u_nx-(1-u_n)z/n}{2}\right)^n\right]dz\,dx.
\]
The second term is uniformly bounded after integration by \(n2^{-n}\), hence vanishes. For the first term, the integrand tends pointwise to \(e^{-(\tau x+z)/2}\). Because \(1-u_n\ge1/2\), it is bounded by \(e^{-z/4}\), an integrable dominator on \([0,1]\times[0,\infty)\). Dominated convergence gives
\[
\lim n(1-Q_n)=2\int_0^1 e^{-\tau x/2}dx\int_0^\infty e^{-z/2}dz
=4\int_0^1e^{-\tau x/2}dx=G(\tau).
\]
At fixed \(u>0\), all terms in the closed formula except the \(2^{n+2}\) term are exponentially smaller, hence \(n^2(1-Q_n)\to8/[u(1-u)]\). These are different limits: no fixed-shape asymptotic is asserted uniformly down to \(u=0\).

## Verification
The included standalone `CHECKER.py` runs using only the Python standard library. It compares the closed formula with an independently expanded exact binomial-moment integral for 28 rational parameter cases, checks exact extremal bounds, computes independent convex hulls of simulated boundary points under multiple nonorthogonal shears, and checks both asymptotic regimes numerically. An actual invocation reported `EXACT_TWO_INDEPENDENT_INTEGRATIONS_AND_SHARP_BOUNDS_PASSED 28`, `AFFINE_SHEAR_ANGLE_BLINDNESS_DIAGNOSTICS_PASSED`, `FIXED_SHAPE_AND_THIN_BOUNDARY_LAYER_LIMITS_PASSED`, and `ALL_CHECKS_PASSED`. Finite experiments and floating-point limits are diagnostics only; the exact integral identity, convexity argument, and dominated-convergence argument prove the stated universal results.

## Relationship to prior work
Reitzner, Schütt and Werner, *The convex hull of random points on the boundary of a simple polytope* (first available as arXiv:1911.05917 on November 14, 2019), prove general expected missing-volume asymptotics; their Theorem 1.2 gives the order rather than an exact finite-sample, side-ratio-dependent formula for parallelograms. Prochno, Schütt, Sonnleitner and Werner, *Random approximation of convex bodies in Hausdorff metric* (arXiv:2404.02870, April 3, 2024), investigate expected **Hausdorff** approximation, a different error functional. Previously established corner-limit results for general polygon boundary hulls yield the fixed-shape leading area-deficit term and an exponentially accurate finite-sample approximation, but not the exact finite-sample shape ordering or the collapsing-side crossover. The present claim excludes those existing leading-order results from its novelty assertion. Search and full-text comparison did not identify stronger or equivalent exact claims; historical priority is provisional, and the general literature on boundary-sampled random polygons is extensive.

## Limitations
Only iid uniform arclength boundary samples and the normalized **expected area** are covered. No statement is made about variance of the area, stochastic domination of the full hull-area distribution, higher-dimensional parallelotopes, nonuniform side probabilities, or quantitative stability under noisy empirical estimates. The result cannot reconstruct the parallelogram's angle; rhombi of different angles have identical normalized expected-area profiles. The thin limit requires \(n u_n\to\tau\) and does not replace a general uniform approximation for arbitrary diverging \(n u_n\). Independent mathematical audit and historical-priority certification have not been performed.

## References
1. M. Reitzner, C. Schütt, E. M. Werner, “The convex hull of random points on the boundary of a simple polytope,” arXiv:1911.05917, first posted November 14, 2019. https://arxiv.org/abs/1911.05917. Open-access journal version: *Discrete & Computational Geometry* 69 (2023), 453–504, DOI:10.1007/s00454-022-00460-2.
2. J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, “Random approximation of convex bodies in Hausdorff metric,” arXiv:2404.02870, first posted April 3, 2024. https://arxiv.org/abs/2404.02870.
3. B. Efron, “The convex hull of a random set of points,” *Biometrika* 52 (1965), 331–343. DOI:10.1093/biomet/52.3-4.331. General integral-expression background, not a direct source of the present sharp formula.
