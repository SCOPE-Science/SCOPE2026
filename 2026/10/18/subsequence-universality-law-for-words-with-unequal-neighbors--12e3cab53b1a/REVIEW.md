# Scientific review

**Correctness — PASS.** A unique greedy arch decomposition reduces universality to first-cover factors. In an incomplete arch with \(j\) observed letters, there are exactly \(j-1\) allowed repeated-letter transitions and \(q-j\) new-letter transitions. This yields the four rational factors and the stated bivariate generating function by unique concatenation. For a uniform proper word, these transitions yield an i.i.d. geometric-sum arch law, from which the mean, variance and central limit theorem follow. The standalone program independently enumerates short proper words, directly checks their subsequence universality, and matches exact coefficient arithmetic; it reports `ALL CHECKS PASSED`.

**Originality — PASS, with residual literature risk.** The 2023 regular-language universality paper establishes generic counting algorithms, not the uniform-in-alphabet closed formula or regeneration law for the proper-word language. The 2023 arch-factorization article establishes the decomposition but does not analyze this restricted language. The unrestricted counting paper likewise has different boundary transitions. Searches for the proper-coloring, no-immediate-repeat and Markov-coupon equivalents did not identify prior coverage. This is evidence of non-coverage by inspected sources, not a proof of absolute priority.

**Mathematical value — PASS.** Requiring unequal neighboring letters is a natural constrained-word class. The result determines its complete finite-length universality-index distribution uniformly for every alphabet size and identifies a special regenerative structure and exact Gaussian constants. This is more than a single instance of the general automata-counting algorithm or a numerical sequence: the symbolic reduction eliminates the alphabet-dependent state tracking, revealing an independent renewal law.

Closest literature: Schnoebelen–Veron (arXiv:2304.11932), Adamson et al. (arXiv:2311.10658), and Adamson (arXiv:2304.04583). Limits: general transition graphs and nonuniform sources are outside scope; equivalent unindexed previous work remains possible.

Self-review: passed. Independent audit: not yet performed.
