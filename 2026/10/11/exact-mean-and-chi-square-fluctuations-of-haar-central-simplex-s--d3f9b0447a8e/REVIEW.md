# Scientific review: Haar simplex-section vertex counts

## Correctness (PASS)

The proof reconstructs the central-section geometry: a generic cut of the coordinate regular simplex has precisely one section vertex per crossed edge, hence \(N_m=K_m(m-K_m)\). Projecting an isotropic Gaussian onto the zero-sum subspace proves the Haar correspondence; its pairwise correlation is \(-1/(m-1)\), yielding the exact mean by angular Gaussian sign probabilities. The weak limit follows from a moving-threshold empirical-CDF argument with an explicit grid-and-variance estimate, the ordinary i.i.d. CLT, and the quadratic identity. The normalization \(\sigma^2=1/4-1/(2\pi)\), the domain \(m\ge3\), and the exact low-dimensional cases were checked. The standalone checks cover 1,002 finite rational sign patterns and seeded simulations; neither finite data nor a failed test would prove or disprove the infinite limit without the analytic proof.

## Originality (PASS, with explicitly bounded risk)

The closest full-text geometric comparisons are De Loera–Lopez-Campos–Torres (arXiv:2412.12419), on maximal section-vertex counts and gaps, and the published note *Quantitative stability and exact Hessian for minimal central simplex sections*, on the **volume** of central regular-simplex slices. Neither derives an orientation-weighted expected vertex count or a vertex-deficit distribution. The fresh Ambrus–Gárgyán (arXiv:2609.12714) source states a minimum-volume result, not a Haar vertex-count theorem; only its public abstract, not its full manuscript, was accessible. Brown–Cohen–Tang–Yam (PNAS 2021), Section 5, determines sample-mean exceedance laws in the disjoint regime of nonnegative infinite-mean stable distributions. Relevant Gaussian aliases, general-section coverage, and indexed mathematical records were searched and compared by implication. A classical or unindexed equivalent Gaussian orthant or polytope-section formula remains a risk. No search alone is treated as a proof of novelty.

## Value (PASS)

The invariant is the vertex count of a natural random central section, which matters for section combinatorics and complexity. Its exact all-dimensional expectation and non-Gaussian chi-square fluctuation scale measure typical behavior near the extremal balanced cut, a gap not filled by deterministic maximal counts or volume-extremizer results. The result applies to a canonical family in arbitrary dimension and has a substantive probabilistic-geometric interpretation, rather than merely reproducing a known table.

## Limits and comparison

The mean identity is exact but the chi-square statement is asymptotic. Nonregular simplices, noncentral cuts, complete finite-dimensional mass functions and convergence rates are outside scope. The inaccessible full 2026 manuscript and possible older orthant formulations remain originality risks; no independent validation has been performed.

Same-model review: passed. Independent audit: not yet performed.
