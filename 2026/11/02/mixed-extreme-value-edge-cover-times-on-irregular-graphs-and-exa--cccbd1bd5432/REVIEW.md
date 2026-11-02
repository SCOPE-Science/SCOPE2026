# Self-review

## Correctness — PASS

The graph model and all degree hypotheses are explicit. Independent Poisson edge clocks give the exact joint-uncovered identity \(q^{\sum\deg-e(W)}\). Fixed-size factorial moments for the rare degree-one and degree-two populations are asymptotically those of independent Poisson variables because selected adjacent low-degree paths contribute \(O(D^{-(s-1)/2})\) for component size \(s\ge2\); high-degree uncovered vertices have expected count at most \(Rq^3=o(1)\). A mixed-observation-time version yields the last-class probability. The leaf-dominant regime is exactly independent across distinct leaf edges. A uniform edge-label exponential-clock coupling gives \(T/m-U\to0\). The finite spider recurrence follows from no adjacent absent arm edges, and its Poisson transform gives all integer-time completion probabilities. The 105 deterministic checker assertions compare the finite formula to independent brute-force enumerations; these checks supplement, and do not substitute for, the infinite proof.

## Originality — PASS (qualified)

Tauraso (2008) already gives a generic exact transform for uniform edge-sampling coverage and regular-graph results. It is not claimed that deriving an arbitrary finite distribution from the generic transform is new. Falgas-Ravry, Larsson and Markström (2016) provide broad structured-coupon collector theory. Godbole, Grubb, Han and Kay (public preprint 26 March 2018) give coverage threshold progression results in other combinatorial settings. Their inspected statements do not provide the explicit two-class extreme-value crossover, its last-vertex degree probability, or the compact balanced-spider factorization as a stated result. Actual semantic searches of published research indexes and accessible prior-claim texts found related spider combinatorics and coupon models without the same claim. The main residual risk is a stronger general Poisson limit theorem or older graph coverage result that implies the claim without using matching terminology; historical priority is not guaranteed.

## Value — PASS

Degree-one and degree-two vertices have different incidence hazards and contribute on competing \(\log L\) versus \(\frac12\log D\) scales. The natural crossover \(L\asymp\sqrt D\) creates a mixed extreme-value distribution that is neither a standard Gumbel nor a mere expectation estimate, and the limiting probability of a leaf being last adds a meaningful marked statistic. The balanced spider is a natural test family in which its arm length and branch count tune the competing populations, with a compact exact finite distribution useful as a benchmark. The result is not just a routine one-parameter substitution or a recomputation of a fixed small instance.

## Sources, risks, and independence

Primary comparisons: Tauraso, *Edge Cover Time for Regular Graphs* (2008), https://cs.uwaterloo.ca/journals/JIS/VOL11/Tauraso/tauraso18.pdf; Falgas-Ravry–Larsson–Markström, arXiv:1601.04455 (2016), https://arxiv.org/abs/1601.04455; Godbole–Grubb–Han–Kay, arXiv:1803.09601 (first public 26 March 2018), https://arxiv.org/abs/1803.09601. General exact transforms and broad random-set covering methods are prior art. No exhaustive historical-priority assessment is claimed. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
