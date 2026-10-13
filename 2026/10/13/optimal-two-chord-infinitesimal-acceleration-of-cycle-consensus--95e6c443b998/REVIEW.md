# Review of the two-chord cycle acceleration theorem

## Correctness — PASS

The claim is a finite-dimensional, complete all-size classification of the coefficient of the first-order increase of the second-smallest Laplacian eigenvalue of an unweighted cycle after two budgeted chords. Its proof checks the exact multiplicity-two Fourier eigenspace, computes each chord's projected squared norm and angle, derives and solves the two-vector smallest-eigenvalue optimization, then exhausts all possible angle and maximum chord-length patterns in the three residue classes of \(n\) modulo four. The strict trigonometric comparison for \(n\equiv2\pmod4\) rules out *all* nonorthogonal competitors, not just sampled pairs. The eigenvalue-separation argument justifies an error uniform over all admissible pairs and weights for each fixed \(n\). The actual packaged verifier independently computes projected matrices and full Laplacian spectra for finite sizes, without treating numerical evidence as the universal proof.

## Originality — PASS (self-review, not independent priority certification)

The closest fully inspected older work is Ghosh–Boyd (2006), *Growing Well-Connected Graphs*, especially Section III on perturbation heuristics and eigenvalue multiplicity. It establishes that one edge cannot increase an eigenvalue of multiplicity two, but it neither calculates optimal *pairs* on a cycle nor classifies chord lengths or continuous fractions. Ghosh–Boyd (2006), *Upper bounds on algebraic connectivity via convex optimization*, discusses general semidefinite bounds and ring-like graph families, but not this pair-restricted, fixed-base infinitesimal design. Deng–Chang–Yang (2026), *Single-Chord Augmentation of Weighted Cycles*, restricts its analysis to one chord and identifies several-chord extension as future work. Published mathematical-database searches found no directly covering pairwise cycle formula; nearby graph-spectral entries concern different graphs, spectral quantities, or uniformly applied edges. A single-chord Kirchhoff-index problem and optimization of fully weighted circulant networks have different objectives and feasible sets; neither statement entails the rank-two, two-chord local optimum. Historical equivalence in unexamined sources remains a risk.

## Value — PASS

For a cycle the lowest positive Laplacian eigenvalue has multiplicity two: an arbitrarily strong single shortcut cannot improve consensus rate, whereas two carefully selected weak shortcuts do. The theorem gives a sharp all-size engineering design rule under a natural small added-conductance budget, exposes a previously non-obvious modulus-four transition, and proves why two *longest* chords lose to a long/short pair precisely when \(n\equiv2\pmod4\). The exact first-order gain and all optimum allocations are relevant to minimal network augmentation; this is not a claim about arbitrary finite budgets.

## Residual limitations

The quantitative result is first-order near zero budget and assumes an unweighted undirected baseline cycle, equal chord conductance price, and no geometric crossing restrictions. Relevance to finite budgets, physical wire lengths, and nonuniform baseline cycles requires additional study. Same-model scientific scrutiny is not independent validation.

Self-review: passed. Independent audit: not yet performed.
