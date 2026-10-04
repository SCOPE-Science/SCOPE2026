# Second-order conservative decay after Hall-class Hill bias correction

## Finding

Assume that the tail quantile is eventually
\[
U(t)=t^{1/\alpha}\left(1+c t^{-\beta}\right),
\qquad \alpha,\beta>0,\quad c\ne0,
\]
and is positive and nondecreasing on that tail. Its second-order parameter is \(\rho=-\beta\), with auxiliary function
\[
A(t)=-\beta c t^{-\beta}.
\]
Let \(H_{k,n}\) be the Hill statistic based on the largest \(k=k_n\) observations and use the first-order oracle correction
\[
\widetilde H_{k,n}=H_{k,n}-\frac{A(n/k)}{1+\beta}.
\]
For any \(\theta_n\ge0\), put
\[
\delta_n=\theta_n+\frac{\alpha A(n/k)^2}{\beta(1+2\beta)}.
\]
If \(k\to\infty\), \(k/n\to0\), \(\delta_n\to0\), and \(k\delta_n^2\to\infty\), then
\[
-\log\Pr\!\left\{\frac{1-\theta_n}{\widetilde H_{k,n}}>\alpha\right\}
\sim\frac{k\delta_n^2}{2}.
\]
The reciprocal is interpreted as \(+\infty\) when its denominator is nonpositive.

In particular, when \(\theta_n=0\) and \(kA(n/k)^4\to\infty\),
\[
-\log\Pr\!\left\{\frac1{\widetilde H_{k,n}}>\alpha\right\}
\sim
\frac{k\alpha^2A(n/k)^4}{2\beta^2(1+2\beta)^2}.
\]
The residual is conservative in the same direction for both signs of \(c\).

For a target exponent \(\lambda_n\to\infty\) with \(\lambda_n=o(n)\), the zero-rescaling relation gives
\[
k\sim
\left(\frac{2(1+2\beta)^2}{\alpha^2\beta^2c^4}\lambda_n\right)^{1/(4\beta+1)}
n^{4\beta/(4\beta+1)}.
\]

## Assumptions and scope

The result concerns an exact eventual Hall quantile, not the full second-order regular-variation class. Below the point from which the displayed Hall formula is positive and nondecreasing, \(U\) may be completed arbitrarily as a valid tail quantile; because \(k/n\to0\), this completion does not affect the asymptotics.

The correction uses the true \(A(n/k)\) and \(\beta\), so this is an oracle benchmark. It does not assert that estimated second-order parameters preserve the same exponent. The reciprocal convention is the one used in the motivating work.

## Proof

Write \(X_i=U(e^{E_i})\) with independent \(E_i\sim\operatorname{Exp}(1)\), and let \(E_{k,n}\) be the \(k\)-th largest exponential order statistic. The unordered excesses above \(E_{k,n}\) are \(k-1\) independent standard exponentials \(Y_1,\ldots,Y_{k-1}\), independent of \(E_{k,n}\).

For \(u\) in the Hall tail set \(z=c e^{-\beta u}\). For an excess \(Y\),
\[
\alpha\log\frac{U(e^{u+Y})}{U(e^u)}
=
Y+\alpha\ell_z(Y),
\qquad
\ell_z(Y)=\log(1+z e^{-\beta Y})-\log(1+z).
\]
If \(Y\sim\operatorname{Exp}(1)\), then \(e^{-Y}\) is uniform on \((0,1)\). Therefore, for \(|z|<1\),
\[
m(z):=\mathbb E[\ell_z(Y)]
=
\sum_{j\ge1}\frac{(-1)^j\beta z^j}{1+j\beta}
=
-\frac{\beta z}{1+\beta}
+\frac{\beta z^2}{1+2\beta}
+O(z^3).
\]

Let
\[
z_n=c(k/n)^\beta,\qquad
A_n=-\beta z_n,\qquad
b_n=\frac{\alpha\beta z_n^2}{1+2\beta}
=\frac{\alpha A_n^2}{\beta(1+2\beta)}.
\]
The first-order correction cancels the linear term because
\[
-\frac{\alpha A_n}{1+\beta}
=
\frac{\alpha\beta z_n}{1+\beta}.
\]

It remains to control the random threshold. Put \(q_n=|z_n|\). Since \(\delta_n=\theta_n+b_n\ge b_n\), one has \(q_n^2=O(\delta_n)\). Choose
\[
r_n=\min\left\{\sqrt{\delta_n},\frac{\delta_n}{\sqrt{q_n}}\right\}.
\]
Then \(r_n\to0\), \(\delta_n=o(r_n)\), and \(q_nr_n=o(\delta_n)\). Standard concentration for \(E_{k,n}\) gives
\[
\Pr\!\left(\left|E_{k,n}-\log(n/k)\right|>r_n\right)
\le2\exp\!\left(-\frac{kr_n^2}{32}\right),
\]
which is exponentially negligible relative to speed \(k\delta_n^2\).

On the complementary threshold event,
\[
z=z_ne^{-\beta(E_{k,n}-\log(n/k))}
=z_n(1+O(r_n)).
\]
Thus, uniformly there,
\[
\alpha m(z)-\frac{\alpha A_n}{1+\beta}
=
b_n+o(\delta_n).
\]
For sufficiently small \(|z|\), every centered correction \(\ell_z(Y)-m(z)\) is bounded in absolute value by a constant times \(q_n\). Hoeffding's inequality therefore makes deviations of its empirical mean by \(\varepsilon\delta_n\) exponentially negligible at speed \(k\delta_n^2\).

Consequently,
\[
\alpha\widetilde H_{k,n}-1
=
\frac{\Gamma_{k-1}}k-1+b_n+R_n,
\]
where \(\Gamma_{k-1}\) is gamma with shape \(k-1\), rate \(1\), and for every fixed \(\varepsilon>0\),
\[
\frac1{k\delta_n^2}
\log\Pr\!\left(|R_n|>\varepsilon\delta_n\right)
\longrightarrow-\infty.
\]
The missing \(1/k\) in the mean of \(\Gamma_{k-1}/k\) is \(o(\delta_n)\), because \(k\delta_n^2\to\infty\).

Finally,
\[
\left\{\frac{1-\theta_n}{\widetilde H_{k,n}}>\alpha\right\}
=
\left\{\alpha\widetilde H_{k,n}<1-\theta_n\right\}.
\]
The preceding exponential equivalence turns this into
\[
\frac{\Gamma_{k-1}}k-1<-\delta_n+o(\delta_n).
\]
The gamma moderate-deviation law for \(\delta_n\to0\) and \(k\delta_n^2\to\infty\) gives the exponent \(k\delta_n^2/2\). Setting \(\theta_n=0\) gives the fourth-order Hall-amplitude exponent. Substituting \(A(n/k)=-\beta c(k/n)^\beta\) and solving for \(k\) gives the displayed target-exponent scale.

## Verification

The only special coefficient is checked from
\[
m(z)=\sum_{j\ge1}\frac{(-1)^j\beta z^j}{1+j\beta}.
\]
After the linear correction,
\[
\frac{m(z)+\beta z/(1+\beta)}{z^2}\longrightarrow\frac{\beta}{1+2\beta},
\]
for either sign of \(z\). The included deterministic `verify.py` evaluates this convergent series and checks the threshold-scale algebra. It is a reproducibility check for the expansion, not a substitute for the probabilistic proof.

## Relationship to prior work

Gösgens, van Parys, and Zwart prove moderate-deviation asymptotics for the first-order bias-corrected Hill statistic under a second-order condition. Their Theorem 3 and Corollary 7 require \(|A(n/k)|=O(\theta_n)\) for the bias-corrected one-sided decay
\[
-\log\Pr\!\left\{\frac{1-\theta_n}{\widetilde H_{k,n}}>\alpha\right\}
\sim\frac{k\theta_n^2}{2}.
\]
They also leave the separate choice of \(k\) for a desired decay rate as future work. The present Hall-model result reaches the next regime, where the first-order correction has canceled an \(A(n/k)\) bias and \(\theta_n\) may be as small as \(A(n/k)^2\), including \(\theta_n=0\).

Earlier reduced-bias Hill literature removes the dominant second-order bias and studies asymptotic normality, mean-squared error, or practical threshold selection. Those results provide the bias-reduction context but do not imply the one-sided moderate-deviation exponent above. The contribution claimed here is the explicit Hall residual coefficient together with its induced conservative exponent and target-decay threshold scale.

## Limitations

The coefficient is specific to the exact eventual Hall quantile \(t^{1/\alpha}(1+c t^{-\beta})\). A general third-order regular-variation class can add another term at the same \(A(n/k)^2\) scale.

The result assumes oracle knowledge of \(A(n/k)\) and \(\beta\). Estimation error in those quantities may dominate the residual.

Only the one-sided overestimation probability is asserted. No finite-sample probability bound is claimed.

## References

1. M. Gösgens, B. P. G. van Parys, and B. Zwart, *Large and Moderate Deviations for Conservative Tail-Index Estimation*, arXiv:2609.31127v1, 25 September 2026.
2. G. Maribe, A. Verster, and J. Beirlant, *Reducing bias and MSE in estimation of heavy tails: a Bayesian approach*, arXiv:1606.05687, 2016.
3. I. Cabral, F. Caeiro, and M. I. Gomes, *Reduced bias Hill estimators*, AIP Conference Proceedings 1790, 080006, 2016, DOI 10.1063/1.4968687.
