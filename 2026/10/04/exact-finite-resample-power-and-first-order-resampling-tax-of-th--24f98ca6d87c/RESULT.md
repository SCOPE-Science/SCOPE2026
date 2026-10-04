# Exact finite-resample power and first-order resampling tax of the Gaussian CRT
## Finding
Consider the one-sided model-X conditional randomization test (CRT) in the Gaussian model
\[
X_i\stackrel{\mathrm{iid}}{\sim}N(0,1),\qquad
Y_i=\beta X_i+\varepsilon_i,\qquad
\varepsilon_i\stackrel{\mathrm{iid}}{\sim}N(0,\sigma^2),
\]
with \(X\) independent of \(\varepsilon\). Use the marginal-covariance statistic \(T_0=X^\top Y\), generate \(B\) independent null resamples \(X^{(b)}\sim N(0,I_n)\), and set
\[
p_B=\frac{1+\#\{b:(X^{(b)})^\top Y\ge T_0\}}{B+1}.
\]
Write \(\delta=\beta/\sigma\), let \(R\sim\chi_n\) and \(Z\sim N(0,1)\) be independent, and define
\[
S=\frac{\delta R+Z}{\sqrt{1+\delta^2}},\qquad m=\lfloor\alpha(B+1)\rfloor.
\]
Then the exact finite-\(n\), finite-\(B\) power is
\[
\pi_{n,B}(\delta,\alpha)
=\mathbb E\!\left[
\sum_{j=0}^{m-1}{B\choose j}
\{1-\Phi(S)\}^{j}\Phi(S)^{B-j}
\right],
\]
with an empty sum interpreted as zero. Under \(\delta=0\), the exact null rejection probability is \(m/(B+1)\).

There is also a sharp resampling-budget correction in the local-signal regime. Put \(\beta_n=\sigma h/\sqrt n\) with fixed \(h>0\). For fixed \(B\),
\[
\pi_{n,B}(h/\sqrt n,\alpha)\longrightarrow
\Pi_B(h,\alpha)
=\mathbb E_Z\!\left[
\sum_{j=0}^{m-1}{B\choose j}
\{1-\Phi(h+Z)\}^{j}\Phi(h+Z)^{B-j}
\right].
\]
If \(\alpha=1/q\) for an integer \(q\ge2\) and \(B=q\ell-1\), so that the Monte Carlo test has exact null size \(\alpha\), then, writing \(z=z_{1-\alpha}\),
\[
\Pi_B(h,\alpha)
=\Phi(h-z)
-\frac{\alpha(1-\alpha)h}{2(B+2)\phi(z)}
\exp\!\left(hz-\frac{h^2}{2}\right)
+O(B^{-2}).
\]
Thus finite resampling has a strictly negative first-order power effect for every \(h>0\). At \(\alpha=0.05\) and \(h=2\), the infinite-resample local power is \(0.6387600313\), whereas \(B=19\), the smallest budget that can reject at the \(5\%\) level, has limiting power \(0.5579895753\). The first-order coefficient is \(-1.6726211489\).

## Assumptions and scope
The statement is for a single Gaussian predictor with known model-X law, Gaussian homoskedastic noise, a one-sided test, and the marginal-covariance statistic. The null resamples are independent of each other and of the observed data conditional on \(Y\). The exact formula holds for every integer \(n\ge1\), every \(B\ge1\), \(\sigma>0\), and real \(\beta\); the local expansion assumes fixed \(h>0\), fixed reciprocal level \(\alpha=1/q\), and budgets on the exact-size subsequence \(B=q\ell-1\) as \(\ell\to\infty\).

No claim is made that the marginal-covariance statistic is optimal against all alternatives. The result isolates the finite-resampling effect for a canonical statistic whose asymptotic power has already been studied.

## Proof
Condition on the realized response vector \(Y=y\). Joint Gaussian conditioning gives
\[
X\mid Y=y\sim N\!\left(
\frac{\beta}{\beta^2+\sigma^2}y,
\frac{\sigma^2}{\beta^2+\sigma^2}I_n
\right).
\]
Moreover \(\|Y\|/(\sqrt{\beta^2+\sigma^2})\sim\chi_n\). Therefore the observed standardized score satisfies
\[
\frac{X^\top Y}{\|Y\|}\ \stackrel d=\
\frac{\delta R+Z}{\sqrt{1+\delta^2}}=S.
\]
For every resample, conditional on \(Y\),
\[
\frac{(X^{(b)})^\top Y}{\|Y\|}\stackrel{\mathrm{iid}}{\sim}N(0,1),
\]
and these standardized resampled scores are independent of the Gaussian residual in \(S\). Consequently, conditional on \(S=s\), the number of resampled statistics at least as large as the observed statistic is
\[
N_s\sim\operatorname{Bin}\!\left(B,1-\Phi(s)\right).
\]
The event \(p_B\le\alpha\) is exactly \(N_s\le m-1\), which yields the displayed finite-sample formula after averaging over \(S\). At \(\delta=0\), the observed and resampled standardized scores are \(B+1\) iid continuous variables, so the observed rank is uniform and the null rejection probability is exactly \(m/(B+1)\).

For the local alternative \(\delta_n=h/\sqrt n\), the law of large numbers for \(R^2\sim\chi_n^2\) gives \(R/\sqrt n\to1\) in probability, hence \(S\Rightarrow h+Z\). The binomial-CDF integrand is bounded and continuous, proving the fixed-\(B\) limit.

For the first-order budget expansion, take \(\alpha=1/q\) and \(B=q\ell-1\), so \(m=\ell\). Transform the observed local score to \(U_0=\Phi(h+Z)\), and transform the \(B\) null resample scores to iid uniforms. Rejection occurs exactly when \(U_0\) exceeds the \((B-m+1)\)-st uniform order statistic
\[
V\sim\operatorname{Beta}((q-1)\ell,\ell).
\]
Its mean is \(1-\alpha\) and its variance is \(\alpha(1-\alpha)/(B+2)\). With
\[
g(u)=\Pr\{\Phi(h+Z)>u\}=\Phi\!\left(h-\Phi^{-1}(u)\right),
\]
we have \(\Pi_B(h,\alpha)=\mathbb E[g(V)]\). At \(u=1-\alpha\), writing \(z=\Phi^{-1}(1-\alpha)\),
\[
g''(u)=-\frac{h}{\phi(z)}\exp\!\left(hz-\frac{h^2}{2}\right).
\]
A Taylor expansion about the beta mean gives
\[
\mathbb E[g(V)]
=g(1-\alpha)+\frac12 g''(1-\alpha)\operatorname{Var}(V)+O(B^{-2}),
\]
because the third centered beta moment and the fourth centered moment are both \(O(B^{-2})\) and \(g\) is smooth on a fixed neighborhood of \(1-\alpha\); the beta tails outside that neighborhood are exponentially small. Substitution yields the stated coefficient.

## Verification
The embedded `verify.py` independently evaluates the finite-\(B\) integral by Gauss-Legendre quadrature using only the Python standard library. It checks exact null-size identities, finite-\(n\) numerical benchmarks, the fixed-\(B\) local powers for several exact-size budgets at \(\alpha=0.05\), and convergence of the scaled power gap toward the analytic \(1/B\) coefficient. A clean replay prints `VERIFY_OK`.

For a finite-sample benchmark with \(n=20\), \(\delta=0.5\), and \(\alpha=0.05\), the exact-quantile power is \(0.6359132525\), while the finite-resample powers are \(0.5514164152\), \(0.5920303376\), and \(0.6181528224\) for \(B=19,39,99\), respectively.

## Relationship to prior work
Candès, Fan, Janson, and Lv introduced the model-X CRT as a simulation-based conditional randomization procedure and emphasized its computational cost. Their discussion explicitly relates a finite resampling count to binomial Monte Carlo uncertainty in the randomization p-value. Wang and Janson later derived asymptotic power formulas for the CRT with the marginal-covariance statistic. Crucially for the present comparison, they state that their empirical CRT has a finite-sample correction but that their power results study an analytical cutoff and continue to apply when the number of resamples tends to infinity. The fixed-resample regime is therefore not covered by that asymptotic statement.

Katsevich and Ramdas studied power from a different angle: they identify likelihood-based statistics as most powerful against point alternatives and derive limiting power under local semiparametric alternatives. The claim here is narrower in statistic and model but resolves the orthogonal finite-resampling question exactly, including the persistent fixed-\(B\) local-power loss and its explicit large-\(B\) coefficient.

Targeted searches using conditional-randomization, finite-resample, Monte Carlo rank, Gaussian marginal-covariance, beta-order-statistic, and resampling-budget formulations did not locate this exact formula or coefficient. Generic Monte Carlo randomization-test rank corrections are established background and are not claimed as new.

## Limitations
The derivation exploits exact Gaussian conditioning and does not automatically extend to non-Gaussian model-X laws, estimated conditional distributions, two-sided statistics, nuisance covariates, or adaptive/early-stopped Monte Carlo CRT implementations. The \(O(B^{-2})\) expansion is asserted on the exact-size subsequence \(B=q\ell-1\) at reciprocal levels; other \(B\) values have an additional lattice effect because \(\lfloor\alpha(B+1)\rfloor/(B+1)\) differs from \(\alpha\).

The originality comparison is targeted rather than exhaustive. Older Monte Carlo randomization-test literature could contain a generic order-statistic expansion that specializes to the displayed coefficient under a change of notation. No such direct implication was located in the inspected sources or searches.

## References
1. E. Candès, Y. Fan, L. Janson, and J. Lv, *Panning for Gold: Model-X Knockoffs for High-dimensional Controlled Variable Selection*, arXiv:1610.02351; JRSS B 80 (2018), 551–577.
2. E. Katsevich and A. Ramdas, *On the power of conditional independence testing under model-X*, arXiv:2005.05506; Electronic Journal of Statistics 16 (2022), 6348–6394.
3. W. Wang and L. Janson, *A High-Dimensional Power Analysis of the Conditional Randomization Test and Knockoffs*, arXiv:2010.02304; Biometrika 109 (2022), 631–645.
