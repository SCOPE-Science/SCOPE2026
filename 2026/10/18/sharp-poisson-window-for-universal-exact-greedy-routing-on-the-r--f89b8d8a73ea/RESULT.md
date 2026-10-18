# Sharp Poisson window for universal exact greedy routing on the random circle

## Finding
For \(n\) independent uniform points on the unit circle, let the directed one-layer nearest-neighbor graph be obtained by retaining the \(m\) closest points at each vertex as a candidate pool and selecting its closest clockwise and closest counterclockwise member when the corresponding direction is represented. Let \(W_{n,m}\) count the missing directional selections (over all \(2n\) possible selections). For any integer sequence \(m=m_n\) with \(n2^{-m}\to\lambda\in(0,\infty)\),
\[
 d_{\mathrm{TV}}\!\left(\mathcal L(W_{n,m}),\operatorname{Poisson}(2n2^{-m})\right)\longrightarrow0.
\]
Consequently, the probability that greedy navigation returns an *exact* closest stored point from *every* initial vertex for *every* query position converges to \(e^{-2\lambda}\). The same probability tends to \(1\) if \(n2^{-m}\to0\), and to \(0\) if \(n2^{-m}\to\infty\). Thus the sharp first-order pool threshold is \(\log_2 n\), with the Poisson critical window specified by the integer subsequences \(n2^{-m}\to\lambda\). No continuous non-oscillatory limit is asserted when the integer rounding prevents the latter convergence.

## Assumptions and scope
The circle is \(\mathbb T=\mathbb R/\mathbb Z\), endowed with geodesic distance \(d(x,y)=\min(|x-y|,1-|x-y|)\). There are exactly \(n\) independent Haar-uniform points. Ties in distances or query minima have probability zero for fixed query; for the universal-query statement a tie can be resolved arbitrarily, with any minimizer a success. At a vertex, the \(m\) other vertices of least circular distance form its candidate pool, and at most one directed edge is drawn in each of the two orientation sectors, to the least-distance candidate from that sector. Greedy navigation repeatedly takes a strictly nearer outgoing neighbor relative to the query, stopping if none exists; any tie among improving neighbors may be settled arbitrarily. We require \(1\le m\le n-2\). Statements are asymptotic as \(n\to\infty\). The primary subject is geometric probability, MSC2020 \(60D05\).

## Proof
**1. Exact exponential representation.** Order the sample clockwise, labeling vertices cyclically by \(i\in\mathbb Z/n\mathbb Z\). Its ordered spacings admit the exact representation \(G_i=Z_i/S\), where \(S=\sum_iZ_i\) and the \(Z_i\) are independent mean-one exponentials. Because candidate-pool rankings depend only on spacing ratios, the common denominator cancels. A vertex \(i\) has no counterclockwise candidate if and only if the immediate counterclockwise neighbor lies farther away than its first \(m\) clockwise neighbors. Equivalently,
\[
 A_i=\left\{Z_{i-1}>\sum_{r=0}^{m-1}Z_{i+r}\right\}.
\]
Similarly, the clockwise sector is missing exactly on
\[
 B_i=\left\{Z_i>\sum_{r=1}^{m}Z_{i-r}\right\}.
\]
For \(m=O(\log n)\) these identities hold on the event that all arcs inspected on the two sides are shorter than a semicircle; for completeness, this event has probability \(1-o(1)\) uniformly in that regime, by a union bound on sums of \(m+1\) exponential gaps and the sample maximum gap. More directly, when one side is absent, the candidate comparisons have the same inequality after passing to the shortest arc; the complementary distance for long arcs can matter only if a sample gap is at least a semicircle, an event bounded by \(n2^{-(n-1)}\). We use the latter negligible event throughout. Each flag has probability \(2^{-m}\) by its exponential Laplace transform. Define \(\widetilde W=\sum_i(\mathbf 1_{A_i}+\mathbf 1_{B_i})\). Then \(\mathbb E\widetilde W=2n2^{-m}\), and \(\mathbb P(W\ne\widetilde W)\le n2^{-(n-1)}\).

**2. Adjacent-indicator dependence.** We bound joint probabilities for distinct indicators with overlapping exponential supports. For equal orientation and offset \(1\le k\le m\), an exponential tilt by the first event gives exactly
\[
 \Pr(A_i\cap A_{i+k})=4^{-m}(2/3)^k,
\]
with the same identity for the reflected \(B\)'s. Opposite orientations at the same vertex are incompatible. For the opposite pair sharing the *same large gap*, the two comparison sums are disjoint, and the conditional exponential tail and \(\max(u,v)\ge(u+v)/2\) yield
\[
 \Pr(A_i\cap B_{i-1})\le (4/9)^m.
\]
For distinct opposite-orientation large gaps, either their mutual inclusion in the two competing sums makes the events disjoint, or their long comparison sums overlap at \(r\in\{1,\ldots,m\}\) exponentials; independence of the two large gaps then gives \(3^{-r}4^{-(m-r)}\le3^{-m}\). All remaining pairs are independent. For \(n>6m\), each indicator has at most \(4m+2\) dependent partners. Thus every dependent off-diagonal joint probability is at most \((4/9)^m\). The standard dependency-graph Chen–Stein bound of Arratia–Goldstein–Gordon, applied with \(p=2^{-m}\), yields, for a universal constant \(C\),
\[
 d_{\mathrm{TV}}\!\left(\mathcal L(\widetilde W),\operatorname{Poisson}(2n2^{-m})\right)
 \le C\min\{1,(2n2^{-m})^{-1}\}\,nm(4/9)^m.
\]
For \(n2^{-m}\to\lambda\in(0,\infty)\), \(m=\log_2 n+O(1)\) and \(nm(4/9)^m\to0\) because \(\log_2(9/4)>1\). This proves Poisson convergence, including total variation, by the negligible-gap coupling. The displayed bound is for the critical and near-critical regime \(n>6m\); it is not asserted for arbitrary \(m\) comparable with \(n\).

**3. Zero-one regimes.** If \(n2^{-m}\to0\), the same union bound \(\Pr(W>0)\le2n2^{-m}+o(1)\) proves full directional coverage. This inequality remains valid even for \(m\) comparable with \(n\), since the exact exponential flag identities hold outside the exceptional maximum-gap event. Alternatively, it follows by monotonicity in the pool size from a capped logarithmic pool. If \(n2^{-m}\to\infty\), we have \(m\le\log_2 n+o(1)\), so \(n>6m\) eventually. The preceding overlap estimates give
\[
 \operatorname{Var}(\widetilde W)\le 2n2^{-m}+Cnm(4/9)^m.
\]
Dividing by \((2n2^{-m})^2\), the first term vanishes by assumption, and the second vanishes since \(m(16/9)^m/n\to0\) whenever \(m\le\log_2 n+o(1)\), using \(\log_2(16/9)<1\). Chebyshev's inequality implies \(\Pr(W=0)\to0\).

**4. Coverage equals universal exact navigation.** Outside the negligible event of a gap of length at least \(1/2\), every vertex's nearest clockwise and counterclockwise points are its immediate cyclic neighbors. Thus \(W=0\) makes the directed graph the full bidirectional nearest-neighbor cycle. For any query and any nonoptimal vertex, the cyclic neighbor in the direction along the shorter arc toward the query is strictly closer, except at an equidistant alternative minimizer; at a vertex adjacent to the query's containing gap, the other endpoint is closer whenever that vertex is not a minimizer. Hence any strictly improving greedy path ends at a closest point.
Conversely, if a sector at vertex \(v\) is empty, let its missing-side cyclic gap have length \(a<1/2\), and the other neighboring gap length \(b<1/2\). Choose a query in the empty-sector gap just beyond its midpoint measured from \(v\), at circular distance \(\delta>a/2\) from \(v\), so close to \(a/2\) that \(2\delta<1-b\). The missing-side neighbor is closer to the query than \(v\). The sole potential outgoing edge lies on the opposite side and is farther away than \(v\), since its two arc distances from the query are \(b+\delta>\delta\) and \(1-b-\delta>\delta\). Greedy navigation from \(v\) therefore fails. The reflected case is identical. Thus the universal exact-routing event equals \(\{W=0\}\) outside the negligible exceptional configurations, giving the claimed probability limits.

## Verification
The independent executable `verify.py` reproduces (i) the equivalence of missing-sector flags and the exponential-gap inequalities for finite random circles, (ii) the universal greedy-success equivalence by testing all candidate graphs against query intervals, (iii) the tilted same-orientation joint probability against direct finite-dimensional numerical integration using exact exponential moments, and (iv) the exponents needed for the Poisson and concentration bounds. These are finite checks only. Infinite-dimensional distributional assertions rely on the analytic argument above and the cited Chen–Stein theorem.

## Relationship to prior work
Bhamidi, Dhara, Schroeder and Stegehuis (2026), arXiv:2610.12312v1, define directional candidate-pool graphs on the torus and establish high-probability *approximate* routing for sufficiently large unspecified logarithmic pool constants. Their full-text model, navigation and probability bounds do not give this exact one-dimensional directional-defect count, sharp base-two pool threshold, or the Poisson critical window for *universal exact* routing. Arratia, Goldstein and Gordon (1989) provide the general Chen–Stein local-dependence tool, not the model-specific exponential comparisons. Glaz, Naus, Roos and Wallenstein (1994) study Poisson approximations for ordered \(m\)-spacings and are closest in extreme-spacing methodology; their accessible abstract does not establish or exclude a ratio-gap/greedy-routing result. A complete comparison to their paywalled full text remains a residual originality risk.

## Limitations
The sample is iid uniform on the circle, the graph has only one layer, and the query guarantee is universal over both starts and targets. Different sampling laws, dimensions, beam search, or stacked hierarchies are not addressed. The discrete integer pool size can produce subsequence-dependent critical probabilities. The dependence estimates invoke the usual standard Poisson approximation theorem rather than an original general bound. A related historical ordered-spacing result not available in full text might imply the Poisson step, although the exact routing equivalence and threshold are not stated in its abstract. All reported reviews are non-independent; no independent validation is claimed.

## References
1. S. Bhamidi, S. Dhara, L. Schroeder, C. Stegehuis, *The Geometry of Hierarchical Navigation: Accuracy and Query Cost for Point Process Input*, arXiv:2610.12312v1, first submitted 2026-10-08. https://arxiv.org/html/2610.12312v1
2. R. Arratia, L. Goldstein, L. Gordon, *Two moments suffice for Poisson approximations: the Chen–Stein method*, Annals of Probability 17 (1989), 9–25. https://doi.org/10.1214/aop/1176991491
3. J. Glaz, J. Naus, M. Roos, S. Wallenstein, *Poisson approximations for the distribution and moments of ordered m-spacings*, Journal of Applied Probability 31A (1994), 271–281. https://doi.org/10.2307/3214961
