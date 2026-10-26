# Review of the positional-gap inversion theorem

## Correctness

PASS. Conditioning sorts the selected values while keeping the unordered selected-value set uniformly random and preserving exchangeability of the other values. Conditional pair-comparison probabilities are derived from the \(k+1\) equally likely ranks of an unselected value. Summing comparisons gives the weighted interior-gap formula; weak-composition symmetry gives the mixture, and the exact size-bias identity gives the covariance. All boundary cases \(2\leq k\leq n\) are covered, including \(k=n\). Exhaustive rational enumeration through \(n=7\), run from the attached standalone checker, agrees for every eligible marked set and every claimed identity.

## Originality

PASS under the documented accessible-source comparison, subject to independent priority checking. Pinsky (arXiv:math/0407353) explicitly defines the same marked-subsequence mixture and proves approximation properties but does not give a position-dependent inversion law in the inspected relevant sections. Janson--Nakamura--Zeilberger (arXiv:1312.3955) develops generic fixed-pattern mixed-moment methods; the examined covariance examples and asymptotic claims neither state nor force the sharp layout dependence. Even-Zohar (arXiv:1811.07883) gives asymptotic profile structure for fixed patterns. Searched research records on cycle counts and inversion-indicator geometry concern distinct observables. The main conditional theorem has strictly richer information than a global covariance and is not inferred by simply matching titles or parameters. Residual risk: an unlocated special-case calculation in older linear-extension or permutation-pattern literature could coincide with this formula.

## Value

PASS. The marked-position mixture was introduced as a precise model of partial randomization of permutations, so inversion count is a natural measure of remaining order. The theorem determines, for every finite \(n,k\), the exact effect of each interior unmarked gap and the best/worst layouts, not merely a numerical moment. The uniform-mixture law is then a derived quantitative diagnostic for growing as well as fixed subsequence lengths. This sharp position-resolved extremal structure motivates the precise statistic and avoids an arbitrary finite slice.

## Closest literature and limits

The closest sources are Pinsky's 2004 increasing-subsequence mixture, Janson--Nakamura--Zeilberger's 2013 pattern-moment methods, and Even-Zohar's fixed-pattern asymptotics. The result is a conditional mean and covariance statement, not a distributional ordering, full inversion-conditioned monotonicity theorem, or independent historical-priority certificate. Exhaustive finite checks support but do not prove the all-size result; the algebraic proof provides the all-size guarantee.

Self-review: passed. Independent audit: not yet performed.
