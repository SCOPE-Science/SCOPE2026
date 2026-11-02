# Small-error advantage and large-error disadvantage of irregular polygons in random boundary approximation

## Finding
Let \(Q\) be a convex Euclidean polygon with \(m\ge 4\) genuine vertices, perimeter \(P\), and interior angles \(\alpha_1,\ldots,\alpha_m\in(0,\pi)\). Independently choose \(n\) points uniformly in arclength from \(\partial Q\), and let \(Q_n\) be their convex hull. Put \(T_n(Q)=n\,d_H(Q,Q_n)/P\). Let \(H_Q(t)=\lim_{n\to\infty}\Pr(T_n(Q)\le t)\), which exists for every \(t>0\) by the cited Poisson-wedge limit theorem.

Define \(\ell(\alpha)=1\) for \(0<\alpha\le\pi/2\) and \(\ell(\alpha)=1/\sin\alpha\) for \(\pi/2<\alpha<\pi\). Write \(\alpha_{\min}=\min_i\alpha_i\). Then the following two **sharp endpoint laws** hold:
\[
\lim_{t\downarrow0}\frac{H_Q(t)}{(2t)^m}=\prod_{i=1}^m\ell(\alpha_i),\qquad
\lim_{t\to\infty}-\frac1t\log(1-H_Q(t))=\frac{2}{\cos(\alpha_{\min}/2)}.
\]
The large-error decay rate therefore determines the smallest interior angle. Let \(R_m\) be any regular \(m\)-gon; its limiting CDF \(H_{R_m}\) is computed using the same perimeter normalization. For **every non-equiangular** \(Q\) with \(m\ge4\), there exist \(0<t_-<t_+<\infty\) such that
\[
H_Q(t)>H_{R_m}(t)\quad(0<t<t_-),\qquad
H_Q(t)<H_{R_m}(t)\quad(t>t_+).
\]
Thus the normalized limiting Hausdorff errors are incomparable in first-order stochastic order. Their small-error preference and their extreme-tail preference point in opposite directions. The same strict inequalities hold for the finite-\(n\) CDFs at each fixed threshold in these ranges for all sufficiently large \(n\) (depending on the threshold).

## Assumptions and scope
All angles are genuine, strictly between zero and \(\pi\); no adjacent collinear polygon sides are counted as distinct. All samples are independent with the uniform arclength law on the boundary. All geometry and distances are Euclidean. The limit first fixes \(Q\) and then takes \(n\to\infty\); the small- and large-threshold limits are taken in that limiting law, not jointly with \(n\). Scale disappears through perimeter normalization. A comparison regular polygon need not have the same scale because of the normalization.

## Proof
**Step 1: published Poisson-wedge limit, with an explicit equivalent representation.** The 2024 preprint of Prochno, Schütt, Sonnleitner and Werner proves the product limit for the random boundary convex-hull Hausdorff error. In the corresponding tangent wedge of interior angle \(\alpha\), the two nearest arclength distances along the independent limiting Poisson rays are independent unit exponential variables \(E,F\). All farther points on the same rays are redundant for the distance of the origin to their convex hull. Choose unit vectors \(u,v\) enclosing \(\alpha\) and define
\[
D_\alpha=\operatorname{dist}(0,[Eu,Fv]),\qquad
G_\alpha(t)=\Pr(D_\alpha\le t).
\]
The cited Poisson-process convergence and independence at distinct vertices yield \(H_Q(t)=\prod_{i=1}^mG_{\alpha_i}(t)\). This is a restatement of the published product law, **not** the new assertion. Here \([a,b]\) is the closed line segment joining the two displayed points.

**Step 2: sharp lower-tail coefficient.** For any \(x,y>0\), every point on \([xu,yv]\) has norm at least \(\min(x,y)\cos(\alpha/2)\). In fact, writing a convex-combination point as \(a u+b v\) with \(a,b\ge0\), the squared norm equals \((a+b)^2\cos^2(\alpha/2)+(a-b)^2\sin^2(\alpha/2)\), and \(a+b\ge\min(x,y)\). Consequently, \(D_\alpha\le t\) requires \(\min(E,F)\le t/\cos(\alpha/2)\). The event in which both exponentials are this small has probability \(O_\alpha(t^2)\). With the opposite exponential held at a fixed positive value and the smaller one going to zero, the nearest-point geometry gives
\[
\lim_{y\downarrow0}\frac{\operatorname{dist}(0,[xu,yv])}{y}
=c_\alpha:=\begin{cases}1&\alpha\le\pi/2,\\ \sin\alpha&\alpha>\pi/2.\end{cases}
\]
For justification of the first-order probability, integrate the density of \(E,F\) over the two strips \(\{E\le t/\cos(\alpha/2)\}\) and \(\{F\le t/\cos(\alpha/2)\}\), subtract their \(O(t^2)\) overlap, and rescale the small coordinate by \(t\). Dominated convergence follows from the displayed global lower bound and bounded exponential densities. Each strip contributes \(t/c_\alpha+o(t)\), so \(G_\alpha(t)=2\ell(\alpha)t+o(t)\). Multiplying over the fixed number of vertices proves the first endpoint law.

**Step 3: exact large-deviation exponent.** For any deterministic \(x,y>0\), one can choose the point \(xy(u+v)/(x+y)\) on \([xu,yv]\), obtaining
\[
\operatorname{dist}(0,[xu,yv])\le\frac{2xy}{x+y}\cos(\alpha/2)
\le\frac{x+y}{2}\cos(\alpha/2).
\]
The bound from Step 2 supplies the reverse comparison \(\operatorname{dist}(0,[xu,yv])\ge\cos(\alpha/2)\min(x,y)\). Set \(\lambda_\alpha=2/\cos(\alpha/2)\). These two inequalities and the exponential and gamma tail formulas give, for all \(t>0\),
\[
e^{-\lambda_\alpha t}\le\Pr(D_\alpha>t)\le(1+\lambda_\alpha t)e^{-\lambda_\alpha t}.
\]
Taking logarithms shows \(-t^{-1}\log\Pr(D_\alpha>t)\to\lambda_\alpha\). Since the number of vertices is fixed and
\[
\max_i\Pr(D_{\alpha_i}>t)\le1-H_Q(t)
\le\sum_i\Pr(D_{\alpha_i}>t),
\]
the second endpoint law follows; \(\lambda_\alpha\) is strictly increasing with \(\alpha\). Thus the slowest tail is determined exactly by the smallest interior angle.

**Step 4: strict crossing.** The mean interior angle is \(\bar\alpha=(m-2)\pi/m\ge\pi/2\). Define \(g(\alpha)=\log\ell(\alpha)\). This function is constant zero on \((0,\pi/2]\), equals \(-\log\sin\alpha\) on \((\pi/2,\pi)\), is convex throughout, and strictly convex wherever \(\alpha>\pi/2\). By the polygon angle sum and Jensen's inequality,
\[
\sum_i g(\alpha_i)>m g(\bar\alpha)
\]
for every nonconstant angle vector: equality in Jensen would require all angles to lie in the flat interval or all equal, and the former is impossible for a non-equiangular polygon when \(m\ge4\). The small-threshold coefficients therefore satisfy
\[
\lim_{t\downarrow0}\frac{H_Q(t)}{H_{R_m}(t)}=
\frac{\prod_i\ell(\alpha_i)}{\ell(\bar\alpha)^m}>1.
\]
On the other hand, nonconstant angles give \(\alpha_{\min}<\bar\alpha\). Step 3 makes the survival probability \(1-H_Q(t)\) exponentially larger than \(1-H_{R_m}(t)\) for large \(t\), so the CDF inequality reverses. Continuity of the CDFs supplies strict inequalities throughout sufficiently small and sufficiently large threshold ranges. Weak convergence at any fixed positive threshold transfers either strict inequality to all sufficiently large finite sample sizes. This proves every assertion.

## Verification
The standalone source file `checks/wedge_crossing_check.py` independently integrates the two-exponential wedge law by conditioning on their sum and checks the small-ball coefficient and a concrete crossing. It uses the distance to the actual segment, including cases where the closest point is an endpoint. Run `python checks/wedge_crossing_check.py` in an environment with NumPy and SciPy. Proof is analytic; these finite numerical checks are diagnostics, not a proof or uniqueness certificate.

In particular, for a square versus a rhombus with interior angles \(\pi/3,2\pi/3,\pi/3,2\pi/3\), the small-threshold CDF ratio (rhombus divided by square) tends to \(4/3\). Their respective exact large-survival exponential rates are \(2\sqrt2\) and \(4/\sqrt3\). Both strict orderings follow without numerical approximations.

## Relationship to prior work
The complete *limiting distribution* of the Hausdorff error under uniform boundary sampling is already proved in Prochno–Schütt–Sonnleitner–Werner, arXiv:2404.02870v1 (first public April 3, 2024), Theorem 1 and its proof. The present finding does **not** claim that product formula as new. Its comparison theorem, strict all-polygon small-versus-large threshold crossing, sharp small-ball coefficients, and exact exponential tail rates arise from additional geometric estimates and angle-sum convexity; they are not explicit in the inspected preprint's theorem, corollaries, remarks, or proof. The existing bound for tails in that paper is qualitative/exponential up to nonsharp constants. Other random-polytope Hausdorff work, including Brunel (2019), treats concentration and rates rather than the stated all-angle-vector crossing. Indexed related research on regular-polygon Gumbel transitions concerns a different double limit and does not establish this nonregular comparison.

## Limitations
This result builds on an existing full asymptotic distribution and is a *new comparison/asymptotic consequence*, not a new distribution theorem. Historical priority is not exhaustively certified, and an inaccessible full manuscript from an indexed related finding could conceal a comparison. The CDF crossing statement is only asserted for the limiting laws and, at fixed thresholds, eventually in sample size; neither a unique crossing point nor a uniform finite-sample crossing threshold is proved. Nothing is claimed for interior sampling, smooth convex curves, or polygon families whose vertex count grows with sample size.

## References
1. J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870v1 (2024-04-03), https://arxiv.org/abs/2404.02870 ; published in *Mathematische Annalen* (2025), DOI:10.1007/s00208-025-03186-7.
2. V.-E. Brunel, *Uniform behaviors of random polytopes under the Hausdorff metric*, *Bernoulli* 25 (2019), 1770–1793, DOI:10.3150/18-BEJ1035.
3. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, *Discrete & Computational Geometry* 69 (2023), 453–504, arXiv:1911.05917.
