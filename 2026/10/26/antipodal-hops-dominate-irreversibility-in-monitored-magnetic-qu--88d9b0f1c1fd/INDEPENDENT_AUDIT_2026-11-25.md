# Independent mathematical audit

## correctness

PASS

For odd N=2m+1, each unordered pair has a unique oriented shortest arc of length d<=m. Its leading transition probability in both directions is b*tau^(2d) with b=A_short²/(d!)²>0; diagonal probabilities tend to 1. The chain is doubly stochastic by unitarity and strictly positive for small nonzero steps, so the stationary weighting is 1/N and grouping the two orders gives the stated entropy without a further factor of two. Hermiticity gives P(-tau)=P(tau)^T. An odd-order coefficient pairs two walks whose concatenation with one reversed is a closed odd walk; below N that is impossible, and at N such a walk must go once around the cycle without backtracking. Thus the relevant amplitude products use the complementary arcs, and the real part of i^(N-2d) exp(i Phi) gives (-1)^(m+d+1) sin(Phi). Twice the cross term and the directional difference give c=4(-1)^(m+d+1) A_short A_long sin(Phi)/(d!(N-d)!). The entropy term starts at c²/b times tau^(2N-2d), with analytic factors after canceling powers in the logarithm. Each paired term is even, so its correction is at least two powers higher. For nonzero sin(Phi) only d=m yields N+1; there are N distinct such pairs, and c²/b cancels the short-arc product exactly. Uniform weights give the stated specialization. On even cycles sublattice conjugation gives reciprocity; for Phi a multiple of pi the real symmetric gauge does so for any length, with zero entropy also on reciprocal zero-probability pairs by the stated convention.

## originality

PASS

The known magnetic-cycle interference and dephasing-to-Markov reduction are not credited. The supported distinction is the stationary path-reversal entropy asymptotic, with its inhomogeneous complementary-arc coefficient and dominance by the least probable, maximally separated transitions. The strongest indexed analogue treats the same full-dephasing map and gives the whole-matrix antisymmetry order and an exact uniform nearest-neighbor contrast; that bounds the scale but does not evaluate the entropy or its leading far-pair terms. The most similar published odd-cycle flux asymptotic inspected concerns Lüders return statistics, not this observable. The comparison does not settle priority or assert exhaustive novelty.

## value

PASS

In a natural model with a uniform stationary state, the exact entropy law distinguishes stationary irreversibility from directional bias of individual transitions. The short-arc cancellation and maximal-distance dominance show why measuring only the common nearest-neighbor steps misses the leading stationary irreversibility. The weighted coefficient supplies a quantitative benchmark for disordered hopping and cannot be read from the directional norm or symmetry tests alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
