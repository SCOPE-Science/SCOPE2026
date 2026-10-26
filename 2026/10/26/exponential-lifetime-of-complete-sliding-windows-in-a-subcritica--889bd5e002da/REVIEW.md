# Scientific review: exponential lifetime of complete sliding windows

## Correctness — PASS
The exact entry conditioning yields a uniform onto common middle block of length \(M-1\) over \(n-1\) coupon types. The finite survival sandwich is checked for all shorter shifts. The size-biased singleton hazard of a surjective occupancy word is \(n^{-\alpha}(1+o(1))\), uniformly over \(O(n^\alpha)\) deletions, by a zero-truncated-Poisson lattice local limit theorem. Summation yields the exponential survival law; the fresh-sample repair probability is bounded by \(O(n^{\alpha-1})\). Stationary mass divided by entry flux gives the finite Stirling-number mean and its asymptotic. The standalone exact-rational verifier passes 98 finite assertions. Limitation: the finite checks do not establish the asymptotic; the local-limit/Fourier estimate is a mathematical proof component.

## Originality — PASS (historical priority unconfirmed)
The most direct source, Long (2026, arXiv:2604.26298v1), supplies the stationary mass, entry flux, rare *first-arrival* exponential limit, and a zero-truncated-Poisson local limit method. Its Remark 4.4 anticipates mean clump duration, and its flux formula immediately implies the exact mean here. None of those statements asserts the entry-conditioned *episode-lifetime distribution*. Long's related arXiv:2605.14511 addresses stationary first entry in nonmonotone coupon collectors; its introductory material and Remark 2.5 do not give this specific lifetime law. The 2012 Joriki discussion anticipates a rare deletion hazard without proving a distributional conditional episode theorem. Semantic database searches over duration, sliding windows, surjection and exponential occupancy limit did not retrieve an equivalent statement; negative searches alone do not establish absolute novelty. An unidentified scan-statistics theorem might imply the specialization.

## Mathematical value — PASS
The finding distinguishes a polynomial \(n^\alpha\) coverage-episode persistence scale from the much longer waiting time to a first complete window. A full conditional exponential law, plus a controlled repair mechanism, is mathematically more informative than the readily deduced stationary average episode duration. The result is directly relevant to interpreting temporal clusters in expiring occupancy and sliding-window scan events, and supplies a tractable benchmark for more general expiration models.

## Limitations
The bound assumes independent uniform draws and fixed \(0<\alpha<1\), not the critical or nonuniform regimes. No quantitative total-variation rate, higher moments, or independence across episodes is claimed. Priority and mathematical correctness have not been checked independently.

Self-review: passed. Independent audit: not yet performed.
