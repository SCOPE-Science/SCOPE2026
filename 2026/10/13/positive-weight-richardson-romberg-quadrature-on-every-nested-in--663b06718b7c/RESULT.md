# Positive-weight Richardson–Romberg quadrature on every nested integer refinement chain
## Finding
Let \(a<b\). Fix any finite strict divisibility chain
\[
N_0\mid N_1\mid\cdots\mid N_d,
\]
so every refinement ratio \(N_{k+1}/N_k\) is an integer at least \(2\). Put \(h_k=(b-a)/N_k\), and let \(T_k\) be the uniform composite trapezoidal rule with \(N_k\) panels. Define the depth-\(d\) Richardson extrapolate
\[
Q_d=\sum_{{k=0}}^d c_kT_k
\]
by the moment conditions
\[
\sum_{{k=0}}^d c_k=1,
\qquad
\sum_{{k=0}}^d c_k h_k^{{2j}}=0\quad(1\le j\le d).
\]
Then, after collecting \(Q_d\) on the finest grid, **every sample weight is strictly positive**. The largest weight is attained precisely at nodes first introduced on level \(d\), and it is
\[
\max_i w_i
=h_d\prod_{{j=0}}^{{d-1}}
\left(1-\left(\frac{{N_j}}{{N_d}}\right)^2\right)^{{-1}}.
\]
Since constants are integrated exactly, positivity also gives
\[
\sum_i |w_i|=b-a.
\]
Thus the induced operator norm from bounded absolute sample perturbations to integration error is exactly \(b-a\), which is the minimum possible for any quadrature rule exact for constants.

The conclusion genuinely uses nesting. For the nonnested panel counts \((1,2,5)\) on \([0,1]\), the Richardson coefficients are \(1/72,-16/63,625/504\); the point \(1/2\) occurs only on the two-panel grid, so its collected weight is \(-8/63\).

## Assumptions and scope
The theorem is exact-arithmetic and finite-depth. Each \(T_k\) is the ordinary closed composite trapezoidal rule on one interval, and the grid chain is strictly nested through integer divisibility. No claim is made for nonnested panel counts, rational extrapolation, floating-point evaluation of the extrapolation tableau, relative sample errors, or stochastic error models.

The coefficients are the unique Lagrange/Richardson coefficients associated with the distinct positive nodes \(h_k^2\). The theorem concerns the final collected quadrature weights, not cancellation in an implementation that first evaluates the \(T_k\) and then combines them.

## Proof
Set \(x_k=h_k^2\), so
\[
x_0>x_1>\cdots>x_d>0,
\qquad
x_{{k+1}}\le \frac{x_k}{4}.
\]
Lagrange interpolation at zero gives
\[
c_k=
\prod_{{j\ne k}}\frac{{-x_j}}{{x_k-x_j}},
\qquad
\operatorname{{sgn}}(c_k)=(-1)^{{d-k}}.
\]
Define
\[
b_k=|c_k|h_k.
\]
We first prove that \(b_0<b_1<\cdots<b_d\). Direct cancellation in the adjacent ratio yields
\[
\frac{{b_{{k+1}}}}{{b_k}}
=
\sqrt{{\frac{{x_k}}{{x_{{k+1}}}}}}
\prod_{{j\ne k,k+1}}
\frac{{|x_k-x_j|}}{{|x_{{k+1}}-x_j|}}.
\]
Every factor with \(j>k+1\) is greater than \(1\). For \(j<k\), writing \(m=k-j\), \(X=x_j/x_k\), and \(y=x_{{k+1}}/x_k\), nesting gives \(X\ge4^m\) and \(0<y\le1/4\), hence
\[
\frac{{x_j-x_k}}{{x_j-x_{{k+1}}}}
=
\frac{{X-1}}{{X-y}}
>
1-\frac1X
\ge 1-4^{{-m}}.
\]
Also \(\sqrt{{x_k/x_{{k+1}}}}=N_{{k+1}}/N_k\ge2\). Therefore
\[
\frac{{b_{{k+1}}}}{{b_k}}
>
2\prod_{{m=1}}^k(1-4^{{-m}}).
\]
Using \(\prod_m(1-a_m)\ge1-\sum_m a_m\) for \(0\le a_m\le1\) and
\[
\sum_{{m=1}}^\infty4^{{-m}}=\frac13,
\]
we obtain \(b_{{k+1}}/b_k>4/3\) for \(k\ge1\); for \(k=0\), the ratio is at least \(2\). Thus the magnitudes grow strictly with level.

Now take a finest-grid node that first appears on level \(\ell\). Because the grids are nested, it appears on every level \(k\ge\ell\) and on no earlier level. Its interior collected weight is therefore
\[
W_\ell=\sum_{{k=\ell}}^d c_kh_k
=b_d-b_{{d-1}}+b_{{d-2}}-\cdots.
\]
Pairing terms from the right shows \(W_\ell>0\), since each finer-level magnitude strictly dominates the adjacent coarser one. The two endpoints have weight \(W_0/2>0\). This proves strict positivity.

For \(\ell<d\), the remainder after the leading \(b_d\) is a sum of strictly negative adjacent pairs, so \(0<W_\ell<b_d\). A node first introduced at level \(d\) has weight exactly \(b_d=h_dc_d\). Since
\[
c_d
=
\prod_{{j=0}}^{{d-1}}\frac{{x_j}}{{x_j-x_d}}
=
\prod_{{j=0}}^{{d-1}}
\left(1-\frac{{x_d}}{{x_j}}\right)^{{-1}},
\]
we get
\[
b_d
=h_d\prod_{{j=0}}^{{d-1}}
\left(1-\left(\frac{{N_j}}{{N_d}}\right)^2\right)^{{-1}},
\]
which is the asserted exact maximum.

Finally, exactness for constants gives \(\sum_iw_i=b-a\). Since every \(w_i>0\), \(\sum_i|w_i|=b-a\). Conversely any rule exact for constants satisfies \(\sum_i|w_i|\ge|\sum_iw_i|=b-a\), so this sample-error norm is optimal.

## Verification
For the genuinely mixed refinement chain \((N_0,N_1,N_2)=(1,2,6)\), the coefficients are
\[
\left(\frac1{{105}},-\frac16,\frac{{81}}{{70}}\right),
\]
and the seven finest-grid weights are
\[
\left(\frac5{{84}},\frac{{27}}{{140}},\frac{{27}}{{140}},\frac{{23}}{{210}},\frac{{27}}{{140}},\frac{{27}}{{140}},\frac5{{84}}\right).
\]
The maximum \(27/140\) agrees with the product formula.

The supplied exact-rational checker tests 124 variable nested chains, verifies strict positivity, constant exactness, the exact maximum formula, polynomial exactness through the Richardson degree, alternating coefficient signs, and strict growth of \(|c_k|h_k\). It separately verifies the nonnested \((1,2,5)\) midpoint weight \(-8/63\). These finite checks corroborate the algebra; they are not used as the proof of the all-chain theorem.

## Relationship to prior work
Pagès develops multi-step Richardson–Romberg extrapolation through a Vandermonde formulation and supplies an archive-era reference point for multi-level extrapolation. That work concerns weak discretization error and variance for stochastic Euler schemes, not collected trapezoidal sample-weight positivity.

Farzi treats generalized extrapolation with arbitrary division sequences and explicitly discusses positivity of quadrature weights. The inspected full text states positivity for classical Romberg divisors, selected Bauer subsequences, and failure of the stated positivity property for Bulirsch subsequences; it does not give a positivity theorem for every nested divisibility chain. This is the closest older primary comparison because it puts arbitrary division sequences and positivity in the same framework.

A published published-finding corpus record proves positivity for the special geometric family \(N_k=s r^k\) with one fixed integer refinement factor \(r\ge2\), including the corresponding largest-weight product and sample-noise norm. Its full result explicitly limits the theorem to a single fixed refinement factor and says it is not a theorem for arbitrary division sequences. The present claim strictly enlarges that family to every finite chain \(N_0\mid N_1\mid\cdots\mid N_d\), allowing the integer refinement factor to change at every level. The proof also identifies nesting itself as the structural mechanism through the adjacent-magnitude bound.

## Limitations
The theorem does not characterize all positive extrapolation division sequences: some nonnested families can also have positive weights. It gives a broad sufficient class, not a necessary-and-sufficient classification. The nonnested \((1,2,5)\) example only shows that positivity can fail without nesting.

Historical extrapolation literature is extensive. The full-text and semantic searches found no statement implication-equivalent to the arbitrary nested-divisibility theorem, but an older equivalent criterion under different terminology remains a residual originality risk.

## References
1. G. Pagès, *Multi-step Richardson-Romberg Extrapolation: Remarks on Variance Control and Complexity*, arXiv:math/0612523, first public version 2006-12-18. https://arxiv.org/abs/math/0612523
2. J. Farzi, *Generalized extrapolation methods for solving nonlinear Fredholm integral equations*, Mathematical Communications 19(2) (2014), 375–390. https://www.mathos.hr/mc/index.php/mc/article/view/619
3. *Positive-weight generalized Romberg quadrature for every integer refinement factor*, published-finding corpus record 2026/9/21/SCOPE-generalized-romberg-positive-weights-integer-refinement--b7c2819b6648. https://github.com/published-finding corpus/2026/tree/main/2026/9/21/SCOPE-generalized-romberg-positive-weights-integer-refinement--b7c2819b6648
