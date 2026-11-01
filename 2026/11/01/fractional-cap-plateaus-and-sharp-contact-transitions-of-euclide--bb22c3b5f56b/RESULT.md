# Fractional-cap plateaus and sharp contact transitions of Euclidean cube circumballs

## Finding

For any integer \(n\ge2\) and real \(0\le t\le n\), define the **uniformly capped cube**
\[
K_{n,t}=\left\{x\in[0,1]^n:\sum_{i=1}^n x_i\le t\right\}.
\]
Write \(t=m+\delta\) with \(m=\lfloor t\rfloor\) and \(0\le\delta<1\). (At \(t=n\), take \(m=n\) and \(\delta=0\).) The unique minimum-radius Euclidean ball containing \(K_{n,t}\) has center \(c_{n,t}\mathbf1\). Its center coordinate and squared radius are exactly
\[
\boxed{\begin{aligned}
2m\ge n:\quad & c_{n,t}=\tfrac12,\qquad R_{n,t}^2=\tfrac n4;\\[2pt]
2m<n:\quad & c_{n,t}=\operatorname{median}\left\{\frac mn,\frac\delta2,\frac{m+\delta}{n}\right\},\\
& R_{n,t}^2=nc_{n,t}^2+
\max\left\{m(1-2c_{n,t}),\ m+\delta^2-2(m+\delta)c_{n,t}\right\}.
\end{aligned}}
\tag{1}
\]
When \(\delta=0\), the second expression inside the maximum is identical to the first and is harmless. The median of three numbers is their middle order statistic, with endpoint ties allowed.

The radius in the nonsaturated range has the following sharp **three-branch interpretation**. For \(m<n/2\), put \(a=m/n\), \(b=(m+\delta)/n\), and \(q=\delta/2\):
\[
\boxed{\begin{array}{c|c|c}
\text{condition}&c_{n,t}&R_{n,t}^2\\\hline
q\le a&a&m-m^2/n\\
a\le q\le b&q&m(1-\delta)+n\delta^2/4\\
b\le q&b&m+\delta^2-(m+\delta)^2/n
\end{array}}
\tag{2}
\]
The formulas agree at every shared boundary. For \(1\le m<n/2\), the first condition is precisely \(0\le\delta\le2m/n\), so the enclosing radius has a **nontrivial exact plateau** immediately after the integer cap \(t=m\). If \(n>2\), the next transition occurs at \(\delta=2m/(n-2)\) when this number is at most one. In particular, for \(n=8\), \(m=2\), the plateau persists from \(t=2\) through \(t=5/2\); the mixed region continues to \(t=8/3\), and the final region follows the fractional-contact law.

**Complete contact classification.** If \(2m<n\) and \(0<\delta<1\), each cube vertex of Hamming weight \(m\) lies on the optimal sphere precisely when \(c_{n,t}\ge\delta/2\), and each fractional vertex with \(m\) unit coordinates, one coordinate \(\delta\), and the remainder zero lies on the sphere precisely when \(c_{n,t}\le\delta/2\). All vertices at smaller integer weights are strictly inside (except the zero-cap singleton). If \(\delta=0\) in this range, precisely the binary weight-\(m\) vertices contact. If \(2m\ge n\), **every admitted binary vertex** contacts, while any genuinely fractional vertex lies strictly inside.

## Assumptions and scope

The Euclidean norm is the ordinary coordinate norm on \(\mathbb R^n\); neither an affine image nor a weighted knapsack constraint is asserted to obey (1). The body may be a singleton at \(t=0\); no full-dimensionality hypothesis is needed. All boundary values of \(\delta\), all integer caps, and every dimension \(n\ge2\) are included. A 'fractional vertex' means a vertex with exactly one coordinate strictly between zero and one, possible only when \(\delta>0\). The radius and contact points refer to the smallest enclosing ball, **not** the largest inscribed ball or the minimum-volume enclosing ellipsoid.

## Proof

**1. Identify every vertex.** The defining inequalities are the \(2n\) coordinate bounds and one rank inequality. At a vertex, either all coordinates are at bounds, giving a binary vector with weight at most \(m\), or the rank inequality is active and at least \(n-1\) coordinates are at bounds. Hence when \(\delta>0\) every nonbinary vertex has exactly \(m\) coordinates equal to one, one coordinate equal to \(\delta\), and the others zero. Conversely, all these points are vertices (unless the inequality is redundant at the cube endpoint). This description also holds for \(t=0\), with just the origin. A squared-distance function is convex, so its maximum over the polytope occurs at a vertex.

**2. Reduce the global minimax problem to one variable.** The squared enclosing radius as a function of an arbitrary ball center \(z\) is
\[
F(z)=\max_{x\in K_{n,t}}\|x-z\|^2
=\|z\|^2+\max_{x\in K_{n,t}}(\|x\|^2-2\langle z,x\rangle).
\]
As a positive-definite quadratic plus a convex function, \(F\) is strictly convex and coercive, so it has a unique minimizer. Coordinate permutations preserve the body, hence that minimizer must be \(c\mathbf1\). If \(c<0\), replacing it by zero decreases the distance to every point of \(K_{n,t}\subseteq[0,1]^n\), so \(c\ge0\). If \(c>1/2\), the origin alone gives \(F(c\mathbf1)\ge nc^2>n/4\), whereas the cube's center \(\mathbf1/2\) encloses the whole cube with squared radius \(n/4\). Therefore the unique optimum satisfies \(0\le c\le1/2\).

**3. Exact farthest-distance envelope.** A binary vertex of weight \(j\le m\) has squared distance \(nc^2+j(1-2c)\). For \(0\le c\le1/2\), this is largest when \(j=m\), while a fractional vertex has squared distance
\[
nc^2+m+\delta^2-2(m+\delta)c.
\]
For \(\delta=0\) the two formulas coincide. Thus, for all \(c\in[0,1/2]\),
\[
F(c\mathbf1)=nc^2+
\max\left\{m(1-2c),m+\delta^2-2(m+\delta)c\right\}.
\tag{3}
\]
The two affine branches in the maximum cross at \(c=\delta/2\); for \(c<\delta/2\) the fractional branch is larger, and for \(c>\delta/2\) the binary branch is larger.

**4. Optimize and certify globality.** The binary-branch quadratic has its unconstrained minimizer at \(a=m/n\). The fractional-branch quadratic has its unconstrained minimizer at \(b=(m+\delta)/n\), with \(a\le b\). If \(2m<n\), both \(a<1/2\) and the branch crossing \(q=\delta/2\le1/2\) are in the permitted range. Directly comparing the signs of the one-sided derivatives at the crossing yields the minimizer \(c=\operatorname{median}\{a,q,b\}\). Evaluating (3) gives exactly (1) and (2). If instead \(2m\ge n\), the binary-branch quadratic is nonincreasing throughout \([0,1/2]\), and the fractional branch has slope no greater than it at \(c=1/2\), so the maximum is minimized at the endpoint \(c=1/2\). Then every admitted binary vertex lies at distance \(\sqrt n/2\), while a fractional vertex has squared distance \(n/4-\delta(1-\delta)<n/4\). This gives the saturated branch and all endpoint cases. Strict convexity proved in Step 2 makes the center unique.

For completeness, an independent geometric optimality certificate is available: average each orbit of contact vertices over all coordinate permutations. The average has coordinate value equal to its coordinate sum divided by \(n\). In the binary-only region the contact orbit mean is \(m/n=c\); in the fractional-only region it is \((m+\delta)/n=c\); in the mixed region \(c\) lies between these means and is their convex combination; in the saturated region \(1/2\) lies between zero and \(m/n\), and the origin and binary rank-\(m\) orbits contact. Therefore the proposed center always lies in the convex hull of the contacting vertices, a standard independent certificate for the minimal enclosing ball.

**5. Contact sets and plateau.** For \(2m<n\), equation (3) tells exactly which of the binary rank-\(m\) and fractional orbits meet the sphere. Since \(c<1/2\) here, every integer weight \(j<m\) is strictly interior. At \(m<n/2\), \(q\le a\) is equivalent to \(\delta\le2m/n\), giving the constant radius-square \(m-m^2/n\). The second crossing \(q=b\) is equivalent, for \(n>2\), to \(\delta=2m/(n-2)\), proving the remaining assertions. At a crossing both respective contact orbits touch; there is no numerical or generic-position exception.

## Verification

Run `python3 verify.py` with Python 3 standard library only. The checker uses exact rational arithmetic to enumerate all vertices in 333 combinations of dimensions \(2\le n\le10\), integer caps and selected fractional offsets, verifying every claimed farthest-vertex inequality (103,420 exact vertex distances). It separately verifies the convex-hull contact certificate using orbit means and identifies 63,032 sampled contact vertices. These finite checks are independent corroboration of formulas (1)–(3), not a substitute for the all-dimensional proof. The formulas can be computed in constant arithmetic time once \(n\) and \(t\) are given.

## Relationship to prior work

Gunluk's 2026 work studies deterministic **volume approximation** for cubes clipped by linear and more general separable convex constraints, and introduces the same natural class of knapsack polytopes; it does not derive their exact Euclidean enclosing-ball center/radius. The full HTML version's Theorems 1.2–1.4 and Sections 1–3 address volume approximation and counting, not the minimax problem here.

Published treatments of the **John inscribed ellipsoid of a capped cube** solve an entirely different extremal problem, though for precisely the same body and all real caps. The **Löwner minimum-volume outer ellipsoid of rank-selected Boolean polytopes** treats only convex hulls of zero-one layers: it does not cover the noninteger cap's fractional extreme points, and a nonspherical minimum-volume ellipsoid does not determine a minimum-radius ball. General results on the minimum enclosing sphere of **matroid independence polytopes** already cover the integer-rank uniform-matroid specialization; novelty is **not claimed** for that older integer-only case. They cannot by their Boolean-vertex argument imply the fractional-orbit transition or the positive-length plateau immediately after integer caps. In the same family, weighted capped-cube illumination results address another invariant rather than enclosing radii. Classical smallest-enclosing-sphere algorithms give general optimization procedures but not the displayed explicit all-dimensional fractional-cap branch and contact classification.

## Limitations

This is a theorem for equal coefficient caps, the coordinate Euclidean metric and one clipping inequality. Arbitrary weights, other norms, multiple clipping constraints, and unequal coordinate intervals are not covered. The proof is analytic and does not require the checker to terminate on an infinite class of examples. Historical priority beyond the specifically compared papers and records is provisional, particularly under Chebyshev approximation or continuous knapsack terminology. Independent validation has not been performed.

## References

1. Kyra Gunluk, *Deterministic Volume Estimation of Truncated Hypercubes*, arXiv:2605.19809v1, first publicly posted 2026-05-19; v2 2026-10-15, Sections 1–3, https://arxiv.org/html/2605.19809v2.
2. *Three-phase John ellipsoid of a capped hypercube* (2026), publicly available geometric result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-three-phase-john-ellipsoid-of-a-capped-hypercube--9b8726b32127.
3. *Exact Löwner ellipsoids of arbitrary rank-selected Boolean polytopes* (2026), publicly available geometric result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-l-wner-ellipsoids-of-arbitrary-rank-selected-boolean-polyt--3c04f47dc8c3.
4. *Sharp minimum-sphere bounds for matroid independence polytopes distinguish uniform density from arboricity two* (2026), publicly available geometric result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-minimum-sphere-bounds-for-matroid-independence-polytopes-d--8fea8c7015da.
