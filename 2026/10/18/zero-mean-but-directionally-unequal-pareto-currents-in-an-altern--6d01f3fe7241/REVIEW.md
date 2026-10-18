# Scientific review

## Correctness — PASS

The reset-free current equals the initially-empty right-half occupation. SSEP pair covariance is nonpositive because its linear two-particle evolution has the forcing \(-[\rho_i-\rho_{i+1}]^2\) at adjacent sites and initially zero covariances. Hence variance is bounded by the expected current, whose exact Bessel representation grows as \(\sqrt{t/\pi}\). This proves the current concentration needed for exact rather than heuristic tail coefficients. Alternating-renewal occupation weights give the signed mixture; a uniform short-age second-moment estimate justifies the Pareto-tail limit. The scale-calibration map is strictly increasing onto the positive half-line by monotonicity and an integrable \(3/2\)-moment bound. These arguments establish all quantifiers for \(3/2<\alpha_\pm<2\), \(b_\pm>0\).

Finite-state tests and Bessel quadratures (81 checks) independently test normalizations and inequalities, but do not replace the infinite-lattice proof. The numerical example is not interval certified.

## Originality — PASS

The closest primary works study (i) one step with exponential resets [1], (ii) two complementary configurations reset with constant Poisson rates [2], and (iii) one step with heavy-tailed waiting times [3]. The third establishes general stationary renewal-current ingredients and heavy-tail effects, but not the alternation of different Pareto residence exponents, the unique zero-mean calibration, or both directional tail coefficients jointly. In particular its one-configuration result cannot imply the cancellation criterion without adding a separate alternating two-phase renewal construction. The first two do not include nonexponential residence laws. Current-fluctuation and SSEP negative-dependence foundations [4,5] are not claimed as new. Published mathematical records and primary-literature searches did not identify an exact equivalent statement.

Residual scientific risk: a more general semi-Markov resetting theorem could imply the full result as a corollary; all new results remain subject to independent originality review. Similar source titles do not establish priority, so comparisons were made at theorem/parameter level.

## Value — PASS

The symmetric exclusion process is a canonical interacting-particle transport model; a previously studied zero-mean resetting state can conceal strong nonequilibrium fluctuations. This theorem gives a natural complete calibration and exact two-sided tails for renewal-controlled alternating preparations. Different tail exponents make the nonequilibrium distinction observable even after exact mean cancellation; the finite-first-moment/infinite-second-moment regime is a sharp structural contrast, rather than an arbitrary parameter slice.

## Closest sources and limitations

[1] Basu, Kundu and Pal, arXiv:1906.11801 (2019); [2] Sadekar and Basu, arXiv:2004.00951 (2020); [3] Mishra and Basu, arXiv:2211.14120 (2022); [4] Derrida and Gerschenfeld, arXiv:0902.2364 (2009); [5] Borcea, Brändén and Liggett, arXiv:0707.2340 (2007). The new theorem does not assert first priority over any uninspected equivalent reduction or global-reset-inclusive current theorem. The stationary object is the current since the most recent reset on the infinite lattice.

Self-review: passed. Independent audit: not yet performed.
