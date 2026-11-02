# Scientific review

## Correctness — PASS

For exactly two identical additive agents the maximum envy at each prefix is the absolute signed load difference. The proof uses disjoint parity-indexed step edges for the odd-count and odd-heavy-position cases. For the remaining even-heavy-position case it proves the exact odd-length unit-prefix lower bound \((k+d^2)/2\), combines the next two gap charges with disjoint remaining unit-edge charges, and shows that terminal odd gaps \(d\ge3\) cannot improve on the heavy-last construction. The two explicit policies then meet the piecewise lower bound for every real \(H\ge1\). The descending-regime and integer endpoints were also independently checked by exact rational dynamic programming and brute force, as documented in `VERIFICATION.md`.

## Originality — PASS, with priority risks

The October 7, 2026 primary paper defines the optimization setting, provides the general sequencing lower bound and approximate greedy theorem, and already identifies the special three-good example \(\{1,1,2\}\). No novelty is claimed for that example. A prior exact unit/double subclass also covers \(H=2\) and is not treated as original here. The contribution is a uniform theorem for every real \(H\ge1\) and every multiplicity, resolving which release pattern is optimal and giving the exact tent-shaped greedy regret with both critical thresholds. It is not a mere rescaling of the unit/double result: normalizing the small goods to value one fixes their ratio to the single exceptional value, which can be any real \(H\), not only two. The closest signed-prefix-sum paper preassigns signs and so cannot directly imply the present sign-choice result. Exact-search and semantic-result comparisons yielded no equivalent theorem, but do not establish global novelty. A differently formulated result in discrepancy, scheduling, or prefix-sum optimization remains possible.

## Value — PASS

The exact one-exceptional-good family isolates a natural tractable regime within a generally NP-complete sequencing problem. Unlike a single counterexample, the law proves universal transitions: sorting is optimally safe when the exceptional value is at least three times the base unit, can be suboptimal only for an even number of base goods, and its precise excess peaks at the double-value point. These thresholds and the optimal penultimate-release construction are informative for planned sequential allocation and provide a calibrated benchmark for broader multiple-exceptional-good or weighted-time variants.

## Closest literature and scope

Goldberg, Robinson, and Teh (2026), arXiv:2610.09843v1, Sections 4–5 and Appendix C.5, supplies the optimization model, universal bound and sharp sample. Dobler and Nöllenburg (2025), WADS, Section 3.2, studies an allied but fixed-sign absolute-prefix-sum permutation problem. The result assumes identical additive valuations, two agents, unit goods plus one exceptional good, freely selectable release order and unweighted prefix cost; it does not solve heterogeneous, fixed-order or multiple-exceptional-value cases. No externally independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
