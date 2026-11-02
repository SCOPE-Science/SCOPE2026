# Endpoint-driven Gamma and interior Gaussian fluctuations for random parabolic hulls

## Finding

For every integer \(n\geq3\), every \(a>0\), \(b,c\in\mathbb R\), every \(u\in\mathbb R\) and \(\ell>0\), consider the strictly convex arc
\[
\Gamma=\{(x,ax^2+bx+c):u\leq x\leq u+\ell\}.
\]
Set \(H=a\ell^3/6\), the Euclidean area enclosed by the arc and the chord joining its endpoints. Compare two random convex hulls with **the same total number \(n\) of sampled vertices**:

* In the *anchored* model, include both arc endpoints and independently sample the other \(n-2\) horizontal coordinates uniformly from the open interval.
* In the *unanchored* model, sample all \(n\) horizontal coordinates independently and uniformly from the interval.

Write their Euclidean areas as \(A_n^{\mathrm{anch}}\) and \(A_n^{\mathrm{free}}\). Let \((Q_1,\ldots,Q_{n-1})\sim\operatorname{Dirichlet}(1,\ldots,1)\), put \(Z_n=\sum_{j=1}^{n-1}Q_j^3\), and let \(S_n\sim\operatorname{Beta}(n-1,2)\) be independent of \(Z_n\). Then the **complete finite-sample distributional identities** are
\[
\boxed{A_n^{\mathrm{anch}}\overset d=H(1-Z_n),\qquad
A_n^{\mathrm{free}}\overset d=H S_n^3(1-Z_n).}
\]
For every \(n\ge3\),
\[
\boxed{\mathbb E A_n^{\mathrm{anch}}=H\left(1-\frac6{n(n+1)}\right),\qquad
\mathbb E A_n^{\mathrm{free}}=H\frac{(n-1)(n-2)}{(n+1)(n+2)}.}
\]
The exact variances are
\[
\boxed{\operatorname{Var}(A_n^{\mathrm{anch}})
=H^2\frac{72(n-2)(5n+6)}{n^2(n+1)^2(n+2)(n+3)(n+4)},}
\]
\[
\boxed{\operatorname{Var}(A_n^{\mathrm{free}})
=H^2\frac{18(n-2)(n-1)(n^3+4n^2+n-10)}{(n+1)^2(n+2)^2(n+3)(n+4)(n+5)}.}
\]
The two sampling schemes have different leading error laws:
\[
\boxed{n\frac{H-A_n^{\mathrm{free}}}{H}\Longrightarrow3G,\qquad G\sim\operatorname{Gamma}(2,1),}
\]
whereas
\[
\boxed{n^{5/2}\frac{A_n^{\mathrm{anch}}-\mathbb E A_n^{\mathrm{anch}}}{H}
\Longrightarrow N(0,360).}
\]
The free model retains the same **independent interior Gaussian correction** after its random endpoint span is removed: with \(T_{(1)}\) and \(T_{(n)}\) its extreme *normalized* horizontal sample coordinates and \(S_n=T_{(n)}-T_{(1)}\), one has jointly
\[
\boxed{\left(n(1-S_n),\ n^{5/2}\left(\frac{HS_n^3-A_n^{\mathrm{free}}}{HS_n^3}-\frac6{n(n+1)}\right)\right)
\Longrightarrow (G,N),}
\]
where \(G\sim\operatorname{Gamma}(2,1)\), \(N\sim N(0,360)\) are independent. In particular, \(n^5\operatorname{Var}(A_n^{\mathrm{anch}})/H^2\to360\) and \(n^2\operatorname{Var}(A_n^{\mathrm{free}})/H^2\to18\).

## Assumptions and scope

All areas are ordinary **unsigned Euclidean planar areas**, not arc length or intrinsic surface area. Random coordinates are independent with respect to Lebesgue-uniform *horizontal* sampling, not arclength-uniform sampling. The arc endpoints are deterministic in the anchored model only. The notation \(\operatorname{Gamma}(2,1)\) uses shape \(2\) and rate \(1\); \(N(0,360)\) is a centered normal distribution of variance \(360\). Distributional convergence is for integers \(n\to\infty\). No statement concerns a polygon sampled in the interior of the parabolic cap.

## Proof

**1. Geometric identity.** Translate and rescale horizontal coordinates to \([0,1]\); subtract the affine part of the quadratic graph. The area multiplier is exactly \(a\ell^3\). Since the quadratic graph is strictly convex, every sampled point is a convex-hull vertex, ordered by horizontal coordinate, and the remaining edge joins the two extreme sampled points. If \(t_1<\cdots<t_n\) are their normalized horizontal coordinates, a quadratic secant on an interval of width \(d\) lies above the parabola by a region of area \(d^3/6\). The full chord across a span \(s\) encloses area \(s^3/6\). Subtracting the areas between the parabola and the successive short secants gives exactly
\[
\frac{A}{H}=s^3-\sum_{j=1}^{n-1}(t_{j+1}-t_j)^3.
\]
This identity remains valid in the anchored case where \(s=1\).

**2. Exact independence.** In the anchored model, the \(n-2\) ordered interior uniform coordinates partition \([0,1]\) into \(m=n-1\) spacings. Their joint law is \(\operatorname{Dirichlet}(1^m)\). For the unanchored model, the range \(S_n\) has density \(n(n-1)s^{n-2}(1-s)\) on \((0,1)\), hence \(\operatorname{Beta}(n-1,2)\). Conditional on the two extremes, the \(n-2\) interior coordinates are uniformly distributed on the observed interval; consequently the \(m\) internal gaps divided by the range have the same Dirichlet law, *independently of the range*. This proves the two distributional identities and their exact product coupling.

**3. Moments without approximation.** For a Dirichlet vector with \(m\) unit parameters and nonnegative integers \(r_j\),
\[
\mathbb E\prod_{j=1}^m Q_j^{r_j}=\frac{\prod_j r_j!}{(m)_{\sum_j r_j}},
\]
where \((m)_k=m(m+1)\cdots(m+k-1)\) is the rising factorial. Expanding the square of \(Z_n\) gives
\[
\mathbb E Z_n=\frac6{n(n+1)},\quad
\mathbb E Z_n^2=\frac{36(n+18)}{n(n+1)(n+2)(n+3)(n+4)},
\]
\[
\operatorname{Var}(Z_n)=\frac{72(n-2)(5n+6)}{n^2(n+1)^2(n+2)(n+3)(n+4)}.
\]
The beta range moments are
\[
\mathbb E S_n^3=\frac{n(n-1)}{(n+2)(n+3)},\qquad
\mathbb E S_n^6=\frac{n(n-1)}{(n+5)(n+6)}.
\]
Insert these into the product law. Independence gives the displayed means and variances, including the full degree-five numerator in the free variance.

**4. Endpoint Gamma limit.** For independent uniform points, \(nT_{(1)}\) and \(n(1-T_{(n)})\) converge jointly to two independent rate-one exponential variables. Therefore \(n(1-S_n)\) converges to their sum \(G\sim\operatorname{Gamma}(2,1)\). Also \(Z_n=O_{\mathbb P}(n^{-2})\), using its exact expectation. Since \(1-S_n^3=(1-S_n)(1+S_n+S_n^2)\),
\[
 n\frac{H-A_n^{\mathrm{free}}}{H}
 =n(1-S_n^3)+nS_n^3 Z_n\Longrightarrow3G.
\]
The leading free variance is \(18H^2/n^2\), consistent with \(\operatorname{Var}(3G)=18\).

**5. Interior Gaussian limit and independence.** Write the Dirichlet spacings as \(Q_j=E_j/(\sum_{i=1}^m E_i)\) for independent rate-one exponentials \(E_i\), where \(m=n-1\). Then
\[
 m^2 Z_n=\frac{m^{-1}\sum_iE_i^3}{(m^{-1}\sum_iE_i)^3}.
\]
The bivariate central limit theorem applies to the sample averages of \(E_i\) and \(E_i^3\) because their sixth moments are finite. At their means \((1,6)\), the gradient of the displayed ratio is \((-18,1)\). Since \(\operatorname{Var}(E_i)=1\), \(\operatorname{Var}(E_i^3)=684\), and \(\operatorname{Cov}(E_i,E_i^3)=18\), the delta-method variance equals \(324+684-648=360\). Hence
\[
 n^{5/2}\left(Z_n-\frac6{n(n+1)}\right)\Longrightarrow N(0,360).
\]
Taking a negative of this centered variable gives the anchored-area Gaussian limit, without changing its law. The exact finite-sample independence of \(S_n\) and \(Z_n\) gives the stated joint limit with independent coordinates. These arguments prove all limits for every allowed fixed quadratic arc.

## Verification

Run `python checks/verify.py` with Python 3. The standard-library checker independently computes convex hull areas by a monotone-chain algorithm and shoelace determinants, compares these to the geometric cubic-gap formula, tests independently expanded Dirichlet/beta moment identities with exact rational arithmetic for all \(3\le n\le350\), and uses reproducible random samples to compare theoretical and observed means and variances. It also checks the anchored triangle boundary case and the predicted variance scales. The numerical tests corroborate but do not substitute for the analytical proof of the weak limits.

## Relationship to prior work

Besau, Rosen, and Thäle (arXiv:2005.10502) study asymptotic normal approximation for volumes of random polytopes sampled on entire smooth closed convex-body boundaries; they use parabolic local approximations. The present exact law concerns a **single open quadratic arc** with *horizontal-parameter sampling*, and the free model has a Gamma, not normal, leading area-deficit limit. Reitzner, Schütt, and Werner (arXiv:1911.05917) investigate surface-sampled polytopal bodies and their face and volume asymptotics, rather than the two endpoint designs here. Calka and Yukich (arXiv:1912.10304) use parabolic hull-process limits for perturbed spherical point samples, a different point process and geometric statistic. Existing published gap-functional results for circular shapes or disk intersections use different geometry and do not supply this parabolic range–shape product law or its two fluctuation scales. The standard uniform-spacing and beta identities are not claimed as original; the assessed result is their exact geometric coupling and sharp sampling-design fluctuation dichotomy.

## Limitations

The theorem is specific to **quadratic** arcs and independent uniform horizontal parameters. It does not claim a Gamma law for general closed convex curves, a Gaussian correction for arbitrary smooth nonquadratic arcs, or any arclength-sampling result. The finite-sample distribution is specified by an explicit beta–Dirichlet pushforward, not an elementary closed-form cumulative distribution for each \(n\). Historical priority of this particular combination of identities remains subject to independent literature review. No independent mathematical audit has been performed.

## References

1. F. Besau, D. Rosen, C. Thäle, *Random inscribed polytopes in projective geometries*, arXiv:2005.10502 (first posted 2020-05-21); *Mathematische Annalen* 381 (2021), 1345–1372. https://arxiv.org/abs/2005.10502
2. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (2019); *Discrete & Computational Geometry* 69 (2023), 453–504. https://arxiv.org/abs/1911.05917
3. P. Calka, J. E. Yukich, *Convex hulls of perturbed random point sets*, arXiv:1912.10304 (2019). https://arxiv.org/abs/1912.10304
