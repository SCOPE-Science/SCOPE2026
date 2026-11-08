# Review of the nested uniform temporal-tree covariance theorem

## Correctness

**PASS.** The root-children decomposition is exact because each child either enters at its own edge label (taking its full descending subtree) or does not enter. The mean integral equation has solution \(e^{np}\). Differentiating the independent-child second-moment identity yields a linear ODE with the displayed closed form, and disjoint root-label bins give the mixed covariance. The factorization determines the unique sign crossing; the limits follow from elementary exponential asymptotics. The multithreshold independence consequence uses the published one-threshold exponential limit and an explicit Laplace factorization, without assuming stronger source results. The reproducibility script passed 301 finite assertions, including rational finite-depth calculations and independent simulations. Those checks support, but do not replace, the analytic argument.

## Originality

**PASS, provisional historical assessment.** The full relevant sections of Atamanchuk–Devroye–Lugosi (arXiv:2501.13044, especially Theorem 2.1 and its proof) concern one-threshold size and related structural statistics. Their theorem does not imply the mixed covariance identity by mere specialization, nor the sign-reversal window. Hu–Wu–Dong (2022) study counts at different *depth* cutoffs and pair-accessibility probabilities for a single fixed root label; those quantities are related but do not state the cross-threshold sign classification. Semantic searches of related research records and published literature did not identify an equivalent theorem. The uninspected complete 2022 article and other earlier accessibility results are the main residual priority risks. A failed search is not proof of uniqueness.

## Mathematical value

**PASS.** The original object was introduced to model temporal reachability as a cutoff varies. Nested reachable sets need not have positively correlated cardinalities, and the exact crossover \((\log n)/n\) identifies the scale at which a shared ancestral contribution is overtaken by competition between disjoint root-label bins. The same analysis supplies the microscopic positive-correlation kernel, a negative fixed-separation correction, and finite-dimensional asymptotic independence. This is a structural dependence phase diagram for a natural observable, not an arbitrary parameter slice or a recomputation of the one-point mean.

## Literature and limitations

Primary model and one-point theorem: https://arxiv.org/html/2501.13044 (2025). Closest earlier accessible-path model and depth-profile theorems: https://doi.org/10.52396/JUSTC-2022-0059 (2022). The 2022 full PDF was not inspected, leaving some priority uncertainty. No independent mathematical audit has been performed. Neither a functional threshold-process limit nor boundary-scale results for vanishing \(p\) are claimed.

Self-review: passed. Independent audit: not yet performed.
