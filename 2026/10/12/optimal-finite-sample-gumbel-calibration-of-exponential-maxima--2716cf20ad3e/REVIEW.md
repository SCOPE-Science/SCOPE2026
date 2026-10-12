# Review of optimal finite-sample Gumbel calibration of exponential maxima

## Correctness — PASS

For all integers \(n\ge1\), the beta representation of the exponential maximum gives exact moments and differential entropy. Minimizing first over the Gumbel location yields the scalar objective, whose second derivative \(t^{-2}+\sum_{j=1}^{n}(t+j)^{-2}\) is positive for every \(t>0\). The derivative crosses zero exactly once; boundary behavior is covered. A comparison across sample sizes and Taylor expansion at the unique root prove the strict scale ordering and both sharp asymptotic limits. Direct quadrature, moments, and a standard-library verifier corroborate finite numerical cases, without replacing analytic proof.

## Originality — PASS, with bibliographic uncertainty

Johnson (arXiv:2007.03569, Proposition 2.4, Theorem 4.4, Remark 4.6) gives the forward-relative-entropy identity, fixed-target convergence and exact entropy of the normalized exponential maximum. The new result does not claim those ingredients: it performs the unrestricted finite-sample location-scale information projection and obtains its unique root and optimized asymptotic constant. Zarfaty, Barkai, and Kessler (arXiv:2006.13677) improve extreme-value norming by distribution-function matching and fitting rather than forward-KL minimization; Cardone, Dytso, and Rush (arXiv:2205.04621) study entropic Gaussian limits for central ranks, not maximum-rank Gumbel calibration. Targeted comparisons did not identify an implying result, but unindexed historical fitting studies or the inaccessible full treatise of Reiss could overlap. A failed search is not a proof of priority.

## Value — PASS

The precise best finite-sample Gumbel law for maxima of exponentials is a natural question in information-theoretic extreme-value approximation. This theorem determines it for every integer sample size and supplies the sharp forward-KL improvement \(1/2-3/\pi^2\) versus \(1/2\) under optimized location alone. The scope is deliberately limited to this canonical parent and this direction of divergence; no universal extreme-value convergence theorem or statistical fitting procedure is asserted.

Self-review: passed. Independent audit: not yet performed.
