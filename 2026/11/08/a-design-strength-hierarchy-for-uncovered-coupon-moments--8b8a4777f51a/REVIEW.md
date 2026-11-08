# Review of the design-strength uncovered-moment theorem

## Correctness
**PASS.** The exact factorial-moment expression follows by conditioning on an unseen \(r\)-set and counting ordered tuples. Since fixed-size blocks leave the same number of \(r\)-subsets disjoint from each block, the average avoidance probability is independent of the sampling law; strict convexity proves the inequality and equality test. Complement double-counting and inclusion–exclusion establish the weighted-design equivalence under \(r\le\min(k,v-k)\), and projective-plane line incidence proves the all-order triple formula. The standalone exact-rational verification replays small cases without assuming the theorem; none of the infinite assertions depend on finite extrapolation.

## Originality
**PASS, with historical risk.** The nearest directly inspected work, Barak-Pelleg and Berend, *Fano Geometry and Slow Coupon Collecting* (arXiv:2606.28216), studies mean coverage times and finite-order projective-plane comparisons rather than moment-design rigidity. Grunbaum and Yaakobi (arXiv:2510.25305) and Berend and Sher (arXiv:2509.17201) address recovery sets and completion-time expectations. The combination of a universal factorial-moment bound, a sharp equality characterization for all weighted fixed-size mechanisms, and an exact first differing moment in all existing finite projective planes was not identified in the inspected statements. Earlier equivalent design/coverage identities remain a priority risk; absence in searches is not a uniqueness proof.

## Mathematical value
**PASS.** The motivating fair-mechanism papers show that comparison of expected coverage times is delicate. The result supplies a separate exact diagnostic: a weighted design's strength is the order through which repeated-batch unseen-count factorial moments are indistinguishable from uniform sampling. Projective planes give an infinite (for prime-power orders) and axiomatic family whose first two unseen-count moments conceal nonuniform geometric sampling while the third moment detects it with a closed rational separation for two rounds. This is a structural information boundary, not a cosmetic parameter substitution. It does not settle the difficult completion-time ordering question.

## Limitations
The proof does not establish stochastic dominance, completion-time inequalities, or uniqueness of all schemes. Historical priority relative to older general moment and design theory requires further independent attention. The verification script is a finite reproducibility check rather than an external proof certificate.

Self-review: passed. Independent audit: not yet performed.
