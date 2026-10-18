# Exact corner law for circumradii of boundary-random polygonal triangles

## Finding

Let \(K\subset\mathbb R^2\) be a nondegenerate convex polygon with \(m\ge3\) genuine vertices, perimeter \(L>0\), and interior angles \(\theta_1,\ldots,\theta_m\in(0,\pi)\). Choose \(X_1,X_2,X_3\) independently and uniformly with respect to Euclidean arclength on \(\partial K\), and let \(\rho\) be their triangle's Euclidean circumradius, with \(\rho=+\infty\) for collinear triples. There exists \(t_K>0\) such that **for every** \(0\le t<t_K\), not just asymptotically,

\[
\Pr(\rho\le t)=\frac{16t^3}{L^3}\sum_{i=1}^m\frac{(1+\cos\theta_i)^2}{\sin\theta_i}.
\tag{1}
\]

Thus the entire sufficiently small circumradius distribution is exactly cubic. Its coefficient depends only on the perimeter and the corner angles, not individually on the side lengths.

The scale-free coefficient \(B(K)=\lim_{u\downarrow0}u^{-3}\Pr(\rho\le uL)\) satisfies the sharp inequality

\[
B(K)=16\sum_{i=1}^m\frac{(1+\cos\theta_i)^2}{\sin\theta_i}
\ \ge\ \frac{32m\sin^3(\pi/m)}{\cos(\pi/m)},
\tag{2}
\]

with equality **if and only if** \(K\) is equiangular. For a regular \(m\)-gon of circumradius \(R\), the coefficient in (1) simplifies exactly to \(4/(m^2R^3\cos(\pi/m))\); in particular \(m^2R^3\lim_{t\downarrow0}t^{-3}\Pr(\rho\le t)\to4\) as \(m\to\infty\).

## Assumptions and scope

A genuine vertex means that consecutive edges are not collinear; any collinear intermediate points in a polygonal representation must first be omitted. All polygons are fixed, compact, convex, two-dimensional, and have finitely many sides. The samples are independent, and each side receives probability proportional to its Euclidean length. Circumradius is defined by the unique circle through three noncollinear points, and assigned \(+\infty\) for collinear triples. Such triples have **positive** probability when all three points fall on one polygon side; the convention makes the unconditional distribution in (1) well defined. The existence of \(t_K\) is asserted for each fixed polygon; it need not be uniform as the polygon degenerates or the number of its sides increases. Formula (1) is **not** claimed for arbitrary \(t\).

## Proof

**1. Only two incident sides matter at small radius.** A triangle with circumradius at most \(t\) has all pairwise vertex distances at most \(2t\), by the extended sine law. Consider a sequence of such triples with \(t\downarrow0\). By compactness of \(\partial K\), a subsequence of all three points converges to one boundary point \(x\). If \(x\) lies in the relative interior of an edge, eventually all three points lie on that same edge, so their circumradius is \(+\infty\), a contradiction. Hence \(x\) is a vertex. Near a genuine vertex exactly its two incident sides occur; since the triangle is noncollinear, exactly two sample points must lie on one incident side and the third on the other. If this description failed for arbitrarily small positive \(t\), such a sequence would exist, so there is a positive localization threshold.

At a vertex of angle \(\theta\), write distances along the two rays as \(a,b,c\ge0\), with \(a,b\) on the first ray and \(c\) on the second. The distance between a point on one ray and a point on the other is at least the first point's distance from the vertex multiplied by \(\sin\theta\), and likewise for the other point. Since each pairwise distance is at most \(2t\), the three ray coordinates are at most \(2t/\sin\theta\). Taking the localization threshold smaller if necessary makes every such qualifying triple lie strictly before the far endpoints of the corresponding polygon sides. Thus the exact local probability can be computed on infinite rays and added over vertices without double-counting.

**2. One corner integral.** Choose ray directions \((1,0)\) and \((\cos\theta,\sin\theta)\) and write \(q=\cos\theta\), \(s=\sin\theta>0\). Apart from the null set \(a=b\), the area and side-length formula for the circumradius gives

\[
\rho(a,b,c)=\frac{\sqrt{a^2+c^2-2acq}\,\sqrt{b^2+c^2-2bcq}}{2cs}.
\tag{3}
\]

Let \(I_\theta(t)\) denote the three-dimensional Lebesgue measure of \(\{(a,b,c)\in(0,\infty)^3:\rho(a,b,c)\le t\}\). Substitute \(a=cu\), \(b=cv\), whose Jacobian is \(c^2\). With \(D(u)=\sqrt{u^2-2qu+1}\), equation (3) becomes \(\rho=cD(u)D(v)/(2s)\). Tonelli's theorem therefore yields

\[
\begin{aligned}
I_\theta(t)
&=\int_0^\infty\int_0^\infty\int_0^{2st/[D(u)D(v)]}c^2\,dc\,du\,dv\\
&=\frac{8s^3t^3}{3}\left[\int_0^\infty(u^2-2qu+1)^{-3/2}\,du\right]^2.
\end{aligned}
\tag{4}
\]

Because \(s^2=1-q^2\), direct differentiation gives

\[
\int_0^\infty(u^2-2qu+1)^{-3/2}\,du
=\left[\frac{u-q}{s^2\sqrt{(u-q)^2+s^2}}\right]_0^\infty
=\frac{1+q}{s^2}.
\tag{5}
\]

Consequently,

\[
I_\theta(t)=\frac{8t^3}{3}\frac{(1+\cos\theta)^2}{\sin\theta}.
\tag{6}
\]

**3. Sampling factors.** Each ordered triple of arclength coordinates has joint density \(L^{-3}\). For one vertex there are three choices of the sample on the second side when the first side is doubled, and three choices when the second side is doubled. Both integrals equal (6). Thus that vertex contributes \(6I_\theta(t)/L^3\). Summing and using (6) proves (1) for all sufficiently small \(t\), as claimed.

**4. Sharp shape ordering.** Write each exterior turning angle as \(\delta_i=\pi-\theta_i\in(0,\pi)\), so \(\sum_i\delta_i=2\pi\). Then

\[
\frac{(1+\cos\theta_i)^2}{\sin\theta_i}=f(\delta_i),\qquad
f(\delta)=\frac{2\sin^3(\delta/2)}{\cos(\delta/2)}.
\]

Putting \(z=\tan(\delta/2)>0\), one has \(f(\delta)=2z^3/(1+z^2)\) and

\[
f''(\delta)=z(1+z^2)+\frac{2z}{1+z^2}>0.
\tag{7}
\]

Strict Jensen gives \(\sum_i f(\delta_i)\ge m f(2\pi/m)\), with equality exactly when all exterior angles are \(2\pi/m\), equivalently when \(K\) is equiangular. This proves (2). For the regular \(m\)-gon, \(L=2mR\sin(\pi/m)\) and \(f(2\pi/m)=2\sin^3(\pi/m)/\cos(\pi/m)\); substituting into (1) yields \(4/(m^2R^3\cos(\pi/m))\). Since \(\cos(\pi/m)\to1\), the final limit follows.

## Verification

The elementary local integral was independently checked numerically at angles \(60^\circ\), \(90^\circ\), and \(120^\circ\) by integrating its factored one-dimensional kernel and by quasi-Monte-Carlo integration over ray triples. Direct arclength sampling on a square, an equilateral triangle, and an irregular convex pentagon also agreed with the exact probabilities at radii small enough for localization. The included reproducibility script uses only the Python standard library and checks the integral, the regular-polygon simplification, strict Jensen behavior, and independent polygon-boundary simulations. Finite numerical tests corroborate, but do not substitute for, the proof for all polygons and small radii.

## Relationship to prior work

Péter Kórus, *Average Values of Triangles* (2020), studies triangles from uniformly selected points on a fixed circle and triangles with randomly selected side lengths subject to fixed perimeter; its circumradius computations use a different random object. Gilbert Labelle, *Probability distributions arising from isoperimetric random triangles* (2023), derives circumradius distributions when the **side-length triple**, not the vertices of a fixed polygon, is sampled. Werner's 2022 survey concerns random polygonal approximations of convex bodies and supplies background for boundary sampling, not (1). The present exact polygonal corner law is not a consequence of the small-circumradius expansion for **interior-uniform** samples in smooth bodies or the short pair-distance law for **two** polygon-boundary points: the sample space, event and dimensional tail exponent differ.

## Limitations

No claim is made about the full distribution for larger radii, a uniform positive radius threshold across all polygons, smooth-boundary sampling laws, or independent publication/certification. The coefficient's strict minimization concerns **fixed side count and the scale-free local distribution**, not an arbitrary finite-radius stochastic ordering. Unindexed equivalent formulae in the geometric-probability literature may exist.

## References

1. P. Kórus, *Average Values of Triangles*, Fundamental Journal of Mathematics and Applications 3(1) (2020), 57–60. DOI: 10.33401/fujma.692916. First publicly available 2020-06-10.
2. G. Labelle, *Probability distributions arising from isoperimetric random triangles*, Maple Transactions 3(4), article 17136 (2023). DOI: 10.5206/mt.v3i4.17136.
3. E. M. Werner, *Floating bodies and approximation of convex bodies by polytopes*, Probability Surveys 19 (2022), 113–128. DOI: 10.1214/22-PS5.
