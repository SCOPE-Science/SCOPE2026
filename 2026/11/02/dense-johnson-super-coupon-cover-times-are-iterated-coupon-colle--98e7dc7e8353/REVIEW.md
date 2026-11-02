# Review of dense Johnson super-coupon coverage

## Correctness (C): PASS

The theorem specifies the pre-update exchange kernel and initial observation at time zero. The omitted-set transversal condition is equivalent to coverage of every target \(s\)-subset. In a fresh-label slot construction, each label occupies a single interval, and greedy interval covering identifies the minimum transversal size with completed independent coupon-collection epochs. Mapping ideal labels onto actual labels makes the actual process no faster; a first-recurrence union bound gives the stated total-variation estimate. A uniform finite-block success event bounds the mean residual time for fixed \(k,s\), giving the claimed expected-value rate. The growing-\(k\) statement uses only the verified coupling bound and the classical coupon-collector Gumbel theorem. A standalone exact-combinatorial and randomized diagnostic checker replays successfully; diagnostics are not substitutes for these infinite proofs.

## Originality (O): PASS (qualified)

Athreya, Mukherjee and Mukherjee's 2023 preprint and 2025 full published article define the same temporally dependent Johnson-swap super-coupon process and develop fixed-parameter results and a conjecture. The inspected introduction, theorem statements and Markovian proof sections do not provide the near-census \(n-r=k\) limit or its independent-epoch factorization. The fixed-parameter formulations in the source keep \(r\) independent of \(n\) and therefore do not imply a constant-order dense-complement limit or a sum-of-Gumbels law. Standard coupon-collector results provide the epoch distribution once the new interval-transversal reduction is established, but not that reduction itself. Historical priority remains qualified: some earlier subset-coverage and interval-stabbing literature could contain an equivalent probabilistic formulation not identified in the reviewed material.

## Value (V): PASS

The near-census regime of the published temporally dependent super-coupon model has qualitatively different cover-time behavior: \(skH_k\) updates at fixed complement size instead of a growing fixed-\(r\) timescale, an explicit quantitative coupling, and a multi-Gumbel growing-complement transition. The interval formulation explains the mechanism and is structurally useful for high-density sampling, rather than merely evaluating a small special case.

## Limits and closest literature

The fixed-parameter Markovian conjecture is neither proved nor contradicted. A growing-complement expected-time limit is not claimed. The main source is S. Athreya, S. Mukherjee and S. S. Mukherjee, arXiv:2304.01145, doi:10.1007/s10959-025-01417-w. The older coupon-subset literature concerns related but not evidently identical temporal dynamics; complete historical priority is not certified.

Self-review: passed. Independent audit: not yet performed.
