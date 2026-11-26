# Independent mathematical audit

## correctness

PASS

Independently expand R(h(X−1)) using (1−tX)^−2 and sum each residue class modulo n. With a_r=(1−t)t^r/(1−t^n), the coefficient is a_r times [(1+√2)(1−t)(r+1+n t^n/(1−t^n))−√2]. For h>0 all a_r are positive and the bracket strictly increases with r, so the diagonal alone tests nonnegativity; off-diagonals are strictly positive at either diagonal zero and throughout the positive safe ranges. This does not assert off-diagonal positivity inside the forbidden range. Row sums are one by R(0)=1 and h=0 is the identity. Writing U_n=(1−t)(1+n/(e^(na)−1)) with a=−log t gives strict decrease in n; diagonal sign is that of U_n−γ, equivalently q_n. Independently converting 2−3t−3t²−3t³+15t⁴ on each half interval to Bernstein form gives respectively (2,13/8,9/8,13/32,5/16) and (5/16,7/32,3/4,11/4,8), all positive, and 5q_4 is strictly larger. At t=3/5, q_5=(7205√2−10313)/3125<0. The one sign variation of q'_n and opposite derivative endpoint signs give exactly one minimum; positive q_n endpoints and the negative witness give two simple roots for every n≥5. For the lower limit, signs at β±ε bracket the lower root for large n since U_n→1−t there (choose β+ε<3/5); the upper moves to 1. For fixed s>0, U_n(e^(−s/n))→s/(e^s−1). The latter strictly decreases from 1 to 0, so fixed s on either side of s_* bracket −n log t_n^+, since the comparison points are eventually above 3/5. Converting both limits to h proves the assertions. Independent high-precision bisection reproduces 3.222709632051…, 6.805854390690… and 3.4529561713… .

## originality

PASS

The comparison found the same scalar method and absolute-monotonicity radius in the primary TR-BDF2 paper, but not the cycle-specific necessary-and-sufficient inequalities, the two positive thresholds or the recovery scaling. Exact cycle calculations with other stability functions and the same TR-BDF2 map on a different graph family do not imply this classification. The supported distinct result is the directed-cycle classification, not the method formula or the value of the known radius itself.

## value

PASS

The smallest counterexample, exact disconnected safe set, and linear recovery scaling together calibrate the gap between a general sufficient positivity step and the actual endpoint behavior on a natural conservative irreducible test family. In particular, neither L-stability nor conservation guarantees nonnegative transitions, and failure at one step does not imply failure at all larger steps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
