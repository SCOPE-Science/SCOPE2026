# Independent mathematical audit

## correctness

PASS

PASS: From the actual over-relaxed ADMM equations (source Eq.16) specialized to rho=delta>0, alpha=2, symmetric Q positive definite, the x step is (Q+delta I)^-1(delta z^k-mu^k-q). For eta^k=mu^k-delta z^k and x*=-(Q+delta I)^-1 q, x^{k+1}-x*=-(Q+delta I)^-1 eta^k, z^{k+1}-x*=(Q-delta I)(Q+delta I)^-1 eta^k/(2delta), and mu^{k+1}=delta z^{k+1}. Thus eta^1=0 for arbitrary initialization and exactly x²=z²=x*, mu²=delta x*, with one-update termination iff eta^0=0 (invertibility of Q+delta I). Independently exact rational scalar witness Q=2 delta=1 q=-3 z0=0 mu0=1 produces first (2/3,7/6,7/6), second (1,1,1). Proof is general matrix algebra, not finite empirical extrapolation.

## originality

PASS

PASS, qualified: Ghadimi--Teixeira--Shames--Johansson Theorem 2 says optimal rho=delta, alpha=2 converges in one iteration under their arbitrary-start setup; Appendix establishes mu^{k+1}=delta z^{k+1} but then substitutes mu^k=delta z^k at initial k=0 without hypothesis. The explicit warm-start iff and uniform two-update correct bound are not stated in those examined primary passages. Subsequent Giselsson--Boyd DRS/ADMM rate analysis addresses asymptotic contractivity rather than this start-manifold issue. Search cannot exclude an unindexed erratum; the original parameter-rate optimality is not newly claimed.

## value

PASS

PASS: Corrects a concrete finite-termination claim under the actual source initialization convention by identifying the exact invariant warm-start manifold and giving a uniformly sharp two-step alternative, with an explicit counterexample. This is a motivated reproducibility and algorithm-interpretation issue, not merely a routine numerical discrepancy. No claim beyond regularized split quadratics in exact arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
