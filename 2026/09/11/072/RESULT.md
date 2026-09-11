# Explicit singular uniform exponent 3/5 for the factorial-block vector sigma0

## Context

In simultaneous Diophantine approximation in R^2 with the sup norm, Dirichlet's
theorem gives, for every x, infinitely uniform solubility with exponent 1/2.
Vectors beating every constant factor are singular; vectors beating the
exponent are strictly singular with a quantified gap. Existential abundance
theorems (Beresnevich–Guan–Marnat–Ramirez–Velani) and dimension/spectrum
theorems (Cheung–Chevallier, Das–Fishman–Simmons–Urbanski, Schleischitz)
describe set size and the full Dirichlet spectrum, but attach no pointwise
uniform exponent to an explicit named factorial pair. The admitted target asks
for such a pointwise certificate at
sigma0 = (sum_{k>=1} 10^{-k!}, sum_{k>=1} 10^{-(k!+k)}), threshold 3/5.

## Definitions

Let ||.|| denote distance to the nearest integer and for x in R^2
||q x|| = max(||q x_1||, ||q x_2||). The simultaneous sup-norm uniform
exponent is hatomega(x) = sup{omega : for all large T there exists 1<=q<=T
with ||q x|| <= T^{-omega}}. Dirichlet gives hatomega >= 1/2 always.
A vector is singular if the Dirichlet constant can be improved by every
c > 0, equivalently (for a strict gap) hatomega > 1/2. Dani correspondence:
u_x = [[I_2, x],[0,1]], g_t = diag(e^{t/2},e^{t/2},e^{-t}); uniform
improvement corresponds to divergence of g_t u_x Z^3 with a matching rate.

## Result

Theorem: For sigma0 defined above, hatomega(sigma0) >= 3/5. Explicitly, for
every T >= T0 = 10^28 there is 1 <= q <= T with ||q sigma0|| <= T^{-3/5}.
Hence sigma0 is singular with a quantified gap above 1/2. Lemma: 1, alpha,
beta are linearly independent over Q, so sigma0 is totally irrational and
singularity is non-degenerate. Corollary: the Dani first minimum satisfies
delta_1(g_t u_{sigma0} Z^3) <= e^{-t/16} for all large t; the orbit diverges.

## Proof / evidence

Put q'_K = 10^{K!+K}. For j <= K all exponents K!+K-j! and K!+K-j!-j are
nonnegative integers, so the j<=K partial sums of q'_K alpha and q'_K beta
are integers; remainders R_K, S_K have leading exponents
-M_1 = K!+K-(K+1)!, -M_2 = K!+K-((K+1)!+K+1), i.e. M_1 = K*K!-K,
M_2 = K*K!+1. Successive tail exponents drop by j*j! >= 4 (alpha) and
j*j!+1 >= 5 (beta), so every tail ratio is <= 1/10 and
10^{-M_i} <= tail <= (10/9)10^{-M_i}. Since M_i >= 2, tails are < 1/2, so
||q'_K alpha|| = R_K, ||q'_K beta|| = S_K and E_K := ||q'_K sigma0|| <=
(10/9)10^{-M_1}. For T >= q'_4 = 10^28 let K = max{k : q'_k <= T} >= 4;
reuse q = q'_K <= T. Since T < q'_{K+1}, T^{-3/5} > (q'_{K+1})^{-3/5}, so it
suffices that (10/9)10^{-M_1} <= (q'_{K+1})^{-3/5}, i.e.
M_1 - log10(10/9) >= (3/5)((K+1)!+K+1). With
g(K) = K*K!-K-(3/5)((K+1)!+K+1), g(K+1)-g(K) = (K!(2K^2-K+2)-8)/5 > 0 for
K >= 2; at K = 4, M_1 = 92, (3/5)(125) = 75, and 5*92-3*125 = 85 >= 1 >
5log10(10/9), so the inequality holds at K = 4 and hence all K >= 4.
Blocks K = 2,3 genuinely fail (margins negative), so T0 is necessary.
Total irrationality: if a alpha + b beta = u/v, then with Q_K = v 10^{K!+K},
v(aR_K+bS_K) = 0 must hold, but |aR_K+bS_K| >= |a|10^{-M_1}-|b|(10/9)10^{-M_2}
> 0 for large K when a != 0 (since M_2-M_1 = K+1 -> infinity), and = |b|S_K
> 0 when a = 0; contradiction. Dani: from |q sigma0-p| <= T^{-3/5} with
q <= T, v = (q sigma0-p,q) gives ||g_t v||_infty = max(e^{t/2}T^{-3/5},
e^{-t}T); balancing at T = e^{15t/16} gives e^{-t/16}.

## Limitations

Certificate covers the admitted 3/5 threshold (method extends to any fixed
omega < 1 with larger T0, not claimed here). T0 = 10^28 is sufficient, not
optimal. No upper bound on hatomega(sigma0) is established; exact value
remains open. The Dani rate e^{-t/16} is the balanced transfer of 3/5, not
an optimal escape rate.

## Reproducibility

Stdlib-only script verify_sigma0.py checks for 2 <= K <= 6: denominator
clearing (min exponents >= 0), tail < 1/2, tail-ratio bounds, margin
inequality (negative at K = 2,3; +16.95 at K = 4, growing thereafter),
exact integer certificate 5*M_1-3*logq = 85 >= 1 at K = 4, and monotonicity
of (2K-3)K!-(8K+3) for 4 <= K <= 8. Output VERIFY_OK. Independently
re-executed by the auditor with identical margins.

## References

- V. Beresnevich, L. Guan, A. Marnat, F. Ramirez, S. Velani, Dirichlet is
  not just Bad and Singular, Adv. Math. 401 (2022), arXiv:2008.04043.
- J. Schleischitz, Exact uniform approximation and Dirichlet spectrum in
  dimension at least two, Selecta Math. 29:86 (2023), arXiv:2202.04951.
- Y. Cheung, N. Chevallier, Hausdorff dimension of singular vectors,
  Duke Math. J. 165 (2016).
- T. Das, L. Fishman, D. Simmons, M. Urbanski, A variational principle in
  the parametric geometry of numbers.
- O. German, On Diophantine exponents and Khintchine's transference
  principle, Moscow J. Comb. Number Theory 2 (2012).
