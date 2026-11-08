# Scientific review

## Correctness — PASS

For fixed integers \(1\le s<r\), the random walk and full shadow-coverage time are explicitly defined. The proof derives the Johnson transition formula from single replacements and uses the fixed-\(r\) eigenvalue gap. For each fixed finite collection of distinct targets it computes the stationary union-entrance flux and bounds its discrepancy from the sum of individual fluxes by \(O(n^{-s-1})\). The killed-chain principal eigenvalue differs from its entrance flux by \(O(n^{-s-1/2})\), by Poincaré and a sharp one-step entrance bound. Interlacing gives uniform multiplicative joint avoidance probabilities on the coupon-collector time scale, from which factorial moments prove the stated Gumbel law. A one-target union bound proves the expected-time asymptotic. The standalone exact-rational checker reconstructs the local identities on finite examples; its simulation is diagnostic only. No finite test is claimed to prove the limit.

## Originality — PASS, with historical risk

Athreya, Mukherjee and Mukherjee, arXiv:2304.01145, Conjecture 2.4, explicitly conjecture the fixed-parameter temporally dependent expectation scale addressed here. Their Theorem 2.3 covers independent draws and their Theorem 2.5 covers equal target/sample size \(s=r\), rather than the dependent \(s<r\) Gumbel theorem. The 2025 journal version retains Conjecture 2.4. Searches comparing this formulation, a Johnson-graph shadow-cover formulation, rare-target entrance rates, stronger cover-time results, and published mathematical-record summaries did not identify a theorem implying this result. Relevant spectral/mixing and unrelated coupon-collector results do not yield the needed joint avoidance theorem as stated. The possibility of a general abstract rare-event cover theorem subsuming the result, or a later unindexed resolution, remains a residual historical-priority risk. A failed search alone is not a uniqueness proof.

## Value — PASS

The conjecture asks for the leading cover-time constant in a natural temporally dependent subset-sampling model. The dependence causes repeated occupation of the same target; its correct effective entrance intensity is \(\binom{r-1}{s-1}/\binom ns\), rather than the independent-draw occupation intensity \(\binom rs/\binom ns\). Proving a standard Gumbel law in addition to the mean asymptotic identifies the whole extreme-value transition and explains its dependency correction. This resolves a specific published problem for a fixed-parameter family, not a routine relabeling or a pre-existing independent-draw special case.

## Closest literature and limitations

Source: S. Athreya, S. Mukherjee and S. S. Mukherjee, *On a generalisation of the coupon collector problem*, arXiv:2304.01145 (first public 2023-04-03), Conjecture 2.4 and Theorems 2.3, 2.5; also its 2025 open-access journal version, DOI 10.1007/s10959-025-01417-w. The result applies to the exact Johnson replacement rule with fixed \(r,s\), does not give explicit finite-size error constants, and has not received an independent mathematical audit or exhaustive historical-priority certification.

Self-review: passed. Independent audit: not yet performed.
