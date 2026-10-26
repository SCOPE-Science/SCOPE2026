# Scientific assessment

## Correctness — PASS

The result makes a global claim for every finite nonnegative rectangular input. The central equality of feasible sets is proved in both directions: signed outer products yield two diagonally opposite nonnegative rank-at-most-one rectangles; conversely independently chosen nonnegative rank-one blocks can be realized by one signed outer product. Rank constraints are closed determinantal conditions, and a finite union is closed; coercivity in the output matrix proves attainment without assuming bounded factors. Nonnegative singular vectors for a nonnegative block justify sharp attainment of Eckart--Young's rank-one error. The summed block residual yields the exact displayed objective, including zero and empty-block cases. The previously established rank-two, three-by-three counterexample gives sharpness of the low-dimensional frontier. The packaged checker reconstructs every tested signed factor and error identity; its finite cases supplement rather than replace the proof.

## Originality — PASS, subject to historical indexing limits

The directly relevant recent full text [1] proves rank-one NP-hardness and rank-two ill-posedness, but not rank-one attainment or the two-block spectral optimum. The closest earlier full text [2] establishes direct rank-one attainment only for a specific two-by-two matrix and explicitly indicates that general ReLU well-posedness was not established there. The later subzero-completion study [4] concerns geometric ranks and learning algorithms rather than this two-block global Frobenius characterization. Actual semantic searches of published research records and targeted literature queries found no implication covering the theorem, but cannot establish exhaustive novelty. Saul's [3] publisher abstract was accessible; the full older text was not materially inspected, leaving a residual bibliographic risk.

## Mathematical value — PASS

A genuine boundary question is created by the juxtaposition of [1]'s NP-hard rank-one approximation and a rank-two nonattained infimum. The theorem proves well-posedness for the entire rank-one model, provides a concrete spectral optimization formula and a constructive global minimizer, and shows that the rank-two three-by-three failure has the smallest possible latent rank and ambient dimension. This is a structural distinction relevant to global numerical optimization and model selection. The exponential sign search is a limitation, not a polynomial-time performance claim.

## Closest literature and restrictions

References [1]--[4] are documented in RESULT.md. The distinction between direct Frobenius ReLU decomposition and latent surrogates is essential. The novelty comparison does not exclude unpublished or inadequately indexed variants of the sign-partition construction. Statements do not extend rank-one formulas to arbitrary signed targets or attainment to general higher ranks. A follow-up independent check remains unperformed.

Self-review: passed. Independent audit: not yet performed.
