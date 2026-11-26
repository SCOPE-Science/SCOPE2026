# Independent mathematical audit

## correctness

PASS

The invariant-measure inverse-branch weights telescope, giving P_N g_m=(N+x)/(m+x) for almost every x and derivative u_N(1−u_N)/N+O(N^−2). With z=N+x, P_N id=N(z Σ_{j≥0}(z+j)^−2−1). Its derivative equals N times the difference of the sum of inverse squares and 2z times the sum of inverse cubes. The two Euler–Maclaurin expansions give −N/(2z²)+O(Nz^−3), uniformly on [0,1]. The branch-index tail (N+x)/(a+x) increases in x, so a common quantile couples the sampled inverse points in reverse order. Thus the difference of their means bounds the Lipschitz action of P_N, giving an O(N^−1) seminorm bound. Each iteration multiplies the affine slope by −1/(2N) with an additional O_k(N^−k−1) Lipschitz error at lag k. Stationarity moves P_N^k to the first indicator; Cov(id,1_[0,v_N]) under μ_N is −v_N(1−v_N)/2+O(N^−1). This gives both the sign and exact coefficient uniformly in the stated interior ratios at fixed k. Terminating points are null; there is no claim for growing k. The first-lag integral and second threshold image also follow by logarithmic integration and digamma partial fractions. The frozen `python3 verify.py` (mpmath) was inspected, not run: its 56 comparisons check kernel/mean identities and sampled lags 1 and 2, not all k.

## originality

PASS

The operator, reversal of monotonicity, sign alternation and a nonsharp O(N^−k) scale are already available from earlier work. The supported distinct contribution is the signed nonzero fixed-lag coefficient with both moving threshold factors and a uniform one-order-smaller remainder. The closest inspected primary results give the operator and bounds, not that asymptotic on its iterates against these observables. This is a best-of-knowledge comparison, not a claim of historical priority.

## value

PASS

This is a quantitative independence law for natural macroscopic digit events. It fixes the leading magnitude as well as the sign, identifies the universal ratio between successive lags, and treats both thresholds as moving parameters. The rank-one mechanism explains why a contraction estimate by itself does not capture the coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
