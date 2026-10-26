# Review: inversion–cycle covariance reversal in Mallows permutations

## Correctness — PASS
The claimed covariance is the exact parameter derivative \(q\mu_n'(q)\). At the uniform point, a self-contained two-prescribed-arc completion argument gives \(\operatorname{Cov}(C,\operatorname{inv})=-(2n-1)/12\). Near the identity, the unique zero-inversion permutation and the \(n-1\) one-inversion neighbors determine the negative first term. Near the reversal, the unique maximum-inversion permutation and its \(n-1\) immediate neighbors yield the exact parity-dependent positive first term. Continuity gives a zero above \(1\); an elementary rational formula handles \(n=2\). The \(n=3\) derivative and uniqueness follow from an explicit polynomial and Descartes' rule. Exact enumeration through \(n=8\) is supporting evidence, not an infinite proof.

## Originality — PASS (with priority uncertainty)
The 2016 Gladkich–Peled work treats cycle-count order estimates under \(0<q<1\); its reflected-regime discussion does not imply an all-size sign reversal. The 2022 He–Müller–Verstraaten paper studies limiting distributions and asymptotics as \(n\to\infty\) at fixed \(q\), not the finite-size derivative with respect to \(q\) and its near-reversal coefficient. A published published-finding corpus result already gives the \(q=1\) covariance, so that part is acknowledged as prior; it alone does not imply positivity at strong reverse bias. Targeted searches for aliases of cycle/inversion covariance, Mallows monotonicity, and extreme-bias expansions found no matching positive-bias theorem. Residual risk: an older finite-\(n\) identity or discussion may cover this sign change without the searched wording; global novelty is not independently established.

## Value — PASS
The parameter \(q\) directly biases the ranking model toward more inversions. The intuitive inference that this should monotonically reduce the number of permutation cycles fails **for every nontrivial size \(n\ge3\)**, not just at an isolated parameter example. The theorem identifies the complete size boundary \(n=2\) versus \(n\ge3\), the exact leading sign and coefficient on both parameter extremes, and an interior turning point. This is a structural dependence change in a classical probability model; it is not merely a small computational improvement or a relabeling of the known uniform-point identity.

## Limitations
The number and positions of positive-parameter covariance zeros remain unclassified for \(n\ge4\). The asymptotics fix \(n\); there is no uniform statement about growing \(n\) and simultaneous parameter scaling. Search and self-review do not substitute for independent priority verification.

Self-review: passed. Independent audit: not yet performed.
