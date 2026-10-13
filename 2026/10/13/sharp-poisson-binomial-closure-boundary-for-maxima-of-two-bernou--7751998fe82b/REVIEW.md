# Scientific review

## Correctness (PASS)

The distributional CDF-square identity is exact. For two arbitrary Bernoulli summands its quadratic PGF discriminant is the product of two nonnegative factors. For larger homogeneous binomial sums, the rescaled PGF converges coefficientwise to \(2(1+u)^m-1\); its simple nonreal roots persist under sufficiently small perturbations when \(m\ge3\). At three trials, explicit probabilities and a fully specified cubic discriminant yield a strictly monotone polynomial whose unique zero locates the real-rootedness transition. The equivalence between real nonpositive PGF zeros and finite Bernoulli convolutions handles factorization and the boundary cases. Exact-rational checks in `verify.py` are supplemental and do not certify the universal statement.

## Originality (PASS, residual risk)

The 2023 order-statistics theorem of Badiella, del Castillo, and Puig establishes preservation of ultra log-concavity, not the stronger Pólya-frequency/real-rooted-PGF condition defining Poisson-binomial distributions. The 2022 article of Jakimiuk and collaborators addresses inequalities and extremal laws among log-concave or ultra-log-concave distributions, not maxima of independent Bernoulli sums. Tang and Tang's survey gives polynomial tools and distribution learning but not the CDF-square operator's exact small-dimensional phase. Published-record and semantic mathematical-result searches did not identify a result implying this three-part classification. Terminology or an older unindexed paper could nevertheless contain it; no independent literature audit has occurred.

## Value (PASS)

Order-statistic formation is known to preserve ultra log-concavity. The identified sharp cutoff between two and three trials shows why this does not extend automatically to Poisson-binomial structure, and the exact three-trial transition identifies where the stronger structure reappears. The result is a complete natural minimal-size boundary, a uniform negative classification at higher sizes near zero, and an exact first nontrivial parameter phase diagram, not an isolated numerical example.

## Closest literature and limits

The nearest theorem is Badiella–del Castillo–Puig (2023), Theorem 2, whose conclusion is strictly weaker. No claim is made about arbitrary three-trial heterogeneous laws or the full parameter region at trial count four and beyond. Potential equivalence through classical Pólya-frequency terminology remains the main originality risk.

Self-review: passed. Independent audit: not yet performed.
