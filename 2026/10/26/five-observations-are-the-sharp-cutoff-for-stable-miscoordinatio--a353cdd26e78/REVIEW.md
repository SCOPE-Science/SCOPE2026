# Scientific review — finite-sample threshold in coordination sampling dynamics

## Correctness (PASS)

The specified response is exactly the binomial upper-tail probability with integer cutoff \(\lceil k/(1+u)\rceil\). For \(k\le4\), factorization by \(p(1-p)\) produces the explicitly displayed at-most-quadratic polynomials. In \(1<u<3\), their weighted sum is concave and has endpoint \(h(1)=1-\theta(1)\ge0\): when the inequality is strict, an interior root cannot have the local positive-to-negative sign change required for two-sided asymptotic attraction. With all weight on \(k=1\), every point is stationary but none attracts neighbors. At \(u\ge3\), the remaining components are strictly positive. Endpoint values \(u=2,3\) and sample-tie behavior are covered explicitly.

For \(1<u<3/2\), the \(k=2,5\) upper tails yield \(p(1-p)[2\alpha-1-(1-\alpha)(6p^3-9p^2+p)]\). The cubic has just one positive local maximum on \((0,1)\) before turning negative, so a positive-to-negative-to-positive pair of crossings exists exactly at \(1/2<\alpha<7\sqrt7/(18+7\sqrt7)\). The first crossing is attracting and the second repelling, with the claimed one-dimensional basins. At the fold, the double-zero is only one-sided attracting and is not asymptotically stable. An exact-rational standard-library script confirms finite polynomial identities and strict rational brackets; the root count and universal four-sample exclusion are proved analytically.

## Originality (PASS, residual bibliographic risk)

The full Arigapudi–Heller–Schreiber primary text (arXiv:2305.10301v2) introduces precisely the stated one-population dynamics. Its Theorem 1 excludes stable interior states for homogeneous, not heterogeneous, sample sizes. Its Theorem 2 ensures some heterogeneous samples sufficiently large to create stable miscoordination but does not give a universal minimum *maximum* sample size. Its examples and appendix were compared; none supplies the quantitative two-versus-five fold interval or proves no mixture supported on \(\{1,2,3,4\}\) can work. The paper does illustrate a different two-population antisymmetric game involving size five; this is not an implication of the present one-population classification.

Oyama–Sandholm–Tercieux (2015), Sections 3.2–3.3, establish sampling-dependent equilibrium selection under different sufficient conditions, without the exact first attainable cardinality or fold law. Izquierdo–Izquierdo's treatment of inference and pure-equilibrium stability does not entail interior-state sample-size minimality. Published-mathematics searches, including aliases of the binomial response and fold, produced related but logically different results on binomial ranking, sample extrema and other dynamical games. Lack of a retrieved equivalent theorem is not a uniqueness certificate. Older or differently titled binomial-mixture coordination calculations are a residual risk, and independent bibliographic evaluation has not occurred.

## Value (PASS)

The originating paper proves stable miscoordination is possible when sample sizes differ but leaves the smallest required observation budget unspecified. That is a natural design restriction for populations with bounded individual information. The result gives the sharp budget five, excludes every smaller budget uniformly over payoff advantage and heterogeneous sample distribution, and isolates an exact first-attainable mixing window with stable/unstable branches and basin separator. Its narrow width is structurally explained by the small positive local maximum of a binomial-tail cubic, not chosen as an arbitrary numeric experiment. Thus it is a finite-threshold classification with a genuinely motivated use in limited-observation learning, not merely a new instantiation of heterogeneous existence.

## Limitations and relationship to sources

The results apply only to the explicitly normalized symmetric coordination game, fixed finitely supported sample distribution, sampling best response with favorable tie-breaking and the infinite-population deterministic flow. No generalization to asymmetric games, other noise models, unknown dynamics outside the described regimes, or finite-population behavior is asserted. The source paper and previous equilibrium-selection literature retain priority for the model and qualitative possibility of stable miscoordination.

Self-review: passed. Independent audit: not yet performed.
