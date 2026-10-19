# Scientific review: switching-reservoir exclusion correlations

## Correctness — PASS

The finite-state generator is specified completely, including environment independence, rate normalization, and all boundaries. The constant-reservoir covariance used as a premise is reconstructed from the stationary moment equations and separately documented in Derrida–Lebowitz–Speer, §7.2, Eq. (7.13). Singular-limit arguments are finite-dimensional: frozen-bath sector invariant measures and fast-bath averaged dynamics are each uniquely determined. The explicit slow- and fast-rate covariances have opposite strict signs for every pair, with the two-site rational covariance following from exactly solved mixed-moment equations. The all-size result is proved rather than extrapolated from experiments. `verify.py` checks the exact two-site identity, stationary full generators on chains through five sites, and fixed-bath moment identities through eighty sites.

## Originality — PASS, with limited bibliographic uncertainty

The closest directly examined paper, Derrida–Lebowitz–Speer (arXiv:cond-mat/0109346, pp. 3–4 and §7.2), derives static-reservoir correlations, not the switching-bath claim. Santos–Schütz (arXiv:cond-mat/0104147, pp. 1–3) studies a single constant-density reservoir on a semi-infinite chain, not the finite telegraph boundary. Floreani and collaborators (Journal of Statistical Physics 186, 33, 2022, §§1, 3.1–3.3) allow particle jump-rate/type switching with prescribed reservoirs rather than random switching of reservoir occupancy. Targeted bibliographic and published-claim searches for random/telegraph boundary densities, stationary SSEP covariance reversals, finite-size formulas, and equivalent switching-process formulations found no demonstrated stronger coverage. A specialized publication under alternate terminology could exist; the searches are not a uniqueness certificate.

## Value — PASS

For classical boundary-driven SSEP, fixed reservoirs enforce nonpositive off-site correlations. The theorem isolates a competing physically meaningful mechanism, common temporal boundary fluctuations, and proves that it overturns this sign for every pair in every finite chain when sufficiently slow. The opposite fast-switching regime and exact minimal-size critical rate make the effect quantitative, rather than a generic assertion about mixtures. This is a finite-volume correlation property relevant to interpreting driven transport measurements in fluctuating environments; it does not require a downstream general theorem to be useful.

## Limitations and closest sources

No uniqueness or rate formula for zero-crossings is claimed beyond two sites. The slow/fast limits are not asserted uniformly over growing chain lengths. Additional literature under dynamic-boundary or random-environment terminology is a residual overlap risk. The references and scientific limits are described in RESULT.md. Independent validation is not included.

Self-review: passed. Independent audit: not yet performed.
