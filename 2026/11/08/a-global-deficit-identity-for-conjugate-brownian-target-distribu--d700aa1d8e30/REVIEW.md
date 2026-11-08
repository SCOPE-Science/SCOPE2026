# Scientific review: global conjugate-target resetting optimality

## Correctness — PASS

The renewal mean is an exact ratio for a fixed target and any proper iid positive clock. The free Brownian survival solves the backward heat equation, yielding the positive Green-kernel identity, whose boundary conditions are checked. The reference finite first moment guarantees finite normalization and mean. Swapping variables in a positive double integral gives a squared-ratio deficit with no unproved sign step, including infinite competitor values. Strict equality uses positivity, continuous ratios, the unit limiting hit probability at zero target distance, and uniqueness of the Laplace transform of a nonnegative reset duration. The numerical checker independently passed 37 assertions; all-protocol quantification relies on the exact proof. No finite search is asserted exhaustive.

## Originality — PASS, with publication-priority risk

Evans and Ray (arXiv:2410.01941, originally 2024-10-02) already derive \(p_0\propto f_0^2\), the renewal mean, and a vanishing first variation; these are treated as premises rather than contributions. Their main-text passage following the first-variation derivation expressly says minimization remains to be confirmed, then verifies it numerically only within two parametric clock families. The new squared-ratio Green-kernel identity establishes a nonnegative gap and unique global optimum across all iid positive reset clocks. General restart results (Pal–Reuveni 2016), optimal spatial-reset location (Evans–Majumdar 2011), and bounded-domain position-dependent resetting (García-Valladares et al. 2025/2026) do not assert this theorem. An earlier study of annealed time tails under Poisson resetting is distinct from protocol optimization. Remaining risk: an unidentified implicit general positive-kernel inequality or more recent source could establish equivalent coverage. This review does not assert publication priority conclusively.

## Mathematical value — PASS

The principal paper explicitly leaves the minimum-versus-stationarity question open analytically; a full-protocol global gap is an object-specific structural resolution, not a small numerical improvement. The strict equality characterization distinguishes all non-Poisson competitors and explains why a non-Poisson reference may itself be the uniquely optimal restart law for its conjugate random-target distribution. The identity quantifies departures and handles singular and heavy-tailed competitors without discretization.

## Limits and references

The theorem is one-dimensional, uses a target fixed during each complete search, iid reset intervals, and finite mean for the reference. It does not compare adaptive, position-triggered, or costly resets. Primary sources: https://arxiv.org/abs/2410.01941 (main text and supplementary material read), https://arxiv.org/abs/1607.06048, https://arxiv.org/abs/1107.4225, and https://arxiv.org/abs/2505.16626.

Self-review: passed. Independent audit: not yet performed.
