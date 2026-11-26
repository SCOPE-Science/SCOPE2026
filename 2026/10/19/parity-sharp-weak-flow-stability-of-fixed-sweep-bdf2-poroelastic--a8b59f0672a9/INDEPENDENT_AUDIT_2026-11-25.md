# Independent mathematical audit

## correctness

PASS

Equations (3.6a–d) specialize to the relaxed multiplier -w/(2+w) and an unrelaxed final solve, with w=kappa/(1+epsilon), so the final pressure input uses q=(-w/(2+w))^(K-1). Put A=(1-q)/(1+w), H=(4zeta-1)/(3(1+epsilon)), and v=2zeta-1. The two-by-two final update on a mode has trace H[1+(kappa-w)A]-wqv and determinant -kappa qvH. Its two-step companion characteristic polynomial is thus the stated monic quartic, including on the full four-state space and without dividing by zeta. At zero flow the factorization gives roots 1, 1/3 and the pair from zeta^2+2a_K zeta-a_K. The strict Jury inequalities are exactly -1<a_K<1/3. Outside the closure, a_K<-1 forces modulus greater than one by the root product, and a_K>1/3 makes the quadratic negative at -1, forcing a real root below -1. Exactly P_epsilon(1)=epsilon(1+wq)/(1+epsilon+kappa) and P_0'(1)=2(1+a_K)/3; the simple root moves into the disk with slope -3/[2(1+kappa)]. The other strict inequalities persist by continuity, which also preserves an unstable root in the outer regimes. At K=2,kappa=3/2, a_K=-9/14 yields the stated roots and modulus. The K=2 frontier 2 is a fixed-coupling weak-flow limit; the published sufficient frontier 1 is likewise limiting in this comparison. Equality cases, including the multiple root at a_K=-1 where the simple-root argument does not apply, are not classified. Source checker and recorded 469-check output inspected; the conclusion rests on the recurrence and exact algebra, not running that script.

## originality

PASS

The BDF2 algorithm, sufficient condition and the empirical even-sweep advantage are antecedents. The one-pass scheme and a delay-based one-third sufficient condition are also prior. The supported distinct result is the sharp strict scalar fixed-sweep weak-flow separation for general K, proving that the even-K improvement really enlarges the open spectral regime of the specified four-state recurrence. No exact matching theorem was verified; historical priority is not certified.

## value

PASS

A sharp fixed-coupling spectral frontier explains a previously numerical parity advantage, distinguishes actual instability from failure of a sufficient condition, and gives an exact stable witness outside the published sufficient range. It is a natural, reproducible benchmark for general splitting analysis, not a claim of spatial or nonlinear stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
