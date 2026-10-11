# Clipped-curvature minimax sampling for Hausdorff and area approximation of convex curves

## Finding
Let \(K\subset\mathbb R^2\) have strictly convex \(C^3\) boundary with strictly positive curvature \(\kappa(s)\), where \(s\) denotes arclength. Let \(P_n(f)\) be the convex hull of \(n\) independent samples drawn from \(\partial K\) with respect to a continuous density \(f>0\), normalized by \(\int f\,ds=1\). Put
\[
V=\int_{\partial K}\sqrt\kappa\,ds,\qquad Z=\int_{\partial K}\kappa^{1/3}\,ds.
\]
For every such density the following leading expectation limits hold:
\[
\lim_{n\to\infty}\left(\frac{n}{\log n}\right)^2\mathbb E\,d_H(P_n(f),K)=\frac18\max_{\partial K}\frac{\kappa}{f^2},
\]
\[
\lim_{n\to\infty}n^2\mathbb E\bigl(|K|-|P_n(f)|\bigr)
=\frac12\int_{\partial K}\frac{\kappa}{f^2}\,ds.
\]
Normalize the two leading coefficients by their independent minima, \(V^2/8\) and \(Z^3/2\), and denote the resulting ratios by \(R_H(f)\) and \(R_A(f)\). These ratios are at least one. If \(K\) is a disk, their minimax value is one and the unique minimizer is uniform arclength sampling.

For noncircular \(K\), define
\[
d\mu=\frac{\sqrt\kappa}{V}\,ds,\quad a=\kappa^{-1/2},\quad m=\int a^{1/3}\,d\mu,\quad t_A=\min\frac{a^{1/3}}m<1.
\]
For every \(t_A<t<1\), there is a unique \(c_t>0\) satisfying
\[
\int\max\{t,c_t a^{1/3}\}\,d\mu=1.
\]
Write \(q_t=\max\{t,c_t a^{1/3}\}\) and \(F(t)=m^{-3}\int a q_t^{-2}\,d\mu\). The function \(F\) is continuous and strictly increasing from \(F(t_A)=1\) to \(F(1)=m^{-3}\int a\,d\mu>1\) (with endpoint definitions understood by continuity). Hence there is a unique \(t_*\in(t_A,1)\) solving
\[
F(t_*)=t_*^{-2}.
\]
The unique minimizer of \(\max\{R_H(f),R_A(f)\}\) among all positive continuous densities is
\[
\boxed{f_*(s)=\frac{\sqrt{\kappa(s)}}V\max\{t_*,c_{t_*}\kappa(s)^{-1/6}\}},
\]
with exact optimal value \(\boxed{t_*^{-2}=F(t_*)>1}\). The two normalized errors balance at this density; a nonempty open portion of the boundary lies on the sampling-density floor \(f_*=t_*\sqrt\kappa/V\). In particular, the optimizer is in general *clipped*, rather than a single power of curvature.

## Assumptions and scope
The body is planar, strictly convex, with \(C^3\) boundary and curvature bounded away from zero. The sampling density is continuous and everywhere strictly positive; piecewise smooth densities, including the displayed optimizer, are allowed. All expectations use one fixed density as \(n\to\infty\). The normalizations compare the two errors at their separate asymptotic optima. They do not compare unnormalized quantities with different physical units and different powers of \(n\).

## Proof
**Step 1: expected missed area.** Every sample point is a vertex of the inscribed random polygon. An arclength gap of length \(\ell\) beginning at \(s\) cuts off area
\[
\frac{\kappa(s)}{12}\ell^3+O_K(\ell^4)
\]
uniformly on the compact curve. Use the cumulative probability coordinate \(u=\int_0^s f(v)\,dv\), interpreted periodically. Then \(\ell=\Delta u/f(s)+o(\Delta u)\) uniformly. Uniform points on the probability circle have exchangeable circular spacings; each gap has beta distribution with third moment \(6/[n(n+1)(n+2)]\). Rotational invariance makes a chosen gap independent of its starting coordinate. Consequently, taking expectation of the sum of the \(n\) cubic segment terms gives
\[
\frac1{12}\frac{6n}{n(n+1)(n+2)}\int_0^1\frac{\kappa(s(u))}{f(s(u))^3}\,du
=\frac{1+o(1)}{2n^2}\int_{\partial K}\frac{\kappa}{f^2}\,ds.
\]
The maximum probability spacing tends to zero and its fourth-moment sum is \(O(n^{-3})\); uniform continuity of \(f\) and \(\kappa\) handles the Taylor remainder and the change of coordinates. Thus the first limit follows, including for continuous \(f>0\).

**Step 2: expected Hausdorff error for continuous densities.** For a short arclength gap \(\ell\) beginning at \(s\), its maximal chord deviation from the convex arc is \(\kappa(s)\ell^2/8+o(\ell^2)\), uniformly. Therefore, as the maximum gap tends to zero, the polygon's Hausdorff deviation satisfies
\[
d_H(P_n(f),K)=(1+o(1))\frac18\max_i\left[\frac{\sqrt{\kappa(s_i)}}{f(s_i)}\,\Delta u_i\right]^2.
\]
For uniform probability-circle samples, \(n\max_i\Delta u_i/\log n\to1\) in probability. Moreover, inside *any fixed open subarc* of positive probability, the largest contained gap has the same limit: subdivide the subarc into \(\asymp n/\log n\) intervals of length \((1-\varepsilon)\log n/n\). The expected number of empty intervals diverges and their emptiness indicators have nonpositive pairwise covariance, yielding existence of one empty interval with probability tending to one. This and uniform continuity of \(\sqrt\kappa/f\) give
\[
\frac n{\log n}\max_i\frac{\sqrt{\kappa(s_i)}}{f(s_i)}\Delta u_i
\ \xrightarrow{\mathbb P}\ \max_{\partial K}\frac{\sqrt\kappa}{f}.
\]
The union bound \(P(n\max_i\Delta u_i>z)\le n\exp[-(1-1/n)z]\) for \(z\ge2\log n\), together with \(\inf f>0\), makes the normalized Hausdorff errors uniformly integrable. Hence convergence also holds in expectation. This direct planar argument removes any \(C^1\)-density restriction and admits the clipped optimum. The resulting coefficient agrees with the general smooth-density asymptotics described by Sonnleitner [1].

**Step 3: normalize.** The sharp inequalities \(\max(\kappa/f^2)\ge V^2\) and \(\int\kappa/f^2\,ds\ge Z^3\) follow respectively by integrating the pointwise bound and by Hölder. Equality holds only for \(f_H=\sqrt\kappa/V\) and \(f_A=\kappa^{1/3}/Z\), respectively. Under the probability measure \(d\mu=\sqrt\kappa\,ds/V\) put \(q=f/f_H\) and \(a=\kappa^{-1/2}\), \(m=\int a^{1/3}\,d\mu\). Then
\[
\int q\,d\mu=1,\qquad R_H(q)=(\min q)^{-2},\qquad R_A(q)=\frac{\int a q^{-2}\,d\mu}{m^3}.
\]
The separate area-optimal density corresponds to \(q_A=a^{1/3}/m\). Its minimum \(t_A<1\) for any nonconstant curvature; the equality of the two individual optimum laws occurs only for constant curvature, hence only for a circle.

**Step 4: solve the constrained Pareto frontier.** Fix \(t_A<t<1\) and minimize \(\int a q^{-2}\,d\mu\) subject to \(\int q\,d\mu=1\) and \(q\ge t\). The scalar equation \(\int\max\{t,c a^{1/3}\}\,d\mu=1\) has exactly one positive solution \(c=c_t\), since its left side is continuous and strictly increasing once above \(t\), starting below one and diverging as \(c\to\infty\). Set \(q_t=\max\{t,c_t a^{1/3}\}\). Convexity of \(x\mapsto a/x^2\) gives, for every feasible \(q\),
\[
\int a(q^{-2}-q_t^{-2})\,d\mu
\ge\int(-2a/q_t^3)(q-q_t)\,d\mu.
\]
On \(\{q_t>t\}\) the last derivative is \(-2/c_t^3\); on \(\{q_t=t\}\) it is at least \(-2/c_t^3\), while \(q-q_t\ge0\) there. Since \(\int(q-q_t)\,d\mu=0\), the right-hand side is nonnegative. Strict convexity forces equality only for \(q=q_t\). Thus \(q_t\) uniquely minimizes the area objective at a prescribed Hausdorff floor. The set \(\{q_t=t\}\) has positive \(\mu\)-measure whenever \(t>t_A\): otherwise \(q_t=q_A\) would violate the floor. Consequently \(\min q_t=t\), and increasing \(t\) strictly increases its area error by strict convexity and nesting of the feasible sets. Continuity follows from uniqueness of the scalar normalizer. Endpoints give \(F(t_A)=1\) and \(F(1)=\int a\,d\mu/m^3>1\), the latter strict by Hölder unless curvature is constant.

**Step 5: balance and uniqueness.** The decreasing function \(t^{-2}\) exceeds \(F\) at \(t_A\) and lies strictly below it at one, so they meet exactly once at \(t_*\). A density with minimum \(t\in[t_A,1]\) has normalized errors satisfying
\[
\max\{R_H(q),R_A(q)\}\ge\max\{t^{-2},F(t)\},
\]
with equality for \(q_t\). Densities with \(\min q<t_A\) have strictly larger Hausdorff ratio than the value at the crossing. Therefore the displayed \(q_{t_*}\) uniquely minimizes the maximum. Both ratios equal \(t_*^{-2}>1\). The active floor set has nonempty interior because \(a\) is continuous, nonconstant and \(t_*>t_A\). Uniqueness is up to equality of densities everywhere, not merely almost everywhere, because all admitted densities are continuous and \(\mu\) has full support.

## Verification
All formulas above are analytic and apply to the complete continuous boundary and all admissible positive densities. A standalone standard-library program, `NUMERIC_CHECK.py`, independently evaluates the normalized curvature integrals on uniform angular meshes for ellipses, solves the two scalar equations by bisection, checks probability normalization, verifies balancing, and tests the circle limit. On semiaxes \((2,1)\), it gives \(t_*\approx0.98481689\), normalized error \(\approx1.03107207\), and an active floor of about \(0.665\) in \(\mu\)-mass. These are illustrative numerical checks; the proof does not depend on discretizing the curve.

## Relationship to prior work
Sonnleitner [1], originally made public on 2025-08-22, proves the Hausdorff limit for positive smooth boundary densities, identifies the separately optimal square-root-curvature law, and notes the distinct volume-optimal curvature-power law. Besau, Rosen and Thäle [2] develop random boundary-sampled polytope volume and weighted-volume limit theory, without the present joint Hausdorff/area minimax classification. The separate density problems do not determine the max-of-two-objectives optimum because the Hausdorff coefficient is a supremum whereas the missed-area coefficient is an integral. The contribution here is the exact clipped-density Pareto frontier, unique balanced optimum, noncircular strict cost, and a direct continuous-density planar justification. A related previously recorded result optimizes area versus perimeter for *ellipses* using two integral functionals; its optimizer is a smooth cube-root blend and its statement neither implies nor contains this supremum-versus-integral tradeoff.

## Limitations
The result concerns independent, identically distributed samples of a fixed positive continuous boundary density in the plane and leading expected errors only. It does not claim optimality for adaptive sampling, densities depending on sample size, interior samples, higher dimensions, arbitrary finite sample size, or full extreme-value distribution at the clipped density. No independent audit has been performed. Although targeted published-literature and mathematical-record comparisons found no equivalent balanced clipped law, incomplete indexing and broader general-purpose constrained-optimization principles remain originality risks.

## References
[1] M. Sonnleitner, *A limit theorem for Hausdorff approximation by random inscribed polytopes*, arXiv:2508.16442v1 (2025-08-22), https://arxiv.org/abs/2508.16442 . Relevant primary text: Introduction (Hausdorff limit, density (2), and volume-optimal density) and Theorems 1–2.

[2] F. Besau, D. Rosen, C. Thäle, *Random inscribed polytopes in projective geometries*, Mathematische Annalen 381 (2021), DOI: 10.1007/s00208-021-02257-9. Theorem 1.15 studies weighted boundary-sampled random polytopes with continuous densities.

[3] M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, Discrete & Computational Geometry 69 (2023), 453–504, DOI: 10.1007/s00454-022-00460-2. Background on boundary-sampled random polytopes; nonsmooth polytope regime.
