# Optimal finite-sample Gumbel calibration of exponential maxima

## Finding

Let \(n\geq 1\) be an integer, let \(X_1,\ldots,X_n\) be independent \(\operatorname{Exp}(1)\) variables, and put \(Z_n=\max_i X_i-\log n\). Among **all** two-parameter Gumbel laws
\[
G_{\mu,\beta}(z)=\exp\{-\exp[-(z-\mu)/\beta]\},\qquad \mu\in\mathbb R,\quad\beta>0,
\]
there is a unique minimizer of the forward Kullback--Leibler divergence \(D(\mathcal L(Z_n)\|G_{\mu,\beta})\).

Define \(H_n=\sum_{j=1}^{n}j^{-1}\) and
\[
A_n(t)=n^{t+1}B(t+1,n)=n^{t+1}\frac{\Gamma(t+1)\Gamma(n)}{\Gamma(n+t+1)},\qquad t>0.
\]
Let \(t_n\in(1,\infty)\) be the unique solution of
\[
H_n=\frac1{t_n}+\sum_{j=1}^{n}\frac1{t_n+j}.
\]
Then the optimal parameters and the exact optimal divergence are
\[
\boxed{\quad\beta_n=\frac1{t_n},\qquad
\mu_n=-\frac{\log A_n(t_n)}{t_n},\qquad
K_n=\frac1n+(t_n-1)(H_n-\log n)-\log t_n+\log A_n(t_n).\quad}
\]
The inverse scales strictly decrease: \(t_1=(1+\sqrt5)/2>t_2>\cdots>1\). Moreover,
\[
\boxed{\quad\lim_{n\to\infty}n(t_n-1)=\frac6{\pi^2},\qquad
\lim_{n\to\infty}n^2 K_n=\frac12-\frac3{\pi^2}>0.\quad}
\]
For comparison, with unit scale but freely optimized location the exact divergence is \(n^{-1}-\log(1+n^{-1})\), while the unadjusted standard Gumbel has divergence \(1/[n(n+1)]\). Thus two-parameter calibration improves the sharp leading forward-KL constant from \(1/2\) to \(1/2-3/\pi^2\), and the limiting Gumbel is not the exactly optimal finite-sample scale.

## Assumptions and scope

The divergence convention is \(D(P\|Q)=\int\log(dP/dQ)\,dP\) in natural units. Only the forward direction is considered: reverse KL from a full-support Gumbel law to the bounded-below law of \(Z_n\) is infinite. Parameters \(\mu\) and \(\beta\) range without restrictions beyond \(\beta>0\); all integer sample sizes \(n\ge1\) are included. For independent \(\operatorname{Exp}(\lambda)\) observations, \(\lambda>0\), the normalized variable \(\lambda\max_iX_i-\log n\) has the same law, so the formula is rate-invariant. On the original lifetime scale the optimal location and scale are \((\log n+\mu_n)/\lambda\) and \(\beta_n/\lambda\).

## Proof

**1. An exact beta representation.** The variables \(U_i=e^{-X_i}\) are independent uniform variables on \((0,1)\). Hence \(W_n=e^{-Z_n}=n\min_i U_i\) has density
\[
f_{W_n}(w)=(1-w/n)^{n-1}\,\mathbf 1_{(0,n)}(w).
\]
It follows by a beta integral that \(\mathbb E e^{-tZ_n}=A_n(t)\) for every \(t>0\). The exponential-order-statistic identity gives \(m_n=\mathbb EZ_n=H_n-\log n\). Directly, the density of \(Z_n\) is \(f_n(z)=e^{-z}(1-e^{-z}/n)^{n-1}\) on \(z>-\log n\), and \(\mathbb E\log(1-W_n/n)=-1/n\), so its differential entropy is \(h_n=1+m_n-1/n\). These identities include \(n=1\).

**2. Exactly reduce the unrestricted Gumbel fit to one variable.** Write \(t=1/\beta>0\). The Gumbel density is
\[
g_{\mu,1/t}(z)=t\exp\{-t(z-\mu)-e^{-t(z-\mu)}\}.
\]
Substituting into KL gives
\[
D(\mathcal L(Z_n)\|G_{\mu,1/t})=-h_n-\log t+t(m_n-\mu)+e^{t\mu}A_n(t).
\]
For every fixed \(t>0\), the derivative with respect to \(\mu\) is \(t[-1+e^{t\mu}A_n(t)]\), with unique zero \(\mu(t)=-t^{-1}\log A_n(t)\). It decreases before the zero and increases after, and diverges at both ends (the linear term controls \(\mu\to-\infty\), the exponential term controls \(\mu\to+\infty\)). Consequently the global two-parameter problem is equivalent to minimizing
\[
F_n(t)=\frac1n+(t-1)m_n-\log t+\log A_n(t),\qquad t>0.
\]
Differentiating the finite gamma product \(A_n(t)=n^{t+1}\Gamma(t+1)\Gamma(n)/\Gamma(n+t+1)\) yields
\[
F_n'(t)=H_n-\frac1t-\sum_{j=1}^{n}\frac1{t+j},\qquad
F_n''(t)=\frac1{t^2}+\sum_{j=1}^{n}\frac1{(t+j)^2}>0.
\]
Thus \(F_n\) is strictly convex. Since \(F_n'(1)=-1/(n+1)<0\) and \(\lim_{t\to\infty}F_n'(t)=H_n>0\), there is exactly one global minimizer \(t_n>1\). This also proves uniqueness of the original location-scale pair, without restricting the search to any compact parameter set.

**3. Dependence on sample size.** At each fixed \(t>0\),
\[
F_{n+1}'(t)-F_n'(t)=\frac1{n+1}-\frac1{t+n+1}>0.
\]
Strict increase of each derivative implies \(t_{n+1}<t_n\). Solving the case \(n=1\) gives \(t_1^2-t_1-1=0\), hence \(t_1=(1+\sqrt5)/2\). In particular \(1<t_n\le t_1\). By the mean value theorem,
\[
\frac1{n+1}=F_n''(\xi_n)(t_n-1),\qquad 1<\xi_n<t_n.
\]
The second derivative is bounded below by \(t_1^{-2}\) on this interval, so \(t_n\to1\). Since \(F_n''(\xi_n)\to\sum_{j=1}^{\infty}j^{-2}=\pi^2/6\), the first stated asymptotic follows.

**4. Sharp optimal entropy loss.** At \(t=1\), the beta integral gives \(A_n(1)=n/(n+1)\), hence
\[
F_n(1)=\frac1n-\log(1+1/n),\qquad \lim_{n\to\infty}n^2F_n(1)=\frac12.
\]
Taylor expansion from \(t=1\) to \(t=t_n\), the exact identity \(F_n'(1)=-1/(n+1)\), the limit \(n(t_n-1)\to6/\pi^2\), and the uniform convergence of \(F_n''\) along that interval yield
\[
\lim_{n\to\infty}n^2\bigl[F_n(t_n)-F_n(1)\bigr]=-\frac3{\pi^2}.
\]
Adding the limits proves the sharp KL constant. Finally, the unshifted Gumbel comparison has density \(e^{-z-e^{-z}}\), so the log likelihood ratio is \((n-1)\log(1-W_n/n)+W_n\); using the beta moments yields exactly \(1/[n(n+1)]\).

## Verification

The standalone script `verify_gumbel.py` uses only Python's standard library. It independently evaluates the derivative roots for \(n=1,\ldots,100\), confirms decreasing inverse scales and strict improvement, checks 500 pairs of beta moments, integrates the original log-density ratio numerically for four sample sizes, and tests the asymptotic constants at three larger sample sizes. The successful output is `VERIFY_OK roots=100 moment_pairs=500 quadratures=4 asymptotic_points=3`. These numerical checks are corroboration, not proof for all \(n\); the analytic argument above establishes the unrestricted result.

## Relationship to prior work

Oliver Johnson, *Information-theoretic convergence of extreme values to the Gumbel distribution* (arXiv:2007.03569, first posted 2020-07-07), proves relative-entropy convergence to a fixed limiting Gumbel and gives the entropy of the normalized exponential maximum explicitly in Remark 4.6. Proposition 2.4 gives a general relative-entropy identity, which supplies one of the starting ingredients here. Those published statements do not optimize simultaneously over both Gumbel parameters, establish the uniquely calibrated finite-sample scale, or evaluate the optimized sharp \(n^{-2}\) constant. The present result is an exact finite-sample optimization of that naturally motivated model, not a claim that the base convergence or entropy identity is new.

Zarfaty, Barkai, and Kessler, *Accurately approximating extreme value statistics* (arXiv:2006.13677, 2020), develop Gumbel location/width norming sequences, functional corrections, and fitting procedures. Their Section II calibrates by distribution-function matching, not by forward-KL minimization; the precise finite-sample KL-optimal scale and sharp information-loss constant proved here are not among the inspected results.

Cardone, Dytso, and Rush, *Entropic CLT for Order Statistics* (arXiv:2205.04621, 2022), treat Gaussian approximation for central ranks with rank proportion fixed in \((0,1)\). Their regime does not include the maximum-rank Gumbel calibration problem. Standard beta identities and exponential-spacing formulas are used as known tools.

## Limitations

Only exponential parent laws, ordinary iid maxima, forward KL, and approximating Gumbel distributions with freely chosen location and scale are covered. No claim is made for other parents, a general optimal convergence rate over an extreme-value domain of attraction, reverse KL, total variation, or finite-sample estimators fitted to observed data. The uniqueness and asymptotic constant are mathematical statements about population laws. Earlier treatises on order statistics and extreme-value fitting may contain comparable implicit optimizations; independent bibliographic assessment has not been performed.

## References

1. O. Johnson, *Information-theoretic convergence of extreme values to the Gumbel distribution*, arXiv:2007.03569 (initial public version 2020-07-07; Journal of Applied Probability 61 (2024), 244--254). https://arxiv.org/abs/2007.03569
2. L. Zarfaty, E. Barkai, and D. A. Kessler, *Accurately approximating extreme value statistics*, arXiv:2006.13677 (initial public version 2020-06-24). https://arxiv.org/abs/2006.13677
3. M. Cardone, A. Dytso, and C. Rush, *Entropic CLT for Order Statistics*, arXiv:2205.04621 (initial public version 2022-05-10); subsequently *Entropic Central Limit Theorem for Order Statistics*, IEEE Transactions on Information Theory 69 (2023), 2193--2205. https://arxiv.org/abs/2205.04621
4. R.-D. Reiss, *Approximate Distributions of Order Statistics: With Applications to Nonparametric Statistics*, Springer, 1989; reprint 2012 (general order-statistic approximation background, not relied on for any theorem here).
