# Local curvature from the logarithmic containment law of random inscribed polygons

## Finding

For each fixed integer \(n\ge3\), let \(H_n\) be the convex hull of \(n\) independent points sampled from a smooth, positively curved convex plane curve with positive arclength density \(f\). The inclusion probability of a point at inward normal distance \(\delta\) from a specified boundary point \(z\) has the sharp form
\[
\Pr\{z+\delta\nu(z)\in H_n\}
=\frac{2n(n-1)f(z)^2}{\kappa(z)}\,\delta\log\frac{L}{\delta}
+O_{K,f,n,z}(\delta).
\]
The coefficient is local: only the sampling density and curvature at \(z\) occur. For uniform arclength sampling the resulting logarithmic limit determines \(\kappa(z)\) given the perimeter, thereby supplying a local stochastic curvature probe.

## Assumptions and scope

Let \(K\subset\mathbb R^2\) be a compact, full-dimensional, strictly convex body whose boundary \(\Gamma\) is a regular \(C^3\) closed curve, with strictly positive Euclidean curvature everywhere. Let \(L\) be its Euclidean perimeter; let \(f:\Gamma\to(0,\infty)\) be a \(C^1\) probability density with respect to arclength, \(\int_\Gamma f\,ds=1\). For a fixed integer \(n\ge3\), choose \(X_1,\ldots,X_n\) independently from \(f\,ds\), and let \(H_n=\operatorname{conv}\{X_1,\ldots,X_n\}\). Fix \(z\in\Gamma\), denote inward unit normal by \(\nu(z)\) and curvature by \(\kappa(z)>0\); set \(p_\delta=z+\delta\nu(z)\). The asymptotic holds as \(\delta\downarrow0\) through sufficiently small positive distances for which \(p_\delta\) lies in the interior. Constants implicit in \(O(\delta)\) may depend on the fixed curve, density, number of samples and point, but not on \(\delta\).

In the uniform case \(f\equiv 1/L\),
\[
\lim_{\delta\downarrow0}
\frac{\Pr(p_\delta\in H_n)}{\delta\log(L/\delta)}
=\frac{2n(n-1)}{L^2\kappa(z)}.
\]

## Proof

**1. Exact half-circle identity.** Parametrize the boundary counterclockwise by arclength \(\gamma:[0,L]\to\Gamma\), choosing \(\gamma(0)=\gamma(L)=z\). For any interior point \(p\), radial projection from \(p\) induces an orientation-preserving circle homeomorphism from \(\Gamma\) onto the circle of directions. For each \(s\), let \(\gamma(\tau_p(s))\) be the intersection of the ray from \(p\) opposite to \(\gamma(s)-p\) with \(\Gamma\), chosen counterclockwise after \(s\) modulo the perimeter. Define \(Q_p(s)\) as the sampling mass of the open counterclockwise boundary arc from \(\gamma(s)\) to that opposite point. Apart from measure-zero angular degeneracies, \(p\notin H_n\) exactly when all directions lie in an open semicircle. Every configuration of \(n\ge2\) directions contained in an open semicircle has exactly one cyclic starting sample whose forward semicircle contains every remaining direction (its unique gap of length exceeding a semicircle). Consequently,
\[
\Pr(p\notin H_n)=n\int_0^L f(s)Q_p(s)^{n-1}\,ds.\tag{1}
\]

**2. Boundary limit and geometry of the short chord.** Let \(Q_0(s)=\int_s^L f(t)\,dt\) for \(0<s<L\); this is the limit of \(Q_{p_\delta}(s)\) for every fixed \(s\). Because \(Q_0'(s)=-f(s)\),
\[
n\int_0^L f(s)Q_0(s)^{n-1}\,ds=1.\tag{2}
\]
Choose tangent-normal coordinates at \(z\) with \(z=(0,0)\), positive tangent first and inward normal second. The \(C^3\) arclength expansion reads
\[
\gamma(u)=\bigl(u+O(u^3),\,\tfrac12\kappa(z)u^2+O(u^3)\bigr)
\]
for signed \(u\) close to zero. The chord connecting nearby boundary parameters \(s>0\) and \(t<0\) meets the normal line at height
\[
-\tfrac12\kappa(z)st\bigl(1+O(|s|+|t|)\bigr).
\]
The condition that this chord pass through \(p_\delta=(0,\delta)\), followed by the implicit-function theorem, gives for any sufficiently small fixed \(\eta>0\) and sufficiently large fixed \(C\), uniformly on \(C\delta\le s\le\eta\), an opposite point at signed arclength
\[
 t_\delta(s)=-\frac{2\delta}{\kappa(z)s}
 +O\!\left(\delta+\frac{\delta^2}{s^2}\right).\tag{3}
\]
For \(s>0\) this point is counterclockwise just before the parameter origin. Thus
\[
Q_{p_\delta}(s)-Q_0(s)
=\int_0^{t_\delta(s)} f(u)\,du
=-\frac{2f(0)\delta}{\kappa(z)s}
+O\!\left(\delta+\frac{\delta^2}{s^2}\right).\tag{4}
\]
Periodically extend \(f\) for signed arguments. The expansions use the fixed bounds \(f\in C^1\), \(\kappa(z)>0\), and local strict convexity; they do not rely on a circular approximation outside this local chart.

**3. Extracting the logarithm and bounding the remainder.** Write \(m=n-1\ge2\). By (1)--(2),
\[
\Pr(p_\delta\in H_n)
=n\int_0^L f(s)\bigl(Q_0(s)^m-Q_{p_\delta}(s)^m\bigr)\,ds.\tag{5}
\]
For \(s\in[C\delta,\eta]\), use (4) and \(Q_0(s)=1+O(s)\), \(f(s)=f(0)+O(s)\). Taylor expansion of the power, including its quadratic remainder, yields
\[
 f(s)\bigl(Q_0(s)^m-Q_{p_\delta}(s)^m\bigr)
=\frac{2m f(0)^2\delta}{\kappa(z)s}
+O\!\left(\delta+\frac{\delta^2}{s^2}\right).
\]
Integration gives \(2m f(0)^2\delta\log(1/\delta)/\kappa(z)+O(\delta)\). The discarded initial interval \([0,C\delta]\) contributes \(O(\delta)\) because probabilities are bounded by one. On every closed subarc away from \(z\) the opposite-endpoint map varies smoothly with \(\delta\), hence its contribution is \(O(\delta)\).

It remains to control the other side of \(z\), where \(s=L-u\), \(0<u<\eta\). For \(u\ge C\delta\), its opposite endpoint changes by \(O(\delta/u)\) in arclength. Hence \(Q_0(L-u)=O(u)\) and \(|Q_{p_\delta}(L-u)-Q_0(L-u)|\le C_1\min(1,\delta/u)\). Using
\[
|x^m-y^m|\le m|x-y|\max(x,y)^{m-1},
\]
and splitting the integral at \(u=\sqrt\delta\), the contribution of \([C\delta,\eta]\) is \(O(\delta)\) for every \(m\ge2\); the final interval \([L-C\delta,L]\) also contributes \(O(\delta)\). These estimates are uniform at fixed \(z\) and fixed \(n\). Combining all arcs in (5) gives
\[
\Pr(p_\delta\in H_n)
=\frac{2n(n-1)f(z)^2}{\kappa(z)}\delta\log(1/\delta)
+O(\delta).
\]
Replacing \(\log(1/\delta)\) by the dimensionless \(\log(L/\delta)\) only changes the stated \(O(\delta)\) term. This completes the proof.

## Verification

The standalone `verify_boundary_absorption.py` checks the exact semicircle-anchor integral in several analytically and geometrically independent ways. For the unit circle and three points, it reproduces the previously known dilogarithm law to high numerical precision. For sample counts \(3,4,5,7\), it checks convergence toward the stated logarithmic coefficient; for an ellipse with semiaxes \(2\) and \(1\), it incorporates exact elliptic-integral arclength weights and the local curvature at a major-axis tip. Nonuniform circular densities test the predicted square of the local density. Finally, independently sampled inscribed elliptical polygons are classified by oriented edge halfplanes and compared to the exact one-dimensional integral. All checks passed; numerical convergence alone is not an infinite-dimensional or asymptotic proof.

## Relationship to prior work

Brunel (2015, arXiv:1503.01504) studies Hausdorff accuracy for random polytopes, including boundary sampling and large-sample behavior, rather than the fixed-sample local absorption probability here. Prochno and collaborators (2024, arXiv:2404.02870) consider random approximation in Hausdorff distance; their setup and estimands are different. Ismailov (2026, arXiv:2601.02929) discusses the known exact probability that three uniform unit-circle points enclose a specified interior point, involving a dilogarithm: that important special case implies the circular \(n=3\) asymptotic, so it is not independently new. The asserted contribution is the full fixed-\(n\), smooth-curve, density-dependent local formula and curvature-recovery interpretation, which do not follow from those special formulas without the geometric boundary-layer argument.

## Limitations

The formula assumes smooth strictly convex planar curves with positive curvature and positive differentiable boundary density. It is a fixed-sample, local near-boundary result; it is not uniform in \(n\), does not cover corners, vanishing curvature or densities vanishing at the specified boundary point, and does not determine finite-depth probabilities. Definitive historical priority and independent validation are not established. The leading logarithmic term is universal under these hypotheses, but the unreported \(O(\delta)\) coefficient can depend on global shape and density.

## References

1. Victor-Emmanuel Brunel, *Uniform Behaviors of Random Polytopes under the Hausdorff Metric*, arXiv:1503.01504, publicly posted 5 March 2015. https://arxiv.org/abs/1503.01504
2. J. Prochno and collaborators, *Random approximation of convex bodies in Hausdorff distance*, arXiv:2404.02870, 2024. https://arxiv.org/abs/2404.02870
3. A. Ismailov, *With what probability does an inscribed triangle contain a given point?*, arXiv:2601.02929, publicly posted 6 January 2026. https://arxiv.org/abs/2601.02929
