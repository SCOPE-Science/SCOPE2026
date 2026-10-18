# Exact barycentric inclusion depth for side-stratified random triangles

## Finding

Let \(T=\operatorname{conv}\{A,B,C\}\) be any nondegenerate Euclidean triangle. Draw independent points \(X\in AB\), \(Y\in BC\), and \(Z\in CA\), each uniformly in arclength along its respective **entire** side. For a fixed point \(P\in T\) with barycentric coordinates \((\alpha,\beta,\gamma)\), so \(\alpha,\beta,\gamma\ge0\) and \(\alpha+\beta+\gamma=1\), set

\[
D_T(P)=\Pr\bigl(P\in\operatorname{conv}\{X,Y,Z\}\bigr).
\]

Define \(\phi(t)=t(1-t)\log((1-t)/t)\) for \(0<t<1\), with its continuous endpoint values \(\phi(0)=\phi(1)=0\). Then **the entire pointwise inclusion-probability profile is independent of triangle shape**:

\[
\boxed{D_T(P)=\phi(\alpha)+\phi(\beta)+\phi(\gamma).}
\]

This symmetric function is **strictly Schur-concave on the open barycentric simplex**. Its unique maximizing point is the centroid \(G=(A+B+C)/3\), and its sharp maximum is

\[
\boxed{D_T(G)=\frac{2\log 2}{3}.}
\]

The probability vanishes at every host-boundary point. More precisely, for each fixed \(0<q<1\), a point moving toward vertex \(A\) through barycentric coordinates \((1-\varepsilon,\varepsilon q,\varepsilon(1-q))\) has the first-order law

\[
\boxed{D_T(P)=\varepsilon H(q)+O_q\!\left(\varepsilon^2\log\frac1\varepsilon\right),\quad H(q)=-q\log q-(1-q)\log(1-q).}
\]

The spatial mean of the exact inclusion profile is \(1/4\), equal to the known mean-area fraction of the side-stratified random triangle.

## Assumptions and scope

The host is an arbitrary Euclidean triangle of strictly positive area, with no angle or side-length restrictions. The three side points are independent and each is uniform with respect to **its own side's arclength**, not sampled uniformly from the pooled perimeter. The point \(P\) is deterministic. Inclusion means the closed convex hull; boundary coincidences in the random experiment have probability zero when \(P\) is interior. The barycentric coordinates are taken with respect to the ordered host vertices, not the sampled points. Logarithms are natural. The sharp extremum holds among all points of the closed host triangle. The directional boundary expansion is for fixed \(q\in(0,1)\), not a uniform assertion as \(q\) approaches an endpoint.

## Proof

**1. Affine normalization and geometric partition.** The law of a uniform arclength fraction on a straight segment is preserved by any invertible affine map: segment lengths are multiplied by a constant factor on that segment. Normalize \(A=(0,0)\), \(B=(1,0)\), \(C=(0,1)\). Almost surely the three side points are distinct, the inner triangle has positive area, and the host decomposes into the inner triangle and three corner triangles \(AXZ\), \(BXY\), and \(CYZ\), with disjoint interiors. For a fixed interior point, the complementary inclusion events associated with those corner triangles are therefore disjoint up to null boundaries.

**2. One corner probability.** In the basis \((B-A,C-A)\), write the fixed point as \((x,y)\), with \(x,y>0\) and \(x+y<1\). Write the independently uniform side fractions for \(X\) and \(Z\) as \(U,V\in[0,1]\). Except on null boundaries, \(P\in AXZ\) if and only if

\[
\frac{x}{U}+\frac{y}{V}\le1.
\]

The inequality requires \(U\ge x/(1-y)\) and, conditional on such a \(U=u\), requires \(V\ge yu/(u-x)\). Consequently the corner probability is the exact integral

\[
\begin{aligned}
F(x,y)&=\int_{x/(1-y)}^1\left(1-\frac{yu}{u-x}\right)du\\
&=1-x-y-xy\log\frac{(1-x)(1-y)}{xy}.
\end{aligned}
\]

The integrand and integration limits are valid because \(x+y<1\); no approximation has been made.

**3. Sum of the three mutually exclusive corner probabilities.** For barycentric coordinates \((\alpha,\beta,\gamma)\), the pairs \((x,y)\) at vertices \(A,B,C\) are \((\beta,\gamma)\), \((\gamma,\alpha)\), and \((\alpha,\beta)\), respectively. Hence

\[
D_T(P)=1-F(\beta,\gamma)-F(\gamma,\alpha)-F(\alpha,\beta).
\]

The constant and linear terms cancel. The remaining three logarithmic terms regroup because each barycentric coordinate occurs alongside the other two, whose sum is its complement:

\[
D_T(P)=\sum_{\{i,j\}}t_it_j\log\frac{(1-t_i)(1-t_j)}{t_it_j}
=\sum_{i=1}^3t_i(1-t_i)\log\frac{1-t_i}{t_i},
\]

where \((t_1,t_2,t_3)=(\alpha,\beta,\gamma)\) and the first sum runs over the three unordered pairs. This proves the formula for interior points; continuity and the geometric boundary observation give the closed-simplex extension. On any boundary edge, the two nonzero barycentric coordinates are complementary and \(\phi(t)+\phi(1-t)=0\), so \(D_T(P)=0\) there.

**4. Strict Schur concavity and the exact maximizer.** On \((0,1)\), direct differentiation gives

\[
\phi'(t)=(1-2t)\log\frac{1-t}{t}-1,\qquad
\phi''(t)=-2\log\frac{1-t}{t}-\frac{1-2t}{t(1-t)}.
\]

For \(0<t<1/2\), both summands in the formula for \(\phi''(t)\) are strictly negative. Also \(\phi'(t)=\phi'(1-t)\). If two strictly positive barycentric coordinates satisfy \(a>b\), then \(a+b<1\). When \(a\le1/2\), the strict decrease of \(\phi'\) on \((0,1/2)\) gives \(\phi'(a)<\phi'(b)\). When \(a>1/2\), one has \(b<1-a<1/2\), and therefore \(\phi'(a)=\phi'(1-a)<\phi'(b)\). Thus every nontrivial equalizing transfer between two unequal coordinates, holding the third fixed and positive, strictly **increases** their contribution to \(D_T\). This is strict Schur concavity on the open simplex. Repeated pairwise equalization makes all coordinates equal and uniquely maximizes \(D_T\) at \((1/3,1/3,1/3)\). The boundary has value zero while interior values are positive, so there is no omitted boundary maximizer. Substitution gives \(D_T(G)=2\log2/3\).

**5. The directional vertex law.** For fixed \(q\in(0,1)\), the identity \(\phi(1-t)=-\phi(t)\) gives

\[
D_T(P)=\phi(\varepsilon q)+\phi(\varepsilon(1-q))-\phi(\varepsilon).
\]

As \(t\downarrow0\), \(\phi(t)=-t\log t+O(t^2\log(1/t))\). Substitute the three arguments: the \(\varepsilon\log\varepsilon\) terms cancel, leaving \(\varepsilon H(q)\) and the stated remainder.

**6. An integral consistency identity.** Let \(P\) now be uniform in area over the host, independently of \(X,Y,Z\). By Fubini, \(\mathbb E_P D_T(P)=\mathbb E[\operatorname{area}(XYZ)]/\operatorname{area}(T)\). Direct integration of the proved formula over the barycentric simplex gives

\[
\mathbb E_P D_T(P)=6\int_0^1(1-t)\phi(t)\,dt=\frac14.
\]

Indeed, \(\int_0^1 t(1-t)^2\log(1-t)\,dt=-7/144\) and \(\int_0^1 t(1-t)^2\log t\,dt=-13/144\). This reproduces the known mean-area fraction independently of the new pointwise calculation.

## Verification

The included standalone `checker.py` uses the Python standard library and may be executed with `python3 checker.py`. It checks the corner integral against numerical quadrature at six parameter pairs; four direct Monte Carlo containment rates (180,000 independent trials each); a grid of pairwise derivative comparisons consistent with the proved strict Schur inequality; numerical integration of the spatial mean; and five directional vertex limits. All tests passed. Random sampling and finite grids are **corroboration only**, not infinite certification; the preceding calculation is the proof.

## Relationship to prior work

Maesumi, *Triangle Inscribed-Triangle Picking* (arXiv:1804.11007, initial public arXiv release 30 April 2018), uses exactly one independent uniform point per triangle side but obtains the **distribution and moments of area** rather than the probability that the resulting triangle contains each fixed host point. Knowing the area distribution, or even its mean \(1/4\), does not determine the spatial inclusion function. Reitzner, Schütt, and Werner, *The convex hull of random points on the boundary of a simple polytope* (arXiv:1911.05917, initial public release 14 November 2019), study pooled-boundary independent points and asymptotic mean face counts and volume differences; neither their sampling law nor their quantitative claims imply this conditional three-side pointwise profile. Ismailov, *With what probability does an inscribed triangle contain a given point?* (arXiv:2601.02929, January 2026), investigates independent uniform points on a **circle**, with a radial dilogarithmic probability law. Affine mapping cannot turn that circle-uniform law into independently uniform fractions on three specified straight sides.

The present result concerns the exact barycentric **spatial depth** and its strict majorization extremum under three side-stratified samples; it does not claim to replace or extend the area CDFs, asymptotic boundary-polytope results, or circle formulas above. A bibliographically unindexed derivation of this elementary-profile formula remains possible.

## Limitations

The formula is specific to one sample from each side of a host triangle. It does not assert the same law for perimeter-pooled sampling, three interior points, circles, arbitrary polygons, or correlated samples. The entropy expansion has a fixed approach direction, not a uniform bound as that direction degenerates. The proof is mathematical rather than computer-assisted; computational tests are finite and independent mathematical auditing has not been conducted. The originality comparison is limited to identifiable and accessible literature, so unindexed equivalent work is a residual risk.

## References

1. A. Maesumi, *Triangle Inscribed-Triangle Picking*, arXiv:1804.11007 (first arXiv version 30 April 2018), https://arxiv.org/abs/1804.11007.
2. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first version 14 November 2019), https://arxiv.org/abs/1911.05917.
3. A. Ismailov, *With what probability does an inscribed triangle contain a given point?*, arXiv:2601.02929 (first version 6 January 2026), https://arxiv.org/abs/2601.02929.
4. C. Buchta, *On the boundary structure of the convex hull of random points*, Advances in Geometry 12 (2012), 179–190, https://doi.org/10.1515/ADVGEOM.2011.041 (background on geometric random hulls; primary MSC 52A22).
