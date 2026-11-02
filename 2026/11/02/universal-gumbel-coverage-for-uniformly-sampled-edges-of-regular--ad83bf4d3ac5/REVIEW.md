# Scientific review: Universal Gumbel coverage for uniformly sampled edges of regular graphs

## Correctness — PASS

The proof explicitly specifies independent uniformly sampled edges of a finite simple regular graph of any degree at least two and uses Poisson thinning to produce independent untouched-edge flags. Adjacent vertices share precisely one flag, giving the stated finite moments. The monotone size-biased coupling of a uniformly chosen vertex has exact added-count expectation \(p[1+d(q^{-1}-1)]\); the classical Stein inequality and decreasing function \(d(e^{u/d}-1)\) give the graph-uniform total-variation rate. A complete-coverage event has exactly zero untouched vertices. De-Poissonization and uniformly integrable two-sided tails give both the discrete-time Gumbel limit and the Euler correction. The sharp degree-one exception is exactly a perfect-matching coupon collector. The standalone verifier passed 593 exact-rational/numerical assertions. Infinite limit arguments are mathematical proofs, not finite-enumeration extrapolations.

## Originality — PASS, qualified

The nearest full primary article, Betken and Thäle, arxiv:2202.07485 (first posted 2022-02-15), draws all equally probable fixed-size groups. Schilling and Henze (2021), Section 3, perturb every group probability near uniform; nonedges with exactly zero probability are outside their assumptions. Falgas-Ravry, Larsson and Markström, arxiv:1601.04455 (2016), give first-order concentration for structured coupons, which does not imply this centered limiting distribution or graph-uniform explicit rate. The closest historical edge-coupon claim addresses many degree-two/degree-one vertices, so it does not imply the degree-at-least-three part. The independent algebraic calculations support exact moments, but similarity-search failure is **not** novelty proof. A general unindexed sparse-group coupon theorem could conceivably dominate this result; independent historical-priority verification remains necessary.

## Value — PASS

The statement answers a natural distributional coverage question for arbitrary regular graph topologies without expansion or connectivity, quantifies the rarity of uncovered vertices with a uniform explicit total-variation rate, and identifies why degree-one pair coverage behaves differently. This provides a useful structural boundary and mathematically meaningful second-order completion-time information beyond first-order coupon estimates.

## Limitations and closest literature

No assertions about irregular or weighted edge-sampling, dependent samples, process-level total variation, or sharp finite-n discrete-time error. The expectation error is only \(o(n)\). The degree-one exception is a known coupon-collector reduction and is not separately claimed as new. Closest sources: Betken–Thäle (2022/2023), Schilling–Henze (2021), Falgas-Ravry–Larsson–Markström (2016/2020). Mathematical independence and complete historical priority are unverified.

Self-review: passed. Independent audit: not yet performed.
