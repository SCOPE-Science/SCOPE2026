# Exact polylogarithmic tail constants and quantile correction for the LGF model
## Finding
For the logarithmic–gamma frailty (LGF) first-failure model with parameters \(\theta,\lambda>0\) and \(0<\eta<1\), the survival function is
\[
S(y)=\frac{1}{-\log(1-\eta)}
\sum_{n=1}^{\infty}\frac{\eta^n}{n}
\left(\frac{\lambda}{\lambda+n\theta y}\right)^\lambda.
\]
Write
\[
L_s(\eta)=\operatorname{Li}_s(\eta)
=\sum_{n=1}^{\infty}\frac{\eta^n}{n^s}.
\]
Then, as \(y\to\infty\),
\[
S(y)=A y^{-\lambda}
\left(1-\frac{B}{y}+O(y^{-2})\right),
\]
with
\[
A=
\frac{(\lambda/\theta)^\lambda L_{\lambda+1}(\eta)}
{-\log(1-\eta)},
\qquad
B=
\frac{\lambda^2}{\theta}
\frac{L_{\lambda+2}(\eta)}
{L_{\lambda+1}(\eta)}.
\]
Hence the hazard has the sharper expansion
\[
h(y)=\frac{\lambda}{y}-\frac{B}{y^2}+O(y^{-3}).
\]

If \(Q(p)\) is the \(p\)-quantile, then
\[
Q(p)=
\left(\frac{A}{1-p}\right)^{1/\lambda}
-\frac{B}{\lambda}
+O((1-p)^{1/\lambda})
\qquad(p\uparrow1).
\]

The 2026 source states only
\[
S(y)\sim C(\eta,\lambda)y^{-\lambda},
\qquad
h(y)\sim \frac{\lambda}{y},
\]
with an unspecified positive constant \(C(\eta,\lambda)\), and consequently gives an extreme-quantile approximation in terms of that unspecified constant. The formulas above identify that constant exactly and provide the first nonzero correction for both the hazard and the extreme quantile.

## Assumptions and scope
The result uses the LGF model as defined in Rahmouni (2026): the latent component count has the logarithmic law with parameter \(\eta\), the shared frailty is gamma with shape and rate \(\lambda\), and the conditional component lifetime is exponential with baseline rate \(\theta\).

The displayed formulas assume \(0<\eta<1\). They extend continuously to the boundary \(\eta=0\): since \(L_s(\eta)/[-\log(1-\eta)]\to1\) and \(L_{\lambda+2}(\eta)/L_{\lambda+1}(\eta)\to1\),
\[
A\to(\lambda/\theta)^\lambda,
\qquad
B\to\lambda^2/\theta.
\]
The quantile expansion then agrees with the exact Lomax boundary quantile.

## Proof
Starting from the published survival series,
\[
S(y)=
\frac{1}{-\log(1-\eta)}
\sum_{n\ge1}\frac{\eta^n}{n}
\left(\frac{\lambda}{\lambda+n\theta y}\right)^\lambda,
\]
factor out the dominant power:
\[
\left(\frac{\lambda}{\lambda+n\theta y}\right)^\lambda
=
\left(\frac{\lambda}{\theta y}\right)^\lambda
n^{-\lambda}
\left(1+\frac{\lambda}{n\theta y}\right)^{-\lambda}.
\]
For large \(y\),
\[
(1+x)^{-\lambda}
=
1-\lambda x+\frac{\lambda(\lambda+1)}{2}x^2+O(x^3).
\]
Because \(n\ge1\) and \(\eta^n\) decays geometrically, this expansion may be summed termwise with an \(O(y^{-3})\) remainder dominated by a convergent geometric series. Therefore
\[
S(y)
=
\frac{(\lambda/\theta)^\lambda y^{-\lambda}}
{-\log(1-\eta)}
\left[
L_{\lambda+1}(\eta)
-\frac{\lambda^2}{\theta y}L_{\lambda+2}(\eta)
+O(y^{-2})
\right].
\]
Factoring \(L_{\lambda+1}(\eta)\) gives the stated constants \(A\) and \(B\).

Since \(h(y)=-\frac{d}{dy}\log S(y)\),
\[
\log S(y)
=
\log A-\lambda\log y+\log\left(1-\frac{B}{y}+O(y^{-2})\right),
\]
so
\[
h(y)=\frac{\lambda}{y}-\frac{B}{y^2}+O(y^{-3}).
\]

For the quantile, put \(q=1-p\) and
\[
y_0=\left(\frac{A}{q}\right)^{1/\lambda}.
\]
Write \(Q(p)=y_0+\delta+O(y_0^{-1})\). Substitution into
\[
q=AQ(p)^{-\lambda}\left(1-\frac{B}{Q(p)}+O(Q(p)^{-2})\right)
\]
gives at order \(y_0^{-1}\)
\[
-\lambda\delta-B=0.
\]
Thus
\[
\delta=-\frac{B}{\lambda},
\]
and \(y_0^{-1}=O(q^{1/\lambda})\), proving the quantile expansion.

## Verification
The included checker evaluates the published survival series directly for \(\lambda=2.3\), \(\theta=1.7\), and \(\eta=0.6\), and independently computes the polylogarithmic constants.

It verifies numerically that
\[
y^\lambda S(y)\to A,
\qquad
y\left(\frac{S(y)}{A y^{-\lambda}}-1\right)\to-B,
\]
and
\[
y^2\left(\frac{\lambda}{y}-h(y)\right)\to B.
\]
It also solves the exact survival equation for upper-tail probabilities and confirms that
\[
Q(p)-\left(\frac{A}{1-p}\right)^{1/\lambda}
\to-\frac{B}{\lambda}.
\]

These finite calculations are replayable consistency checks; the asymptotic proof is the termwise analytic expansion above.

## Relationship to prior work
Rahmouni (2026) gives the LGF survival series and states that its tail is regularly varying with index \(-\lambda\), but leaves the positive tail constant as an unspecified \(C(\eta,\lambda)\). The same section gives only the leading hazard equivalence \(h(y)\sim\lambda/y\). Proposition 9 then expresses the extreme-quantile approximation using that unspecified \(C(\eta,\lambda)\).

Rahmouni's related 2026 finite logistic-weighted Lomax mixture paper describes power-law tails and says that the mixture constant is determined by the weights and scales, but does not provide this logarithmic-mixture polylogarithmic constant or the present second-order correction.

The 2025 doubly generalized exponential-geometric frailty model uses geometric rather than logarithmic mixing and a different failure rule. It does not imply the polylogarithmic constants above.

Focused searches for the LGF model together with polylogarithm, exact tail constant, second-order hazard, and extreme-quantile correction did not locate a covering statement or correction.

## Limitations
The result is asymptotic and does not give a uniform finite-\(y\) error bound. The \(O(y^{-2})\) and \(O(y^{-3})\) remainders can be expanded further by the same method, but higher coefficients are not claimed here.

No claim is made about optimal numerical use of the second-order quantile approximation for every parameter regime. The exact finite quantile remains defined by the survival equation.

## References
1. M. Rahmouni, “A logarithmic–gamma frailty model for first-failure times with heavy-tailed risk,” AIMS Mathematics 11 (2026), 8945–8965. DOI: 10.3934/math.2026369.
2. M. Rahmouni, “Frailty-Augmented Logistic-Weighted Lomax Mixture regression for survival analysis,” AIMS Mathematics 11 (2026), 6329–6349. DOI: 10.3934/math.2026261.
3. M. Rahmouni, “The doubly generalized exponential-geometric frailty distribution,” AIMS Mathematics 10 (2025), 30384–30428. DOI: 10.3934/math.20251334.
