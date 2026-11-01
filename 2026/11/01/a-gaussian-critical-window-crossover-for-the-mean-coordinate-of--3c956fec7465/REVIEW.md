# Scientific review

**Correctness: PASS.** The shell Markov recurrence is exact; kernel cancellation yields the mean-coordinate generating function, and the first-passage ballot coefficient theorem yields a finite binomial formula. The triangular-array central limit theorem with uniform integrability then proves the critical-window coefficient. The script `checker.py` independently checks direct branch integration against the ballot identity in 27 exact-rational cases. These finite checks are supplementary to the proof.

**Originality: PASS within inspected literature.** Monthus, arXiv:2409.19999, already gives the finite-time propagator, the one-time coordinate observable in Eqs. 157–159, and fixed-critical-time shell asymptotics in Eq. 66; Yan et al., arXiv:2308.09269, already establish the model's transition and discuss correlations. The exact finite-time formula is an algebraic organization of this established system, not a new general ergodic principle. The distinct claim is the moving-probability critical-window limit and its Gaussian crossover, not stated in the inspected source sections. Unread or unindexed equivalent asymptotic analyses remain a priority risk.

**Mathematical value: PASS.** A natural width in a finite-time observation of the intermittent threshold is \(n^{-1/2}\): this theorem identifies the entire crossover curve for a physical observable with an exact coefficient, including its strict monotonicity, convexity and the two edge regimes. It cannot be obtained by inserting \(p=1/2\) into a fixed-parameter stationary formula, as the critical law has no finite stationary density. The exact walk representation makes the finite-time comparison reproducible.

**Limitations.** Uniform initial distribution; annealed first moment only; the source literature has strong prior full-time formulas from which this focused limit can be derived. Independent publication-priority checking and independent mathematical audit have not been performed.

Self-review: passed. Independent audit: not yet performed.
