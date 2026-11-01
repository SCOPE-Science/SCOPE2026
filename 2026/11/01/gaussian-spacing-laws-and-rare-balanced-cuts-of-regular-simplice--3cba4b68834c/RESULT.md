# Gaussian spacing laws and rare balanced cuts of regular simplices

## Finding

Let \(m\ge3\) be an integer. Take a regular \((m-1)\)-simplex, select an affine hyperplane according to the rotation-and-translation-invariant hyperplane measure conditioned on intersecting the simplex, and let \(N_m\) be the number of vertices of its section. Let \(G_1,\ldots,G_m\) be independent standard normal variables, \(G_{(1)}<\cdots<G_{(m)}\) their order statistics, and \(\mu_m=\mathbb E G_{(m)}>0\). Then, for every integer \(1\le r\le\lfloor m/2\rfloor\),

\[
\boxed{\mathbb P\{N_m\ge r(m-r)\}=\frac{\mathbb E G_{(m-r+1)}}{\mu_m}.}
\]

These are all possible values of \(N_m\), and successive differences of the displayed tail probabilities give the complete distribution. In particular,

\[
\boxed{\mathbb E N_m=\frac{m(m-1)}{2\sqrt\pi\,\mu_m}
\sim\frac{m^2}{2\sqrt{2\pi\log m}}.}
\]

Despite this exact mean law, the typical complexity has a random exponent:

\[
\boxed{\frac{\log N_m}{\log m}\ \Longrightarrow\ 2-U^2,\qquad U\sim\mathrm{Uniform}[0,1].}
\]

The limiting distribution has cumulative distribution function \(F(y)=1-\sqrt{2-y}\) for \(1\le y\le2\). Moreover, for any fixed \(0<q<1/4\), let

\[
z_q=\Phi^{-1}\!\left(\frac{1+\sqrt{1-4q}}2\right),
\]

where \(\Phi\) is the standard normal distribution function. The probability of a section with a macroscopic fraction of the maximum possible vertices obeys the sharp law

\[
\boxed{\sqrt{2\log m}\,\mathbb P\{N_m\ge q m^2\}\longrightarrow z_q.}
\]

The exact finite-dimensional law, sharp expectation, random-exponent limit, and rare macroscopic-section asymptotic are asserted together for the stated sampling model.

## Assumptions and scope

The simplex is the convex hull of the coordinate vertices \(e_1,\ldots,e_m\) in the Euclidean affine subspace \(\{x\in\mathbb R^m:\sum_i x_i=1\}\), isometric to any regular \((m-1)\)-simplex up to scale. An invariant affine hyperplane has parametrization \(\{x:\langle u,x-c\rangle=t\}\), where \(c=(1/m,\ldots,1/m)\), \(u\) is a Haar-uniform intrinsic unit normal in \(L=\{x:\sum_i x_i=0\}\), and \(t\) carries Lebesgue measure. Condition on intersection with the simplex. The exceptional null set of hyperplanes through simplex vertices is disregarded. This is not the distribution of uniformly chosen central hyperplanes and is not a model of uniformly chosen orientations followed by a normalized offset without width weighting.

## Proof

**Step 1: invariant measure and Gaussian scores.** The centered simplex vertices are \(v_i=e_i-c\). Let \(G_i\) be independent \(N(0,1)\), put \(\overline G=m^{-1}\sum_iG_i\) and \(R=(\sum_i(G_i-\overline G)^2)^{1/2}\). Then \(u=(G-\overline G\mathbf1)/R\) is Haar-uniform on the unit sphere of \(L\) and is independent of \(R\). The directional vertex scores are \(\langle u,v_i\rangle=(G_i-\overline G)/R\). The admissible offset interval has length \((G_{(m)}-G_{(1)})/R\). Since \(R\) and \(u\) are independent, inserting the corresponding factor into both numerator and denominator shows that, for any event determined by the score ranking and position of the offset, its conditioned probability equals its Gaussian-score representation

\[
\mathbb P(\mathcal E)=
\frac{\mathbb E\int_{G_{(1)}}^{G_{(m)}}\mathbf1_{\mathcal E(G,s)}\,ds}
{\mathbb E(G_{(m)}-G_{(1)})}.
\]

Explicitly, one may sample the Gaussian vector with likelihood proportional to its range and then sample the threshold uniformly on that range. The factor of two for unoriented hyperplanes cancels.

**Step 2: edge-crossing count.** For every generic threshold \(s\), suppose exactly \(k\) of the \(m\) scores lie below \(s\). Each of the \(k(m-k)\) edges connecting opposite score sides is cut transversally; every section vertex comes from exactly one cut edge. Therefore \(N_m=k(m-k)\). The event \(N_m\ge r(m-r)\) is exactly \(r\le k\le m-r\). Its permissible thresholds form the interval \([G_{(r)},G_{(m-r+1)}]\). Exchangeability and Gaussian symmetry imply

\[
\mathbb E G_{(r)}=-\mathbb E G_{(m-r+1)},\qquad
\mathbb E(G_{(m)}-G_{(1)})=2\mu_m.
\]

Taking expected interval lengths proves the exact tail formula and the finite support assertion. The index \(r=1\) gives probability one, as required. The mass at the value \(r(m-r)\) is the tail for \(r\) minus the tail for \(r+1\), taking the latter to be zero above \(\lfloor m/2\rfloor\).

**Step 3: exact first moment.** Sum the indicators that each edge is cut. In the Gaussian threshold representation, edge \((i,j)\) contributes expected offset interval length \(\mathbb E|G_i-G_j|=2/\sqrt\pi\). As there are \(\binom m2\) edges and the normalizing expected full range is \(2\mu_m\),

\[
\mathbb E N_m=\frac{\binom m2(2/\sqrt\pi)}{2\mu_m}
=\frac{m(m-1)}{2\sqrt\pi\,\mu_m}.
\]

Standard Gaussian upper-tail estimates imply \(\mu_m/\sqrt{2\log m}\to1\); this proves the stated sharp expectation equivalent.

**Step 4: rare macroscopic sections.** Fix \(0<q<1/4\) and put \(\rho_q=(1-\sqrt{1-4q})/2\), so \(0<\rho_q<1/2\). For all sufficiently large \(m\), the event \(N_m\ge q m^2\) is equivalent to \(N_m\ge r_m(m-r_m)\), where \(r_m=\lceil\rho_q m\rceil\). The value \(r_m\) is the smallest integer for which \(r_m(m-r_m)\ge q m^2\), since \(r\mapsto r(m-r)\) is increasing on \(1\le r\le m/2\); thus integer rounding is exact. By the weak law for Gaussian empirical quantiles and uniform integrability of central order statistics,

\[
\mathbb E G_{(m-r_m+1)}\longrightarrow
\Phi^{-1}(1-\rho_q)=z_q.
\]

Combining with the exact survival probability and the estimate for \(\mu_m\) yields the asserted constant in the rare macroscopic-section law. Note that \(q=1/4\) is deliberately excluded because it lies at the endpoint of the quantile regime.

**Step 5: random typical exponent.** Put \(b_m=\sqrt{2\log m}\). Standard Gaussian-maximal inequalities imply the Gaussian sample range \(S_m=G_{(m)}-G_{(1)}\) satisfies \(S_m/(2b_m)\to1\) in \(L^1\). Consequently the Gaussian sample law reweighted by \(S_m/\mathbb E S_m\) is asymptotically identical in total variation to the original sample law. Under the unreweighted law, draw an independent \(V\sim\mathrm{Uniform}[0,1]\) and choose threshold \(s=G_{(1)}+VS_m\). Then \(s/b_m\to2V-1\) in probability. For every fixed \(v\in(0,1)\) with \(2v-1\ne0\), sandwich the random threshold between levels \((2v-1\pm\eta)b_m\). The Gaussian tail estimate

\[
\mathbb P\{G_1>c b_m\}=m^{-c^2+o(1)}\quad(0<c<1)
\]

and binomial concentration imply that the smaller of the score counts on either side of the threshold has logarithm divided by \(\log m\) tending to \(1-(2v-1)^2\) in probability. The larger count has exponent one; at \(v=1/2\) both counts have exponent one as well. Hence conditional on almost every \(v\), \(\log N_m/\log m\to2-(2v-1)^2\) in probability. Integrating in \(v\), and using the vanishing total-variation change under range weighting, proves distributional convergence to \(2-(2V-1)^2\). Since \(|2V-1|\) is uniform on \([0,1]\), the claimed limit follows.

## Verification

The accompanying standard-library `verify.py` numerically evaluates the Gaussian order-statistic expectations by Simpson quadrature for dimensions \(m=3,4,5,6,8,10,12\) and independently checks the edge-sum expectation identity. Gaussian range-weighted Monte Carlo experiments with 90,000 trials at each of \(m=4,8,12\) agree with those formulas within declared numerical tolerances; the executable reports `ALL_CHECKS_PASSED`. These finite diagnostics do **not** certify the infinite-dimensional limit laws, which follow analytically from Steps 4–5. The exact tetrahedral value at \(m=4\) is a consistency check, not a novelty claim.

## Relationship to prior work

Brandenburg, De Loera, and Meroni (2023) provide slicing-chamber parametrizations and optimize combinatorial and metric properties of affine sections; their chamber structure motivates asking for invariant-hyperplane probabilities but does not itself give the Gaussian-spacing law or rare balanced-cut asymptotic. König (2020) treats extremal noncentral simplex sections by volume and perimeter, rather than random vertex-count distributions. Published calculations for Haar-random **central** simplex sections concern an offset fixed at the centroid, not this width-conditioned invariant affine-hyperplane model. A distinct earlier calculation for invariant affine sections of a cross-polytope has a superficially similar random complexity exponent, but its section vertex-count law, edge incidence, geometry, and first-moment constant differ from the present simplex theorem. Reusing the general edge-counting strategy does not establish the new Gaussian order-statistic identities or macroscopic rare-event coefficient without fresh analysis.

## Limitations

The simplex is regular and the hyperplane selection uses precisely the invariant affine-hyperplane measure conditioned on intersection. The results do not cover general nonsymmetric simplices, alternative orientation-offset sampling, or higher-codimension flats. The rare-event statement requires fixed \(q\in(0,1/4)\), not an endpoint or a dimension-dependent threshold. Mathematical correctness is supported by the proof and diagnostic computations but has not received independent review; historical priority is not established by exhaustive literature inspection, and some indexed related works were available only as summaries.

## References

1. M.-C. Brandenburg, J. A. De Loera, and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1, publicly posted 2023-04-27, https://arxiv.org/abs/2304.14239.
2. H. König, *Non-central sections of the simplex, the cross-polytope and the cube*, arXiv:2002.10743v1, publicly posted 2020-02-25, https://arxiv.org/abs/2002.10743.
3. Related published result: *Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts*, published-finding corpus entry `d3f9b0447a8e` (central-section model).
4. Related published result: *Joint chi-square face-vector fluctuations of random central regular-simplex sections*, published-finding corpus entry `aa90c887fe90` (central-section model).
