# Scientific review — critical Zipf quorum fluctuations

## Correctness
PASS. The exact finite-time mean and variance follow from independence of the Poisson arrival clocks. The key infinite harmonic-sum asymptotic is obtained by splitting at the scaled index and controlling two bounded-variation Riemann sums. Its finite cutoff tail gives the explicit first correction to the deterministic mean root. A triangular-array Lindeberg argument handles rare early indices separately from small later summands, and time inversion at fixed offsets gives the central limit theorem. The shift exponent \(3\theta/2-1\) determines the stated two-thirds threshold. The exact proof is in RESULT.md. The accompanying computational checks support finite formulae and normalized constants, but cannot certify an asymptotic limit.

## Originality
PASS, subject to the stated residual historical-priority risk. Müller and Šebek (arXiv:2607.08551v1, especially Lemma 6.2 and Theorem 6.3) already prove the first-order critical Zipf quorum constant; this contribution does not claim that constant. The new claim adds a hitting-time central limit theorem at the exact mean root and identifies the nontrivial finite-population bias and its sharp two-thirds phase transition. Chebunin and Zuyev's 2020/2022 infinite-urn functional CLT uses a fixed summable sequence of frequencies and does not, as stated, cover triangular harmonic normalization or the finite-cutoff shift. Baake and Baake's 2026 multiple-coupon paper concerns Markov-generator embeddability. Actual semantic-record and literature comparisons did not reveal an equivalent or stronger covering statement; negative search results alone do not establish priority.

## Mathematical value
PASS. The source's leading-order law does not determine uncertainty at the hitting-time scale. This theorem identifies the exact Gaussian standard deviation and proves a sharp boundary at which a natural published leading-order centering ceases to be suitable for uncertainty quantification. The positive deterministic bias is caused specifically by the upper cutoff of the critical Zipf frequency profile, a structural effect rather than a numerical improvement. The exact-root formulation remains valid on both sides of the boundary.

## Closest prior literature and limitations
Müller–Šebek (2026) is the direct antecedent. Chebunin–Zuyev (published online 2020) supplies relevant but not directly applicable missing-mass CLTs; Baake–Baake (2026) gives adjacent coupon-sampling structures. The result is limited to fixed \(\theta\in(0,1)\), independent exponential first arrivals, and critical harmonic aligned frequencies. It does not prove an all-threshold functional limit, convergence rate, or analogous de-Poissonized theorem. Broader unpublished or older inversion theorems could affect historical priority and have not been exhaustively ruled out.

Self-review: passed. Independent audit: not yet performed.
