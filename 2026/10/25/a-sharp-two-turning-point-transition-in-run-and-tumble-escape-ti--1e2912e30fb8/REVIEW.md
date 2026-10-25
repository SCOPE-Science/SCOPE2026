# Review of the sharp sticky-wall variance transition

## Correctness

PASS. An incoming-state backward two-component boundary problem gives the exact exit-time Laplace transform. Its Taylor derivatives and a separately derived pair of backward-moment ODEs agree identically on the displayed first two moments; the included SymPy checker replays both routes. The variance derivative has a quartic numerator with strictly positive second derivative in the bulk rate and strictly positive derivative in wall detachment, with exact sign witnesses at the parameter endpoints. This establishes a unique collision parameter and the complete zero count without numerical extrapolation. The nondegenerate tangency establishes the square-root merger. The physically singular zero-excess corner is excluded.

## Originality

PASS with residual priority uncertainty. The primary 2014 first-passage work supplies a mean-only reflection calculation. The 2023 generic-boundary work includes a general first-passage Laplace law, which implicitly covers all computable moments; that existing forward law is acknowledged as prior coverage. The 2024 sharp optimum concerns the mean from central/symmetric injection, not the variance from directed entrance-wall injection. The 2021 gated-target study explicitly examines relative-variance nonmonotonicity but has a different target mechanism and geometry. Claim-level comparison isolates the newly derived all-parameter variance-extrema count, its unique disappearance threshold and its square-root merger. Semantic searches of accessible mathematical records did not locate an equivalent statement, but absence from search results does not establish priority over unlocated sources.

## Value

PASS. Enhancing wall release is an intrinsic tuning parameter in persistent transport, and the transition changes the fluctuation response qualitatively, from a local maximum followed by a local minimum to monotonic growth. Unlike in prior mean-optimality scenarios, the mean in this defined experiment is strictly monotone, so mean-only optimization cannot reveal the variance bifurcation. The exact threshold and fold scaling turn a general forward-transform calculation into a sharp experimentally interpretable classification with nontrivial parameter boundaries.

## Remaining limitations

No independent audit has been performed; the analysis depends on exactly the stated velocity-reversal convention, initial orientation, wall-release rule and observable. Generic-boundary first-passage transforms in the literature raise residual risk that a mathematically equivalent optimization may be obtainable or previously recorded elsewhere, even though inspected primary statements do not assert this parameter-complete result. No claim of a new general transform or new variance-moment method is made.

Self-review: passed. Independent audit: not yet performed.
