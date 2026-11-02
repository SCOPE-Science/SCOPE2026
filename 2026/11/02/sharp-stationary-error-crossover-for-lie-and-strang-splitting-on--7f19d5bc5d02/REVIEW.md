# Review of the three-state stationary-error crossover

## Correctness — PASS

The finite-state Markov generator, exact Lie and symmetric Strang factor order, strict positive-rate domain, and total-variation metric are fully specified. Symbolic invariant-law substitution and a separate cofactor derivation agree. Exact deviation signs remove the absolute-value ambiguity, and polynomial factorization plus strict positivity of every coefficient of the polynomial derivative prove precisely one crossover. The general-rate statement uses a direct exact Lie invariant, analytic small-step perturbation of the simple stationary eigenvector, and deterministic large-step limits. The packaged verifier completed all symbolic assertions and 300 exact-rational checks. No infinite conclusion relies on finite enumeration.

## Originality — PASS (with stated risk)

The most relevant inspected full texts concern positivity/mass preservation in graph-Laplacian solvers and relative-entropy analyses of stochastic splitting. Neither inspected source states the exact all-step stationary total-variation laws, unique degree-seven threshold, or general orientation-dependent reversal for conventional edge exponentials. Earlier balanced-splitting work clearly establishes steady-state bias and corrective methods, so neither phenomenon is presented as new. Its detailed PDF was not accessible; the repository abstract alone cannot exclude specialized overlap, which remains an explicit priority risk. Equivalent statements phrased as a three-state Markov kernel, ordered graph-edge exponential, or stationary splitting bias were considered rather than searching titles alone.

## Value — PASS

This is a sharp, analytically complete benchmark for long-time errors of unconditional positivity- and mass-preserving operator splitting. It shows a concrete, non-pathological circumstance in which the scheme with the formally higher local order becomes worse for the invariant distribution at every sufficiently large step, with exactly one error-ranking transition in the minimal directed-cycle example. The precise threshold can test step-selection criteria and diagnose steady-state distortion in finite-state integrators. No general method performance or novel stationary-bias phenomenon is asserted.

## Relevant prior literature and scientific limitations

The relevant background is Blanes–Iserles–Macnamara (2021 preprint), Gourgoulias–Katsoulakis–Rey-Bellet (2015 preprint), and Speth–Green–MacNamara–Strang (2013). The 2013 repository abstract is available but the complete paper was not read, so its full scope is unresolved. The exact phase diagram applies to a specified three-state cycle and specific edge ordering; the arbitrary-rate portion establishes at least one reversal only under the stated inequality. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
