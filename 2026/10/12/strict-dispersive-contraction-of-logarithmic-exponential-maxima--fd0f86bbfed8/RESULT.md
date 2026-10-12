# Strict dispersive contraction of logarithmic exponential maxima

## Finding
Let \(E_1,E_2,\ldots\) be independent exponential random variables of mean one, and set \(Y_n=\log\max_{1\le i\le n}E_i\). For every integer \(n\ge1\) and every \(0<u<v<1\), the corresponding quantiles satisfy the strict dispersive inequality
\[
Q_{n+1}(v)-Q_{n+1}(u)<Q_n(v)-Q_n(u).
\]
Consequently, \(\operatorname{Var}(Y_{n+1})<\operatorname{Var}(Y_n)\) for every \(n\ge1\).

Indeed, the stronger result holds for the continuous one-parameter family \(Y_a\) with cumulative distribution function \(G_a(y)=(1-e^{-e^y})^a\), for every real \(a>0\): whenever \(b>a>0\), \(Y_b\) is strictly smaller in dispersive order than \(Y_a\).

Writing the alternating binomial sums of Doumas [1] as
\[
c_n=-\frac1n\sum_{j=1}^n(-1)^j\binom nj\log j,
\qquad w_n=-\frac1n\sum_{j=1}^n(-1)^j\binom nj(\log j)^2,
\]
the sharp consequence is
\[
0<\frac{\pi^2}{6}+(n+1)w_{n+1}-(n+1)^2c_{n+1}^2
<\frac{\pi^2}{6}+nw_n-n^2c_n^2,
\qquad n\ge1.
\]
This resolves the strict-monotonicity question explicitly stated in [1, closing paragraph].

## Assumptions and scope
All logarithms are natural. The exponential observations are independent and identically distributed, with rate one; changing their common positive rate translates the logarithmic maximum and does not alter the dispersive order or variance. Quantiles use the left-continuous inverse convention, equivalent here to the unique continuous inverse. Strict dispersive contraction means the displayed inequality for **every** \(0<u<v<1\), rather than only comparison of variances.

## Proof
For any real \(a>0\), define \(G_a(y)=(1-e^{-e^y})^a\) for real \(y\). This is a genuine continuous distribution function. Its quantile is
\[
Q_a(u)=\log\bigl[-\log(1-u^{1/a})\bigr],\qquad 0<u<1.
\]
For integer \(a=n\), the distribution agrees exactly with that of \(Y_n\).

Fix \(u\in(0,1)\), and write \(t=u^{1/a}\in(0,1)\). Differentiating with respect to the quantile level \(u\) yields
\[
Q_a'(u)=\frac{t}{a u(1-t)[-\log(1-t)]}
=\frac{1}{u[-\log u]}\,\Phi(t),
\quad
\Phi(t)=\frac{t[-\log t]}{(1-t)[-\log(1-t)]}.
\]
The crucial inequality is that \(\Phi\) is strictly **decreasing** on \((0,1)\). Logarithmic differentiation gives
\[
\frac{\Phi'(t)}{\Phi(t)}
=\frac{1}{t(1-t)}-\frac{1}{t[-\log t]}-
\frac{1}{(1-t)[-\log(1-t)]}.
\]
After multiplication by the positive number \(t(1-t)\), the right-hand side becomes
\[
1-\frac{1-t}{-\log t}-\frac{t}{-\log(1-t)}<0.
\]
Indeed, the two elementary strict logarithm inequalities
\[
-\log t<\frac{1-t}{t},\qquad
-\log(1-t)<\frac{t}{1-t}
\]
show separately that the two subtracted fractions exceed \(t\) and \(1-t\), respectively. This proves strict negativity for every interior \(t\).

For fixed \(u\in(0,1)\), the value \(u^{1/a}\) is strictly increasing in \(a>0\). Thus \(Q_a'(u)\) is strictly decreasing as \(a\) increases. If \(b>a>0\) and \(0<u<v<1\), the fundamental theorem of calculus gives
\[
Q_b(v)-Q_b(u)=\int_u^v Q_b'(s)\,ds
<\int_u^v Q_a'(s)\,ds=Q_a(v)-Q_a(u),
\]
establishing the continuous-parameter strict dispersive order.

All of the \(Y_a\) have finite second moments. To see this directly, as \(y\to-\infty\), \(G_a(y)\sim e^{a y}\), and as \(y\to+\infty\), \(1-G_a(y)\sim a e^{-e^y}\); their two tails are integrable against quadratic moments. Let \(U,V\) be independent uniform random variables on \((0,1)\). The variance identity
\[
\operatorname{Var}(Y_a)=\frac12\,\mathbb E[(Q_a(U)-Q_a(V))^2]
\]
holds because \(Q_a(U)\) has distribution \(G_a\). Whenever \(U\ne V\), the absolute quantile difference for \(b>a\) is strictly smaller than for \(a\). Since \(\Pr(U\ne V)=1\), the integrand is strictly smaller almost surely, proving \(\operatorname{Var}(Y_b)<\operatorname{Var}(Y_a)\).

Finally, [1, Eq. (15)] identifies \(\operatorname{Var}(Y_n)\) exactly with \(\pi^2/6+n w_n-n^2c_n^2\). Substitution proves the displayed strict inequalities. Positivity holds because every \(Y_n\) is nondegenerate.

## Verification
The proof requires no limit exchange or finite enumeration: the sole nonstandard inequality is the displayed negative logarithmic derivative of \(\Phi\), proved globally by two strict logarithm inequalities. The independently executable companion `CHECK.py` evaluates that sign and the quantile-derivative ordering over deterministic interior grids, and approximates several variances. Those numerical tests illustrate, but do not establish, the quantified theorem. The integral proof establishes strictness even arbitrarily close to \(u=0\) or \(u=1\), where finite grids cannot certify anything.

## Relationship to prior work
Doumas [1] identified the exact alternating binomial coefficient with \(\operatorname{Var}(\log\max E_i)\), proved its positivity and vanishing limit, and expressly left monotonicity open. The new statement settles that question and proves the strictly stronger all-quantile-gap contraction. Jeon, Kochar and Park [2] provide the general dispersive-order framework and its variance implication, but not this exponential-logarithm family or the claimed monotonicity. Shekari and coauthors [3] study dispersive comparisons of maxima between heterogeneous and homogeneous **fixed-size** dependent gamma–Gompertz samples, rather than comparisons across sample sizes of log-exponential maxima. Lando and Bertoli-Barsotti [4] study second-order stochastic dominance for general order statistics, a different order that does not by itself yield the centered quantile-gap contraction proved here.

## Limitations
The argument is specific to the logarithm of exponential maxima and the real-shape family \(G_a\); it does not imply decreasing variance of untransformed exponential maxima, and does not claim such a result. No rate for the variance decrease, generalized parent-law theorem, or independent audit is provided. Priority could be affected by an unindexed equivalent dispersive-order theorem; the comparisons cited below are the materially inspected sources.

## References
[1] A. V. Doumas, *An inequality involving alternating binomial sums*, arXiv:2603.11129v1 (submitted 11 March 2026), especially equations (2), (3), (15) and the final open question. https://arxiv.org/html/2603.11129v1

[2] J. Jeon, S. Kochar and C. G. Park, *Dispersive ordering—Some applications and examples*, Statistical Papers **47** (2006), 227–247. https://doi.org/10.1007/s00362-005-0285-4

[3] M. Shekari, G. S. K. Barmalzan, Z. Pakdaman and N. Balakrishnan, *Dispersion and variation orders of extreme order statistics from dependent unit gamma Gompertz random variables*, Journal of Inequalities and Applications (2025). https://doi.org/10.1186/s13660-025-03290-x

[4] T. Lando and L. Bertoli-Barsotti, *Second-order stochastic comparisons of order statistics*, arXiv:2006.02302 (2020). https://arxiv.org/html/2006.02302v1
