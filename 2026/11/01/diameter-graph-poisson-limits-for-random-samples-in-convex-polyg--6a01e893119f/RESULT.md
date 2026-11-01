# Diameter-graph Poisson limits for random samples in convex polygons

## Finding
Let \(P\subset\mathbb R^2\) be any fixed convex polygon of positive area \(A\), diameter \(D\), and with no redundant collinear listed vertices. For independent area-uniform \(X_1,\ldots,X_n\in P\), put \(M_n=\max_{i<j}|X_i-X_j|\). The finite **diameter graph** consists of the vertices of \(P\) and edges \(e=\{v,w\}\) whenever \(|v-w|=D\).

At each vertex incident with a diameter edge put an independent homogeneous Poisson point process \(\Pi_v\) on the inward tangent cone \(C_v\), with intensity \(1/A\) per unit planar area. For each incident edge \(e=\{v,w\}\), let \(u_{v,e}=(w-v)/D\) and \(H_{v,e}=\inf_{z\in\Pi_v} u_{v,e}\cdot z\). These infima are almost surely finite and positive. Then
\[
\sqrt n\,(D-M_n)\ \Longrightarrow\ Y_P:=\min_{\{v,w\}\in E_D}(H_{v,e}+H_{w,e}).
\]
The formula covers arbitrary diameter graphs, including **different diameter edges sharing vertices**. All randomness is specified by one independent process per *polygon vertex*, rather than falsely declaring the diameter edges independent.

Let \(a_v,b_v\) be the two inward unit edge directions from \(v\), with interior angle \(\theta_v\in(0,\pi)\). For every diameter-edge incidence define the positive geometric coefficient
\[
\gamma_{v,e}=\frac{\sin\theta_v}{2A\,(u_{v,e}\cdot a_v)(u_{v,e}\cdot b_v)}.
\]
Then \(\Pr(H_{v,e}>t)=e^{-\gamma_{v,e}t^2}\), for \(t\ge0\). The *joint* law at a vertex is explicit: for any positive thresholds \((t_e)_{e\ni v}\),
\[
\Pr(H_{v,e}>t_e\ \forall e\ni v)=
\exp\!\left[-\frac1A\operatorname{area}\left(\bigcup_{e\ni v}\{z\in C_v:u_{v,e}\cdot z\le t_e\}\right)\right].
\]
The edge-sum variables \(H_{v,e}+H_{w,e}\) are mutually independent **exactly when** the diameter graph is a matching. If two diameter edges share a vertex, their edge-sums have strictly positive covariance. This classifies the dependence obstruction that arises for nonregular polygons.

Two sharp, geometric small-deficit laws are
\[
\Pr(Y_P\le t)=\frac{t^4}{6}\sum_{e=\{v,w\}\in E_D}\gamma_{v,e}\gamma_{w,e}+O_P(t^6),\qquad t\downarrow0,
\]
and, for independent area-uniform \(X,X'\in P\),
\[
\Pr(|X-X'|>D-\varepsilon)=\frac{\varepsilon^4}{3}\sum_{e=\{v,w\}\in E_D}\gamma_{v,e}\gamma_{w,e}+O_P(\varepsilon^5),\qquad\varepsilon\downarrow0.
\]
The first limit describes the sample diameter, while the second is a separate two-point extreme-distance tail. Their leading coefficients differ by a factor two.

For the **nonregular isosceles triangle** with vertices \((-1,0),(1,0),(0,2)\), the diameter is \(\sqrt5\) and the diameter graph is a two-edge star. The apex incidence coefficients equal \(1/3\), and those at the base corners equal \(1/2\). Consequently \(\Pr(Y_P\le t)=t^4/18+O(t^6)\) and \(\Pr(|X-X'|>\sqrt5-\varepsilon)=\varepsilon^4/9+O(\varepsilon^5)\). Both edge-sum variables are dependent because they share the apex process.

## Assumptions and scope
The polygon is nondegenerate, convex, fixed as \(n\to\infty\), with positive area; its listed vertices are its genuine extreme points. All samples are independent and uniform with respect to two-dimensional area. A diameter graph edge is an unordered pair of *actual* vertices at the full Euclidean diameter. All tangent cones use **inward** directions. Constants implicit in \(O_P\) may depend on the fixed polygon. This is the Euclidean diameter, not a distance induced by the polygon's Minkowski functional.

## Proof
**1. Diameters have finitely many vertex endpoints and positive linear deficits.** A maximizer of \(|x-y|\) over \(P\times P\) can be moved to a vertex in each coordinate, by strict convexity of squared Euclidean distance along every nontrivial line segment. Indeed, if \(x\) were in the relative interior of an edge, \(|x-y|^2\) would be strictly convex along that edge and could not attain its maximum there. Thus all maximum pairs are exactly the finitely many diameter graph edges.

Fix \(e=\{v,w\}\in E_D\), write \(u=(w-v)/D\), and take an inward edge ray \(a\) at \(v\). For every small \(s>0\), \(|w-v-sa|^2=D^2-2Ds(u\cdot a)+s^2\le D^2\); hence \(u\cdot a>0\) (and likewise for the other ray and at \(w\)). Thus \(u_{v,e}\cdot z\ge c_{v,e}|z|\) on \(C_v\) for some positive \(c_{v,e}\). Near \((v,w)\), a Taylor expansion yields
\[
D-|v+z-w-q|=u_{v,e}\cdot z+u_{w,e}\cdot q+O(|z|^2+|q|^2),
\]
where \(u_{w,e}=-u_{v,e}\). Shrinking the neighborhoods makes the linear term dominate; the actual deficit is bounded below by a positive constant times \(|z|+|q|\). By compactness, distance near \(D\) forces each endpoint into one of these finitely many vertex neighborhoods.

**2. Independent limiting Poisson processes.** Rescale every sampled point near each distinct diameter vertex by \(\sqrt n\), translating the vertex to the origin. On every bounded region of its tangent cone, the binomial number of points converges to a Poisson count of mean \(\operatorname{area}/A\). Counts in disjoint cones are asymptotically independent, and the corresponding marked point processes converge jointly to the independent \(\Pi_v\). Because the deficit lower bound from step 1 forces every near-diametral pair into bounded scaled neighborhoods, a truncation argument reduces \(\sqrt n(D-M_n)\) to the finite minimum of the Poisson linear costs plus an error tending to zero in probability. As the truncation radius increases, the probability of missing an improving pair tends to zero: every vertex cone has arbitrarily many available points at finite linear cost almost surely. This proves the distributional convergence.

**3. Exact cone rates and incidence dependence.** Write \(z=ra_v+sb_v\), \(r,s\ge0\). The Jacobian is \(\sin\theta_v\), and the sublevel region \((u\cdot a_v)r+(u\cdot b_v)s\le t\) is a right triangle in the \((r,s)\) chart. Its physical area is \(\sin\theta_v\,t^2/[2(u\cdot a_v)(u\cdot b_v)]\). The Poisson void probability immediately gives the stated Rayleigh-type survival law and, for any family of sublevel triangles, their *union-area* joint law.

Different vertex processes are independent. If two edges share \(v\), their positive-threshold sublevel triangles overlap in a positive-area neighborhood of the origin. The joint survival of \(H_{v,e}\) and \(H_{v,f}\) is therefore strictly larger than the product of their survival probabilities for every positive pair of thresholds. Integrating the resulting positive survival difference over thresholds proves \(\operatorname{Cov}(H_{v,e},H_{v,f})>0\). The other endpoints of these two distinct edges have independent processes, so the two edge-sums also have strictly positive covariance. If the graph is a matching, different sums use disjoint processes and are independent. This proves the exact independence criterion.

**4. Small-\(t\) law.** At a single edge, the two independent corner deficits have densities \(2\gamma_{v,e}s e^{-\gamma_{v,e}s^2}\) and \(2\gamma_{w,e}s e^{-\gamma_{w,e}s^2}\). Integrating their product over \(s+r\le t\) gives \(\gamma_{v,e}\gamma_{w,e}t^4/6+O(t^6)\). For two different edges, the intersection of the two low-sum events requires a point of bounded cost at *at least three distinct vertices*; its probability is \(O(t^6)\), even if the two edges share a vertex. Finite inclusion-exclusion gives the first sharp law.

**5. Two-point tail.** For each ordered neighborhood pair \((v,w)\) of a diameter edge, the measure of \(\{(z,q)\in C_v\times C_w: u_{v,e}\cdot z+u_{w,e}\cdot q\le\varepsilon\}\), normalized by \(A^2\), equals \(\gamma_{v,e}\gamma_{w,e}\varepsilon^4/6\), since it is a four-dimensional linear simplex. There are two orders for each unordered edge. The Taylor remainder shifts the integration boundary by \(O(\varepsilon^2)\) uniformly in each scaled cone neighborhood; integrating gives an \(O(\varepsilon^5)\) remainder. Compactness excludes all other neighborhoods, yielding the second law.

**6. Two-edge-star example.** The apex \((0,2)\) has incident inward edge rays \((-1,-2)/\sqrt5\) and \((1,-2)/\sqrt5\), whose determinant has magnitude \(4/5\). For either diametral direction its dot products with these rays are \(1\) and \(3/5\), and \(A=2\), so \(\gamma=1/3\). At either base corner the corresponding rays have sine \(2/\sqrt5\), projection products \(1/\sqrt5\), giving \(\gamma=1/2\). Substitution into the two general small-tail coefficients gives \(1/18\) and \(1/9\).

## Verification
The accompanying `verify_diameter_graph.py` recomputes the cone coefficients and both leading-tail constants for the nonregular two-diameter triangle, the equilateral triangle (a known special case), and a rectangle whose diameter graph is a matching. It also checks a positive-measure overlap between the two apex sublevel triangles. Running `python verify_diameter_graph.py` returns `ALL_CHECKS_PASSED`. These finite and algebraic checks supplement, but do not replace, the full Poisson convergence proof above.

## Relationship to prior work
Wei Lao (2010), Section 6.4 and Theorem 6.8, establishes the corresponding diameter limit for **regular polygons with an even number of sides**, where the diametral vertex pairs are disjoint, and explicitly identifies disjoint diametral endpoints as a crucial independence hypothesis. The present theorem accommodates *arbitrary convex polygons and shared endpoints*, identifies the full incidence-dependent joint law and gives geometric two-point-tail constants.

Appel, Najim and Russo (2002) derive limits under geometric assumptions including a unique major axis; only the abstract and subsequent detailed descriptions were accessible for this comparison, so stronger unstated coverage remains a priority risk. Schrempp (public preprint September 12, 2017) treats smooth-boundary bodies with a unique diameter and a different curvature-controlled scaling, not corner cones and multiple diametral pairs. An earlier exact equilateral-triangle corner-process calculation is a strict special case and is not claimed as new; the genuine extension here is the arbitrary polygon diameter-graph dependence classification and its nonregular realizations.

## Limitations
The limit is for a *fixed* convex polygon and area-uniform samples. It does not describe smooth curved bodies, distributions with vanishing/inhomogeneous density at vertices, polygon sequences changing with sample size, or finite-sample exact diameter distributions. Historical priority is unresolved for inaccessible portions of the 2002 paper and other specialized distance-extreme literature. No independent review or certification has been performed.

## References
1. M. Schrempp, *Limit laws for the diameter of a set of random points from a distribution supported by a smoothly bounded set*, arXiv:1709.03706, initial public version 2017-09-12, https://arxiv.org/abs/1709.03706 .
2. W. Lao, *Some Weak Limit Laws for the Diameter of Random Point Sets in Bounded Regions*, KIT Scientific Publishing, 2010, Section 6.4 / Theorem 6.8, https://doi.org/10.5445/KSP/1000019800 .
3. M. J. B. Appel, C. A. Najim, R. P. Russo, *Limit laws for the diameter of a random point set*, Adv. Appl. Probab. 34 (2002), 1–10, https://doi.org/10.1239/aap/1019160946 .
