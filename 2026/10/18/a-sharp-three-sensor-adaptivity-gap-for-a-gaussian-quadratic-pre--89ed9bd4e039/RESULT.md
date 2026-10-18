# A sharp three-sensor adaptivity gap for a Gaussian quadratic prediction goal

## Finding

A two-stage Bayesian sensor selection problem with only three independent Gaussian coordinates admits an exact, strictly beneficial adaptive policy even though each sensor measures one coordinate linearly with independent Gaussian noise. The largest possible ratio of **adaptive** to **nonadaptive** expected posterior-variance reduction in this entire family is
\[
\boxed{1+\sqrt{\frac{2}{\pi}}e^{-1/2}=1.4839414490382866995\ldots.}
\]
The sharp constant is attained at a unique balance between the bilinear and linear portions of the prediction goal, for **every** positive noise variance. An optimal adaptive policy begins with a sensor whose one-step expected risk reduction is zero; myopic selection therefore misses the strict improvement.

## Assumptions and scope

Let \(X_1,X_2,X_3\) be independent standard Gaussian parameters. A single reading of coordinate \(i\) is \(Y_i=X_i+\varepsilon_i\), where the independent noise variables have common variance \(\sigma^2>0\) and are independent of the parameters. Each coordinate may be read at most once. Define
\[
\rho=(1+\sigma^2)^{-1}\in(0,1),\qquad
Z_i=\frac{Y_i}{\sqrt{1+\sigma^2}},\qquad
g(X)=X_1X_2+aX_3,\quad a>0.
\]
All \(Z_i\) are standard normal, with \(\operatorname{Corr}(X_i,Z_i)=\sqrt\rho\). A design uses **exactly two distinct sensors**. In a nonadaptive design the pair is fixed before observing data. In an adaptive design one coordinate is selected first and, after seeing its reading, the second coordinate may be selected as a measurable function of that reading. Arbitrary randomization cannot improve the optimum. The criterion is the **prior-predictive expected posterior variance**
\[
R(\Pi)=\mathbb E\bigl[\operatorname{Var}(g(X)\mid\mathcal T_\Pi)\bigr],
\]
where \(\mathcal T_\Pi\) is the transcript of observed coordinate labels and readings; the objective is to maximize \(\operatorname{Var}(g)-R(\Pi)\). Let \(\phi\) and \(\overline\Phi\) denote the standard Gaussian density and upper-tail function.

Put \(c=a^2/\rho\) and \(Z\sim N(0,1)\). The optimal nonadaptive and optimal adaptive variance reductions are exactly
\[
G_{\mathrm{fixed}}=\rho^2\max\{1,c\},\qquad
G_{\mathrm{adapt}}=\rho^2\,\mathbb E\max\{Z^2,c\}
=\rho^2\left[c+2\bigl(\sqrt c\,\phi(\sqrt c)+(1-c)\overline\Phi(\sqrt c)\bigr)\right].
\]
An optimal policy first reads coordinate \(1\) or \(2\). If coordinate \(1\) is first and its standardized observation is \(z\), the second sensor is coordinate \(2\) when \(\rho z^2\ge a^2\), and coordinate \(3\) otherwise (with either choice allowed at equality). The other first-coordinate choice is symmetric. For all finite \(a>0\),
\[
G_{\mathrm{adapt}}>G_{\mathrm{fixed}}.
\]
The ratio \(G_{\mathrm{adapt}}/G_{\mathrm{fixed}}\) is strictly increasing as \(c\) ranges over \((0,1)\), strictly decreasing over \((1,\infty)\), and attains its unique maximum at \(c=1\), equivalently \(a^2=\rho\).

## Proof

**1. Conditional Gaussian regression.** The Gaussian regression identities yield \(\mathbb E[X_i\mid Z_i]=\sqrt\rho\,Z_i\); posterior means of unread coordinates remain zero. Independence then gives the posterior means of the goal for each possible set of at most two readings:
\[
\begin{aligned}
\mathbb E[g\mid Z_1]&=\mathbb E[g\mid Z_2]=0,\\
\mathbb E[g\mid Z_3]&=a\sqrt\rho\,Z_3,\\
\mathbb E[g\mid Z_1,Z_2]&=\rho Z_1Z_2,\\
\mathbb E[g\mid Z_1,Z_3]&=a\sqrt\rho\,Z_3,\\
\mathbb E[g\mid Z_2,Z_3]&=a\sqrt\rho\,Z_3.
\end{aligned}
\]
The law of total variance says that expected posterior-risk reduction is exactly the variance of the posterior mean. Thus the three fixed pairs have reductions \(\rho^2\), \(a^2\rho\), and \(a^2\rho\), respectively. This proves the nonadaptive optimum.

**2. Optimality among all adaptive policies.** If the first sensor is coordinate \(1\), the posterior mean of the goal is initially zero. Conditional on \(Z_1=z\), revealing \(Z_2\) gives an additional expected reduction \(\operatorname{Var}(\rho zZ_2)=\rho^2z^2\). Revealing \(Z_3\) gives \(\operatorname{Var}(a\sqrt\rho Z_3)=a^2\rho\). Both potential second readings are independent of \(Z_1\), hence the optimal second decision is the stated threshold. Averaging its maximum gain over the first reading gives \(\rho^2\mathbb E\max\{Z^2,c\}\). Initial sensor \(2\) is symmetric. If sensor \(3\) is first, it yields \(a^2\rho\), but reading either \(1\) or \(2\) next contributes no further reduction, because the other bilinear factor remains unobserved. Consequently, choosing \(1\) or \(2\) first is globally optimal. Independent randomization only averages the values of deterministic alternatives, so cannot exceed them. The transcript reveals the first observation and its contingent second-sensor label, so the conditioning above already includes any selection information.

**3. Exact Gaussian integral and strict gap.** For \(t=\sqrt c\), integrating both Gaussian tails and integrating by parts gives
\[
\begin{aligned}
\mathbb E\max\{Z^2,c\}
&=c+\mathbb E[(Z^2-c)_+]\\
&=c+2\int_t^\infty(z^2-c)\phi(z)\,dz\\
&=c+2\bigl(t\phi(t)+(1-c)\overline\Phi(t)\bigr).
\end{aligned}
\]
The random variable \(Z^2\) takes values strictly below and above every fixed finite positive \(c\) with positive probability. Hence \(\mathbb E\max\{Z^2,c\}>\max\{\mathbb EZ^2,c\}=\max\{1,c\}\), establishing the strict adaptive advantage.

**4. Sharp universal ratio.** Write
\[
Q(c)=\frac{\mathbb E\max\{Z^2,c\}}{\max\{1,c\}}.
\]
For \(0<c<1\), the denominator is one and differentiating under the expectation gives \(Q'(c)=\Pr\{Z^2<c\}>0\). For \(c>1\), use \(Q(c)=\mathbb E\max\{Z^2/c,1\}\); differentiation gives
\[
Q'(c)=-c^{-2}\mathbb E[Z^2\mathbf1_{\{Z^2>c\}}]<0.
\]
Thus \(c=1\) is the unique maximizer. At \(c=1\), the integrated formula reduces to \(\mathbb E\max\{Z^2,1\}=1+2\phi(1)=1+\sqrt{2/\pi}e^{-1/2}\). Since \(c=a^2/\rho\) can equal one for every \(\rho\in(0,1)\), the upper bound is attained for every positive noise variance. This completes the full policy comparison and all claimed quantifiers.

## Verification

The standalone file `verify.py` uses exact symbolic Gaussian moments to confirm the posterior-mean variance for all possible one- and two-coordinate sensor sets. Independent high-precision Gaussian quadrature checks the exact tail integral, strict adaptive gain, and unique ratio maximum across multiple noise levels and amplitudes. Its derivative sign tests are numerical corroboration only; the preceding analytical proof covers the full parameter ranges. Run `python verify.py` with Python 3, SymPy, and mpmath.

## Relationship to prior work

Wu, Chen, and Ghattas (2021) study linear goal-oriented Bayesian sensor selection; their objective and fixed-design setting do not determine the present adaptive nonlinear-goal threshold. Koval and Nicholson (2024) study nonintrusive Bayesian approximation-error sensor placement in nonlinear inverse problems, with different posterior criteria. Neuberger, Alexanderian, and van Bloemen Waanders (first public November 2024) derive a broad nonadaptive quadratic-goal posterior-variance criterion; specializing it can recover the fixed-pair Gaussian calculations here, so **those fixed-pair calculations alone are not claimed as a new discovery**. The additional conclusion is an exact global optimization over measurable contingent second-sensor policies and its unique sharp relative advantage. Related sequential Bayesian OED and sensor-selection literature treats more general models but was not found to imply this particular three-sensor constant. General stochastic Gaussian-conditioning and normal-tail identities are classical and are not claimed as new.

## Limitations

The result is an exact example and complete optimization **within the stated family**, not a bound for general adaptive designs. Its sharp \(48.394\%\) relative gain concerns expected posterior **variance reduction**, not a \(48.394\%\) reduction in posterior variance or a comparable gain in entropy, parameter recovery, or realized loss. The sensors are one-per-coordinate, conditionally independent, homoscedastic, and not repeatable; the prior is independent standard Gaussian; the goal has exactly one bilinear and one linear term. The optimal first sensor has zero myopic benefit for this special family. The source-priority check is not exhaustive and independent scientific audit has not occurred.

## References

1. Wu, Chen, and Ghattas, *An efficient method for goal-oriented linear Bayesian optimal experimental design: Application to optimal sensor placement*, arXiv:2102.06627, first public 2021-02-12, https://arxiv.org/abs/2102.06627.
2. Koval and Nicholson, *Non-intrusive optimal experimental design for large-scale nonlinear Bayesian inverse problems using a Bayesian approximation error approach*, arXiv:2405.07412, first public 2024-05-13, https://arxiv.org/abs/2405.07412.
3. Neuberger, Alexanderian, and van Bloemen Waanders, *Goal oriented optimal design of infinite-dimensional Bayesian inverse problems using quadratic approximations*, arXiv:2411.07532, first public 2024-11-12, https://arxiv.org/abs/2411.07532. Later related literature, not the dated source of this finding.
4. Huan, Jagalur, and Marzouk, *Optimal experimental design: Formulations and computations*, Acta Numerica 33 (2024), pp. 715–840, https://doi.org/10.1017/S0962492924000023.
5. Chamon, Pappas, and Ribeiro, *Approximate Supermodularity of Kalman Filter Sensor Selection*, arXiv:1912.03799, https://arxiv.org/abs/1912.03799.
