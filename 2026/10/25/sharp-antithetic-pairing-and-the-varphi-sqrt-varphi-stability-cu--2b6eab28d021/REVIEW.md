# Scientific review

## Correctness — PASS

For each ordered component pair the two-stage rotation update is a scalar-plus-skew matrix; its squared norm is exactly \((1-\eta^2uv)^2+\eta^2v^2\) times the initial squared norm. This gives all three expectation multipliers and their affine coupling interpolation. Pairwise independence across iterations gives the exact power law for expected squared error; there is no reliance on sampling experiments for the infinite-horizon result. The stability thresholds reduce to three explicit quadratic inequalities, whose ordering follows from an exact reciprocal quartic factorization. The open example at \((a,b,\eta)=(1,2,3/5)\) is rationally verified. The checker supplies 1,490 independent exact-rational assertions, not a substitute for the proof.

## Originality — PASS (self-review)

A source-to-claim comparison was made with the original same-sample SEG analysis (Mishchenko et al., arXiv:1905.11373), general S/I-SEG convergence theory (Gorbunov et al., arXiv:2111.08611), bilinear last-iterate and averaging analysis (Li et al., arXiv:2107.00464), exact planar S/I-SEG multipliers (Yoon--Loizou, arXiv:2608.06182, Lemma 3.11), same-sample across-iteration flip-flop shuffling (Chae et al., arXiv:2501.00511), and antithetic midpoint randomization of a different method (Luo et al., arXiv:2603.22155). Closest mathematical records describe deterministic normal-operator extragradient minimax polynomials or mean-square thresholds for distinct optimizers. No checked statement entails a sharp fixed-marginal *within-step joint-sampling* optimum or the exact antithetic-only stability region. Residual risk: a specialized coupling/transport formulation or an unindexed note could contain an equivalent result; search absence is not proof of novelty.

## Value — PASS

Both sampling conventions are established implementations of stochastic extragradient with the same two oracle-evaluation budget. Their failure on bilinear problems is a fundamental algorithm-design issue. This finding supplies a nontrivial third choice, proves it is the globally optimal paired sampling law above an exact step-size crossing, and classifies precisely when it alone restores mean-square stability. The natural heterogeneity cutoff is an algebraic constant \(\varphi+\sqrt\varphi\), not an arbitrary numerical slice. The result does not claim universal efficacy beyond its explicitly solvable two-component class, and it does not equate mean-square expansion with almost-sure divergence.

## Closest literature and limitations

The 2019 and 2021/2022 works motivate the distinction between same and independent samples but do not give a coupled-pair optimality theorem. The 2026 exact planar analysis shares the normal-form multiplier mechanism but studies the conventional pairing policies and different dynamical objectives; the explicit boundary and three-way separation are not consequences of its stated results. The generality is intentionally confined to two positive bilinear coefficients with uniform marginals, fixed equal stage steps, and independent pair draws between iterations. Publication-priority review remains subject to unindexed literature and independently conducted expert scrutiny.

Self-review: passed. Independent audit: not yet performed.
