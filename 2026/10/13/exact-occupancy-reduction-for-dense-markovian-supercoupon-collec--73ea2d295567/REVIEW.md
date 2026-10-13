# Scientific review

## Correctness — PASS

The complement identity is pathwise, not merely an expectation calculation: an \(s\)-set is still unseen exactly when it contains every omitted vertex. The current omitted vertex cannot repeat immediately, but the *number* of distinct omitted vertices has a birth probability \((n-k)/(n-1)\) independent of the previous omission history. This identifies the full scalar Markov transition law with iid-coupon occupancy, after a one-round shift. Strong Markov waiting-time decomposition yields independent geometrics, including the degenerate first waiting time. The Stirling formula counts onto words, and the exact finite mean/variance formulas follow with no asymptotic approximation. For proportional \(s\), positive variance limit and bounded geometric moments validate Lyapunov's theorem. Exhaustive rational computations corroborate, rather than replace, the all-parameter analytic argument.

## Originality — PASS, with residual risks

The primary 2023 manuscript and its open 2025 published text were inspected, especially their Markovian Conjecture 2.4 and \(r=s\) Theorem 2.5. Those give the model and a known cover-time boundary, but do not state the pathwise uncollected-set identity, full \(r=n-1\) occupancy process, independent-geometric representation for all interior \(s\), or proportional-size Gaussian consequence. The earlier partial coupon collector already has the occupancy formulas; the mathematical contribution is the specific complement-lumping equivalence that brings the *dependent supercoupon process* into that classical class. Searches of related mathematical records and terminology did not identify a dominating formulation. Since the complement observation is elementary, an equivalent older result could exist under complete-graph subset-cover language; this is a residual bibliographic risk, not evidence of proven global priority.

## Value — PASS

The largest nontrivial display size \(r=n-1\) is a canonical endpoint of the Markovian supercoupon problem, not a tuned parameter slice. Across **every** number \(s\) of coupons per supercoupon, the problem of covering \(\binom ns\) correlated targets collapses to a one-dimensional process and yields an exact all-time uncollected-target law, a complete finite stopping-time distribution, and a distinct proportional-size Gaussian regime. The reduction also explicitly isolates the already known \(s=n-1\) case. This is a structural classification of a motivated stochastic model rather than a renamed standalone occupancy exercise. It does not address general \(r\le n-2\), and equivalent older subset-cover results remain a bibliographic risk.

## Closest literature and limitations

S. Athreya, S. Mukherjee, and S. S. Mukherjee, arXiv:2304.01145 (first public 2023-04-03), especially Conjecture 2.4 and Theorem 2.5; journal version DOI:10.1007/s10959-025-01417-w. Generic coupon-collector occupancy laws are acknowledged as classical and used only after the new model-specific reduction. The fixed-display-size conjectural asymptotic regime is not addressed. Finite verifier checks do not establish infinite statements independently.

Self-review: passed. Independent audit: not yet performed.
