# Explicit Lee–Yin boundary certificate for the log-corrected tail-exponent-5 Wigner law, with impossibility of coincidence coupling at the admitted truncation

## Context
Lee and Yin proved Tracy–Widom edge universality for Wigner matrices holds iff lim_{s->inf} s^4 P(|x12| >= s) = 0, noting infinite fourth moment does not preclude universality (illustrated by an informal |x|^-5 log|x| example with no constants or rate). The quantitative side — which explicit infinite-fourth-moment laws retain TW with what truncation cost — was left open. The admitted target sought TW1 persistence with Kolmogorov O((log N)^-1/4) at fixed B_N = N^{1/2}(log N)^-2 for the named p=1/2 law. Steps (i)-(ii) succeeded; step (iii) at fixed B_N is proved impossible by direct coincidence, and is reported honestly as an emergent obstruction.

## Definitions
Let g(x) = (1+|x|)^-5 (log(e+|x|))^-1/2, Z0 = int_R g, c* = 1/Z0, f_Y = c* g, Y ~ f_Y, sigma^2 = E[Y^2], X = Y/sigma. Off-diagonal Wigner entries are X/sqrt(N); diagonal entries are standard (mean zero, finite variance). T(t) = P(|Y| > t), p_N = P(|X| > B_N), B_N = N^{1/2}(log N)^-2, E(N) = N^2 p_N, c' = c*/(2 sigma^4), L(x) = log(e+x).

## Result
1. Well-defined standardized law. 0 < Z0 < inf (Z0 <= 2.5) and 0 < sigma^2 < inf, so X is symmetric with E[X^2] = 1; density f*(x) = sigma c* g(sigma x).
2. Infinite fourth moment. E[X^4] = inf; 2 int_1^R x^4 g >= 2^-5 L(R)^-1/2 log R -> inf.
3. Explicit Lee–Yin tail. s^4 P(|X| > s) = (1+o(1)) c' (log s)^-1/2 -> 0; hence the Lee–Yin criterion holds.
4. Fixed-truncation coincidence impossible. E(N) = (1+o(1)) c' sqrt(2) (log N)^{15/2} -> +inf; with M = N(N-1)/2, P(all |Xij| <= B_N) = (1-p_N)^M <= exp(-M p_N) -> 0. No vanishing-error transfer by direct coincidence coupling at this B_N is possible. Coincidence needs N^2 B_N^-4 (log B_N)^-1/2 -> 0, i.e. B_N >> N^{1/2}(log N)^-1/8 up to slowly varying factor; exponent -2 is strictly on the wrong side.
5. Qualitative persistence (attributed corollary). By Lee–Yin Thm 1.2 sufficiency, N^{2/3}(lambda_N - 2) => F_TW1. No rate is claimed here.

## Proof / evidence
- Finiteness via g <= 1 on [-1,1], g <= |x|^-5 outside; x^2 g <= (1+x)^-3.
- Fourth-moment divergence via (1+x)^-5 >= 2^-5 x^-5 (x >= 1) and slowest-log pullout.
- Upper tail: pull L^-1/2 <= L(t)^-1/2 out of [t,inf), exact int_t^inf (1+x)^-5 = (1+t)^-4/4; squeeze [t/(1+t)]^4 -> 1, log t/L(t) -> 1 gives limsup <= c*/2.
- Lower tail (lambda-block): restrict to [t, lambda t], L^-1/2 >= L(lambda t)^-1/2; t^4[(1+t)^-4-(1+lambda t)^-4] -> 1-lambda^-4, log ratio -> 1; liminf >= (c*/2)(1-lambda^-4); lambda -> inf gives liminf >= c*/2.
- Standardization change of variables; log(sigma s)/log s -> 1.
- Insert B_N into tail: N^2 B_N^-4 = (log N)^8, (log B_N)^-1/2 = sqrt(2)(log N)^-1/2(1+o(1)); union/exponential bound.
- Numeric companions (stdlib-only, approximations): Z0 ~ 0.47704, c* ~ 2.09627, sigma^2 ~ 0.28376, c' ~ 13.02; squeeze factors U = 0.866/0.958/0.996 at t = 30/100/1000; E(N)/(log N)^{15/2} -> c' sqrt(2) ~ 18.41.

## Limitations
- No TW convergence rate and no new Green-function comparison inequality are proved; the target Kolmogorov O((log N)^-1/4) at fixed B_N is not established (coincidence route disproved).
- TW1 limit is a corollary of published Lee–Yin, not an independent universality proof.
- Digits are reproducible approximations, not interval-certified; no proved statement depends on them.
- Diagonal entries assumed standard; certificate concerns the off-diagonal law.

## Reproducibility
Run stdlib scripts: python3 output/artifacts/prove_squeeze.py (squeeze factors, quadrature, E(N) scaling, VERIFY_OK) and python3 output/artifacts/tail_moments.py (enclosures (a)-(e), E(N) and q stress test). Analytic limits in DRAFT Sec.2 do not depend on quadrature digits.

## References
- J. O. Lee, J. Yin, A Necessary and Sufficient Condition for Edge Universality of Wigner matrices, Duke Math. J. 163 (2014), 117-173. arXiv:1206.2251.
- K. Schnelli, Y. Xu, Convergence Rate to the Tracy–Widom Laws for the Largest Eigenvalue of Wigner Matrices, Commun. Math. Phys. (2022). https://doi.org/10.1007/s00220-022-04377-y
- K. Schnelli, Y. Xu, Quantitative Tracy–Widom laws for generalized Wigner matrices, EJP (2023). https://doi.org/10.1214/23-ejp1028
- G. Ben Arous, A. Auffinger, S. Peche, Poisson convergence for heavy-tailed random matrices (2009). https://arxiv.org/abs/0710.3132
