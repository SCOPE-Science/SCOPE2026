# A random-exponent law and rare quadratic sections of high-dimensional regular simplices

## Finding

Let \(m\ge3\) and let \(\Delta_{m-1}\) be a regular \((m-1)\)-simplex with \(m\) vertices. Choose an **affine** hyperplane \(H\) from the motion-invariant hyperplane measure, conditioned on intersecting \(\Delta_{m-1}\). Concretely, identify the affine hull with Euclidean \(\mathbb R^{m-1}\); the probability law is the normalized measure \(d\sigma(u)\,dt\) on pairs \((u,t)\) for which \(H=\{x:\langle u,x\rangle=t\}\) meets the simplex, with \(u\) uniform on the unit sphere, \(t\) Lebesgue, and the two orientations identified. This is **not** the model that first takes a uniformly random normal and then independently chooses a uniform admissible offset: the normal here is weighted by the directional width.

Let \(V_m\) denote the number of vertices of \(H\cap\Delta_{m-1}\). Let \(Z_1,\ldots,Z_m\) be independent standard Gaussians, let \(\mu_m=\mathbb E\max_i Z_i\), and put \(b_m=\sqrt{2\log m}\). Then:

**Exact finite-dimensional expectation.** For every integer \(m\ge3\),
\[
\boxed{\mathbb E V_m=\frac{\binom m2}{\sqrt\pi\,\mu_m}.}
\]
In particular,
\[
\mathbb E V_m\sim\frac{m^2}{2\sqrt{2\pi\log m}}.
\]

**Typical random-exponent law.** There is convergence in distribution
\[
\boxed{\frac{\log V_m}{\log m}\ \Longrightarrow\ 2-U^2,\qquad U\sim\operatorname{Unif}[-1,1].}
\]
Equivalently, its limiting cumulative distribution is \(0\) below \(1\), is \(1-\sqrt{2-t}\) for \(1\le t\le2\), and is \(1\) above \(2\). Thus the normalized vertex count \(V_m/m^2\) tends to zero in probability even though its expectation decays on the much slower scale \(1/\sqrt{\log m}\).

**Rare quadratically complex sections.** Fix any \(a\in(0,1/4)\), write \(\Phi\) for the standard Gaussian cumulative distribution, and set
\[
q_a=\Phi^{-1}\!\left(\frac{1+\sqrt{1-4a}}2\right).
\]
Then
\[
\boxed{\lim_{m\to\infty}b_m\,\mathbb P\{V_m\ge a m^2\}=q_a.}
\]
Moreover, conditional on this event, \(V_m/m^2\) converges in law to \(\Phi(S)(1-\Phi(S))\), where \(S\) is uniform on \([-q_a,q_a]\). The event threshold \(a\) is fixed before letting \(m\) increase; neither endpoint \(a=0\) nor \(a=1/4\) is asserted.

## Assumptions and scope

All simplices are nondegenerate and regular. Similarities do not affect the vertex count or the normalized invariant hyperplane law. The hyperplane is conditioned to intersect the simplex; tangencies and hyperplanes passing through a vertex have probability zero. Its section is an \((m-2)\)-polytope almost surely. Only hyperplane **sections**, not projections, are sampled. The asymptotic conclusions concern the limit \(m\to\infty\) through integers. No claim is made about nonregular simplices, other probability measures on hyperplanes, or sections of higher codimension.

## Proof

**1. Edge crossing and Gaussian representation.** Realize the simplex as the convex hull of \(v_i=e_i-\mathbf1/m\), \(1\le i\le m\), in \(E=\{x\in\mathbb R^m:\sum_i x_i=0\}\). For generic \(H\), each vertex of its section is exactly the intersection of \(H\) with one edge of the simplex. If the hyperplane separates \(k\) simplex vertices from the remaining \(m-k\), its section has exactly
\[
V_m=k(m-k)
\]
vertices. This uses the complete graph of simplex edges and holds even when \(H\cap\Delta_{m-1}\) is not simplicial.

For the Gaussian representation put \(\bar Z=m^{-1}\sum_i Z_i\), \(G=(Z_i-\bar Z)_{i=1}^m\), \(R=\|G\|\), and \(W=\max_i Z_i-\min_i Z_i\). The direction \(G/R\) is uniformly distributed on the unit sphere of \(E\), independently of \(R\). In this direction the simplex width is \(W/R\). Thus for any bounded measurable function \(f\) of the section vertex count, the *exact* motion-invariant model satisfies
\[
\mathbb E f(V_m)=
\frac{\displaystyle\mathbb E\left[\frac1R\int_{\min Z_i}^{\max Z_i}
 f\bigl(K_m(s)(m-K_m(s))\bigr)\,ds\right]}
{\displaystyle\mathbb E[W/R]},\qquad
K_m(s)=\#\{i:Z_i<s\}.
\tag{1}
\]
The integral over offsets, rather than a uniform-normal shortcut, is essential to the normalizing factor.

**2. Exact expectation.** Integrate the edge-count identity over offsets. For fixed Gaussian data, the resulting integral is \(\sum_{i<j}|Z_i-Z_j|\). By independence of Gaussian radius and direction, taking expectations of the numerator and denominator of (1) yields
\[
\mathbb E V_m
=\frac{\sum_{i<j}\mathbb E|Z_i-Z_j|}{\mathbb E W}
=\frac{\binom m2(2/\sqrt\pi)}{2\mu_m},
\]
since \(Z_i-Z_j\sim N(0,2)\) and symmetry gives \(\mathbb E W=2\mu_m\). Standard Gaussian extreme-value estimates imply \(\mu_m/b_m\to1\), giving the displayed expectation asymptotic.

**3. Typical sections.** The centered Gaussian radius obeys \(R/\sqrt m\to1\) in \(L^2\); the sample extrema satisfy \(\max Z_i/b_m\to1\) and \(\min Z_i/b_m\to-1\) in \(L^2\). For sufficiently large \(m\), the reciprocal-radius moments needed below are finite. These facts show
\[
\frac{(W/R)}{\mathbb E(W/R)}\longrightarrow1\quad\text{in }L^1.
\tag{2}
\]
Thus replacing the tilted Gaussian law implicit in (1) by an ordinary independent Gaussian sample followed by a uniform offset between its minimum and maximum changes any probability by \(o(1)\) in total variation.

Under that ordinary law, if \(S_m\) is the offset in Gaussian coordinates, the sample-extreme limits give \(S_m/b_m\Rightarrow U\), with \(U\) uniform on \([-1,1]\). At any fixed \(u\in(0,1)\), Mills' ratio implies \(1-\Phi(ub_m)=m^{-u^2+o(1)}\); a binomial concentration bound then gives \(\#\{i:Z_i>ub_m\}=m^{1-u^2+o_{\mathbb P}(1)}\). The matching statement holds for \(u<0\), while for \(u=0\) both sides contain a linear fraction of the vertices. Monotonicity in the threshold and a finite grid of \(u\)-values, followed by removal of arbitrarily small neighborhoods of \(\pm1\), make these statements uniform enough for the random \(S_m\). Consequently
\[
\frac{\log(K_m(S_m)(m-K_m(S_m)))}{\log m}
=2-(S_m/b_m)^2+o_{\mathbb P}(1),
\]
which proves the random-exponent limit, also under the original law by (2).

**4. Rare high-complexity sections and their marks.** Fix \(a\in(0,1/4)\). Define the length of the admissible Gaussian-offset interval
\[
L_m(a)=\operatorname{Leb}\left\{s\in[\min Z_i,\max Z_i]:
\frac{K_m(s)}m\left(1-\frac{K_m(s)}m\right)\ge a\right\}.
\]
The empirical Gaussian distribution function converges uniformly to \(\Phi\). Because \(a\) is strictly between \(0\) and \(1/4\), its two limiting boundary quantiles are the regular points \(-q_a\) and \(q_a\). Gaussian order-statistic quantile bounds therefore imply \(L_m(a)\to2q_a\) in \(L^2\), and the corresponding intervals converge in both endpoints. (For completeness, these uniform-integrability bounds follow by expressing a fixed central sample quantile's tail as a binomial tail and applying a Chernoff bound together with the Gaussian tail.)

Since \(\sqrt m/R\to1\) in \(L^2\) and its second moment is bounded, Cauchy–Schwarz yields
\[
\mathbb E[L_m(a)/R]\sim\frac{2q_a}{\sqrt m},\qquad
\mathbb E[W/R]\sim\frac{2b_m}{\sqrt m}.
\]
Applying (1) to the event indicator proves \(b_m\mathbb P(V_m\ge a m^2)\to q_a\). Applying (1) instead to any bounded continuous test function of \(V_m/m^2\), multiplied by that indicator, shows that its conditional limit is the image of normalized Lebesgue measure on \([-q_a,q_a]\) under \(s\mapsto\Phi(s)(1-\Phi(s))\). This proves the entire theorem.

## Verification

The companion standalone `verify.py` uses only Python's standard library and a deterministic seed. It tests 2,310 direct edge-crossing identities, four independent finite-dimensional weighted Monte Carlo means against the exact Gaussian-integral expression, the identity \(\int_{\mathbb R}\Phi(s)(1-\Phi(s))\,ds=1/\sqrt\pi\), and three rare-event quantile identities. It was executed successfully after being saved. The Gaussian integral and Monte Carlo checks have finite tolerances, while the displayed asymptotic assertions rest on the analytical arguments above; finite checks cannot verify asymptotic convergence.

## Relationship to prior work

Kabluchko, Litvak, and Zaporozhets (first posted 2015) prove Gaussian-range formulas for the directional mean width and fluctuations of regular simplices; those results support the Gaussian reduction but do not count vertices of independently translated **affine** slices or derive the random-exponent law. Swan (2018) proves a different expectation theorem for isotropic sections of hypercubes and parallelotopes, using their zonotope structure; neither their bodies nor their vertex-count asymptotics are this simplex problem. De Loera, Lopez-Campos, and Torres (2024 preprint, 2025 revision) classify attainable vertex counts and bounds for hyperplane sections of polytopes, without the motion-invariant measure or the present probability limit laws. Published work on **central** simplex sections fixes the offset at the centroid and therefore operates under a different probability law; even its quadratic-size typical section count does not imply the affine-section rare-event rate.

## Limitations

The exact expectation depends on the specific motion-invariant conditioning. Choosing a uniform normal first and a uniform offset second would define a different finite-dimensional distribution. The bulk exponent and rare-event results are asymptotic, with no uniform-in-\(a\) rate of convergence asserted. The result does not evaluate all finite-dimensional probabilities, and no assertion of independent peer review or historical-priority certification is made. A logically equivalent treatment under another stochastic-section parameterization remains a bibliographic possibility.

## References

1. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, first public 2015-11-26; especially §3.2 and Theorem 3.7. https://arxiv.org/abs/1511.08479
2. H. Swan, *Expected Number of Vertices of a Hypercube Slice*, arXiv:1808.09482 (2018). https://arxiv.org/abs/1808.09482
3. J. A. De Loera, G. Lopez-Campos, A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419 (first posted 2024-12-17, revised 2025). https://arxiv.org/abs/2412.12419
4. R. Schneider and W. Weil, *Stochastic and Integral Geometry*, Springer (2008), reference for motion-invariant hyperplane measure (also cited in Swan's work).
