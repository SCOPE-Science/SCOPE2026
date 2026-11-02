# Scientific review

## Correctness — PASS

The count of intact sibling cohorts is well-defined even when the parent recruits other cohorts. The precise three-outcome Markov kernel and both conditional drift recurrences have been reconstructed from the tree construction. Exact means and all three second-moment recurrences were independently compared with exhaustive rational state evolution for small cases. The martingale triangular-array proof identifies correct weights, conditional covariance, bounded jumps, and the required variances, including the singular one-child boundary. The coupling to independent Bernoulli variables gives a quantitative, finite-size total-variation Poisson bound. The standalone test passed 1,955 assertions, and the infinite conclusions follow analytically rather than from extrapolation.

## Originality — PASS (provisional)

The 2026 construction paper studies distances, not these birth-cohort statistics. The 2014 blocks-tree paper and the 2020 hooking-network central limit theorem establish related but narrower fixed-block *leaf/degree marginal* laws. The 2017 fringe-subtree theorem is for different tree distributions and counts actual fringe subtrees; in the present tree an intact sibling cohort can have a parent with arbitrarily many other children. The 2023 \(m\)-ary hooking-network parameter is a capacity constraint, not simultaneous cohort size. The compared published mathematical finding on random-recursive-tree root-degree/leaf covariance is not a birth-cohort result. The new finite covariance profile plus independent two-scale triangular limit and Poisson crossover are not implications of those cited statements alone. Broad general martingale/urn methods may encompass intermediate steps; further independent priority checking is still appropriate.

## Mathematical value — PASS

Intact birth cohorts capture the persistence of an entire simultaneous recruitment event, not merely the degree of an individual node. Their fluctuations remain of order \(\sqrt n\), while leaf fluctuations shrink to order \(\sqrt{n/m}\) for growing batch sizes. This resolves a structural dependence and scaling question in a recent random-tree model. When \(m\) becomes proportional to \(n\), the leaf excess instead has a discrete Poisson limit, exposing a sharp boundary between a Gaussian many-event regime and a rare-event regime. These are natural observables and quantitative regimes with possible use in other block-growth or batch-recruitment models; no broad application theorem is claimed.

## Sources and residual risks

Primary model: Bhutani et al. (2026), arXiv:2609.33636. Related established results: Desmarais–Holmgren (2020), DOI 10.37236/9139; Gopaladesikan–Mahmoud–Ward (2014), DOI 10.1017/S0269964813000338; Bhutani–Kalpathy–Mahmoud (2023), arXiv:2308.03857; Holmgren–Janson–Sileikis (2017), arXiv:1603.08125. Residual risks include indirect coverage by a general marked-urn limit theorem and unindexed literature. No claim of independently certified novelty is made. The proof requires uniform recruiter selection and equal-sized batches per row.

Self-review: passed. Independent audit: not yet performed.
