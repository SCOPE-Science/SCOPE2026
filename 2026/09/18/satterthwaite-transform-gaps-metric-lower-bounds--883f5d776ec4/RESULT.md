# Laplace-transform gaps and metric lower certificates for Satterthwaite Gamma approximation

## Statement

Let \(G_1,\ldots,G_N\) be independent Gamma random variables in shape-scale parametrization,
\[
G_i\sim \mathcal G_{\alpha_i,\beta_i},
\qquad \alpha_i>0,\quad \beta_i>0,
\]
and put
\[
S=\sum_iG_i,\qquad
A=\sum_i\alpha_i\beta_i,\qquad
B=\sum_i\alpha_i\beta_i^2.
\]
Let \(U\) be the Gamma law matching the first two moments of \(S\):
\[
U\sim\mathcal G_{A^2/B,\,B/A}.
\]
Define
\[
w_i=\frac{\alpha_i\beta_i}{A},\qquad
\beta=\frac BA=\sum_iw_i\beta_i,\qquad
V_\beta=\sum_iw_i(\beta_i-\beta)^2,
\qquad M=\max_i\beta_i.
\]

Then for every \(s>0\),
\[
L_S(s)\le L_U(s),
\]
with strict inequality whenever the scales are not all equal, and
\[
\log\frac{L_U(s)}{L_S(s)}
\ge
\frac{A V_\beta s^3}{3(1+sM)^3}.
\]

Let
\[
d_1(X,Y)=\sup_{\|h'\|_\infty\le1}|\mathbb Eh(X)-\mathbb Eh(Y)|
\]
and
\[
d_2(X,Y)=\sup_{\|h''\|_\infty\le1}|\mathbb Eh(X)-\mathbb Eh(Y)|.
\]
Because \(S\) and \(U\) have the same first two moments, these differences are well defined in the present setting. Writing
\[
\Delta(s)=L_U(s)-L_S(s),
\]
one has
\[
d_1(S,U)\ge \sup_{s>0}\frac{\Delta(s)}s,
\qquad
d_2(S,U)\ge \sup_{s>0}\frac{\Delta(s)}{s^2}.
\]
Consequently,
\[
d_1(S,U)\ge
\sup_{s>0}\frac{(1+s\beta)^{-A/\beta}}s
\left[
1-\exp\left\{-\frac{A V_\beta s^3}{3(1+sM)^3}\right\}
\right],
\]
and
\[
d_2(S,U)\ge
\sup_{s>0}\frac{(1+s\beta)^{-A/\beta}}{s^2}
\left[
1-\exp\left\{-\frac{A V_\beta s^3}{3(1+sM)^3}\right\}
\right].
\]

Equality \(L_S(s)=L_U(s)\) at one positive \(s\) occurs if and only if all scales \(\beta_i\) are equal, in which case \(S\) is exactly Gamma with the matched parameters.

## Proof

Set
\[
g_s(x)=\frac{\log(1+sx)}x=\int_0^s\frac{du}{1+ux}.
\]
Then
\[
g_s''(x)=\int_0^s\frac{2u^2}{(1+ux)^3}\,du>0.
\]
Moreover, for \(0<x\le M\),
\[
g_s''(x)\ge \frac{2s^3}{3(1+sM)^3}.
\]
The Laplace transforms satisfy
\[
\log L_S(s)=-A\sum_iw_i g_s(\beta_i),
\qquad
\log L_U(s)=-A g_s(\beta).
\]
Jensen's inequality gives \(L_S(s)\le L_U(s)\), with strictness unless all scales agree. The displayed lower bound for \(g_s''\) and the standard strong-convexity Jensen gap give the quantitative logarithmic estimate.

For the metric bounds, the function
\[
q_s(x)=\frac{1-e^{-sx}}s
\]
satisfies \(\|q_s'\|_\infty\le1\), hence
\[
d_1(S,U)\ge\frac{L_U(s)-L_S(s)}s.
\]
Likewise
\[
r_s(x)=\frac{e^{-sx}}{s^2}
\]
satisfies \(\|r_s''\|_\infty\le1\), so
\[
d_2(S,U)\ge\frac{L_U(s)-L_S(s)}{s^2}.
\]
Taking suprema and substituting the logarithmic gap proves the formulas.

## Prior coverage and scope

Mountain and Sherlock proved in 2021 that, for a sum of independent Gamma variables, the first-two-moment matched Gamma distribution has no larger cumulants of any integer order at least three, and consequently no larger integer moments. That prior theorem covers the all-order cumulant hierarchy stated in the earlier version of this record and also yields the positive-parameter MGF comparison within the common convergence interval. Those facts are therefore not claimed here.

The surviving result is the negative-axis Laplace-transform ordering, its explicit scale-variance gap, and the resulting lower certificates in the \(d_1\) and \(d_2\) metrics. These complement recent Gamma-Stein upper bounds for Satterthwaite approximation.

## Limitations

The summands are independent Gamma variables with positive shapes and scales. The transform order is not promoted to ordinary stochastic order. The metric lower certificates are not claimed optimal, and no Kolmogorov lower bound is obtained. A highly relevant 2014 paper by Covo and Elalouf could not be inspected in full during the literature comparison, so an unnoticed related transform inequality remains a residual originality risk.

## References

1. R. Mountain and C. Sherlock, *Recruitment prediction for multicenter clinical trials based on a hierarchical Poisson–gamma model: Asymptotic analysis and improved intervals*, Biometrics 78 (2022), 636–651. DOI: 10.1111/biom.13447.
2. G. Bailly, F. Rapin, Y. Swan, R. von Sachs, *Explicit Gamma-Stein Bounds for Satterthwaite's Approximation*, arXiv:2609.17880 (2026).
3. S. Covo and A. Elalouf, *A novel single-gamma approximation to the sum of independent gamma variables, and a generalization to infinitely divisible distributions*, Electronic Journal of Statistics 8 (2014), 894–926. DOI: 10.1214/14-EJS914.
