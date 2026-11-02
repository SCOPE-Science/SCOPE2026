# Scientific review: Poisson singleton clocks and exponential coverage episodes

## Correctness — PASS

For fixed \(0<\alpha<1\), the statement is an entrance-conditioned, not first-hit, limit. The proof reconstructs the exact Palm law: conditional on a newly appended color, the shared \(M-1\) positions are a uniform surjection onto the other \(n-1\) colors. Poissonization with zero-truncated Poisson counts, conditioned on their sum, is exact. The local central limit estimate for the sum has positive span-one variance and supplies a uniform conditional one-coordinate bound; Long (2026, Appendix A) also proves the relevant estimate. Under that bound the singleton count concentrates, the exchangeable singleton positions converge to a unit-rate Poisson process on the \(n^\alpha\) scale, and the expected number of multirepresented colors completely lost in a bounded time horizon tends to zero. Replacement drawings perturb the first-loss event with probability at most the rescaled horizon times \(\mathbb ER_t/n=o(1)\). This yields the stated exponential episode law. The exact finite mean follows from stationary mass divided by entry flux, with its asymptotic justified independently by the singleton exit-hazard formula rather than weak convergence alone.

The saved standard-library verifier enumerates small surjection words and transitions, checking the entrance Palm uniformity, the Stirling mean ratio, uniform singleton locations, singleton expectation, and the pathwise probability sandwich. Replayed result: 403 deterministic exact assertions passed. Finite tests do not constitute an infinite proof.

## Originality — PASS, with historical-priority qualification

Long (arXiv:2604.26298v1, April 29, 2026) is the main source. Its Sections 2–7 and Appendix A were read for the exact flux, conditional surjection, local estimate and declumping argument; its proved exponential limit is for the *time until the next entrance*, not the time an entered episode remains complete. The finite exact mean can already be deduced from its stationary mass and entry flux, so that part is not presented as novel. Joriki's 2012 Mathematics Stack Exchange answer contains prior heuristic intuition for the \(n^\alpha\) timescale; it does not prove the Palm process limit. Barbour, Braunsteins and Ross (2019) provide general occupancy local-limit methods, not the complete-window episode theorem in their inspected applications. Barbour and Gnedin (2009) was checked at abstract level only and is about infinite occupancy small counts. Searches for aliases (surjection singleton positions, conditional occupancy, coverage clump length) found no directly covering statement. A general earlier clumping/Poisson conditional-occupancy theorem could still imply this special case; independent priority review is needed.

## Mathematical value — PASS

Completion with deterministic expiry produces rare long-separated visits to the complete-window set, so the stationary occupancy probability and entrance flux differ by the episode length. Existing flux asymptotics alone do not determine its distribution. The theorem identifies the microscopic structural cause of persistence (the spatial Poisson process of uniquely represented coupons), gives the full exponential law at its natural scale for every fixed \(0<\alpha<1\), and provides an exact finite mean. The combination resolves a natural duration/declumping question rather than a free parameter variant. The result does not treat nonuniform coupons, the endpoints, or joint episode renewal limits.

## Sources and residual risks

- Christopher D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298v1, 2026-04-29: https://arxiv.org/html/2604.26298v1 . Relevant full text, particularly Sections 3, 5 and Appendix A, inspected.
- Joriki, *Expiring coupon collector's problem*, Mathematics Stack Exchange, 2012: https://math.stackexchange.com/questions/188889/expiring-coupon-collectors-problem . Heuristic anticipation of the timescale, explicitly credited.
- A. D. Barbour, P. Braunsteins, N. Ross, *Local limit theorems for occupancy models*, arXiv:1908.00251v1, 2019: https://arxiv.org/abs/1908.00251 . Relevant full-text methods and applications inspected.
- A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, Electronic Journal of Probability 14 (2009), 365–384: https://doi.org/10.1214/EJP.v14-608 . Abstract-only inspection; indirect relationship.

The scientific risks are implicit coverage by broader classical clump theory and potential unforeseen hypotheses in using local central limit estimates. The present proof states and verifies the required conditioning bounds explicitly.

Self-review: passed. Independent audit: not yet performed.
