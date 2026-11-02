# Scientific review

## Correctness — PASS

The final claim is the sharp complete-state mean-square stability region for the exact three-state maximal-feedback EControl recurrence, with a stronger primal nonconvergence assertion when the erasures are genuinely random. The update matrices were reconstructed from the actual EControl algorithm, including the separate memory and stored-gradient updates. The symmetric-matrix moment operator has six coordinates, and its determinant is exactly factored as in the proof. For transmission probability exceeding two thirds, the displayed positive-definite two-by-two Lyapunov matrix proves stability of the fast memory mode at zero step size; the isolated slow eigenvalue has derivative \(-2\). The cone-preserving spectral-radius and determinant argument excludes a hidden unit-circle crossing and establishes the exact full interval. A common-invariant-subspace argument supplies a positive-definite dual Perron matrix, so the lower bound is not an artifact of special covariance initial conditions. The primal one-step identity forces auxiliary mean-square decay if the primal mean square decays. The case of perfect transmission is treated separately. Exact rational path enumeration and symbolic identities passed; these finite checks are corroboration, not the infinite proof.

## Originality — PASS, qualified

The motivating EControl article [arXiv:2311.05645](https://arxiv.org/abs/2311.05645) gives the algorithm and illustrates failure at full feedback in a different multidimensional Top-1 setting; it does not state the exact random-erasure cutoff or step-size formula. [EF21](https://arxiv.org/abs/2106.05203) has a different memory scheme. The subsequent [arXiv:2605.31594](https://arxiv.org/abs/2605.31594) gives broad and empirically optimized feedback conclusions, but not the corresponding three-state Bernoulli moment polynomial. A prior scalar Bernoulli-error-feedback result bounds a different geometric-delay recurrence by \(2q/(2-q)\); it does not logically cover a model with no stable positive step for \(q\le2/3\). The aliases and stronger-coverage searches returned no demonstrably dominating claim. Priority is nevertheless qualified because abstract-level access to the prior technical record and undiscovered compressed-gradient literature do not constitute an exhaustive novelty certificate.

## Value — PASS

The exact hard reliability threshold for *any* positive step size is algorithmically diagnostic: the motivating EControl study emphasizes controlling error feedback but does not quantify the all-step impossibility under independent erasures. Even after gradient-consistent initialization, below the critical reliability the primal mean square cannot converge. The explicit boundary identifies when smaller positive steps help and when they provably cannot; it is therefore more than a reparameterization of existing sufficient convergence rates. The conclusion is deliberately limited to scalar maximal feedback and should not be read as an indictment of safely regulated EControl.

## Closest literature and limits

Closest inspected sources: Gao–Islamov–Stich (2023), Algorithm 2 and Appendix C; Richtárik–Sokolov–Fatkhullin (2021), EF21 update and guarantees; Thomsen–Taylor–Dieuleveut (2026), EControl tuning discussion. A published scientific note on classical Bernoulli error feedback is also compared by implication rather than title alone, but only its searchable abstract could be accessed. Other specialized stability results might contain equivalent calculations. The evidence is self-review, not independent expert review.

Self-review: passed. Independent audit: not yet performed.
