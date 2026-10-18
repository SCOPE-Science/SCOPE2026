# Independent mathematical audit

## correctness

PASS

Unrolling the first EMA for (-1)^(t-1)G gives mhat_t/g_t = (1-beta1)/(1+beta1) * [1-(-beta1)^t]/[1-beta1^t]. It equals a on every even step and a(1+beta1^t)/(1-beta1^t) on odd steps. Constant g_t^2 forces v_t=G^2(1-beta2^t) and vhat_t=G^2. Thus the denominator is |G|+epsilon independent of nu2,beta2. Differentiation yields d q_inf/d beta1=-2nu1/(1+beta1)^2, which is zero at nu1=0 and strictly negative only if nu1>0. The source RESULT.md wrongly said strictly decreasing for all fixed nu1, contradicting its own derivative. The full replacement RESULT.md corrects this boundary while retaining and proving the Nyquist response and sharp floor. Independent recurrence/limit checks corroborate but do not establish the analytic proof.

## originality

PASS

The source Ma--Yarats QHAdam formula establishes the algorithm and motivation for immediate gradient mixing; its broad norm bounds and WMT16 sweep do not give the exact period-two bias-corrected parity, second-moment erasure and sharp first-discount Nyquist gain. Published Resultary comparisons with AdaMomentum and A2Grad alternating diagnostics concern different algorithms, not an implication for QHAdam. The exact analysis may be elementary but is not located as a prior statement.

## value

PASS

Stale gradients and immediate-gradient discounts are precisely why quasi-hyperbolic momentum was introduced. Exact alternating-signal response distinguishes first and second moment roles at a natural highest temporal frequency; the nu1=0 correction matters for the complete hyperparameter boundary, and WMT16 calibration yields a concrete interpretable gain. Narrow signal diagnostic, not convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
