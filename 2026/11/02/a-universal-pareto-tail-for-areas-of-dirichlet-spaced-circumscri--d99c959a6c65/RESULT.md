# A universal Pareto tail for areas of Dirichlet-spaced circumscribed polygons

## Finding
Fix an integer \(n\ge3\) and a real \(\alpha>0\). Let the cyclic angular gaps between \(n\) tangency normals to a unit circle, divided by \(2\pi\), have the symmetric Dirichlet distribution \(Y=(Y_1,\ldots,Y_n)\sim\operatorname{Dirichlet}(\alpha,\ldots,\alpha)\). Write \(B_n=\{\max_iY_i<1/2\}\). On \(B_n\), the intersection of the corresponding tangent half-planes containing the unit disk is a bounded convex \(n\)-gon. Let \(A\) be its Euclidean area, and let \(P\) be its perimeter. Define
\[
 p_{n,\alpha}=1-n\left(1-I_{1/2}\bigl(\alpha,(n-1)\alpha\bigr)\right),\qquad
 c_{n,\alpha}=\frac{n\,2^{2-n\alpha}}{\pi\,\mathrm B(\alpha,(n-1)\alpha)\,p_{n,\alpha}},
\]
where \(I\) is the regularized incomplete beta function and \(\mathrm B\) is Euler's beta function. Both constants are strictly positive. Then
\[
 \lim_{t\to\infty}t\,\Pr\{A>t\mid B_n\}=c_{n,\alpha},\qquad P=2A\quad\text{on }B_n.
\]
Consequently, for every real \(q\),
\[
 \mathbb E[A^q\mid B_n]<\infty\quad\Longleftrightarrow\quad q<1.
\]
In particular, conditioning on the existence of a bounded polygon does not make its mean area or perimeter finite. For the independent-uniform-tangency model \(\alpha=1\),
\[
 p_{n,1}=1-\frac{n}{2^{n-1}},\qquad
 c_{n,1}=\frac{n(n-1)}{\pi\,2^{n-2}(1-n/2^{n-1})}.
\]
For example, for three independently and uniformly sampled tangencies, \(\Pr(B_3)=1/4\) and \(\lim_{t\to\infty}t\Pr(A>t\mid B_3)=12/\pi\).

## Assumptions and scope
The circle has radius one. The variables \(Y_i\) denote cyclic angular *gaps*, not independent normal angles. A uniform overall rotation is immaterial to area; for \(\alpha=1\) the Dirichlet gaps are exactly those induced by independent uniform contact points. The theorem applies at each **fixed** \(n\ge3\) and \(\alpha>0\) as the area threshold \(t\to\infty\); it does not assert a uniform limit in either parameter. The random area is defined only on the measurable event \(B_n\). The exceptional equality event \(\max_iY_i=1/2\) has probability zero.

## Proof
**Geometry and feasibility.** Write ordered normal angles \(\theta_i\), with successive increments \(2\pi Y_i\). Their supporting half-planes are \(H_i=\{x:\langle x,(\cos\theta_i,\sin\theta_i)\rangle\le1\}\). The intersection \(K=\bigcap_iH_i\) is bounded exactly when the normals are not contained in a closed semicircle, equivalently when every cyclic gap is strictly less than \(\pi\), that is \(\max_iY_i<1/2\). On this event all \(n\) constraints define sides. Adjacent tangents whose normal gap is \(2\pi y\) meet at distance \(\sec(\pi y)\) from the origin on their bisector. The two tangent segments adjacent to the same contact point have lengths \(\tan(\pi y_{i-1})\) and \(\tan(\pi y_i)\); summing and using that a polygon tangent to the unit disk has area equal to its semiperimeter gives
\[
 A=\frac P2=\sum_{i=1}^n\tan(\pi Y_i).
\]
Since the Dirichlet gaps have a continuous distribution, no two gaps are simultaneously greater than one half. Hence the union of the disjoint events \(\{Y_i\ge1/2\}\) has probability \(n\Pr(Y_1\ge1/2)\). The Dirichlet beta marginal \(Y_1\sim\operatorname{Beta}(\alpha,(n-1)\alpha)\) yields the stated formula for \(p_{n,\alpha}\). It is positive: an open neighborhood of equal gaps \(Y_i=1/n\) lies inside \(B_n\).

**Single large-gap probability.** The marginal density is
\[
 f(x)=\frac{x^{\alpha-1}(1-x)^{(n-1)\alpha-1}}{\mathrm B(\alpha,(n-1)\alpha)},\qquad f(1/2)=\frac{2^{2-n\alpha}}{\mathrm B(\alpha,(n-1)\alpha)}.
\]
For a threshold \(u>0\), \(\tan(\pi Y_1)>u\) and \(Y_1<1/2\) are equivalent to \(Y_1\in(x_u,1/2)\), with \(x_u=\arctan(u)/\pi=1/2-1/(\pi u)+O(u^{-3})\). By continuity of \(f\),
\[
 \Pr\{x_u<Y_1<1/2\}\sim\frac{f(1/2)}{\pi u}.
\]
Conditioning on \(Y_1=x=1/2-\varepsilon\), the remaining \(n-1\) gaps divided by \(1-x\) have a symmetric Dirichlet law. The chance that one of those gaps reaches \(1/2\) is \(O(\varepsilon^{(n-2)\alpha})\): its complementary sum of \(n-2\) Dirichlet components would have to be at most \(\varepsilon/(1/2+\varepsilon)\), and its beta lower-tail probability has this order. Therefore the extra condition \(B_n\) changes the single-large-gap probability only by a lower-order term, and
\[
 \Pr\{B_n,\tan(\pi Y_1)>u\}\sim\frac{f(1/2)}{\pi u}.
\]

**Two large gaps cannot contribute at first order.** Fix \(\eta>0\). If \(B_n\) holds and both \(\tan(\pi Y_i)>\eta t\) and \(\tan(\pi Y_j)>\eta t\) for distinct indices, both corresponding gaps belong to \((1/2-C_\eta/t,1/2)\) for a constant \(C_\eta\). The sum of the other \(n-2\) gaps is then at most \(2C_\eta/t\). Integrating the Dirichlet density over this corner of the simplex (with the first two coordinates bounded away from zero) gives
\[
 \Pr\{B_n,\tan(\pi Y_i)>\eta t,\tan(\pi Y_j)>\eta t\}
 =O_{n,\alpha,\eta}\bigl(t^{-1-(n-2)\alpha}\bigr)=o(t^{-1}).
\]
For clarity, this corner estimate holds also when \(0<\alpha<1\): integrating the density of the total mass of the remaining \(n-2\) coordinates contributes the factor of order \(t^{-(n-2)\alpha}\), and the first free near-half gap contributes \(t^{-1}\).

**One-large-gap squeeze.** Put \(T_i=\tan(\pi Y_i)>0\) on \(B_n\). Always \(\{\max_iT_i>t\}\subseteq\{\sum_iT_i>t\}\). For any fixed \(\delta\in(0,1)\), if \(\sum_iT_i>t\) but \(\max_iT_i\le(1-\delta)t\), then at least two terms exceed \(\delta t/(n-1)\); otherwise the sum would be at most \((1-\delta)t+(n-1)\delta t/(n-1)=t\). Finite unions, the single-gap asymptotic and the negligible pair intersections therefore imply
\[
 \frac{n f(1/2)}{\pi}\le\liminf_{t\to\infty}t\Pr\{A>t,B_n\}
 \le\limsup_{t\to\infty}t\Pr\{A>t,B_n\}
 \le\frac{nf(1/2)}{\pi(1-\delta)}.
\]
Letting \(\delta\downarrow0\) and dividing by \(\Pr(B_n)=p_{n,\alpha}\) proves the tail coefficient.

**Moment threshold.** Since \(K\) contains the unit disk, \(A\ge\pi\), so all negative moments are finite. For \(q>0\), the layer-cake identity \(\mathbb E[A^q\mid B_n]=q\int_0^\infty t^{q-1}\Pr(A>t\mid B_n)\,dt\) and the strictly positive \(c_{n,\alpha}/t\) tail show that the integral converges precisely when \(q<1\), and diverges logarithmically at \(q=1\). The perimeter statement follows from \(P=2A\). For \(\alpha=1\), the beta marginal is \(\operatorname{Beta}(1,n-1)\), giving the explicit specialization. \(\square\)

## Verification
Run `python verify.py` with dependencies in `requirements.txt`. The checker recomputes the beta probabilities and coefficients, reconstructs random tangent polygons independently using adjacent-line intersection vertices and the shoelace formula, confirms \(A=\sum_i\tan(\pi Y_i)\), tests the near-semicircle beta-edge density, and compares simulated large-area tails against the analytic constants for several sample sizes and Dirichlet parameters. The deterministic geometric comparisons, density checks, and numerical experiments reported success. These finite calculations corroborate but do not establish the asymptotic proof; the proof above controls every threshold analytically.

## Relationship to prior work
Besau, Rosen and Thäle [1] provide a geometric setting for random inscribed polytopes and dual circumscribing polyhedral sets, emphasizing large-sample normal approximation. Wang, Li and Xu [2] study the symmetric-Dirichlet tangency construction itself, including perimeter/area approximations and nonlinear extrapolation as the number of sides grows; that construction and its large-sample estimates are expressly not new here. Xu [3] earlier introduced the independent-uniform circumscribing model and noted that areas can be unbounded even when a polygon exists. The presently assessed statement concerns an orthogonal limit: **fixed** \(n\) and \(\alpha\), then **large area threshold**, with a sharp coefficient and an exact moment-existence boundary. Neither the inspected full text of [1] or [2], nor the accessible abstract of [3], states this coefficient; however, [3] is a direct predecessor whose full text could not be inspected, so its possible priority remains a real residual risk. Newman [4] is a related but different random-polytope model.

## Limitations
No claim is made about thresholds uniform in \(n\) or \(\alpha\), nonsymmetric Dirichlet laws, correlations between successive gaps beyond the Dirichlet specification, noncircular tangent supports, or higher dimensions. The result supplies a one-term tail asymptotic, not a closed finite-threshold distribution or rates of tail convergence. It is a self-reviewed mathematical finding, not an independently audited result. Historical priority, especially relative to the inaccessible full text of Xu [3], remains provisional.

## References
1. Besau, F., Rosen, D., and Thäle, C. (2020), Random inscribed polytopes in projective geometries, arXiv:2005.10502, https://arxiv.org/abs/2005.10502 (public 2020-05-21; primary MSC 52A22).
2. Wang, S., Li, Z., and Xu, W.-Q. (2023), Nonlinear random extrapolation estimates of π under Dirichlet distributions, Journal of Numerical Analysis and Approximation Theory 52(2), 273–294, https://doi.org/10.33993/jnaat522-1360 (online 2023-12-22).
3. Xu, W.-Q. (2015), Random circumscribing polygons and approximations of π, Statistics & Probability Letters 106, 52–57, https://doi.org/10.1016/j.spl.2015.06.026 (full text not accessed; abstract only).
4. Newman, A. (2020), Doubly random polytopes, arXiv:2006.07000, https://arxiv.org/abs/2006.07000.
