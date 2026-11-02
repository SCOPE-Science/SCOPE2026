# Scientific review of the new middle-arrival reversal theorem

## Correctness

**PASS.** The complete first-hit model and both reset protocols are specified. Conditioning on the common Poisson partition gives a binomial mixture; strict convexity of the short-horizon Brownian hitting CDF bounds the conditional hitting chance below one half and gives strict Jensen acceleration at the second arrival. A tilted scalar renewal theorem proves sharp first- and second-joint-survival exponents, strict Cauchy–Schwarz proves their nonadditivity, and exponential integrability makes three-joint survival negligible in the median tail. The 154 finite checks are reproducible but do not replace the proof.

## Originality

**PASS, best-knowledge assessment with limitations.** The closest source is Vatash et al. (arXiv:2609.23542), whose visible main text gives full ordered-arrival formulas under independently reset Brownian particles and numerical protocol comparisons; the present calendar-time crossing, early explicit interval and long-time pole ratio were not found in examined material. Biroli et al. (arXiv:2303.18012) study the fastest event and reset protocol, while Belan (arXiv:1906.05619) studies the median quantile of a single completion time. Extensive semantic record queries yielded no matched claim, but the uninspected portions of the 2026 supplement and broader exchangeability/renewal literature remain residual priority risks. General mixture-of-binomial inequalities and the renewal theorem are explicitly treated as known building blocks, not the new result.

## Value

**PASS.** The middle of three arrivals is the smallest nontrivial rank where common-clock synchronization produces neither uniformly earlier nor uniformly later completion. The rigorous sign reversal proves an obstruction to protocol selection by a universal stochastic order, even though both protocols have identical single-particle completion laws. The sharp slow-tail exponent identifies why shared resetting can initially help completion of two labels but later increases the risk of very slow completion; this fills a physically motivated gap in rank-dependent resetting benchmarks.

## Closest literature and limitations

The 2026 rank-dependent paper discusses global resetting through comparisons of optimal rate profiles. The 2023 fastest-searcher paper does not establish a second-arrival sign reversal. Existing general mixture inequalities explain the extreme-rank convex comparison, but do not determine the long-time spectral gap or the middle-rank crossing. The analysis is limited to three independent Brownian drivers, identical starts, strictly positive fixed rate, and instant complete resets. The crossing need not be unique; no independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
