# Scientific review

## Correctness — PASS

The result specifies the full feasible class of symmetric, nonnegative stochastic transition matrices, and the proof establishes a global lower bound by convex automorphism averaging. The two-by-two Fourier block eigenvalues reduce the spectral optimization to a strictly convex one-variable function. The claimed weights uniquely minimize that function. An explicit positive difference of squares controls every negative Fourier mode, including boundary cases and both parities of the cycle length. The exact heuristic formula and limiting gap ratio follow by a separate mode comparison. The embedded script rechecks all symbolic identities and complete dense-matrix spectra for finitely many graph sizes, without treating those checks as an infinite proof.

## Originality — PASS, subject to residual literature uncertainty

Closest primary sources are Boyd–Diaconis–Xiao (2004), the Boyd–Diaconis–Parrilo–Xiao symmetry analysis (initial arXiv 2007), and Olesker-Taylor–Zanetti (2024). The first two give the general convex method and exact results for cycles, wheels, and other symmetric graphs, but their inspected material does not state the present exact optimum for a corona of a cycle. The third concerns geometric mixing-time bounds and not this exact minimax problem. A known exact complete-core corona formula does not establish the distinct cyclic spectrum; the present proof must bound all Fourier modes. Directed, nonsymmetric or nonuniform-stationary results were excluded from equivalence comparisons because their feasible sets differ. A specialized uncatalogued publication with exactly this claim remains possible; the search does not constitute an originality certificate.

## Value — PASS

Pendant states create a genuine design conflict between maintaining high transition rates along the backbone and leaving enough probability to enter and exit leaves. The theorem solves that tradeoff globally in closed form for an entire sparse graph family, not just finitely many instances. It also identifies the zero optimal cycle self-loop, proves uniqueness within the natural invariant class, and quantifies a sharp \(50\%\) asymptotic spectral-gap improvement over two widely used uniform-target weight assignments. The exact result is a useful benchmark for stochastic network optimization and for studying effects of pendant states on mixing.

## Scientific limitations

The claim does not assert uniqueness among all asymmetric edge-weight patterns, nor does it treat nonsymmetric Markov chains, nonuniform stationary laws or non-SLEM mixing objectives. Its mathematical originality is based on inspected primary literature and tested semantic overlap, with residual risk explicitly acknowledged.

Self-review: passed. Independent audit: not yet performed.
