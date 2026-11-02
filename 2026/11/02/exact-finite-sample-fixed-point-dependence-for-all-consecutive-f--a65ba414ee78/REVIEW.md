# Scientific review: fixed-point dependence of consecutive four-patterns

## Correctness — PASS

For a uniform permutation, conditional on one specified fixed point, the remaining values are uniformly ordered. This gives the rank-conditioned binomial probability in the proof. The fourth-order Vandermonde identity makes the covariance a universal term minus an explicit boundary-exclusion count. Each exclusion count is polynomial of degree at most three, so four independently computed exact evaluations prove each of the 24 proposed polynomial identities for every sample size. The three sign reversals follow from the displayed integer quadratics, not finite experiments. The standalone exact-arithmetic checker passed 954 assertions and exhaustively enumerated 46,224 permutations. Remaining correctness risk is manual transcription of the displayed 16-orbit table; both the code and direct binomial expression are supplied for independent comparison.

## Originality — PASS, with historical-priority risk

The closest source checked is Paguyo (arXiv:2112.07728, first posted 2021-12-14), which treats fixed points and descent/inversion statistics of permutations in parabolic double cosets rather than the joint fixed-point/individual-consecutive-four-pattern covariance tensor. Borga (arXiv:2003.08426) proves central limits for consecutive patterns in permutation families but not these finite mixed moments. Fulman–Kim–Lee (arXiv:1902.00978) treats the aggregate number of peaks and cycle structure; peaks are not the individual four-pattern counts. Allen and collaborators (arXiv:2011.12179) count distinct consecutive patterns, not mixed covariance with fixed points. Accessible published mathematical-result summaries cover exact fixed-point–descent dependence and fourth consecutive-pattern frequency polytopes, neither of which algebraically implies this mixed moment table on the inspected statements. A general multivariate pattern generating function might implicitly contain the formulas, and some primary texts were inspected only in relevant portions: historical priority is therefore provisional.

## Value — PASS

This is a natural complete covariance classification for all 24 minimal nontrivial four-letter local order tests jointly with the global fixed-point statistic. It identifies the exact exceptional finite-size behavior rather than an arbitrary case: `2143` crosses through zero at size five, `4231` at size six, and `3142` remains negative until its delayed reversal between sizes seventeen and eighteen. A uniform boundary-exclusion identity explains the source of all differences and provides a reusable conditional-moment method. The facts may support joint finite-sample calibration of local pattern and fixed-point randomness diagnostics. No larger asymptotic theorem or independent validation is claimed.

## Closest literature and limitations

The result is confined to uniform permutations and consecutive patterns of length four. Its covariances decay at order \(n^{-1}\), and it does not establish stochastic independence or a general higher-order sign theorem. Relevant original documents were compared on their actual objects and conclusions, not just paper titles. The possibility of implicit older tabulations or unpublished derivations persists.

Self-review: passed. Independent audit: not yet performed.
