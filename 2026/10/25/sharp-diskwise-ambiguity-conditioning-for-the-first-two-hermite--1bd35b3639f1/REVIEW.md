# Scientific review — sharp diskwise Hermite ambiguity conditioning

## Correctness — PASS

The proof reconstructs the normalized first two Hermite ambiguity factors exactly and reduces the two-channel squared lower singular value to a continuous radial scalar minimum. The derivative yields one interior minimum for weights exceeding one half and an endpoint bottleneck; monotone crossing gives the unique optimal mixture. The implicit equation has exactly one root, its monotonicity is verified, and the boundary/asymptotic regimes are derived analytically. The standard-library checker passed 1,698 numerical assertions, which are corroboration and not a proof for the continuum.

## Originality — PASS, with historical-priority risk

Alaifari–Yang (arXiv:2410.05486, §2.2 and §3.2) study Hermite ambiguity annuli and recovery, not a sharp budget-constrained continuous multiplier norm. Grohs–Liehr–Rathmair (arXiv:2207.10620, §1.1) obtain sampled lattice uniqueness for four mixed Gaussian/Hermite windows, which does not imply the sharp two-channel disk condition number. Published finite cyclic spectrogram weighting and Hermite Gabor frame results concern different objects. Available mathematical claims were compared for exact implication, including a finite eight-measurement quadratic-polynomial weight optimizer. An unseen prior analysis of this scalar minimax problem remains possible.

## Value — PASS

A natural design question in multiwindow ambiguity inversion is how to distribute fixed measurement precision. The theorem solves the complete two-window disk problem, including all maximizing weights, the exact onset radius, the transition asymptotics, and asymptotically linear improvement in inverse conditioning. The result is specifically for unrestricted linear ambiguity-field inversion; it does not assert optimal nonlinear phase retrieval or higher-window optimality.

Self-review: passed. Independent audit: not yet performed.
