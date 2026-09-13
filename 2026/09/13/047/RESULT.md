# Two-sided 2D star-discrepancy rate for the quartic monomial curve

## Context

For a prime p, consider the N = p-1 point set in the unit square obtained by
sampling the monomial curve y = x^4 over the finite field F_p:

  P_p = { (h/p, {h^4/p}) : 1 <= h < p },

where {y} is the fractional part. Such polynomial-curve point sets are
standard test objects in uniform distribution theory: the Weil bound for
polynomial exponential sums predicts near-optimal equidistribution, while
exact lower bounds require identifying a large Fourier coefficient. The
residue class p = 5 mod 12 (hence p = 1 mod 4) is the natural class where
quartic multiplicative characters exist and the quadratic Gauss sum is
positive real.

## Definitions

Write e(t) = exp(2 pi i t), e_p(t) = e(t/p), N = p-1. For a point set Q of
cardinality N in [0,1]^2, the star-discrepancy is

  D*_N(Q) = sup_{0<=a,b<=1} | (1/N) #{q in Q : q_1 <= a, q_2 <= b} - a b |.

Denote G_p = D*_N(P_p). For (m_1,m_2) in Z^2 define

  S(m_1,m_2) = sum_{h=1}^{p-1} e((m_1 h + m_2 h^4)/p),

which equals the Fourier sum of P_p since m_2*{h^4/p} and m_2 h^4/p differ
by the integer m_2*floor(h^4/p). Let T_1 = sum_{x in F_p} e_p(x^4) and
T = sum_{h=1}^{p-1} e(h^4/p) = T_1 - 1.

## Result

Let p run over primes congruent to 5 mod 12. Then there exist absolute
constants C, c > 0 and P_0 such that for every such prime p >= P_0,

  G_p <= C p^{-1/2} (log p)^2,

and there are infinitely many such primes with

  G_p >= c p^{-1/2} / log p.

In fact the lower bound holds in the stronger logarithm-free form
G_p >= c p^{-1/2} for every prime p = 5 mod 24 (e.g. c = 1/(8 pi)),
and there are infinitely many such primes by Dirichlet's theorem, all of
which are 5 mod 12. The target claim is therefore TRUE with both bounds
proved.

## Proof / evidence

Upper bound (Weil + 2D Erdos-Turan-Koksma). For m_2 != 0 mod p the phase
polynomial m_1 x + m_2 x^4 has degree exactly 4 over F_p (p > 4), so the
Weil bound gives |sum_{x in F_p} e_p(m_1 x + m_2 x^4)| <= 3 sqrt(p);
removing x = 0 yields |S(m_1,m_2)| <= 3 sqrt(p)+1 <= 4 sqrt(p). For
m_2 = 0, m_1 != 0, S(m_1,0) = -1. The standard 2D Erdos-Turan-Koksma
inequality gives D*_N << 1/H + sum_{0<||m||_inf<=H} |S(m)|/(N r(m_1)r(m_2))
with r(0)=1, r(m)=|m|. Splitting m_2 = 0 (contribution << (log H)/N) and
m_2 != 0 (contribution << (sqrt(p)/N)(log H)^2) and choosing
H = floor(sqrt(p)) yields G_p << p^{-1/2}(log p)^2. The congruence plays
no role here.

Lower bound (marginal + Koksma + quartic Gauss sums). At a = 1 the 2D box
count equals the 1D count of second coordinates y_h = {h^4/p}, so
G_p >= D*_N(y_1,...,y_N). Koksma's inequality applied to e(k.) gives
D*_N >= |sum_h e(k y_h)|/(2 pi |k| N); with k = 1, G_p >= |T|/(2 pi N).
For p = 5 mod 24 (hence 1 mod 4), order-4 characters exist and
n_a := #{x : x^4 = a} = 1 + chi(a) + phi(a) + chibar(a) for a != 0, so
T_1 = g(chi) + g(phi) + g(chibar) with |g| = sqrt(p). Since p = 1 mod 4,
g(phi) = sqrt(p); since p = 5 mod 8, chi(-1) = -1, so
g(chibar) = -conj(g(chi)) and g(chi)+g(chibar) is purely imaginary. Hence
Re(T_1) = sqrt(p), |T| >= sqrt(p)/2, and G_p >= c p^{-1/2}. Dirichlet
gives infinitely many primes 5 mod 24, all 5 mod 12.

Supporting numerics (not load-bearing): direct evaluation confirms
Re(T_1) = sqrt(p) to < 1e-13 for the 12 primes 5 mod 24 below 600.

## Limitations

Constants C, c are not optimized. The upper bound carries a (log p)^2
factor while the lower bound is logarithm-free, so the exact logarithmic
exponent is not pinned down. The proof invokes standard external theorems
(Weil, Erdos-Turan-Koksma, Koksma, Gauss-sum evaluations, Dirichlet)
without reproving them. No claim is made for other residue classes; the
complementary class p = 1 mod 8 has Re(T_1) = sqrt(p)+2Re(g(chi)) with no
uniform lower bound from this argument.

## Reproducibility

Re-run output/artifacts/verify_gauss.py (Python 3, stdlib only) to check
Re(T_1) = sqrt(p) for p in {5,29,53,101,149,173,197,269,293,317,509,557}.
The analytic proof is self-contained given the cited textbook theorems.

## References

- Schmidt, Equations over Finite Fields, Thm. 2C; Lidl-Niederreiter,
  Finite Fields, Thm. 5.38 (Weil bound).
- Kuipers-Niederreiter, Uniform Distribution of Sequences, Ch. 2;
  Drmota-Tichy, Sequences, Discrepancies and Applications, Ch. 1
  (Erdos-Turan-Koksma, Koksma).
- Ireland-Rosen, A Classical Introduction to Modern Number Theory, Ch. 8;
  Berndt-Evans-Williams, Gauss and Jacobi Sums (Gauss-sum evaluations).
- Dirichlet's theorem on primes in arithmetic progressions.
