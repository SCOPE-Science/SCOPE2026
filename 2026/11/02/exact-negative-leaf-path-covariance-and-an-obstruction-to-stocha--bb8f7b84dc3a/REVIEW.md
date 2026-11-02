# Scientific review

## Correctness — PASS

Exact independent-root-split recurrences lead to a mixed-moment ODE with unique power-series solution; subtracting exact means gives covariance for all n>=2. Exact n=7 bivariate distribution recurrence supplies rational CDF crossing. Standard second-moment recurrences yield variance constants, hence asymptotic correlation. The standalone checker enumerates 8! permutations, checks bivariate recursion and 100 sizes of exact moment identities; finite checks corroborate, not replace, the proof.

## Originality — PASS (best-knowledge, not absolute priority)

Searched published-finding corpus formulas, aliases and nearest published claims as well as full-text Holmgren–Janson (2014), Drmota–Hwang (2005), and relevant multivariate BST survey sections. Available results treat separate random recursive tree statistics, squared-root split imbalance, fixed fringe-count covariances, or level profiles. None of the inspected statements directly implies the explicit leaf-count/total-path covariance and n=7 CDF obstruction; unlocated general joint BST moments remain a priority risk.

Closest identified literature: Holmgren–Janson (2014) for fixed fringe-count covariance and its path-length caveat, Drmota–Hwang (2005) for BST level-profile correlations, and Neininger–Rüschendorf for multivariate cost recurrences. Closest research records are 6d69fbada9a9 (squared root-split imbalance and path length) and ab0acf44833f (root degree versus leaves in the **different** recursive-tree model). Historical generic BST mixed moment formula coverage remains a possible limitation; the Bóna–Pittel leaf-distance paper was only checked at abstract level.

## Value — PASS

Terminal-node count measures branching/shape while internal path length measures sorting/search cost. Their exact finite negative covariance and vanishing Pearson correlation distinguish absolute dependence from asymptotic decorrelation; the n=7 crossing rules out the tempting stronger monotone conditional-risk interpretation. This is a natural two-statistic dependence question, not an arbitrary parameter slice.

## Scope and remaining limits

All probability statements are about random binary search trees with distinct keys and uniform insertion permutation. Exact enumeration covers only \(n\leq8\), whereas the covariance theorem for all \(n\geq2\) follows from a separate algebraic proof. Negative covariance does not imply stochastic ordering; the latter fails at \(n=7\).

Self-review: passed. Independent audit: not yet performed.
