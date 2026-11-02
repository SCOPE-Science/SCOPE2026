# Scientific review

## Correctness — PASS

The proof is an exact finite-dimensional moment calculation with convergence supplied by a strict Schur stability criterion. Independent epoch signs yield a two-step Lyapunov equation, distinct from the iid one-step Lyapunov equation. Exact symbolic rational elimination verifies the three stationary second moments, including the identity relating odd-phase variance to the second coordinate of the epoch-end covariance; factored differences yield each sign interval and boundary case. The initial state disappears geometrically. The rational witness is checked directly. The verifier is supplementary: the paper contains the all-parameter sign proof.

## Originality — PASS (qualified)

The closest primary source, Kühn–Rosenow (arXiv:2306.05300), already analyzes heavy-ball momentum with within-epoch anti-correlations and long-time **averaged** weight variance. Its Appendix A carefully distinguishes time averages from fixed-update-index covariances. The phase-averaged formula here is not advanced as new. The assessed original item is the exact pair of *phase-resolved* variances plus the three sharp crossover thresholds relative to IID; neither was located as a stated or stronger covering result in the inspected source's main text/Appendix B. Ying et al. cover periodic constant-step stochastic reshuffling without momentum, Qiu–Ma–Milzarek address general convergence bounds rather than stationary phase effects, and De Sa provides different counterexamples, so priority for the general sign-reversal idea is not claimed. Published-result similarity searching did not surface an identical phase theorem. Residual possibility remains of an implicit earlier specialized matrix-covariance derivation or equivalently phrased phase law; independent priority verification is outstanding.

## Value — PASS

The distinction is motivated by actual reporting practice: algorithms commonly evaluate loss at epoch ends, while per-step diagnostics or checkpoints can be taken after any minibatch. An exact sharp interval makes it possible for these two protocols to reverse their verdict about the *same* convergent optimizer, and positive momentum creates additional switching intervals beyond epoch-average conclusions. This is a structural sampling/momentum interaction, not a minuscule improvement or arbitrary parameter slice.

## Boundaries and reproducibility

Exactly two equally curved scalar components and equal/opposite offsets, constant hyperparameters, independent permutation each epoch, deterministic initial state, stable \(0<\eta\lambda<2(1+\beta)\), \(0<\beta<1\). Expected errors are stationary second-moment phase limits, not pathwise accuracy. The script `verify_phase.py` uses SymPy and recomputes the covariance systems from the update matrices. Independent scientific validation and independent priority audit are unperformed.

Self-review: passed. Independent audit: not yet performed.
