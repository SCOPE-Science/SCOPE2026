# Self-review

## Correctness — PASS

The complete set of optimal truncations follows from the explicit spectrum and Eckart–Young–Mirsky. Since \(0\preceq P\preceq I\), every off-diagonal projector entry is at least \(-1/2\), and a zero-sum projector containing \( (e_1-e_2)/\sqrt{2} \) attains the bound for every intermediate rank. Partition projectors supply strictly positive rank-r matrices with explicit nonnegative factors and exactly the optimal Frobenius error. Adding \(\varepsilon\) times the attaining projector separates the spectrum, keeps all input entries positive, forces a unique negative-entry optimum, and yields the strict constrained gap by uniqueness plus a closed feasible set; a partition competitor bounds the penalty by \(\varepsilon\sqrt{r-1}\). The dimensional proof is symbolic and exact. 36 dimension/rank rational checks and the \(n=3\) illustration passed; these checks are supplementary.

The worst-entry expression, equality endpoints, positive nonnegative factorization, uniqueness of the perturbed optimum, strict constrained gap, and approximation-error upper bound all pertain to the same claim in RESULT.md. The analytical proof applies for every stated integer dimension and rank, not only those checked numerically.

## Originality — PASS (subject to publication priority)

Targeted semantic searches compared equivalent formulations, dominating parameter statements, numeric tables, and implication relations. Relevant complete texts were inspected, particularly the 2022 randomized low-rank nonnegative approximation study, the 2020 tangent-space alternating projections study, and the 2009 singular-value nonnegativity-perturbation criteria. These study algorithms or sufficient preservation conditions and do not establish the sharp all-tie, all-intermediate-rank compound-symmetric criterion together with zero NMF cost and the vanishing-cost spectral-gap perturbation. The classical spectral and projector ingredients are acknowledged, and absence of indexed direct coverage is not regarded as proof of priority.

Relevant works: Matveev and Budzinskiy (arXiv:2201.11154, 2022), Song, Ng and Jiang (arXiv:2009.03998, 2020), and Montaño, Salas and Soto (DOI:10.1155/2009/301582, 2009). The last source provides substantial preservation inequalities, but no identified theorem implies all parts of the present classification. A still-undiscovered specialized theorem is a residual risk; independent audit has not been performed.

## Value — PASS

Nonnegative low-rank approximation and the distinction between truncated SVD and nonnegative-factorizable optimization are practical numerical-analysis questions. The theorem identifies a precise dimension-scaled parameter threshold independent of truncation rank, shows that the nonnegative constraint can cost nothing even where some unconstrained minimizers are negative, and proves a robust sign-versus-objective-cost separation after arbitrarily small data perturbation. These exact structural facts offer benchmarks for tie-breaking and tolerance-sensitive numerical methods rather than an arbitrary finite example.

## Limitations and evidence

The exact sign threshold is special to strictly positive compound-symmetric matrices, and the perturbation's nonnegative-factorization excess is not determined exactly. The Python verifier tests finite exact-rational cases only; the proof is independent of it. No floating-point or general nonnegative-rank algorithmic claim is made.

Self-review: passed. Independent audit: not yet performed.
